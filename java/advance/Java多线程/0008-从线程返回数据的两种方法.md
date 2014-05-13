从线程中返回数据和向线程传递数据类似。也可以通过类成员以及回调函数来返回数据。但类成员在返回数据和传递数据时有一些区别，下面让我们来看看它们区别在哪。
一、通过类变量和方法返回数据
使用这种方法返回数据需要在调用start方法后才能通过类变量或方法得到数据。让我们先来看看例程2-13会得到什么结果。
```java  
package mythread;  
public class MyThread extends Thread  
{  
    private String value1;  
    private String value2;  
    public void run()  
    {  
        value1 = “通过成员变量返回数据”;  
        value2 = “通过成员方法返回数据”;  
    }  
    public static void main(String[] args) throws Exception  
    {  
        MyThread thread = new MyThread();  
        thread.start();  
        System.out.println(“value1:” + thread.value1);  
        System.out.println(“value2:” + thread.value2);  
    }  
}  
```
运行上面的代码有可能输出如下的结果：
```java  
		value1:null
		value2:null
```
从上面的运行结果看很不正常。在run方法中已经对value1和value2赋了值，而返回的却是null。发生这种情况的原因是调用start方法后就立刻输出了value1和value2的值，而这里run方法还没有执行到为value1和value2赋值的语句。要避免这种情况的发生，就需要等run方法执行完后才执行输出value1和value2的代码。因此，我们可以想到使用sleep方法将主线程进行延迟，如可以在thread.start()后加一行如下的语句：
```java  
		sleep(1000);
```
这样做可以使主线程延迟1秒后再往下执行，但这样做有一个问题，就是我们怎么知道要延迟多长时间。在这个例子的run方法中只有两条赋值语句，而且只创建了一个线程，因此，延迟1秒已经足够，但如果run方法中的语句很复杂，这个时间就很难预测，因此，这种方法并不稳定。
我们的目的就是得到value1和value2的值，因此，只要判断value1和value2是否为null。如果它们都不为null时，就可以输出这两个值了。
我们可以使用如下的代码来达到这个目的：
while (thread.value1 == null || thread.value2 == null); 
使用上面的语句可以很稳定地避免这种情况发生，但这种方法太耗费系统资源。大家可以设想，如果run方法中的代码很复杂，value1和value2需要很长时间才能被赋值，这样while循环就必须一直执行下去，直到value1和value2都不为空为止。因此，我们可以对上面的语句做如下的改进：
```java  
while (thread.value1 == null || thread.value2 == null)  
   sleep(100); 
```
在while循环中第判断一次value1和value2的值后休眠100毫秒，然后再判断这两个值。这样所占用的系统资源会小一些。上面的方法虽然可以很好地解决，但Java的线程模型为我们提供了更好的解决方案，这就是join方法。在前面已经讨论过，join的功能就是使用线程从异步执行变成同步执行。当线程变成同步执行后，就和从普通的方法中得到返回数据没有什么区别了。因此，可以使用如下的代码更有效地解决这个问题：
```java  
		thread.start();
		thread.join();
```
在thread.join()执行完后，线程thread的run方法已经退出了，也就是说线程thread已经结束了。因此，在thread.join()后面可以放心大胆地使用MyThread类的任何资源来得到返回数据。 
二、通过回调函数返回数据
其实这种方法已经在《向线程传递数据的三种方法》中介绍了。在《向线程传递数据的三种方法》一文的例子中通过Work类的process方法向线程中传递了计算结果，但同时，也通过process方法从线程中得到了三个随机数。因此，这种方法既可以向线程中传递数据，也可以从线程中获得数据。