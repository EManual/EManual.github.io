局部变量：不是声明在类体括号里面的变量。
(1)必须要先赋值，后使用，否则通不过编译，局部变量没有默认初始化值。
(2)作用范围：定义开始到定义它的代码块结束。
(3)同一范围内，不允许2个局部变量命名冲突。
参数传递时，简单类型进行值转递(参数进行传递时都会先去栈中生成一个副本的，使用结束后释放)。
* 静态变量和实例变量的区别？
语法定义上的区别：静态变量前要加static关键字，而实例变量前则不加。
程序运行时的区别：实例变量属于某个对象的属性，必须创建了实例对象，其中的实例变量才会被分配空间，才能使用这个实例变量。静态变量不属于某个实例对象，而是属于类，所以也称为类变量，只要程序加载了类的字节码，不用创建任何实例对象，静态变量就会被分配空间，静态变量就可以被使用了。总之，实例变量必须创建对象后才可以通过这个对象来使用，静态变量则可以直接使用类名来引用。
例如，对于下面的程序，无论创建多少个实例对象，永远都只分配了一个staticVar变量，并且每创建一个实例对象，这个staticVar就会加1；但是，每创建一个实例对象，就会分配一个instanceVar，即可能分配多个instanceVar，并且每个instanceVar的值都只自加了1次。
```java  
public class VariantTest{
	public static int staticVar = 0; 
	public int instanceVar = 0; 
	public VariantTest(){
		staticVar++;
		instanceVar++;
		System.out.println(“staticVar=” + staticVar + ”,instanceVar=” + instanceVar);
	}
}
```
类的静态变量在内存中只有一个，java虚拟机在加载类的过程中为静态变量分配内存，静态变量位于方法区，被类的所有实例共享。静态变量可以直接通过类名进行访问，其生命周期取决于类的生命周期。
而实例变量取决于类的实例。每创建一个实例，java虚拟机就会为实例变量分配一次内存，实例变量位于堆区中，其生命周期取决于实例的生命周期。
```java  
public class Temp {  
	int t; //实例变量  
	public static void main(String[] args){  
		int t=1; //局部变量  
		System.out.println(t); //打印局部变量  
		Temp a= new Temp(); //创建实例  
		System.out.println(a.t); //通过实例访问实例变量  
	}  
} 
```
结果为：
```java  
1
0 （成员变量具有缺省值 而局部变量则没有）
```
把代码改为：
```java  
public class Temp {  
	static int t; //类变量  
	public static void main(String[] args) {  
		System.out.println(t); //打印类变量  
		int t=1; //局部变量  
		System.out.println(t); //打印局部变量  
		Temp a= new Temp(); //创建实例  
		System.out.println(a.t); //通过实例访问实例变量  
	}  
} 
```
结果则为：
```java  
0
1
0
```