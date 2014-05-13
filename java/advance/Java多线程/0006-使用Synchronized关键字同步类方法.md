要想解决“脏数据”的问题，最简单的方法就是使用synchronized关键字来使run方法同步，代码如下：
```java  
public synchronized void run()  
{  

} 
```
从上面的代码可以看出，只要在void和public之间加上synchronized关键字，就可以使run方法同步，也就是说，对于同一个Java类的对象实例，run方法同时只能被一个线程调用，并当前的run执行完后，才能被其他的线程调用。即使当前线程执行到了run方法中的yield方法，也只是暂停了一下。由于其他线程无法执行run方法，因此，最终还是会由当前的线程来继续执行。先看看下面的代码：
sychronized关键字只和一个对象实例绑定
```java  
class Test  
{  
     public synchronized void method()  
     {  
            
     }  
}  
   
public class Sync implements Runnable  
{  
    private Test test;  
    public void run()  
    {  
      test.method();  
	}  
    public Sync(Test test)  
    {  
        this.test = test;  
    }  
    public static void main(String[] args) throws Exception  
    {  
        Test test1 =  new Test();  
        Test test2 =  new Test();  
        Sync sync1 = new Sync(test1);  
        Sync sync2 = new Sync(test2);  
        new Thread(sync1).start();  
        new Thread(sync2).start();   
    }  
} 
```
在Test类中的method方法是同步的。但上面的代码建立了两个Test类的实例，因此，test1和test2的method方法是分别执行的。要想让method同步，必须在建立Sync类的实例时向它的构造方法中传入同一个Test类的实例，如下面的代码所示：
```java  
Sync sync1 = new Sync(test1);     
```
不仅可以使用synchronized来同步非静态方法，也可以使用synchronized来同步静态方法。如可以按如下方式来定义method方法：
```java  
class Test   
{  
    public static synchronized void method() {   }  
} 
```
建立Test类的对象实例如下：
```java  
Test test = new Test(); 
```
对于静态方法来说，只要加上了synchronized关键字，这个方法就是同步的，无论是使用test.method()，还是使用Test.method()来调用method方法，method都是同步的，并不存在非静态方法的多个实例的问题。
在23种设计模式中的单件（Singleton）模式如果按传统的方法设计，也是线程不安全的，下面的代码是一个线程不安全的单件模式。
```java  
package test;  
// 线程不安全的Singleton模式       class Singleton     
{  
    private static Singleton sample;  
    private Singleton()  
    {  
    }  
    public static Singleton getInstance()  
    {  
        if (sample == null)  
        {  
           Thread.yield(); // 为了放大Singleton模式的线程不安全性  
           sample = new Singleton();  
        }  
        return sample;  
    }  
}  
public class MyThread extends Thread  
{  
    public void run()  
    {  
        Singleton singleton = Singleton.getInstance();  
        System.out.println(singleton.hashCode());  
    }  
    public static void main(String[] args)  
    {  
        Thread threads[] = new Thread[5];  
        for (int i = 0; i < threads.length; i++)  
            threads[i] = new MyThread();  
        for (int i = 0; i < threads.length; i++)  
            threads[i].start();  
    }  
}  
```
在上面的代码调用yield方法是为了使单件模式的线程不安全性表现出来，如果将这行去掉，上面的实现仍然是线程不安全的，只是出现的可能性小得多。
程序的运行结果如下：
```java  
25358555
26399554
7051261
29855319
5383406
```
上面的运行结果可能在不同的运行环境上有所有同，但一般这五行输出不会完全相同。从这个输出结果可以看出，通过getInstance方法得到的对象实例是五个，而不是我们期望的一个。这是因为当一个线程执行了Thread.yield()后，就将CPU资源交给了另外一个线程。由于在线程之间切换时并未执行到创建Singleton对象实例的语句，因此，这几个线程都通过了if判断，所以，就会产生了建立五个对象实例的情况（可能创建的是四个或三个对象实例，这取决于有多少个线程在创建Singleton对象之前通过了if判断，每次运行时可能结果会不一样）。
要想使上面的单件模式变成线程安全的，只要为getInstance加上synchronized关键字即可。代码如下：
public static synchronized Singleton getInstance() {   } 
当然，还有更简单的方法，就是在定义Singleton变量时就建立Singleton对象，代码如下：
private static final Singleton sample = new Singleton(); 
然后在getInstance方法中直接将sample返回即可。这种方式虽然简单，但不知在getInstance方法中创建Singleton对象灵活。读者可以根据具体的需求选择使用不同的方法来实现单件模式。
在使用synchronized关键字时有以下四点需要注意：
1.synchronized关键字不能继承。
虽然可以使用synchronized来定义方法，但synchronized并不属于方法定义的一部分，因此，synchronized关键字不能被继承。如果在父类中的某个方法使用了synchronized关键字，而在子类中覆盖了这个方法，在子类中的这个方法默认情况下并不是同步的，而必须显式地在子类的这个方法中加上synchronized关键字才可以。当然，还可以在子类方法中调用父类中相应的方法，这样虽然子类中的方法不是同步的，但子类调用了父类的同步方法，因此，子类的方法也就相当于同步了。这两种方式的例子代码如下：
在子类方法中加上synchronized关键字
```java  
class Parent  
{  
    public synchronized void method() {   }  
}  
class Child extends Parent  
{  
    public synchronized void method() {   }  
} 
```
在子类方法中调用父类的同步方法
```java  
class Parent  
{  
    public synchronized void method() {   }  
}  
class Child extends Parent  
{  
    public void method() { super.method();   }  
} 
```
2.在定义接口方法时不能使用synchronized关键字。
3.构造方法不能使用synchronized关键字，但可以使用下节要讨论的synchronized块来进行同步。
4.synchronized可以自由放置。
在前面的例子中使用都是将synchronized关键字放在方法的返回类型前面。但这并不是synchronized可放置唯一位置。在非静态方法中，synchronized还可以放在方法定义的最前面，在静态方法中，synchronized可以放在static的前面，代码如下：
```java  
public synchronized void method();  
synchronized public void method();  
public static synchronized void method();  
public synchronized static void method();  
synchronized public static void method(); 
```
但要注意，synchronized不能放在方法返回类型的后面，如下面的代码是错误的：
```java  
public void synchronized method();  
public static void synchronized method(); 
```
synchronized关键字只能用来同步方法，不能用来同步类变量，如下面的代码也是错误的。
```java  
public synchronized int n = 0;  
public static synchronized int n = 0; 
```
虽然使用synchronized关键字同步方法是最安全的同步方式，但大量使用synchronized关键字会造成不必要的资源消耗以及性能损失。虽然从表面上看synchronized锁定的是一个方法，但实际上synchronized锁定的是一个类。也就是说，如果在非静态方法method1和method2定义时都使用了synchronized，在method1未执行完之前，method2是不能执行的。静态方法和非静态方法的情况类似。但静态和非静态方法不会互相影响。看看如下的代码：
```java  
package test;  
public class MyThread1 extends Thread  
{  
	public String methodName;  
	public static void method(String s)  
	{  
		System.out.println(s);  
		while (true);  
	}  
	public synchronized void method1()  
	{  
		method(“非静态的method1方法”);  
	}  
    public synchronized void method2()  
    {  
        method(“非静态的method2方法”);  
    }  
    public static synchronized void method3()  
    {  
        method(“静态的method3方法”);  
    }  
    public static synchronized void method4()  
    {  
        method(“静态的method4方法”);  
    }  
    public void run()  
    {  
       try 
       {  
           getClass().getMethod(methodName).invoke(this);  
	   }  
       catch (Exception e)  
        {  
        }  
    }  
	public static void main(String[] args) throws Exception  
    {  
        MyThread1 myThread1 = new MyThread1();  
        for (int i = 1; i <= 4; i++)  
        {  
            myThread1.methodName = “method” + String.valueOf(i);  
            new Thread(myThread1).start();  
            sleep(100);  
        }  
    }  
}  
```
运行结果如下：
非静态的method1方法
静态的method3方法
从上面的运行结果可以看出，method2和method4在method1和method3未结束之前不能运行。因此，我们可以得出一个结论，如果在类中使用synchronized关键字来定义非静态方法，那将影响这个中的所有使用synchronized关键字定义的非静态方法。如果定义的是静态方法，那么将影响类中所有使用synchronized关键字定义的静态方法。这有点象数据表中的表锁，当修改一条记录时，系统就将整个表都锁住了，因此，大量使用这种同步方式会使程序的性能大幅度下降。