题目：输入3个数a,b,c，按大小顺序输出。  
```java   
import java.util.Scanner;
public class lianxi34 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("请输入3个整数：");
		int a = s.nextInt();
		int b = s.nextInt();
		int c = s.nextInt();
		if(a < b) {
			int t = a;
			a = b;
			b = t;
		}
		if(a < c) {
			int t = a;
			a = c;
			c = t;
		}
		if(b < c) {
			int t = b;
			b = c;
			c = t;
		}
		System.out.println("从大到小的顺序输出:");
		System.out.println(a + " " + b + " " + c);
	}
} 
```