reflection 的还有一个用处就是改变对象数据字段的值。reflection 可以从正在运行的程序中根据名称找到对象的字段并改变它，下面的例子可以说明这一点：
```java  
import java.lang.reflect.*;
public class field2 {
	public double d;
	public static void main(String args[]) {
		try {
			Class cls = Class.forName("field2");
			Field fld = cls.getField("d");
			field2 f2obj = new field2();
			System.out.println("d = " + f2obj.d);
			fld.setDouble(f2obj, 12.34);
			System.out.println("d = " + f2obj.d);
		} catch (Throwable e) {
			System.err.println(e);
		}
	}
}
```
这个例子中，字段d的值被变为了12.34。