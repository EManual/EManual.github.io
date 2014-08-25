下面的程序由一个单一的类构成，该类表示一对类型相似的对象。它大量使用了5.0版的特性，包括泛型、自动包装、变长参数（varargs）和for-each循环。关于这些特性的介绍，请查看http://java.sun.com/j2se/5.0/docs/guide/language[Java-5.0]。这个程序的main方法只是执行这个类。那么它会打印什么呢？ 
```java   
import java.util.*;
public class Pair<T> {
    private final T first;
    private final T second;

    public Pair(T first, T second) {
        this.first = first;
        this.second = second;
    }

    public T first() {
        return first;
    }
    public T second() {
        return second;
    }
    public List<String> stringList() {
        return Arrays.asList(String.valueOf(first),
                             String.valueOf(second));
    }

    public static void main(String[] args) {
        Pair p = new Pair<Object> (23, "skidoo");
        System.out.println(p.first() + " " + p.second());
        for (String s : p.stringList())
            System.out.print(s + " ");
    }
}
```
这段程序看上去似乎相当简单。它创建了一个对象对，其中第一个元素是一个表示23的Integer对象，第二个元素是一个字符串“skidoo”，然后这段程序将打印这个对象对的第一个和第二个元素，并用一个空格隔开。最后它循环迭代这些元素的string表示，并且再次打印它们，所以这段程序应该打印23 skidoo两次。然而可惜的是，它根本不能通过编译。更糟的是，编译器的错误消息更是另人困惑：
```java    
Pair.java:26: incompatible types;
found: Object, required: String
            for (String s : p.stringList())
                               ^
```
如果Pair.stringList是声明返回List<Object>的话，那么这个错误消息还是可以明白的，但是事实是它返回的是List<String>。究竟是怎么回事呢？ 
这个十分奇怪的现象是因为程序使用了原生类型（raw type）而引起的。一个原生类型就是一个没有任何类型参数的泛型类或泛型接口的名字。例如，List<E> 是一个泛型接口，List<String> 是一个参数化的类型，而List 就是一个原生类型。在我们的程序中，唯一用到原生类型的地方就是在main方法中对局部变量p的声明： 
```java   
Pair p = new Pair<Object> (23, "skidoo"); 
```
一个原生类型很像其对应的参数化类型，但是它的所有实例成员都要被替换掉，而替换物就是这些实例成员被擦除掉对应部分之后剩下的东西。具体地说，在一个实例方法声明中出现的每个参数化的类型都要被其对应的原生部分所取代[JLS 4.8]。我们程序中的变量p是属于原生类型Pair的，所以它的所有实例方法都要执行这种擦除。这也包括声明返回List<String>的方法stringList。编译器会将这个方法解释为返回原生类型List。 
当List<String>实现了参数化类型Iterable<String>时，List也实现了原生类型Iterable。Iterable<String>有一个iterator方法返回参数化类型Iterator<String>，相应地，Iterable也有一个iterator方法返回原生类型Iterator。当Iterator<String>的next方法返回String时，Iterator的next方法返回Object。因此，循环迭代p.stringList()需要一个Object类型的循环变量，这就解释了编译器的那个奇怪的错误消息的由来。这种现象令人想不通的原因在于参数化类型List<String>虽然是方法stringList的返回类型，但它与Pair的类型参数没有关系，事实上最后它被擦除了。 
你可以尝试通过将循环变量类型从String改成Object这一做法来解决这个问题： 
```java   
// Don’t do this; it doesn’t really fix the problem!
for (Object s : p.stringList())
	System.out.print(s + " "); 
```
这样确实令程序输出了满意的结果，但是它并没有真正解决这个问题。你会失去泛型带来的所有优点，并且如果该循环在s上调用了任何String方法，那么程序甚至不能通过编译。正确解决这个问题的方法是为局部变量p提供一个合适的参数化的声明： 
```java   
Pair<Object> p = new Pair<Object>(23, "skidoo"); 
```
以下是要点强调：原生类型List和参数化类型List<Object>是不一样的。如果使用了原生类型，编译器不会知道在list允许接受的元素类型上是否有任何限制，它会允许你添加任何类型的元素到list中。这不是类型安全的：如果你添加了一个错误类型的对象，那么在程序接下来的执行中的某个时刻，你会得到一个ClassCastException异常。如果使用了参数化类型List<Object>，编译器便会明白这个list可以包含任何类型的元素，所以你添加任何对象都是安全的。 
还有第三种与以上两种类型密切相关的类型：List<?>是一种特殊的参数化类型，被称为通配符类型（wildcard type）。像原生类型List一样，编译器也不会知道它接受哪种类型的元素，但是因为List<?>是一个参数化类型，从语言上来说需要更强的类型检查。为了避免出现ClassCastException异常，编译器不允许你添加除null以外的任何元素到一个类型为List<?>的list中。 
原生类型是为兼容5.0版以前的已有代码而设计的，因为它们不能使用泛型。5.0版中的许多核心库类，如collections，已经利用泛型做了改变，但是使用这些类的已有程序的行为仍然与在以前的版本上运行一样。这些原生类型及其成员的行为被设计成可以镜像映射到5.0之前的Java语言上，从而保持了兼容性。 
这个Pair程序的真正问题在于编程者没有决定究竟使用哪种Java版本。尽管程序中大部分使用了泛型，而变量p却被声明成原生类型。为了避免被编译错误所迷惑，请避免在打算用5.0或更新的版本来运行的代码中编写原生类型。如果一个已有的库方法返回了一个原生类型，那么请将它的结果存储在一个恰当的参数化类型的变量中。然而，最好的办法还是尽量将该库升级到使用泛型的版本上。虽然Java提供了原生类型和参数化类型间的良好的互用性，但是原生类型的局限性会妨碍泛型的使用。 
实际上，这种问题在用getAnnotation方法在运行期读取Class的注解（annotations）的情况下也会发生，该方法是在5.0版中新添加到Class类中的。每次调用getAnnotation方法时都会涉及到两个Class对象：一个是在其上调用该方法的对象，另一个是作为传递参数指出需要哪个类的注解的对象。在一个典型的调用中，前者是通过反射获得的，而后者是一个类名称字面常量，如下例所示： 
```java   
Author a = Class.forName(name).getAnnotation(Author.class);
```
你不必把getAnnotation的返回值转型为Author。以下两种机制保证了这种做法可以正常工作：（1）getAnnotation方法是泛型的。它是通过它的参数类型来确定返回类型的。具体地说，它接受一个Class<T>类型的参数，返回一个T类型的值。（2）类名称字面常量提供了泛型信息。例如，Author.class的类型是Class<Author>。类名称字面常量可以传递运行时和编译时的类型信息。以这种方式使用的类名称字面常量被称作类型符号（type token）[Bracha04]。 
与类名称字面常量不同的是，通过反射获得的Class对象不能提供完整的泛型类型信息：Class.forName的返回类型是通配类型Class<?>。在调用getAnnotation方法的表达式中，使用的是通配类型而不是原生类型Class，这一点很重要。如果你采用了原生类型，返回的注解具有的就是编译期的Annotation类型而不是通过类名称字面常量指示的类型了。下面的程序片断错误地使用了原生类型，和本谜题中最初的程序一样不能通过编译，其原因也一样： 
```java   
Class c = Class.forName(name);           // Raw type!
Author a = c.getAnnotation(Author.class);    // Type mismatch
```
总之，原生类型的成员被擦掉，是为了模拟泛型被添加到语言中之前的那些类型的行为。如果你将原生类型和参数化类型混合使用，那么便无法获得使用泛型的所有好处，而且有可能产生让你困惑的编译错误。另外，原生类型和以Object为类型参数的参数化类型也不相同。最后，如果你想重构现有的代码以利用泛型的优点，那么最好的方法是一次只重构一个API，并且保证新的代码中绝不使用原生类型。