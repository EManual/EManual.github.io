概述：
将抽象部分与它的实现部分分离，使它们都可以独立地变化。
类型：结构型模式。
类图：
  
适用性：
1.你不希望在抽象和它的实现部分之间有一个固定的绑定关系。
例如这种情况可能是因为，在程序运行时刻实现部分应可以被选择或者切换。
2.类的抽象以及它的实现都应该可以通过生成子类的方法加以扩充。
这时Bridge模式使你可以对不同的抽象接口和实现部分进行组合，并分别对它们进行扩充。
3.对一个抽象的实现部分的修改应对客户不产生影响，即客户的代码不必重新编译。
4.正如在意图一节的第一个类图中所示的那样，有许多类要生成。
这样一种类层次结构说明你必须将一个对象分解成两个部分。
5.你想在多个对象间共享实现（可能使用引用计数），但同时要求客户并不知道这一点。
参与者：
1.Abstraction
定义抽象类的接口。
维护一个指向Implementor类型对象的指针。
2.RefinedAbstraction
扩充由Abstraction定义的接口。
3.Implementor
定义实现类的接口，该接口不一定要与Abstraction的接口完全一致。
事实上这两个接口可以完全不同。
一般来讲，Implementor接口仅提供基本操作，而Abstraction则定义了基于这些基本操作的较高层次的操作。
4.ConcreteImplementor
实现Implementor接口并定义它的具体实现。
例子：
```java  
Abstraction 
public abstract class Person {

    private Clothing clothing;
    
    private String type;

    public Clothing getClothing() {
        return clothing;
    }

    public void setClothing() {
        this.clothing = ClothingFactory.getClothing();
    }
    
    public void setType(String type) {
        this.type = type;
    }
    
    public String getType() {
        return this.type;
    }
    
    public abstract void dress();
}
RefinedAbstraction 
public class Man extends Person {
    
    public Man() {
        setType(“男人”);
    }
    
    public void dress() {
        Clothing clothing = getClothing();
        clothing.personDressCloth(this);
    }
}
public class Lady extends Person {

    public Lady() {
        setType(“女人”);
    }
    
    public void dress() {
        Clothing clothing = getClothing();
        clothing.personDressCloth(this);
    }
}
Implementor 
public abstract class Clothing {

    public abstract void personDressCloth(Person person);
}
ConcreteImplementor 
public class Jacket extends Clothing {

    public void personDressCloth(Person person) {
        System.out.println(person.getType() + “穿马甲”);
    }
}
public class Trouser extends Clothing {

    public void personDressCloth(Person person) {
        System.out.println(person.getType() + “穿裤子”);
    }
}
Test 
public class Test {

    public static void main(String[] args) {
        
        Person man = new Man();
        
        Person lady = new Lady();
        
        Clothing jacket = new Jacket();
        
        Clothing trouser = new Trouser();
        
        jacket.personDressCloth(man);
        trouser.personDressCloth(man);

        jacket.personDressCloth(lady);
        trouser.personDressCloth(lady);
    }
}
```
result：
```java  
男人穿马甲
男人穿裤子
女人穿马甲
女人穿裤子
```