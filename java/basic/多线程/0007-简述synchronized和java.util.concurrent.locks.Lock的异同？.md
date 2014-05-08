主要相同点：Lock能完成synchronized所实现的所有功能 。
主要不同点：Lock有比synchronized更精确的线程语义和更好的性能。synchronized会自动释放锁，而Lock一定要求程序员手工释放，并且必须在finally从句中释放。Lock还有更强大的功能，例如，它的tryLock方法可以非阻塞方式去拿锁。 
举例说明（对下面的题用lock进行了改写）：
```java  
package com.huawei.interview;
import java.util.concurrent.locks.Lock;    import java.util.concurrent.locks.ReentrantLock;   

public class ThreadTest {
	private int j;
	private Lock lock = new ReentrantLock();
	public static void main(String[] args) {
		ThreadTest tt = new ThreadTest();
		for(int i=0;i<2;i++){
			new Thread(tt.new Adder()).start();
			new Thread(tt.new Subtractor()).start();
		}
	}
	private class Subtractor implements Runnable{
		public void run() {
			while(true){
				/*synchronized (ThreadTest.this) {			
					System.out.println(“j--=” + j--);
					//这里抛异常了，锁能释放吗？
				}*/
				lock.lock();
				try{
					System.out.println(“j--=” + j--);
				}finally{
					lock.unlock();
				}
			}
		}
	}
	
	private class Adder implements Runnable{
		public void run() {
			while(true){
				/*synchronized (ThreadTest.this) {
				System.out.println(“j++=” + j++);	
				}*/
				lock.lock();
				try{
					System.out.println(“j++=” + j++);
				}finally{
					lock.unlock();
				}
			}
		}
	}
}
```