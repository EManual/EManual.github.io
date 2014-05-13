实现Runnable接口的类必须使用Thread类的实例才能创建线程。通过Runnable接口创建线程分为两步：
1.将实现Runnable接口的类实例化。
2.建立一个Thread对象，并将第一步实例化后的对象作为参数传入Thread类的构造方法。
最后通过Thread类的start方法建立线程。
下面的代码演示了如何使用Runnable接口来创建线程：
```java  
package mythread;  
public class MyRunnable implements Runnable  
{  
    public void run()  
    {  
        System.out.println(Thread.currentThread().getName());  
    }  
    public static void main(String[] args)  
    {  
       MyRunnable t1 = new MyRunnable();  
       MyRunnable t2 = new MyRunnable();  
       Thread thread1 = new Thread(t1, “MyThread1”);  
       Thread thread2 = new Thread(t2);  
       thread2.setName(“MyThread2”);  
       thread1.start();  
       thread2.start();  
   }  
}  
```
上面代码的运行结果如下：
```java  
MyThread1
MyThread2
```
举例Java多线程的学习又更近一步了。