Xml配置文件属性的说明：
```java  
<bean id="TheAction" ⑴ 
	class="net.xiaxin.spring.qs.UpperAction" ⑵ 
	singleton="true" ⑶ 
	init-method="init" ⑷ 
	destroy-method="cleanup" ⑸ 
	depends-on="ActionManager" ⑹ >
	<property…>
</bean>
```
⑴ id
Java Bean在BeanFactory中的唯一标识，代码中通过BeanFactory获取。
JavaBean实例时需以此作为索引名称。
⑵ class Java Bean 类名 即真正接口的实现类。
⑶ singleton bean的作用域（创建模式（prototype还是singleton））。
单例（Singleton）模式，如果设为“true”，只维护此Java Bean的一个实例，反之，如果设为“false”，BeanFactory每次都将创建一个新的实例返回。默认为true。
实现方式是第一次getBean时放入Map中保存，第二次再用时直接在Map中拿，类名为key，实例为value。Bean的其他作用域还有prototype：原型模式：在获取prototype定义的bean时都产生新的实例，其生命周期由客户端维护。Session对每次HTTPsession中都回产生一个新的实例。Global session 仅在使用portletcontext的时候才有效，常用的是singleton和prototype
⑷ init-method
初始化方法，此方法将在BeanFactory创建JavaBean实例之后，在向应用层返回引用之前执行。一般用于一些资源的初始化工作。在javaBean中创建init方法，再添加属性init-method=“init”就行
⑸ destroy-method
销毁方法。此方法将在BeanFactory销毁的时候执行，一般用于资源释放。与init用法类似
⑹ depends-on
Bean依赖关系。一般情况下无需设定。Spring会根据情况组织各个依赖关系的构建工作（这里示例中的depends-on属性非必须）。
只有某些特殊情况下，如JavaBean中的某些静态变量需要进行初始化（这是一种BadSmell，应该在设计上应该避免）。通过depends-on指定其依赖关系可保证在此Bean加载之前，首先对depends-on所指定的资源进行加载。
⑺ <value>
通过<value/>节点可指定属性值。BeanFactory将自动根据Java Bean对应的属性类型加以匹配。
下面的”desc”属性提供了一个null值的设定示例。注意<value></value>代表一个空字符串，如果需要将属性值设定为null，必须使用<null/>节点。
⑻ <ref>指定了属性对BeanFactory中其他Bean的引用关系。