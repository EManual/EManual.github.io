文本到这里，所举的例子无一例外都与如何获取类的信息有关。我们也可以用 reflection 来做一些其它的事情，比如执行一个指定了名称的方法。下面的示例演示了这一操作：
```java  
import java.lang.reflect.*;
public class method2 {
	public int add(int a, int b) {
	return a + b;
	}
	public static void main(String args[]) {
		try {
			Class cls = Class.forName("method2");
			Class partypes[] = new Class[2];
			partypes[0] = Integer.TYPE;
			partypes[1] = Integer.TYPE;
			Method meth = cls.getMethod("add", partypes);
			method2 methobj = new method2();
			Object arglist[] = new Object[2];
			arglist[0] = new Integer(37);
			arglist[1] = new Integer(47);
			Object retobj = meth.invoke(methobj, arglist);
			Integer retval = (Integer) retobj;
			System.out.println(retval.intValue());
		} catch (Throwable e) {
			System.err.println(e);
		}
	}
}
```
假如一个程序在执行的某处的时候才知道需要执行某个方法，这个方法的名称是在程序的运行过程中指定的 (例如，JavaBean开发环境中就会做这样的事)，那么上面的程序演示了如何做到。
上例中，getMethod用于查找一个具有两个整型参数且名为add的方法。找到该方法并创建了相应的Method 对象之后，在正确的对象实例中执行它。执行该方法的时候，需要提供一个参数列表，这在上例中是分别包装了整数37和47的两个 Integer对象。执行方法的返回的同样是一个 Integer对象，它封装了返回值84。