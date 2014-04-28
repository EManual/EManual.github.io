题目：判断101-200之间有多少个素数，并输出所有素数。 
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除， 则表明此数不是素数，反之是素数。   
```java  
public class lianxi02 {
	public static void main(String[] args) {
		int count = 0;
		for(int i=101; i<200; i+=2) {
		boolean b = false;
		for(int j=2; j<=Math.sqrt(i); j++) 
		{
			if(i % j == 0) { b = false; break; } 
			else           { b = true; }
		}
		if(b == true) {count ++;System.out.println(i );}
									  }
		System.out.println( "素数个数是: " + count);
	}
}
```