用于 reflection 的类，如 Method，可以在 java.lang.relfect 包中找到。使用这些类的时候必须要遵循三个步骤：第一步是获得你想操作的类的 java.lang.Class 对象。在运行中的 Java 程序中，用 java.lang.Class 类来描述类和接口等。 
下面就是获得一个 Class 对象的方法之一：
```java  
Class c = Class.forName("java.lang.String");
```
这条语句得到一个 String 类的类对象。还有另一种方法，如下面的语句：
```java  
Class c = int.class;
```
或者
```java  
Class c = Integer.TYPE;
```
它们可获得基本类型的类信息。其中后一种方法中访问的是基本类型的封装类 (如 Integer) 中预先定义好的 TYPE 字段。
第二步是调用诸如 getDeclaredMethods 的方法，以取得该类中定义的所有方法的列表。
一旦取得这个信息，就可以进行第三步了——使用 reflection API 来操作这些信息，如下面这段代码：
```java  
Class c = Class.forName("java.lang.String");
Method m[] = c.getDeclaredMethods();
System.out.println(m[0].toString());
```
它将以文本方式打印出 String 中定义的第一个方法的原型。
在下面的例子中，这三个步骤将为使用 reflection 处理特殊应用程序提供例证。
模拟 instanceof 操作符
得到类信息之后，通常下一个步骤就是解决关于 Class 对象的一些基本的问题。例如，Class.isInstance 方法可以用于模拟 instanceof 操作符：
```java  
class A {
}

public class instance1 {
	public static void main(String args[]) {
	try {
		Class cls = Class.forName("A");
		boolean b1 = cls.isInstance(new Integer(37));
		System.out.println(b1);
		boolean b2 = cls.isInstance(new A());
		System.out.println(b2);
	} catch (Throwable e) {
		System.err.println(e);
	}
	}
}
```
在这个例子中创建了一个 A 类的 Class 对象，然后检查一些对象是否是 A 的实例。Integer(37) 不是，但 new A()是。