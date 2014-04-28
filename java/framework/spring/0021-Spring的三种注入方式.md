Spring使用注入方式，为什么使用注入方式，这系列问题实际归结起来就是一句话，Spring的注入和IoC（本人关于IoC的阐述）反转控制是一回事。下面我们详细来了解一下
AD：
1. 接口注入（不推荐）
2. getter，setter方式注入（比较常用）
3. 构造器注入（死的应用）
关于getter和setter方式的注入
```java  
autowire="defualt" 
autowire=“byName”  
autowire="bytype" 
```
例如：有如下两个类需要注入
第一个类：
```java  
package org.jia;  
    
  public class Order {  
      private String orderNum;  
      @SuppressWarnings("unused")  
      private OrderItem orderitem;  
    
      public OrderItem getOrderitem() {  
          return orderitem;  
     }  
   
     public void setOrderitem(OrderItem orderitem) {  
         this.orderitem = orderitem;  
     }  
   
     public String getOrderNum() {  
         return orderNum;  
     }  
   
     public void setOrderNum(String orderNum) {  
         this.orderNum = orderNum;  
     }       
 }  
```
第二个类：
```java  
package org.jia;  
   
 public class OrderItem {  
     private String orderdec;  
   
     public String getOrderdec() {  
         return orderdec;  
     }  
   
     public void setOrderdec(String orderdec) {  
         this.orderdec = orderdec;  
     }  
 } 
``` 
常用getter&&setter方式介绍
方式第一种注入：
```java  
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd"> 
 
<beans> 
    <bean id="orderItem" class="org.jia.OrderItem"> 
        <property name="orderdec" value="item00001"></property> 
    </bean> 
    <bean id="order" class="org.jia.Order" > 
        <!-----注入变量 名字必须与类中的名字一样-------> 
        <property name="orderNum" value="order000007"></property> 
         <！--注入对象 名字为orderitem，所属的类的应用id为orderItem--> 
        <property name="orderitem" ref="orderItem"></property> 
      
    --></bean> 
</beans>
``` 
方式第二种注入：byName
```java  
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">  
<beans>  
    <!--此时的id就必须与Order.java中所定义的OrderItem的对象名称一样了，不然就会找不到-->  
    <bean id="orderitem" class="org.jia.OrderItem">  
        <property name="orderdec" value="item00001"></property>  
    </bean>  
    <bean id="order" class="org.jia.Order"<span style="color:#ff0000;"> autowire="byName"</span>>  
        <property name="orderNum" value="order000007"></property>  
    </bean>  
</beans>
``` 
方式第三种注入：byType
```java  
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd">  
<beans>  
    <!--按照byType注入则就与id没有关系，可以随便定义id ！！！但是不能出现多个此类的id-->  
    <bean id="orderitdfadafaem" class="org.jia.OrderItem">  
        <property name="orderdec" value="item00001"></property>  
    </bean>  
    <bean id="order" class="org.jia.Order" <span style="color:#ff0000;">autowire="byType"</span>>  
        <property name="orderNum" value="order000007"></property>  
    </bean>  
</beans> 
autowire="constructor"
```
需要在Order.java中加入一个构造器
```java  
public Order(OrderItem item )  
{   
      orderitem = item;  
} 
```
XML配置文件
```java  
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" "http://www.springframework.org/dtd/spring-beans.dtd"> 
<beans> 
    <bean id="orderItem" class="org.jia.OrderItem"> 
        <property name="orderdec" value="item00001"></property> 
    </bean> 
    <bean id="order" class="org.jia.Order" autowire="constructor"> 
        <property name="orderNum" value="order000007"></property> 
    </bean> 
</beans> 
```
三种注入方式比较
* 接口注入：
接口注入模式因为具备侵入性，它要求组件必须与特定的接口相关联，因此并不被看好，实际使用有限。
* Setter 注入：
对于习惯了传统 javabean 开发的程序员，通过 setter 方法设定依赖关系更加直观。
如果依赖关系较为复杂，那么构造子注入模式的构造函数也会相当庞大，而此时设值注入模式则更为简洁。
如果用到了第三方类库，可能要求我们的组件提供一个默认的构造函数，此时构造子注入模式也不适用。
* 构造器注入：
在构造期间完成一个完整的、合法的对象。
所有依赖关系在构造函数中集中呈现。
依赖关系在构造时由容器一次性设定，组件被创建之后一直处于相对“不变”的稳定状态。
只有组件的创建者关心其内部依赖关系，对调用者而言，该依赖关系处于“黑盒”之中。
* 总结
Spring使用注入方式，为什么使用注入方式，这系列问题实际归结起来就是一句话，Spring的注入和IoC（本人关于IoC的阐述）反转控制是一回事。
理论上：第三种注入方式（构造函数注入）在符合java使用原则上更加合理，第二种注入方式（setter注入）作为补充。
实际上：我个人认为第二种注入方式（setter注入）可以取得更加直观的效果，在使用工作上有不可比拟的优势，所以setter注入依赖关系应用更加广泛。