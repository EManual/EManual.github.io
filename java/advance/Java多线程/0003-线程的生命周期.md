与人有生老病死一样，线程也同样要经历开始（等待）、运行、挂起和停止四种不同的状态。这四种状态都可以通过Thread类中的方法进行控制。下面给出了Thread类中和这四种状态相关的方法。
```java  
// 开始线程  
public void start( );  
public void run( );  
// 挂起和唤醒线程  
public void resume( );     // 不建议使用  
public void suspend( );    // 不建议使用  
public static void sleep(long millis);  
public static void sleep(long millis, int nanos);   
// 终止线程  
public void stop( );       // 不建议使用  
public void interrupt( );  
// 得到线程状态  
public boolean isAlive( );  
public boolean isInterrupted( );  
public static boolean interrupted( );  
// join方法  
public void join( ) throws InterruptedException;  
```
* 一、创建并运行线程
线程在建立后并不马上执行run方法中的代码，而是处于等待状态。线程处于等待状态时，可以通过Thread类的方法来设置线程不各种属性，如线程的优先级（setPriority）、线程名(setName)和线程的类型（setDaemon）等。
当调用start方法后，线程开始执行run方法中的代码。线程进入运行状态。可以通过Thread类的isAlive方法来判断线程是否处于运行状态。当线程处于运行状态时，isAlive返回true，当isAlive返回false时，可能线程处于等待状态，也可能处于停止状态。下面的代码演示了线程的创建、运行和停止三个状态之间的切换，并输出了相应的isAlive返回值。
```java  
package chapter2;  
public class LifeCycle extends Thread  
{  
   public void run()  
   {  
       int n = 0;  
       while ((++n) < 1000);          
   }  
      
   public static void main(String[] args) throws Exception  
   {  
       LifeCycle thread1 = new LifeCycle();  
       System.out.println(“isAlive: ” + thread1.isAlive());  
       thread1.start();  
       System.out.println(“isAlive: ” + thread1.isAlive());  
       thread1.join();  // 等线程thread1结束后再继续执行   
       System.out.println(“thread1已经结束!”);  
       System.out.println(“isAlive: ” + thread1.isAlive());  
   }  
}  
```
要注意一下，在上面的代码中使用了join方法，这个方法的主要功能是保证线程的run方法完成后程序才继续运行，这个方法将在后面的文章中介绍
上面代码的运行结果：
```java  
isAlive: false
isAlive: true
thread1已经结束!
isAlive: false
```
* 二、挂起和唤醒线程
一但线程开始执行run方法，就会一直到这个run方法执行完成这个线程才退出。但在线程执行的过程中，可以通过两个方法使线程暂时停止执行。这两个方法是suspend和sleep。在使用suspend挂起线程后，可以通过resume方法唤醒线程。而使用sleep使线程休眠后，只能在设定的时间后使线程处于就绪状态（在线程休眠结束后，线程不一定会马上执行，只是进入了就绪状态，等待着系统进行调度）。
虽然suspend和resume可以很方便地使线程挂起和唤醒，但由于使用这两个方法可能会造成一些不可预料的事情发生，因此，这两个方法被标识为deprecated(抗议)标记，这表明在以后的jdk版本中这两个方法可能被删除，所以尽量不要使用这两个方法来操作线程。下面的代码演示了sleep、suspend和resume三个方法的使用。
```java  
package chapter2;  
public class MyThread extends Thread  
{  
   class SleepThread extends Thread  
   {  
       public void run()  
       {  
           try 
           {  
               sleep(2000);  
           }  
           catch (Exception e)  
           {  
           }  
       }  
   }  
	public void run()  
    {  
       while (true)  
           System.out.println(new java.util.Date().getTime());  
    }  
    public static void main(String[] args) throws Exception  
    {  
       MyThread thread = new MyThread();  
       SleepThread sleepThread = thread.new SleepThread();  
       sleepThread.start(); // 开始运行线程sleepThread  
       sleepThread.join();  // 使线程sleepThread延迟2秒  
       thread.start();  
       boolean flag = false;  
       while (true)  
       {  
           sleep(5000);  // 使主线程延迟5秒  
           flag = !flag;  
           if (flag)  
               thread.suspend();   
           else 
               thread.resume();  
       }  
   }  
} 
``` 
从表面上看，使用sleep和suspend所产生的效果类似，但sleep方法并不等同于suspend。它们之间最大的一个区别是可以在一个线程中通过suspend方法来挂起另外一个线程，如上面代码中在主线程中挂起了thread线程。而sleep只对当前正在执行的线程起作用。在上面代码中分别使sleepThread和主线程休眠了2秒和5秒。在使用sleep时要注意，不能在一个线程中来休眠另一个线程。如main方法中使用thread.sleep(2000)方法是无法使thread线程休眠2秒的，而只能使主线程休眠2秒。
在使用sleep方法时有两点需要注意：
1.sleep方法有两个重载形式，其中一个重载形式不仅可以设毫秒，而且还可以设纳秒(1,000,000纳秒等于1毫秒)。但大多数操作系统平台上的Java虚拟机都无法精确到纳秒，因此，如果对sleep设置了纳秒，Java虚拟机将取最接近这个值的毫秒。
2.在使用sleep方法时必须使用throws或try{...}catch{...}。因为run方法无法使用throws，所以只能使用try{...}catch{...}。当在线程休眠的过程中，使用interrupt方法（这个方法将在2.3.3中讨论）中断线程时sleep会抛出一个InterruptedException异常。sleep方法的定义如下：
```java  
public static void sleep(long millis)  throws InterruptedException  
public static void sleep(long millis,  int nanos)  throws InterruptedException 
``` 
* 三、终止线程的三种方法
有三种方法可以使终止线程。
1.使用退出标志，使线程正常退出，也就是当run方法完成后线程终止。
2.使用stop方法强行终止线程（这个方法不推荐使用，因为stop和suspend、resume一样，也可能发生不可预料的结果）。
3.使用interrupt方法中断线程。 
1.使用退出标志终止线程
当run方法执行完后，线程就会退出。但有时run方法是永远不会结束的。如在服务端程序中使用线程进行监听客户端请求，或是其他的需要循环处理的任务。在这种情况下，一般是将这些任务放在一个循环中，如while循环。如果想让循环永远运行下去，可以使用while(true){...}来处理。但要想使while循环在某一特定条件下退出，最直接的方法就是设一个boolean类型的标志，并通过设置这个标志为true或false来控制while循环是否退出。下面给出了一个利用退出标志终止线程的例子。
```java  
package chapter2;  
public class ThreadFlag extends Thread  
{  
    public volatile boolean exit = false;  
 
    public void run()  
    {  
        while (!exit);  
    }  
    public static void main(String[] args) throws Exception  
    {  
        ThreadFlag thread = new ThreadFlag();  
        thread.start();  
		sleep(5000); // 主线程延迟5秒  
		thread.exit = true;  // 终止线程thread  
		thread.join();  
		System.out.println(“线程退出!”);  
	}  
}  
```
在上面代码中定义了一个退出标志exit，当exit为true时，while循环退出，exit的默认值为false。在定义exit时，使用了一个Java关键字volatile，这个关键字的目的是使exit同步，也就是说在同一时刻只能由一个线程来修改exit的值。
2.使用stop方法终止线程
使用stop方法可以强行终止正在运行或挂起的线程。我们可以使用如下的代码来终止线程：
```java  
thread.stop();
```
虽然使用上面的代码可以终止线程，但使用stop方法是很危险的，就象突然关闭计算机电源，而不是按正常程序关机一样，可能会产生不可预料的结果，因此，并不推荐使用stop方法来终止线程。
3.使用interrupt方法终止线程
使用interrupt方法来终端线程可分为两种情况：
（1）线程处于阻塞状态，如使用了sleep方法。
（2）使用while(!isInterrupted()){...}来判断线程是否被中断。
在第一种情况下使用interrupt方法，sleep方法将抛出一个InterruptedException例外，而在第二种情况下线程将直接退出。下面的代码演示了在第一种情况下使用interrupt方法。
```java  
package chapter2;  
public class ThreadInterrupt extends Thread  
{  
	public void run()  
	{  
        try 
	    {  
			sleep(50000);  // 延迟50秒  
		}  
        catch (InterruptedException e)  
        {  
           System.out.println(e.getMessage());  
        }  
    }  
    public static void main(String[] args) throws Exception  
    {  
		Thread thread = new ThreadInterrupt();  
        thread.start();  
        System.out.println(“在50秒之内按任意键中断线程!”);  
        System.in.read();  
        thread.interrupt();  
        thread.join();  
        System.out.println(“线程已经退出!”);  
    }  
}  
```
上面代码的运行结果如下：
在50秒之内按任意键中断线程!
sleep interrupted
线程已经退出!
在调用interrupt方法后， sleep方法抛出异常，然后输出错误信息：sleep interrupted。
注意：在Thread类中有两个方法可以判断线程是否通过interrupt方法被终止。一个是静态的方法interrupted()，一个是非静态的方法isInterrupted()，这两个方法的区别是interrupted用来判断当前线是否被中断，而isInterrupted可以用来判断其他线程是否被中断。因此，while (!isInterrupted())也可以换成while (!Thread.interrupted())。
以上就是线程的生命周期。要进一步学习Java多线程，务必要对Java线程生命周期有着足够的认识。