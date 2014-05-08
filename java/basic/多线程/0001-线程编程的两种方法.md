写一个类，继承Thread类，覆盖Thread类中继承来的run()方法，这样就写好了自定义的线程类。
继承java.lang.Thread类：
```java  
	class MyThread extends Thread{
		public void run(){		       //覆盖run()，线程体方法，自身其实就是普通的方法
			.......
		}
	}
```
启动线程：
```java  
	public class TestThread{
		public static void main(){
			Thread t1=new Mythread();
			T1.start();		           //调用start()来启动线程，线程启动方法，向线程调度器说明当前线程已经准备好了，是一种可运行状态
		}
	}
```	
写一个类，实现Runable接口，实现其中的run()方法。这种方法写好的类的对象需要作为线程类创建对象时构造方法的参数。
实现java.lang.Runnable接口：
```java  
	Class MyThread  implements Runnable{
		public void run(){
		}
	}
```
启动线程：
```java  
	public class TestThread{
		public static void main(){
			Runnable myThread = new MyThread();
			Thread t = new Thread(myThread);
			t.start();
		}
	}
```
从java5开始，还有如下一些线程池创建多线程的方式：
```java  
ExecutorService pool = Executors.newFixedThreadPool(3)
for(int i=0;i<10;i++){
  pool.execute(new Runable(){	public void run(){		}  });
}
Executors.newCachedThreadPool().execute(new Runable(){	public void run(){	}});
Executors.newSingleThreadExecutor().execute(new Runable(){	public void run(){	}});
```