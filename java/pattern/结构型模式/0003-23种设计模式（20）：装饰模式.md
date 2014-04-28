概述：
动态地给一个对象添加一些额外的职责。就增加功能来说，Decorator模式相比生成子类更为灵活。
类型：结构型模式。
类图：
  
适用性：
1.在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责。
2.处理那些可以撤消的职责。
3.当不能采用生成子类的方法进行扩充时。
参与者：
1.Component
定义一个对象接口，可以给这些对象动态地添加职责。
2.ConcreteComponent
定义一个对象，可以给这个对象添加一些职责。
3.Decorator
维持一个指向Component对象的指针，并定义一个与Component接口一致的接口。
4.ConcreteDecorator
向组件添加职责。
例子：
```java  
Component 
public interface Person {

    void eat();
}
ConcreteComponent 
public class Man implements Person {

	public void eat() {
		System.out.println("男人在吃");
	}
}
Decorator 
public abstract class Decorator implements Person {

    protected Person person;
    
    public void setPerson(Person person) {
        this.person = person;
    }
    
    public void eat() {
        person.eat();
    }
}
ConcreteDecorator 
public class ManDecoratorA extends Decorator {

    public void eat() {
        super.eat();
        reEat();
        System.out.println("ManDecoratorA类");
    }

    public void reEat() {
        System.out.println("再吃一顿饭");
    }
}
public class ManDecoratorB extends Decorator {
    
    public void eat() {
        super.eat();
        System.out.println("===============");
        System.out.println("ManDecoratorB类");
    }
}
Test 
public class Test {

    public static void main(String[] args) {
        Man man = new Man();
        ManDecoratorA md1 = new ManDecoratorA();
        ManDecoratorB md2 = new ManDecoratorB();
        
        md1.setPerson(man);
        md2.setPerson(md1);
        md2.eat();
    }
}
```
result：
```java  
男人在吃
再吃一顿饭
ManDecoratorA类
===============
ManDecoratorB类
```