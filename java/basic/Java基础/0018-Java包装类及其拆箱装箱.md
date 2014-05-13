Java包装类，Wrapper~由于在java中，数据类型总共可分为两大种，基本数据类型（值类型）和类类型（引用数据类型）。基本类型的数据不是对象，所以对于要将数据类型作为对象来使用的情况，java提供了相对应的包装类。对于8种数据类型的包装类分别是： 
```java  
int---Integer 
char---Character 
float---Float 
double---Double 
byte---Byte 
short---Short 
long---Long 
boolean--Boolean 
```
包装类提供了很多互相转换的方法，这里不一一细说，这里关注的是包装类的装箱和拆箱问题。 
所谓装箱，就是把基本类型用它们相对应的引用类型包起来，使它们可以具有对象的特质，如我们可以把int型包装成Integer类的对象，或者把double包装成Double，等等。 
所谓拆箱，就是跟装箱的方向相反，将Integer及Double这样的引用类型的对象重新简化为值类型的数据 
J2SE5.0后提供了自动装箱与拆箱的功能，此功能事实上是编译器来帮您的忙，编译器在编译时期依您所编写的方法，决定是否进行装箱或拆箱动作。 
自动装箱的过程：每当需要一种类型的对象时，这种基本类型就自动地封装到与它相同类型的包装中。 
自动拆箱的过程：每当需要一个值时，被装箱对象中的值就被自动地提取出来，没必要再去调用intValue()和doubleValue()方法。 
自动装箱，只需将该值赋给一个类型包装器引用，java会自动创建一个对象。例如：
```java  
Integer i=100;//没有通过使用new来显示建立，java自动完成。
```
自动拆箱，只需将该对象值赋给一个基本类型即可。例如：int j=i; 
```java  
int i = 10;
Integer j =new Integer(i); //手动装箱操作  
int k = j.intValue();      //手动拆箱操作  

int i = 11;
Integer j = i; //自动装箱
int k = j //自动拆箱
```
然而在Integer的自动装拆箱会有些细节值得注意： 
```java  
public static void main(String[] args) {
	Integer a=100;
	Integer b=100;	
	Integer c=200;
	Integer d=200;
	
	System.out.println(a==b);   //1
	System.out.println(a==100); //2	
	System.out.println(c==d);   //3
	System.out.println(c==200); //4
}
```
在java种，"=="是比较object的reference而不是value，自动装箱后，abcd都是Integer这个Oject，因此“==”比较的是其引用。按照常规思维，1和3都应该输出false。但结果是：
```java   
true 
true 
false 
true 
```
结果2和4，是因为ac进行了自动拆箱，因此其比较是基本数据类型的比较，就跟int比较时一样的，“==”在这里比较的是它们的值，而不是引用。 
对于结果1，虽然比较的时候，还是比较对象的reference,但是自动装箱时，java在编译的时候 Integer a = 100; 被翻译成-> Integer a = Integer.valueOf(100); 
关键就在于这个valueOf()的方法。
```java   
public static Integer valueOf(int i) {   
	final int offset = 128;   
	if (i >= -128 && i <= 127) { // must cache   
		return IntegerCache.cache[i + offset];   
	}   
	return new Integer(i);   
}  
 
private static class IntegerCache {   
	private IntegerCache(){}   
	static final Integer cache[] = new Integer[-(-128) + 127 + 1];   
	static {   
		for(int i = 0; i < cache.length; i++)   
			cache = new Integer(i - 128);   
	}   
} 
```
根据上面的jdk源码，java为了提高效率，IntegerCache类中有一个数组缓存了值从-128到127的Integer对象。当我们调用Integer.valueOf（int i）的时候，如果i的值是>=-128且<=127时，会直接从这个缓存中返回一个对象，否则就new一个Integer对象。 
具体如下：
```java   
static final Integer cache[] = new Integer[-(-128) + 127 + 1]; //将cache[]变成静态
static {
	for(int i = 0; i < cache.length; i++)
	cache[i] = new Integer(i - 128); //初始化cache[i]
}
```
这是用一个for循环对数组cache赋值，cache[255] = new Integer(255-128),也就是newl一个Integer(127) ,并把引用赋值给cache[255],好了，然后是Integer b= 127,流程基本一样，最后又到了cache[255] = new Integer(255-128),这一句，那我们迷糊了，这不是又new了一个对象127吗，然后把引用赋值给cache[255]，我们比较这两个引用（前面声明a的时候也有一个）,由于是不同的地址，所以肯定不会相等，应该返回false啊！呵呵，这么想你就错了，请注意看for语句给cache[i]初始化的时候外面还一个{}呢，{}前面一个大大的static关键字，是静态的，那么我们就可以回想下static有什么特性了，只能初始化一次，在对象间共享，也就是不同的对象共享同一个static数据。 
那么当我们Integer b = 127的时候，并没有new出一个新对象来，而是共享了a这个对象的引用，记住，他们共享了同一个引用！！！，那么我们进行比较a==b时，由于是同一个对象的引用（她们在堆中的地址相同），那当然返回true了！！！ 
知道了为什么，我们就来看看下面的代码：
```java   
public class Test {
	public static void main(String args[]){
		Integer m = new Integer(5);
		Integer n = new Integer(5);
		System.out.println(m==n);
		m = m-1;
		n = n-1;
		System.out.println(m==n);
	}
} 
```
输出什么？ 
```java   
false 
true 
```
原因： 
m,n因为都是new出来的对象，内存地址不一样，所以第一次m==n比较的reference不一样。但是，m=m-1首先进行了自动拆箱m.intValue，相减后再进行装箱动作：m=Integer.valueOf(m.intValue-1)，而m和n都在 -128--127的范围，所以自动装箱后，根据上文所述，都是同一个object的引用。因此第二次输出true。 
再看一次（出自java解惑）
```java  
public class TestWhile{ //1
	public static void main(String[] args)//2
	{
		Integer i=0;//3
		Integer j=0;//4
		// Integer i=new Integer(0);//5
		// Integer j=new Integer(0);//6
		while(i<=j & i>=j & i!=j)//7
		{ //8
			System.out.println("0000");//9
		}
	}
}
```
那一行是拆箱?while循环里的条件看似不成立，可为什么可以运行（去掉第5、6行的注释后）？ 
解答： 
这种情况下，循环不能运行。 
对于Integer类型，<,<=,>,>=操作将导致拆箱操作，也就是调用Integer的intValue()方法得到相应的基本类型值，然后比较。 
但是，==，!=比较的，是对象的引用（Reference）。 
```java  
Integer i = 0;//3 
Integer j = 0;//4 
```
这两句使用装箱操作，也就是调用Integer.valueOf(int i);注意，不是使用new。 
由于0在 -128--127之间，根据上述，i和j引用的是同一个对象。 
综上，i<=j & i>=j & i!=j中， 
i<=j 和 i>=j都成立，而i!=j不成立，因为i和j引用的是同一个对象。 
故此，循环不会执行。 
注释掉3，4两句，使用5，6两句时，i和j引用的不是同一个对象，所以i!=j成立。i<=j & i>=j & i!=j成立，循环条件总是成立的，while (i <= j & i >= j & i != j)成为无穷循环，不断输出。 
原题： 
循环者的诅咒 
请提供一个对i的声明，将下面的循环转变为一个无限循环：  
```java  
while (i <= j && j <= i && i != j) { 
} 
```
总结，对于要比较Object的值，最稳妥的方法还是调用equals()这个方法，而不是使用==，因此会比较其引用。
```java  
public boolean equals(Object obj) {
	if (obj instanceof Integer) {
		return value == ((Integer)obj).intValue();
	}
	return false;
}
```
大家可以看到，只要两个Integer的int value是相等的，equals方法总是返回true。