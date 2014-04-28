题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。 
```java    
import java.util.*;
public class lianxi47 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n=1,num;
		while(n<=7){
			do{
				System.out.print("请输入一个1--50之间的整数：");
				num= s.nextInt();
			}while(num<1||num>50);
			for(int i=1;i<=num;i++)
			{System.out.print("*");}
			System.out.println();
			n ++;
		}
	}
} 
```