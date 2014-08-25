下面这个谜题测试了你关于二进制兼容性（binary compatibility）的知识：当你改变了某个类所依赖的另外一个类时，第一个类的行为会发生什么改变呢？更特殊的是，假设你编译的是如下的2个类。第一个作为一个客户端，第二个作为一个库类，会怎么样呢： 
```java  
public class PrintWords {
    public static void main(String[] args) {
        System.out.println(Words.FIRST  + " " + 
                           Words.SECOND + " " +
                           Words.THIRD);
    }
}

public class Words {
    private Words() { };  // Uninstantiable

    public static final String FIRST  = "the";
    public static final String SECOND = null;
    public static final String THIRD  = "set";
} 
```
现在假设你像下面这样改变了那个库类并且重编译了这个类，但并不重编译客户端的程序： 
```java  
public class Words {
    private Words() { };  // Uninstantiable

    public static final String FIRST  = "physics";
    public static final String SECOND = "chemistry";
    public static final String THIRD  = "biology";
}
```
此时，客户端的程序会打印出什么呢？ 
简单地看看程序，你会觉得它应该打印 physics chemistry biology；毕竟Java是在运行期对类进行装载的，所以它总是会访问到最新版本的类。但是更深入一点的分析会得出不同的结论。对于常量域的引用会在编译期被转化为它们所表示的常量的值[JLS 13.1]。这样的域从技术上讲，被称作常量变量（constant variables），这可能在修辞上显得有点矛盾。一个常量变量的定义是：一个在编译期被常量表达式初始化的final的原始类型或String类型的变量[JLS 4.12.4]。在知道了这些知识之后，我们有理由认为客户端程序会将初始值Words.FIRST, Words.SECOND, Words.THIRD编译进class文件，然后无论Words类是否被改变，客户端都会打印the null set。 
这种分析可能是有道理的，但是却是不对的。如果你运行了程序，你会发现它打印的是the chemistry set。这看起来确实太奇怪的了。它为什么会做出这种事情呢？答案可以在编译期常量表达式(compile-time constant expression)[JLS 15.28]的精确定义中找到。它的定义太长了，就不在这里写出来了，但是理解这个程序的行为的关键是null不是一个编译期常量表达式。 
由于常量域将会编译进客户端，API的设计者在设计一个常量域之前应该深思熟虑。如果一个域表示的是一个真实的常量，例如π或者一周之内的天数，那么将这个域设为常量域没有任何坏处。但是如果你想让客户端程序感知并适应这个域的变化，那么就不能让这个域成为一个常量。有一个简单的方法可以做到这一点：如果你使用了一个非常量的表达式去初始化一个域，甚至是一个final域，那么这个域就不是一个常量。你可以通过将一个常量表达式传给一个方法使得它变成一个非常量，该方法将直接返回其输入参数。 
如果我们使用这种方法来修改Word类，在Words类被重新修改和编译之后，PrintWords类将打印出physics chemistry biology： 
```java  
public class Words {
private Words() {};  // Uninstantiable

    public static final String FIRST   = ident("the");
    public static final String SECOND  = ident(null);
    public static final String THIRD   = ident("set");

    private static String ident(String s) {
        return s;
    }
} 
```
在5.0版本中引入的枚举常量（enum constants），虽然有这样一个名字，但是它们并不是常量变量。你可以在枚举类型中加入枚举常量，对它们重新排序，甚至可以移除没有用的枚举常量，而且并不需要重新编译客户端。 
总之，常量变量将会被编译进那些引用它们的类中。一个常量变量就是任何被常量表达式初始化的原始类型或字符串变量。令人惊讶的是，null不是一个常量表达式。 
对于语言设计者来说，在一个动态链接的语言中，将常量表达式编译进客户端可能并不是一个好主意。这让很多程序员大吃一惊，并且很容易产生一些难以查出的缺陷：当缺陷被侦测出来的时候，那些定义常量的源代码可能已经不存在了。另外一方面，将常量表达式编译进客户端使得我们可以使用if语句来模拟条件编译（conditional compilation）[JLS 14.21]。为了正当目的可以不择手段的做法是需要每个人自己来判断的。