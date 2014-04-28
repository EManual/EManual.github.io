概述：
为其他对象提供一种代理以控制对这个对象的访问。
类型：结构型模式。
类图：
  
适用性：
1.远程代理（RemoteProxy）为一个对象在不同的地址空间提供局部代表。
2.虚代理（VirtualProxy）根据需要创建开销很大的对象。
3.保护代理（ProtectionProxy）控制对原始对象的访问。
4.智能指引（SmartReference）取代了简单的指针，它在访问对象时执行一些附加操作。
参与者：
1.Proxy
保存一个引用使得代理可以访问实体。若RealSubject和Subject的接口相同，Proxy会引用Subject。
提供一个与Subject的接口相同的接口，这样代理就可以用来替代实体。
控制对实体的存取，并可能负责创建和删除它。
其他功能依赖于代理的类型：
2.RemoteProxy负责对请求及其参数进行编码，并向不同地址空间中的实体发送已编码的请求。
3.VirtualProxy可以缓存实体的附加信息，以便延迟对它的访问。
4.ProtectionProxy检查调用者是否具有实现一个请求所必需的访问权限。
5.Subject定义RealSubject和Proxy的共用接口，这样就在任何使用RealSubject的地方都可以使用Proxy。
6.RealSubject定义Proxy所代表的实体。
例子：
```java  
Proxy 
public class ProxyObject implements Object {

    Object obj;
    
    public ProxyObject() {
        System.out.println("这是代理类");
        obj = new ObjectImpl();
    }
    
    public void action() {
        System.out.println("代理开始");
        obj.action();
        System.out.println("代理结束");
    }
}
Subject 
public interface Object {

    void action();
}
RealSubject 
public class ObjectImpl implements Object {

    public void action() {
        System.out.println("========");
        System.out.println("========");
        System.out.println("这是被代理的类");
        System.out.println("========");
        System.out.println("========");
    }
}
Test 
public class Test {

    public static void main() {
    	Object obj = new ProxyObject();
        obj.action();
    }
}
```
result：
```java  
这是代理类
代理开始
========
========
这是被代理的类
========
========
代理结束
```