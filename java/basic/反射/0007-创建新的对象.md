对于构造器，则不能像执行方法那样进行，因为执行一个构造器就意味着创建了一个新的对象 (准确的说，创建一个对象的过程包括分配内存和构造对象)。所以，与上例最相似的例子如下：
```java  
import java.lang.reflect.*;    
public class constructor2 {
	public constructor2() {
	}

	public constructor2(int a, int b) {
		System.out.println("a = " + a + " b = " + b);
	}
	public static void main(String args[]) {
		try {
			Class cls = Class.forName("constructor2");
			Class partypes[] = new Class[2];
			partypes[0] = Integer.TYPE;
			partypes[1] = Integer.TYPE;
			Constructor ct = cls.getConstructor(partypes);
			Object arglist[] = new Object[2];
			arglist[0] = new Integer(37);
			arglist[1] = new Integer(47);
			Object retobj = ct.newInstance(arglist);
		} catch (Throwable e) {
			System.err.println(e);
		}
	}
}
```
根据指定的参数类型找到相应的构造函数并执行它，以创建一个新的对象实例。使用这种方法可以在程序运行时动态地创建对象，而不是在编译的时候创建对象，这一点非常有价值。