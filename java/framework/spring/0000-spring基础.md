1含义：为解决企业应用开发的复杂性而创建的开源框架，用基本的javaBean来完成EJB的事情 从大小和开销方向spring都是轻量级的。
2，用途 
①	Ioc容器可以将对象之间的依赖关系交由spring管理，进行控制。
②	AOP:方便进行面向切面的编程，是oop的扩展，想加什么功能直接加。
③	能够集成各种优秀的框架，struts hibernate等。
3，spring 组成内容
  
4，准备配置工作
① 下载SpringFramework的最新版本，并解压缩到指定目录。在IDE中新建一个项目，并将Spring.jar将其相关类库加入项目。
② 配置文件 bean.xml。
③ 在classpath创建日志输出文件。log4j.properties。
④ org.springframework.beans及org.springframework.context包是Spring IoC容器的基础。
5，Spring 基础语义
1）IoC （Inversion of Control）=DI （Dependency Injection）控制反转和依赖注入，它是一种基于接口的编程，bean由容器创建在需要的时候拿来用即可，主要是采用反射来实现，其核心组建就是BeanFactory 但实际开发常用XmlBeanFactory
2）依赖注入的几种实现类型
Type1设值注入：通过类的setter方法完成依赖关系的设置，就是给bean类中属性加set方法。
Type3 构造子注入：即通过构造函数完成依赖关系的设置。
```java  
public class DIByConstructor {
	private final DataSource dataSource;
	private final String message;
	public DIByConstructor(DataSource ds, String msg) {
		this.dataSource = ds;
		this.message = msg;
	}
}
```
3）几种依赖注入模式的对比总结
Type2 设值注入的优势
1．对于习惯了传统JavaBean开发的程序员而言，通过setter方法设定依赖关系显得更加直观，更加自然。
2．如果依赖关系（或继承关系）较为复杂，那么Type3模式的构造函数也会相当庞大（我们需要在构造函数中设定所有依赖关系），此时Type2模式往往更为简洁。
3．对于某些第三方类库而言，可能要求我们的组件必须提供一个默认的构造函数（如Struts中的Action），此时Type3类型的依赖注入机制就体现出其局限性，难以完成我们期望的功能。
Type3 构造子注入的优势：
1．“在构造期即创建一个完整、合法的对象”，对于这条Java设计原则，Type3无疑是最好的响应者。
2．避免了繁琐的setter方法的编写，所有依赖关系均在构造函数中设定，依赖关系集中呈现，更加易读。
3．由于没有setter方法，依赖关系在构造时由容器一次性设定，因此组件在被创建之后即处于相对“不变”的稳定状态，无需担心上层代码在调用过程中执行setter方法对组件依赖关系产生破坏，特别是对于Singleton模式的组件而言，这可能对整个系统产生重大的影响。
4．同样，由于关联关系仅在构造函数中表达，只有组件创建者需要关心组件内部的依赖关系。对调用者而言，组件中的依赖关系处于黑盒之中。对上层屏蔽不必要的信息，也为系统的层次清晰性提供了保证。
5．通过构造子注入，意味着我们可以在构造函数中决定依赖关系的注入顺序，对于一个大量依赖外部服务的组件而言，依赖关系的获得顺序可能非常重要，比如某个依赖关系注入的先决条件是组件的DataSource及相关资源已经被设定。
理论上，以Type3类型为主，辅之以Type2类型机制作为补充，可以达到最好的依赖注入效果，不过对于基于Spring Framework开发的应用而言，Type2使用更加广泛。
4）bean.xml配置文件
Bean Factory，顾名思义，负责创建并维护Bean实例。
Bean Factory负责根据配置文件创建Bean实例，可以配置的项目有：
1．Bean属性值及依赖关系（对其他Bean的引用）
2．Bean创建模式（是否Singleton模式，即是否只针对指定类维持全局唯一的实例）
3．Bean初始化和销毁方法
4．Bean的依赖关系
5)XmlBeanFactory两中注入方式的配置
①property-------?set方法的注入配置
```java  
<p:bean id=”hello” class=”com.kettas.HelloIFImp”>
   <p:property name=”user” value=”xxx”></p:property>
</p:bean>
```
②constructor---------?构造方法的注入配置
```java  
<p:bean id="hello2" class="com.kettas.spring.ioc.day1.HelloIFImpl">
	<p:constructor-arg index=”0” value="world"></p:constructor-arg> 
	<p:constructor-arg type="java.lang.String"”ref="calendar"></p:constructor-arg>
</p:bean>
```
说明： index=”0”构造方法第一个参数，用index可以稍微减少冗余，但是它更容易出错且不如type属性可读性高。你应该仅在构造函数中有参数冲突时使用index。
6) 依赖的目标类型分成三种形式：        
1) 基本类型+String 
   <value>data</value>类型自动转化
2) 对其他bean 的引用 
       <ref bean="target"/>
3) 集合类型       list props set map
list set properties配置类似：
```java  
<p:property name="intList">
	<p:list>
		<p:value>1</p:value>
		<p:value>2</p:value>
	</p:list>
</p:property>
<p:property name="objMap">
	<p:map>
		<p:entry>
			<p:key>
				<p:value>1</p:value>
			</p:key>
			<p:ref local="hello2"/>
		</p:entry>
	</p:map>
</p:property>
<p:property name="pros">
	<p:props>
		<p:prop key="1">red</p:prop>
		<p:prop key="2">green</p:prop>
	</p:props>
</p:property> 
```