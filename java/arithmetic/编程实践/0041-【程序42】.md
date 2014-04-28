题目：809*??=800*??+9*??+1    其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
```java     
//题目错了！809x=800x+9x+1 这样的方程无解。去掉那个1就有解了。
public class lianxi42 { 
	public static void main (String[] args) { 
		int a=809,b,i;
		for(i=10;i<13;i++)
		{
			b=i*a ;
			if(8*i<100&&9*i>=100)
				System.out.println ("809*"+i+"="+"800*"+i+"+"+"9*"+i+"="+b);
		}
	}
} 
```