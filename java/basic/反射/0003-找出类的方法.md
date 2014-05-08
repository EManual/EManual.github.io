找出一个类中定义了些什么方法，这是一个非常有价值也非常基础的 reflection 用法。下面的代码就实现了这一用法：
```java  
import java.lang.reflect.*;
public class method1 {
	private int f1(Object p, int x) throws NullPointerException {
	if (p == null)
		throw new NullPointerException();
	return x;
	}

	public static void main(String args[]) {
		try {
			Class cls = Class.forName("method1");
			Method methlist[] = cls.getDeclaredMethods();
			for (int i = 0; i < methlist.length; i++) {
				Method m = methlist[i];
				System.out.println("name = " + m.getName());
				System.out.println("decl class = " + m.getDeclaringClass());
				Class pvec[] = m.getParameterTypes();
				for (int j = 0; j < pvec.length; j++)
					System.out.println("param #" + j + " " + pvec[j]);
				Class evec[] = m.getExceptionTypes();
				for (int j = 0; j < evec.length; j++)
					System.out.println("exc #" + j + " " + evec[j]);
				System.out.println("return type = " + m.getReturnType());
				System.out.println("-----");
			}
		} catch (Throwable e) {
			System.err.println(e);
		}
	}
}
```
这个程序首先取得 method1 类的描述，然后调用 getDeclaredMethods 来获取一系列的 Method 对象，它们分别描述了定义在类中的每一个方法，包括 public 方法、protected 方法、package 方法和 private 方法等。如果你在程序中使用 getMethods 来代替 getDeclaredMethods，你还能获得继承来的各个方法的信息。 
取得了 Method 对象列表之后，要显示这些方法的参数类型、异常类型和返回值类型等就不难了。这些类型是基本类型还是类类型，都可以由描述类的对象按顺序给出。
输出的结果如下：
```java  
name = f1
decl class = class method1
param #0 class java.lang.Object
param #1 int
exc #0 class java.lang.NullPointerException
return type = int
-----
name = main
decl class = class method1
param #0 class [Ljava.lang.String;
return type = void
```