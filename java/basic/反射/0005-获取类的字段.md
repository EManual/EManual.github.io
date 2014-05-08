找出一个类中定义了哪些数据字段也是可能的，下面的代码就在干这个事情：
```java  
import java.lang.reflect.*;
public class field1 {
	private double d;
	public static final int i = 37;
	String s = "testing";

	public static void main(String args[]) {
		try {
			Class cls = Class.forName("field1");
			Field fieldlist[] = cls.getDeclaredFields();
			for (int i = 0; i < fieldlist.length; i++) {
				Field fld = fieldlist[i];
				System.out.println("name = " + fld.getName());
				System.out.println("decl class = " + fld.getDeclaringClass());
				System.out.println("type = " + fld.getType());
				int mod = fld.getModifiers();
				System.out.println("modifiers = " + Modifier.toString(mod));
				System.out.println("-----");
		}
		} catch (Throwable e) {
			System.err.println(e);
		}
	}
}
```
这个例子和前面那个例子非常相似。例中使用了一个新东西 Modifier，它也是一个 reflection 类，用来描述字段成员的修饰语，如“private int”。这些修饰语自身由整数描述，而且使用 Modifier.toString 来返回以“官方”顺序排列的字符串描述 (如“static”在“final”之前)。这个程序的输出是：
```java  
name = d
decl class = class field1
type = double
modifiers = private
-----
name = i
decl class = class field1
type = int
modifiers = public static final
-----
name = s
decl class = class field1
type = class java.lang.String
modifiers =
```
和获取方法的情况一下，获取字段的时候也可以只取得在当前类中申明了的字段信息 (getDeclaredFields)，或者也可以取得父类中定义的字段 (getFields) 。