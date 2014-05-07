断言(assert)：用来调试、测试代码。
格式：
assert 布尔表达式: 字符串  (如果布尔表达式为false时，这个字符串才会显示)。
* 注意：
assert默认是关闭的，使用时需要使用" -ea "进行开启，" -da "是关闭，如：java -ea 类名。
断言是以异常方式去执行的，当断言的布尔表达式为假时，会中断代码。
不能继承性的打开(java -ea:类名  这样只能打开该类，如果存在父类，不会去打开父类)。
* 什么时候用assert。
JDK1.4之后增加的新关键字——assert，表示断言，即程序执行到某个地方之后值肯定是预计好的；一般开发中很少使用assert；要想使用断言，就必须使用-ea参数。
assertion(断言)在软件开发中是一种常用的调试方式，很多开发语言中都支持这种机制。在实现中，assertion就是在程序中的一条语句，它对一个boolean表达式进行检查，一个正确程序必须保证这个boolean表达式的值为true；如果该值为false，说明程序已经处于不正确的状态下，assert将给出警告或退出。一般来说，assertion用于保证程序最基本、关键的正确性。assertion检查通常在开发和测试时开启。为了提高性能，在软件发布后，assertion检查通常是关闭的。 
```java  
package com.huawei.interview;public class AssertTest {
	public static void main(String[] args) {
		int i = 0;
		for(i=0;i<5;i++){
			System.out.println(i);
		}
		//假设程序不小心多了一句--i;
		--i;
		assert i==5;		
	}
}
```