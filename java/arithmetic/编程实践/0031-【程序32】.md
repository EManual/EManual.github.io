题目：取一个整数a从右端开始的4～7位。
```java     
import java.util.*;
public class lianxi32 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.print("请输入一个7位以上的正整数：");
		long a = s.nextLong();
		String ss = Long.toString(a);
		char[] ch = ss.toCharArray();
		int j=ch.length;
		if (j<7){System.out.println("输入错误！");}
		else {
			System.out.println("截取从右端开始的4～7位是："+ch[j-7]+ch[j-6]+ch[j-5]+ch[j-4]);
		}
	}
}	 
```