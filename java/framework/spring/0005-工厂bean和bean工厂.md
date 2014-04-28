FactoryBean（工厂bean）：是bean的加工工厂，是对已知Bean的加工，是一个接口，要实现三个方法：
① Object getObject()可以对bean进行加工添加功能。
② Class getObjectType()。
③ Boolean isSingleton()。
Bf.getBean(“ab”)只是得到MyFactory.getObject()的object对象 所以最后要强转。
Beanfactory bean工厂 就是生产bean的工厂，注入：
由于Spring IoC容器以框架的方式提供了工厂方法的功能，并以透明的方式给开发者，不过在一些遗留系统或第三方类库中，我们还会碰到工厂方法，这时用户可以使用Sping使用工厂方法注入的方式进行配置。
静态工厂方法：
很多工厂类方法都是静态的，这意味着用户在无须创建工厂类实例的情况就可以调用工厂类方法。因此静态工厂方法比非静态工厂方法的调用更加方便。我们将carFactory类的getCar()方法调整为静态的然后再Spring配置如下：
```java  
<bean id=”car” class =”carFactory” factory-method=”getCar”/>
```
用户直接通过class属性指定工厂类， 然后在通过factory-method指定对应的静态工厂方法创建bean。
如果静态工厂方法需要参数则用<p:constructor-arg index=”1”value="calendar"></p:constructor-arg>传入
实例工厂方法：
有些工厂是非静态的，即必须是实例化工厂类才能调用工厂方法。
下面我们实例化一个工厂类CarFactory类来为Car类提供实例。
```java  
package com.car;
public class CarFactory
{ public Car getCar(){return new Car();}}
```
工厂类负责创建一个或多个目标类实例，工厂类方法一般以接口或抽象类变量的形式返回目标类。工厂类对外屏蔽了目标类的实例化步骤。调
用甚至不知道如何具体的目标类是什么。
下面我们在Spring 配置文件中进行配置
```java  
<!--工厂Bean生成目标Bean-->
<bean id=”carFactory” class=”com.CarFactory”/>
<!--工厂Bean目标Bean-->
<bean id=”car” factory-bean=”carFactory” factory-method=”getCar”/>
```
factory-bean=”carFactory”指定了工厂类Bean，factory-method=”getCar”指定了工厂类Bean创建该Bean的工厂方法。
和静态工厂类似如果工厂方法需要参数则用
```java  
<p:constructor-arg index=”0”value="calendar"></p:constructor-arg>传入
```