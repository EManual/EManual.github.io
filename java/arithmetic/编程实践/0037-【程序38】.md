题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。 
```java    
/*………………
*……题目意思似乎不能用length()函数     */
import java.util.*;
public class lianxi38 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("请输入一个字符串：");
		String str = s.nextLine();
		System.out.println("字符串的长度是："+str.length());
	}
} 
```