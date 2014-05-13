在上面的例子中多次使用到了Thread类的join方法。我想大家可能已经猜出来join方法的功能是什么了。对，join方法的功能就是使异步执行的线程变成同步执行。也就是说，当调用线程实例的start方法后，这个方法会立即返回，如果在调用start方法后后需要使用一个由这个线程计算得到的值，就必须使用join方法。如果不使用join方法，就不能保证当执行到start方法后面的某条语句时，这个线程一定会执行完。而使用join方法后，直到这个线程退出，程序才会往下执行。下面的代码演示了join的用法。 
```java  
package mythread;  
public class JoinThread extends Thread  
{  
    public static int n = 0;  
    static synchronized void inc()  
    {  
        n++;  
    }  
    public void run()  
    {  
       for (int i = 0; i < 10; i++)  
            try 
            {  
                inc();  
                sleep(3);  // 为了使运行结果更随机，延迟3毫秒  
                  
            }  
            catch (Exception e)  
            {  
            }                                        
    }  
    public static void main(String[] args) throws Exception  
    {  
        Thread threads[] = new Thread[100];  
        for (int i = 0; i < threads.length; i++)  // 建立100个线程  
            threads[i] = new JoinThread();  
        for (int i = 0; i < threads.length; i++)   // 运行刚才建立的100个线程  
            threads[i].start();  
        if (args.length > 0)    
            for (int i = 0; i < threads.length; i++)   // 100个线程都执行完后继续  
                threads[i].join();  
        System.out.println(“n=” + JoinThread.n);  
    }  
} 
``` 
在例程2-8中建立了100个线程，每个线程使静态变量n增加10。如果在这100个线程都执行完后输出n，这个n值应该是1000。
1.测试1
使用如下的命令运行上面程序：
```java  
java mythread.JoinThread 
```
程序的运行结果如下：
```java  
n=442
```
这个运行结果可能在不同的运行环境下有一些差异，但一般n不会等于1000。从上面的结果可以肯定，这100个线程并未都执行完就将n输出了。
2.测试2
使用如下的命令运行上面的代码：
在上面的命令行中有一个参数join，其实在命令行中可以使用任何参数，只要有一个参数就可以，这里使用join，只是为了表明要使用join方法使这100个线程同步执行。
程序的运行结果如下：
n=1000
无论在什么样的运行环境下运行上面的命令，都会得到相同的结果：n=1000。这充分说明了这100个线程肯定是都执行完了，因此，n一定会等于1000。