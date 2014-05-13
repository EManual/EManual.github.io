volatile关键字相信了解Java多线程的读者都很清楚它的作用。volatile关键字用于声明简单类型变量，如int、float、boolean等数据类型。如果这些简单数据类型声明为volatile，对它们的操作就会变成原子级别的。但这有一定的限制。例如，下面的例子中的n就不是原子级别的：
```java  
package mythread;  
public class JoinThread extends Thread  
{      public static volatile int n = 0;  
    public void run()  
    {  
        for (int i = 0; i < 10; i++)  
            try 
        {  
                n = n + 1;  
                sleep(3); // 为了使运行结果更随机，延迟3毫秒  
             }  
            catch (Exception e)  
            {  
            }  
    }  
 
    public static void main(String[] args) throws Exception  
    {  
        Thread threads[] = new Thread[100];  
        for (int i = 0; i < threads.length; i++)  
            // 建立100个线程  
            threads[i] = new JoinThread();  
        for (int i = 0; i < threads.length; i++)  
            // 运行刚才建立的100个线程  
            threads[i].start();  
        for (int i = 0; i < threads.length; i++)  
            // 100个线程都执行完后继续  
            threads[i].join();  
        System.out.println(“n=” + JoinThread.n);  
    }  
}  
```       
如果对n的操作是原子级别的，最后输出的结果应该为n=1000，而在执行上面积代码时，很多时侯输出的n都小于1000，这说明n=n+1不是原子级别的操作。原因是声明为volatile的简单变量如果当前值由该变量以前的值相关，那么volatile关键字不起作用，也就是说如下的表达式都不是原子操作：
n = n + 1;
n++;
如果要想使这种情况变成原子操作，需要使用synchronized关键字，如上的代码可以改成如下的形式：
```java  
package mythread;  
public class JoinThread extends Thread  
{  
    public static int n = 0;  
     public static synchronized void inc()  
    {  
        n++;  
    }  
    public void run()  
    {  
        for (int i = 0; i < 10; i++)  
            try 
            {  
                inc(); // n = n + 1 改成了 inc();  
                sleep(3); // 为了使运行结果更随机，延迟3毫秒   
            }  
            catch (Exception e)  
            {  
            }  
    }  
 
    public static void main(String[] args) throws Exception  
    {  
        Thread threads[] = new Thread[100];  
        for (int i = 0; i < threads.length; i++)  
            // 建立100个线程  
            threads[i] = new JoinThread();  
        for (int i = 0; i < threads.length; i++)  
            // 运行刚才建立的100个线程  
            threads[i].start();  
        for (int i = 0; i < threads.length; i++)  
            // 100个线程都执行完后继续  
            threads[i].join();  
        System.out.println(“n=” + JoinThread.n);  
    }  
}  
```
上面的代码将n=n+1改成了inc()，其中inc方法使用了synchronized关键字进行方法同步。因此，在使用volatile关键字时要慎重，并不是只要简单类型变量使用volatile修饰，对这个变量的所有操作都是原来操作，当变量的值由自身的上一个决定时，如n=n+1、n++等，volatile关键字将失效，只有当变量的值和自身上一个值无关时对该变量的操作才是原子级别的，如n = m + 1，这个就是原级别的。所以在使用volatile关键时一定要谨慎，如果自己没有把握，可以使用synchronized来代替volatile。