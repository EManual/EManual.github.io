题目：输入三个整数x,y,z，请把这三个数由小到大输出。  
```java   
import java.util.*;
public class lianxi15 {
	public static void main(String[] args) {
		input fnc = new input();
		int x=0, y=0, z=0;
		System.out.print("输入第一个数字：");
		x = fnc.input();
		System.out.print("输入第二个数字：");
		y = fnc.input();
		System.out.print("输入第三个数字：");
		z = fnc.input();   
		if(x > y) {
		  int t = x;
		  x = y;
		  y = t;
		}
		if(x > z) {
		  int t = x;
		  x = z;
		  z = t;
		}
		if(y > z) {
		  int t = y;
		  y = z;
		  z = t;
		}
		System.out.println( "三个数字由小到大排列为： "+x + " " + y + " " + z);
	}
}
class input{
	public int input() {
		int value = 0;
		Scanner s = new Scanner(System.in);
		value = s.nextInt();
		return value;
	}
} 
```