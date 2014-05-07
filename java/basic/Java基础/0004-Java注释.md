注释是给人看的，不是给计算机看的。Java中共有3种类型的注释：
//	单行注释，到本行结束的所有字符会被编译器忽略。
/* */	多行注释，在/*  */之间的所有字符会被编译器忽略。
/**  */  	文档注释，java特有的，在/**  */之间的所有字符会被编译器忽略。
可以用javadoc把java源程序中这种注释抽取出来形成html页面(只有写在包，类，属性，方法，构造器，引入之前的注释才可以进行抽取)。
```java  
public class Variable
{
	public static void main(String[] args)
	{
		//int a1 = 1;
		//System.out.println("a");
		/*这是多行注释
		  这是多行注释
		  这是多行注释
		  这是多行注释
		*/
		/**			另一种多行注释，文档注释		*/
		//byte b = 100;
		//System.out.println(b);
		//short a = 200;
		//System.out.println(a);
		long a = 1000;
		System.out.println(a);
	}
}
```