本文介绍的 reflection 的最后一种用法是创建的操作数组。数组在 Java 语言中是一种特殊的类类型，一个数组的引用可以赋给 Object引用。观察下面的例子看看数组是怎么工作的：
```java  import java.lang.reflect.*;   
public class array1 {
	public static void main(String args[]) {
		try {
			Class cls = Class.forName("java.lang.String");
			Object arr = Array.newInstance(cls, 10);
			Array.set(arr, 5, "this is a test");
			String s = (String) Array.get(arr, 5);
			System.out.println(s);
		} catch (Throwable e) {
			System.err.println(e);
		}
	}
}
```
例中创建了 10 个单位长度的 String 数组，为第 5 个位置的字符串赋了值，最后将这个字符串从数组中取得并打印了出来。
下面这段代码提供了一个更复杂的例子：
```java  
import java.lang.reflect.*;  
public class array2 {
	public static void main(String args[]) {
		int dims[] = new int[]{5, 10, 15};
		Object arr = Array.newInstance(Integer.TYPE, dims);
		Object arrobj = Array.get(arr, 3);
		Class cls = arrobj.getClass().getComponentType();
		System.out.println(cls);
		arrobj = Array.get(arrobj, 5);
		Array.setInt(arrobj, 10, 37);
		int arrcast[][][] = (int[][][]) arr;
		System.out.println(arrcast[3][5][10]);
	}
}
```
例中创建了一个 5 x 10 x 15 的整型数组，并为处于 [3][5][10] 的元素赋了值为 37。注意，多维数组实际上就是数组的数组，例如，第一个 Array.get 之后，arrobj 是一个 10 x 15 的数组。进而取得其中的一个元素，即长度为 15 的数组，并使用 Array.setInt 为它的第10个元素赋值。
注意创建数组时的类型是动态的，在编译时并不知道其类型。