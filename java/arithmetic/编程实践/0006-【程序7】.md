题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。 
```java    
import java.util.*;
public class lianxi07 {
	public static void main(String[] args) {
		int digital = 0;
		int character = 0;
		int other = 0;
		int blank = 0;
		char[] ch = null;
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		ch = s.toCharArray();
		for(int i=0; i<ch.length; i++) {
			if(ch >= "0" && ch <= "9") {
			   digital ++;
			} else if((ch >= "a" && ch <= "z") || ch > "A" && ch <= "Z") {
			   character ++;
			} else if(ch == " ") {
			   blank ++;
			} else {
			   other ++;
			}
		}
		System.out.println("数字个数: " + digital);
		System.out.println("英文字母个数: " + character);
		System.out.println("空格个数: " + blank);
		System.out.println("其他字符个数:" + other );
	}
}
```