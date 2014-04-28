//用下面的也可以
//for(int i=0,int j=a.length-1;i<j;i++,j--) 是否等效于 for(int i=0;i<a.length/2;i++)呢？
```java  
import java.util.Arrays;

public class SwapDemo{

	public static void main(String[] args){
		int [] a = new int[]{
						(int)(Math.random() * 1000),
						(int)(Math.random() * 1000),
						(int)(Math.random() * 1000),
						(int)(Math.random() * 1000),						
						(int)(Math.random() * 1000)													
		};	
		
		System.out.println(a);
		System.out.println(Arrays.toString(a));
		swap(a);
		System.out.println(Arrays.toString(a));		
	}
	
	public static void swap(int a[]){
		int len = a.length;
		for(int i=0;i<len/2;i++){
			int tmp = a[i];
			a[i] = a[len-1-i];
			a[len-1-i] = tmp;
		}
	}
}
```