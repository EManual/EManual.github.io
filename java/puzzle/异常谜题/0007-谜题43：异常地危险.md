在JDK1.2中，Thread.stop、Thread.suspend以及其他许多线程相关的方法都因为它们不安全而不推荐使用了[ThreadStop]。下面的方法展示了你用Thread.stop可以实现的可怕事情之一。 
```java   
// Don’t do this - circumvents exception checking!
public static void sneakyThrow(Throwable t) {
	Thread.currentThread().stop(t); // Deprecated!!
}
```
这个讨厌的小方法所做的事情正是throw语句要做的事情，但是它绕过了编译器的所有异常检查操作。你可以（卑鄙地）在你的代码的任意一点上抛出任何受检查的或不受检查的异常，而编译器对此连眉头都不会皱一下。 
不使用任何不推荐的方法，你也可以编写出在功能上等价于sneakyThrow的方法。事实上，至少有两种方式可以这么实现这一点，其中一种只能在5.0或更新的版本中运行。你能够编写出这样的方法吗？它必须是用Java而不是用JVM字节码编写的，你不能在其客户对它编译完之后再去修改它。你的方法不必是完美无瑕的：如果它不能抛出一两个Exception的子类，也是可以接受的。 
本谜题的一种解决之道是利用Class.newInstance方法中的设计缺陷，该方法通过反射来对一个类进行实例化。引用有关该方法的文档中的话[Java-API]：“请注意，该方法将传播从空的[换句话说，就是无参数的]构造器所抛出的任何异常，包括受检查的异常。使用这个方法可以有效地绕开在其他情况下都会执行的编译期异常检查。”一旦你了解了这一点，编写一个sneakyThrow的等价方法就不是太难了。 
```java   
public class Thrower {
    private static Throwable t;
    private Thrower() throws Throwable {
         throw t;
    }
    
public static synchronized void sneakyThrow(Throwable t) {
         Thrower.t = t;
         try {
              Thrower.class.newInstance();
         } catch (InstantiationException e) {
              throw new IllegalArgumentException();
         } catch (IllegalAccessException e) {
              throw new IllegalArgumentException();
         } finally {
              Thrower.t = null; // Avoid memory leak
         }
    }
}
```
在这个解决方案中将会发生许多微妙的事情。我们想要在构造器执行期间所抛出的异常不能作为一个参数传递给该构造器，因为Class.newInstance调用的是一个类的无参数构造器。因此，sneakyThrow方法将这个异常藏匿于一个静态变量中。为了使该方法是线程安全的，它必须被同步，这使得对其的并发调用将顺序地使用静态域t。 
要注意的是，t这个域在从finally语句块中出来时是被赋为空的：这只是因为该方法虽然是卑鄙的，但这并不意味着它还应该是内存泄漏的。如果这个域不是被赋为空出来的，那么它阻止该异常被垃圾回收。最后，请注意，如果你让该方法抛出一个InstantiationException或是一个IllegalAccessException异常，它将以抛出一个IllegalArgumentException而失败。这是这项技术的一个内在限制。 
Class.newInstance的文档继续描述道“Constructor.newInstance方法通过将构造器抛出的任何异常都包装在一个（受检查的）InvocationTargetException异常中而避免了这个问题。”很明显，Class.newInstance应该是做了相同的处理，但是纠正这个缺陷已经为时过晚，因为这么做将引入源代码级别的不兼容性，这将使许多依赖于Class.newInstance的程序崩溃。而弃用这个方法也不切实际，因为它太常用了。当你在使用它时，一定要意识到Class.newInstance可以抛出它没有声明过的受检查异常。 
被添加到5.0版本中的“通用类型（generics）”可以为本谜题提供一个完全不同的解决方案。为了实现最大的兼容性，通用类型是通过类型擦除（type erasure）来实现的：通用类型信息是在编译期而非运行期检查的[JLS 4.7]。 
下面的解决方案就利用了这项技术： 
```java   
// Don’t do this either - circumvents exception checking!
class TigerThrower<T extends Throwable> {
    public static void sneakyThrow(Throwable t) {
        new TigerThrower<Error>().sneakyThrow2(t);
    }
    private void sneakyThrow2(Throwable t) throws T {
        throw (T) t;
    }
}
```
这个程序在编译时将产生一条警告信息： 
```java   
TigerThrower.java:7:warning: [unchecked] unchecked cast
found    :  java.lang.Throwable, required: T
           throw (T) t;
                       ^
```
警告信息是编译器所采用的一种手段，用来告诉你：你可能正在搬起石头砸自己的脚，而且事实也正是如此。“不受检查的转型”警告告诉你这个有问题的转型将不会在运行时刻受到检查。当你获得了一个不受检查的转型警告时，你应该修改你的程序以消除它，或者你可以确信这个转型不会失败。如果你不这么做，那么某个其他的转型可能会在未来不确定的某个时刻失败，而你也就很难跟踪此错误到其源头了。对于本谜题所示的情况，其情况更糟糕：在运行期抛出的异常可能与方法的签名不一致。sneakyThrow2方法正是利用了这一点。 
对平台设计者来说，有好几条教训。在设计诸如反射类库之类在语言之外实现的类库时， 要保留语言所作的所有承诺。当从头设计一个支持通用类型的平台时，要考虑强制要求其在运行期的正确性。Java通用类型工具的设计者可没有这么做，因为他们受制于通用类库必须能够与现有客户进行互操作的要求。对于违反方法签名的异常，为了消除其产生的可能性，应该考虑强制在运行期进行异常检查。 
总之，Java的异常检查机制并不是虚拟机强制执行的。它只是一个编译期工具，被设计用来帮助我们更加容易地编写正确的程序，但是在运行期可以绕过它。要想减少你因为这类问题而被曝光的次数，就不要忽视编译器给出的警告信息。