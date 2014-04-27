考虑下面这个简单的例子，让我们看看 reflection 是如何工作的。
```java  
import java.lang.reflect.*;
public class DumpMethods {
public static void main(String args[]) {
	try {
		Class c = Class.forName(args[0]);
		Method m[] = c.getDeclaredMethods();
		for (int i = 0; i < m.length; i++)
		System.out.println(m[i].toString());
	} catch (Throwable e) {
		System.err.println(e);
	}
	}
}
```
按如下语句执行：
```java  
java DumpMethods java.util.Stack
```
它的结果输出为：
```java  
public java.lang.Object java.util.Stack.push(java.lang.Object)
public synchronized java.lang.Object java.util.Stack.pop()
public synchronized java.lang.Object java.util.Stack.peek()
public boolean java.util.Stack.empty()
public synchronized int java.util.Stack.search(java.lang.Object)
```
这样就列出了java.util.Stack 类的各方法名以及它们的限制符和返回类型。
这个程序使用 Class.forName 载入指定的类，然后调用 getDeclaredMethods 来获取这个类中定义了的方法列表。
java.lang.reflect.Methods 是用来描述某个类中单个方法的一个类。