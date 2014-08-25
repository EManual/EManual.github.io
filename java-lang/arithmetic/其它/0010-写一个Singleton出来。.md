第一种：饱汉模式
[code=java]
public class SingleTon {
	private SingleTon(){
		}
	//实例化放在静态代码块里可提高程序的执行效率，但也可能更占用空间	
	private final static SingleTon instance = new SingleTon();
	public static SingleTon getInstance(){
		return instance;
	}
}
[/code]
第二种：饥汉模式
[code=java]
public class SingleTon {
	private SingleTon(){}
	private static instance = null;//new SingleTon();
	public static synchronized SingleTon getInstance(){
		if(instance == null)
			instance = new SingleTon();
		return instance;
	}
}
[/code]
第三种：用枚举
[code=java]
public enum SingleTon{
	ONE;
}
[/code]
第三：更实际的应用（在什么情况用单例）
[code=java]
public class SequenceGenerator{
	//下面是该类自身的业务功能代码
	private int count = 0;
	public synchronized int getSequence(){
		++count;
	}
	
	//下面是把该类变成单例的代码
	private SequenceGenerator(){}
	private final static instance = new SequenceGenerator();
	public static SingleTon getInstance(){
		return instance;
	}	
	
}
[/code]
第四：
[code=java]
public class MemoryDao{
private HashMap map = new HashMap();

public void add(Student stu1){ 
		map.put(SequenceGenerator.getInstance().getSequence(),stu1);
}
//把MemoryDao变成单例 
}
[/code]
Singleton模式主要作用是保证在Java应用程序中，一个类Class只有一个实例存在。 
一般Singleton模式通常有几种种形式: 
第一种形式: 定义一个类，它的构造函数为private的，它有一个static的private的该类变量，在类初始化时实例话，通过一个public的getInstance方法获取对它的引用,继而调用其中的方法。
[code=java] 
public class Singleton { 
private Singleton(){} 
　　//在自己内部定义自己一个实例，是不是很奇怪？ 
　　//注意这是private 只供内部调用 
　　private static Singleton instance = new Singleton(); 
　  //这里提供了一个供外部访问本class的静态方法，可以直接访问　　 
　　public static Singleton getInstance() { 
　　　　return instance; 　　 
　　} 
} 
[/code]
第二种形式: 
[code=java]
public class Singleton { 
　　private static Singleton instance = null; 
　　public static synchronized Singleton getInstance() { 
　　//这个方法比上面有所改进，不用每次都进行生成对象，只是第一次　　　 　 
　　//使用时生成实例，提高了效率！ 
　　if (instance==null) 
　　　　instance＝new Singleton(); 
			return instance; 　　
	} 
} 
[/code]
其他形式: 
定义一个类，它的构造函数为private的，所有方法为static的。 
一般认为第一种形式要更加安全些