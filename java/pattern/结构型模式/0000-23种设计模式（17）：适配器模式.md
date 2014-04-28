概述：
将一个类的接口转换成客户希望的另外一个接口。Adapter模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
类型：结构型模式。
类图：
  
适用性：
1.你想使用一个已经存在的类，而它的接口不符合你的需求。
2.你想创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类（即那些接口
可能不一定兼容的类）协同工作。
3.（仅适用于对象Adapter）你想使用一些已经存在的子类，但是不可能对每一个都进行
子类化以匹配它们的接口。对象适配器可以适配它的父类接口。
参与者
1.Target
定义Client使用的与特定领域相关的接口。
2.Client
与符合Target接口的对象协同。
3.Adaptee
定义一个已经存在的接口，这个接口需要适配。
4.Adapter
对Adaptee的接口与Target接口进行适配
例子：
```java  
Target 
public interface Target {

    void adapteeMethod();
    
    void adapterMethod();
}
Adaptee 
public class Adaptee {

    public void adapteeMethod() {
        System.out.println("Adaptee method!");
    }
}
Adapter 
public class Adapter implements Target {

    private Adaptee adaptee;
    
    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

	public void adapteeMethod() {
		adaptee.adapteeMethod();
	}

	public void adapterMethod() {
		System.out.println("Adapter method!");
    }
}
Client 
public class Test {

    public static void main(String[] args) {
        Target target = new Adapter(new Adaptee());
        target.adapteeMethod();
        
        target.adapterMethod();
    }
}
```
result：
```java  
Adaptee method!
Adapter method!
```