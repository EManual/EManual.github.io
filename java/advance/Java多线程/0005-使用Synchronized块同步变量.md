我们可以通过synchronized块来同步特定的静态或非静态方法。要想实现这种需求必须为这些特性的方法定义一个类变量，然后将这些方法的代码用synchronized块括起来，并将这个类变量作为参数传入synchronized块。下面的代码演示了如何同步特定的类方法：
```java  
package mythread;  
public class SyncThread extends Thread  
{  
    private static String sync = “”;  
    private String methodType = “”;  
    private static void method(String s)  
    {  
        synchronized (sync)  
        {  
            sync = s;  
            System.out.println(s);  
            while (true);  
        }  
    }  
    public void method1()  
    {  
        method(“method1”);  
    }  
    public static void staticMethod1()  
    {  
        method(“staticMethod1”);  
    }  
    public void run()  
    {  
       if (methodType.equals(“static”))  
            staticMethod1();  
        else if (methodType.equals(“nonstatic”))  
            method1();  
    }  
    public SyncThread(String methodType)  
    {  
        this.methodType = methodType;  
    }  
    public static void main(String[] args) throws Exception  
    {  
        SyncThread sample1 = new SyncThread(“nonstatic”);  
        SyncThread sample2 = new SyncThread(“static”);  
        sample1.start();  
        sample2.start();  
    }  
} 
```
运行结果如下：
```java  
method1
staticMethod1
```
看到上面的运行结果很多读者可能感到惊奇。在上面的代码中method1和staticMethod1方法使用了静态字符串变量sync进行同步。这两个方法只能有一个同时执行，而这两个方法都会执行014行的无限循环语句。因此，输出结果只能是method1和staticMethod1其中之一。但这个程序将这两个字符串都输出了。
出现这种结果的愿意很简单，我们看一下012行就知道了。原来在这一行将sync的值改变了。在这里要说一下Java中的String类型。String类型和Java中其他的复杂类型不同。在使用String型变量时，只要给这个变量赋一次值，Java就会创建个新的String类型的实例。如下面的代码所示：
```java  
String s = “hello”;  
System.out.println(s.hashCode());  
s = “world”;  
System.out.println(s.hashCode());   
```
在上面的代码中。第一个s和再次赋值后的s的hashCode的值是不一样的。由于创建String类的实例并不需要使用new，因此，在同步String类型的变量时要注意不要给这个变量赋值，否则会使变量无法同步。
由于在013行已经为sync创建了一个新的实例，假设method1先执行，当method1方法执行了013行的代码后，sync的值就已经不是最初那个值了，而method1方法锁定的仍然是sync变量最初的那个值。而在这时，staticMethod1正好执行到synchronized(sync)，在staticMethod1方法中要锁定的这个sync和method1方法锁定的sync已经不是一个了，因此，这两个方法的同步性已经被破坏了。
解决以上问题的方法当然是将013行去掉。在本例中加上这行，只是为了说明使用类变量来同步方法时如果在synchronized块中将同步变量的值改变，就会破坏方法之间的同步。为了彻底避免这种情况发生，在定义同步变量时可以使用final关键字。如将上面的程序中的005行可改成如下形式：
```java  
private final static String sync = “”;  
```
使用final关键字后，sync只能在定义时为其赋值，并且以后不能再修改。如果在程序的其他地方给sync赋了值，程序就无法编译通过。在Eclipse等开发工具中，会直接在错误的地方给出提示。
我们可以从两个角度来理解synchronized块。如果从类方法的角度来理解，可以通过类变量来同步相应的方法。如果从类变量的角度来理解，可以使用synchronized块来保证某个类变量同时只能被一个方法访问。不管从哪个角度来理解，它们的实质都是一样的，就是利用类变量来获得同步锁，通过同步锁的互斥性来实现同步。
注意：在使用synchronized块时应注意，synchronized块只能使用对象作为它的参数。如果是简单类型的变量(如int、char、boolean等)，不能使用synchronized来同步。