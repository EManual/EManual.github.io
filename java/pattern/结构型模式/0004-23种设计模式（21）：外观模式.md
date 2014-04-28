概述：
为子系统中的一组接口提供一个一致的界面，Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
类型：结构型模式。
类图：
  
1.当你要为一个复杂子系统提供一个简单接口时。子系统往往因为不断演化而变得越来越复杂。大多数模式使用时都会产生更多更小的类。这使得子系统更具可重用性，也更容易对子系统进行定制，但这也给那些不需要定制子系统的用户带来一些使用上的困难。
Facade可以提供一个简单的缺省视图，这一视图对大多数用户来说已经足够，而那些需要更多的可定制性的用户可以越过facade层。
2.客户程序与抽象类的实现部分之间存在着很大的依赖性。引入facade将这个子系统与客户以及其他的子系统分离，可以提高子系统的独立性和可移植性。
3.当你需要构建一个层次结构的子系统时，使用facade模式定义子系统中每层的入口点。
如果子系统之间是相互依赖的，你可以让它们仅通过facade进行通讯，从而简化了它们之间的依赖关系。
参与者：
1.Facade
知道哪些子系统类负责处理请求。
将客户的请求代理给适当的子系统对象。
2.Subsystemclasses
实现子系统的功能。
处理由Facade对象指派的任务。
没有facade的任何相关信息；即没有指向facade的指针。
例子：
```java  
Facade 
public class Facade {

    ServiceA sa;
    
    ServiceB sb;
    
    ServiceC sc;
    
    public Facade() {
        sa = new ServiceAImpl();
        sb = new ServiceBImpl();
        sc = new ServiceCImpl(); 
    }
    
    public void methodA() {
        sa.methodA();
        sb.methodB();
    }
    
    public void methodB() {
        sb.methodB();
        sc.methodC();
    }
    
    public void methodC() {
        sc.methodC();
        sa.methodA();
    }
}
Subsystemclasses 
public class ServiceAImpl implements ServiceA {

    public void methodA() {
        System.out.println("这是服务A");
    }
}
public class ServiceBImpl implements ServiceB {

    public void methodB() {
        System.out.println("这是服务B");
    }
}
public class ServiceCImpl implements ServiceC {

    public void methodC() {
        System.out.println("这是服务C");
    }
}
Test 
public class Test {
    
    public static void main(String[] args) {
    	ServiceA sa = new ServiceAImpl();
    	ServiceB sb = new ServiceBImpl();
        
        sa.methodA();
        sb.methodB();
        
        System.out.println("========");
        //facade
        Facade facade = new Facade();
        facade.methodA();
        facade.methodB();
    }
}
```
result：
```java  
这是服务A
这是服务B
========
这是服务A
这是服务B
这是服务B
这是服务C
```