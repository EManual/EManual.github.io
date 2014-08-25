请考虑下面的两个类： 
```java   
public class Strange1 {
    public static void main(String[] args) {
        try {
            Missing m = new Missing();
        } catch (java.lang.NoClassDefFoundError ex) {
            System.out.println("Got it!");
        }
    }
}

public class Strange2 {
    public static void main(String[] args) {
        Missing m;
        try {
            m = new Missing();
        } catch (java.lang.NoClassDefFoundError ex) {
            System.out.println("Got it!");
        }
    } 
}
Strange1和Strange2都用到了下面这个类： 
class Missing {
    Missing() { }
}
```
如果你编译所有这三个类，然后在运行Strange1和Strange2之前删除Missing.class文件，你就会发现这两个程序的行为有所不同。其中一个抛出了一个未被捕获的NoClassDefFoundError异常，而另一个却打印出了Got it! 到底哪一个程序具有哪一种行为，你又如何去解释这种行为上的差异呢？ 
程序Strange1只在其try语句块中提及Missing类型，因此你可能会认为它捕获NoClassDefFoundError异常，并打印Got it！另一方面，程序Strange2在try语句块之外声明了一个Missing类型的变量，因此你可能会认为所产生的NoClassDefFoundError异常不会被捕获。如果你试着运行这些程序，就会看到它们的行为正好相反：Strange1抛出了未被捕获的NoClassDefFoundError异常，而Strange2却打印出了Got it！怎样才能解释这些奇怪的行为呢？ 
如果你去查看Java规范以找出应该抛出NoClassDefFoundError异常的地方，那么你不会得到很多的指导信息。该规范描述道，这个错误可以“在（直接或间接）使用某个类的程序中的任何地方”抛出[JLS 12.2.1]。当VM调用Strange1和Strange2的main方法时，这些程序都间接使用了Missing类，因此，它们都在其权利范围内于这一点上抛出了该错误。 
于是，本谜题的答案就是这两个程序可以依据其实现而展示出各自不同的行为。但是这并不能解释为什么这些程序在所有我们所知的Java实现上的实际行为，与你所认为的必然行为都正好相反。要查明为什么会是这样，我们需要研究一下由编译器生成的这些程序的字节码。 
如果你去比较Strange1和Strange2的字节码，就会发现几乎是一样的。除了类名之外，唯一的差异就是catch语句块所捕获的参数ex与VM本地变量之间的映射关系不同。尽管哪一个程序变量被指派给了哪一个VM变量的具体细节会因编译器的不同而有所差异，但是对于和上述程序一样简单的程序来说，这些细节不太可能会差异很大。下面是通过执行javap -c Strange1命令而显示的Strange1.main的字节码： 
```java   
0: new
3: dup
4: invokespecial    #3; //Method Missing."<init>":()V
7: astore_1
8: goto 20
11: astore_1
12: getstatic       #5; // Field System.out:Ljava/io/PrintStream;
15: ldc             #6; // String "Got it!"
17: invokevirtual   #7;//Method PrintStream.println: (String); V
20: return
Exception table:
from to target type
  0   8    11    Class java/lang/NoClassDefFoundError
```
Strange2.main相对应的字节码与其只有一条指令不同： 
```java   
11: astore_2
```
这是一条将catch语句块中的捕获异常存储到捕获参数ex中的指令。在Strange1中，这个参数是存储在VM变量1中的，而在Strange2中，它是存储在VM变量2中的。这就是两个类之间唯一的差异，但是它所造成的程序行为上的差异是多么地大呀！ 
为了运行一个程序，VM要加载和初始化包含main方法的类。在加载和初始化之间，VM必须链接（link）类[JLS 12.3]。链接的第一阶段是校验，校验要确保一个类是良构的，并且遵循语言的语法要求。校验非常关键，它维护着可以将像Java这样的安全语言与像C或C++这样的不安全语言区分开的各种承诺。 
在Strange1和Strange2这两个类中，本地变量m碰巧都被存储在VM变量1中。两个版本的main都有一个连接点，从两个不同位置而来的控制流汇聚于此。该连接点就是指令20，即从main返回的指令。在正常结束try语句块的情况下，我们执行到指令8，即goto 20，从而可以到达指令20；而对于在catch语句块中结束的情况，我们将执行指令17，并按顺序执行下去，到达指令20。 
连接点的存在使得在校验Strange1类时产生异常，而在校验Strange2类时并不会产生异常。当校验去执行对Strange1.main的流分析（flow analysis）[JLS 12.3.1]时，由于指令20可以通过两条不同的路径到达，因此校验器必须合并在变量1中的类型。两种类型是通过计算它们的首个公共超类（first common superclass）[JVMS 4.9.2]而合并的。两个类的首个公共超类是它们所共有的最详细而精确的超类。 
在Strange1.main方法中，当从指令8到达指令20时，VM变量1的状态包含了一个Missing类的实例。当从指令17到达时，它包含了一个NoClassDefFoundError类的实例。为了计算首个公共超类，校验器必须加载Missing类以确定其超类。因为Missing.class文件已经被删除了，所以校验器不能加载它，因而抛出了一个NoClassDefFoundError异常。请注意，这个异常是在校验期间、在类被初始化之前，并且在main方法开始执行之前很早就抛出的。这就解释了为什么没有打印出任何关于这个未被捕获异常的跟踪栈信息。 
要想编写一个能够探测出某个类是否丢失的程序，请使用反射来引用类而不要使用通常的语言结构[EJ Item35]。 
下面展示了用这种技巧重写的程序： 
```java  
public class Strange {
    public static void main(String[] args) throws  
    Exception{
        try {
            Object m = Class.forName("Missing").
                       newInstance();
        } catch (ClassNotFoundException ex) {
            System.err.println("Got it!");
        }
    }
}
```
总之，不要对捕获NoClassDefFoundError形成依赖。语言规范非常仔细地描述了类初始化是在何时发生的[JLS 12.4.1]，但是类被加载的时机却显得更加不可预测。更一般地讲，捕获Error及其子类型几乎是完全不恰当的。这些异常是为那些不能被恢复的错误而保留的。