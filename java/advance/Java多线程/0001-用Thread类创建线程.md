在Java中创建线程有两种方法：使用Thread类和使用Runnable接口。在使用Runnable接口时需要建立一个Thread实例。因此，无论是通过Thread类还是Runnable接口建立线程，都必须建立Thread类或它的子类的实例。Thread类的构造方法被重载了八次，构造方法如下：
```java  
1.public Thread( );  
2.public Thread(Runnable target);  
3.public Thread(String name);  
4.public Thread(Runnable target, String name);  
5.public Thread(ThreadGroup group, Runnable target);  
6.public Thread(ThreadGroup group, String name);  
7.public Thread(ThreadGroup group, Runnable target, String name);  
8.public Thread(ThreadGroup group, Runnable target, String name, long stackSize); 
```
* Runnable target
实现了Runnable接口的类的实例。要注意的是Thread类也实现了Runnable接口，因此，从Thread类继承的类的实例也可以作为target传入这个构造方法。
* String name
线程的名子。这个名子可以在建立Thread实例后通过Thread类的setName方法设置。如果不设置线程的名子，线程就使用默认的线程名：Thread-N，N是线程建立的顺序，是一个不重复的正整数。
* ThreadGroup group
当前建立的线程所属的线程组。如果不指定线程组，所有的线程都被加到一个默认的线程组中。关于线程组的细节将在后面的章节详细讨论。
* long stackSize
线程栈的大小，这个值一般是CPU页面的整数倍。如x86的页面大小是4KB。在x86平台下，默认的线程栈大小是12KB。
一个普通的Java类只要从Thread类继承，就可以成为一个线程类。并可通过Thread类的start方法来执行线程代码。虽然Thread类的子类可以直接实例化，但在子类中必须要覆盖Thread类的run方法才能真正运行线程的代码。下面的代码给出了一个使用Thread类建立线程的例子：
```java  
package mythread;     
public class Thread1 extends Thread  
  {  
      public void run()  
      {  
          System.out.println(this.getName());  
      }  
      public static void main(String[] args)  
      {  
          System.out.println(Thread.currentThread().getName());  
          Thread1 thread1 = new Thread1();  
          Thread1 thread2 = new Thread1 ();  
          thread1.start();  
          thread2.start();  
      }  
  } 
//
Thread.currentThread() 
          返回对当前正在执行的线程对象的引用。
```
上面的代码建立了两个线程：thread1和thread2。上述代码中的005至008行是Thread1类的run方法。当在014和015行调用start方法时，系统会自动调用run方法。在007行使用this.getName()输出了当前线程的名字，由于在建立线程时并未指定线程名，因此，所输出的线程名是系统的默认值，也就是Thread-n的形式。在011行输出了主线程的线程名。
上面代码的运行结果如下：
```java  
main
Thread-0
Thread-1
```
从上面的输出结果可以看出，第一行输出的main是主线程的名子。后面的Thread-1和Thread-2分别是thread1和thread2的输出结果。
注意：任何一个Java程序都必须有一个主线程。一般这个主线程的名子为main。只有在程序中建立另外的线程，才能算是真正的多线程程序。也就是说，多线程程序必须拥有一个以上的线程。
Thread类有一个重载构造方法可以设置线程名。除了使用构造方法在建立线程时设置线程名，还可以使用Thread类的setName方法修改线程名。要想通过Thread类的构造方法来设置线程名，必须在Thread的子类中使用Thread类的public Thread(String name)构造方法，因此，必须在Thread的子类中也添加一个用于传入线程名的构造方法。下面的代码给出了一个设置线程名的例子：
```java  
package mythread;  	 
public class Thread2 extends Thread  
{  
    private String who;  
    public void run()  
    {  
        System.out.println(who + “:” + this.getName());  
    }  
    public Thread2(String who)  
    {  
        super();  
        this.who = who;  
    }  
    public Thread2(String who, String name)  
    {  
        super(name);  
        this.who = who;  
    }  
    public static void main(String[] args)  
    {  
        Thread2 thread1 = new Thread2 (“thread1”, “MyThread1”);  
        Thread2 thread2 = new Thread2 (“thread2”);  
        Thread2 thread3 = new Thread2 (“thread3”);  
        thread2.setName(“MyThread2”);  
        thread1.start();  
        thread2.start();  
        thread3.start();  
    }  
```
在类中有两个构造方法：
第034行：public sample2_2(String who)
这个构造方法有一个参数：who。这个参数用来标识当前建立的线程。在这个构造方法中仍然调用Thread的默认构造方法public Thread( )。
第016行：public sample2_2(String who, String name)
这个构造方法中的who和第一个构造方法的who的含义一样，而name参数就是线程的名名。在这个构造方法中调用了Thread类的public Thread(String name)构造方法，也就是第043行的super(name)。
在main方法中建立了三个线程：thread1、thread2和thread3。其中thread1通过构造方法来设置线程名，thread2通过setName方法来修改线程名，thread3未设置线程名。
运行结果如下： 
```java  
thread1:MyThread1
thread2:MyThread2
thread3:Thread-1
```
从上面的输出结果可以看出，thread1和thread2的线程名都已经修改了，而thread3的线程名仍然为默认值：Thread-1。thread3的线程名之所以不是Thread-2，而是Thread-1，这是因为在051行已经指定了thread2的Name，因此，启动thread3时就将thread3的线程名设为Thread-1。因此就会得到上面的输出结果。 
注意：在调用start方法前后都可以使用setName设置线程名，但在调用start方法后使用setName修改线程名，会产生不确定性，也就是说可能在run方法执行完后才会执行setName。如果在run方法中要使用线程名，就会出现虽然调用了setName方法，但线程名却未修改的现象。
Thread类的start方法不能多次调用，如不能调用两次thread1.start()方法。否则会抛出一个IllegalThreadStateException异常。