获取类构造器的用法与上述获取方法的用法类似，如：
```java  
import java.lang.reflect.*;
public class constructor1 {
	public constructor1() {
	}
	protected constructor1(int i, double d) {
	}

	public static void main(String args[]) {
		try {
			Class cls = Class.forName("constructor1");
			Constructor ctorlist[] = cls.getDeclaredConstructors();
			for (int i = 0; i < ctorlist.length; i++) {
			Constructor ct = ctorlist[i];
			System.out.println("name = " + ct.getName());
			System.out.println("decl class = " + ct.getDeclaringClass());
			Class pvec[] = ct.getParameterTypes();
			for (int j = 0; j < pvec.length; j++)
			System.out.println("param #" + j + " " + pvec[j]);
			Class evec[] = ct.getExceptionTypes();
			for (int j = 0; j < evec.length; j++)
			System.out.println("exc #" + j + " " + evec[j]);
			System.out.println("-----");
			}
		} catch (Throwable e) {
			System.err.println(e);
		}
	}
}
```
这个例子中没能获得返回类型的相关信息，那是因为构造器没有返回类型。
这个程序运行的结果是：
```java  
name = constructor1
decl class = class constructor1
-----
name = constructor1
decl class = class constructor1
param #0 int
param #1 double
```