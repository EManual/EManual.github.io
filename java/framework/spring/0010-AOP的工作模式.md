代理主要有静态代理和动态代理。
静态代理：在代理中实现接口并创建实现类对象，在对实现类的方法增加功能（不常用）。
动态代理：实现implements InvocationHandler接口。实现方法：
```java  
public Object invoke(Object proxy, Method method, Object[] args) throws Throwable{
	System.out.println("=========");
	Object o=method.invoke(this.ins, args);
	System.out.println("---------");
	return o;
}
```
  
流程图：在配置文件的配置
  
 配置文件代码：
 ```java  
<!-- pointcut definition -->
	<p:bean id="cf" class="com.kettas.spring.aop.day4.MyClassFilter">
		<p:property name="classes">
			<p:set>
				<p:value>com.kettas.spring.ioc.day1.HelloIF</p:value>   ---
			</p:set>
		</p:property>
	</p:bean>
	<p:bean id="mm" class="com.kettas.spring.aop.day4.MyMethodMatcher">
		<p:property name="methodNames">
			<p:set>
				<p:value>sayHello</p:value>
			</p:set>
		</p:property>
	</p:bean>
	<p:bean id="pc" class="com.kettas.spring.aop.day4.MyPointcut">
		<p:property name="classFilter" ref="cf"></p:property>
		<p:property name="methodMatcher" ref="mm"></p:property>
	</p:bean>
	
	<!--advice   要继承implements MethodInterceptor-->
	<p:bean id="timingAdvice" class="com.kettas.spring.aop.day4.TimingInterceptor"></p:bean>
	
	<!-- advisor  把通知和切入点结合在一起- 最好给代理增加功能->
	<p:bean id="timingAdvisor" class="org.springframework.aop.support.DefaultPointcutAdvisor">
		<p:property name="advice" ref="timingAdvice"></p:property>
		<p:property name="pointcut" ref="pc"></p:property>
	</p:bean>
	
	<!—target 目标 -->
	<p:bean id="helloTarget" class="com.kettas.spring.ioc.day1.HelloIFImpl">
		<p:property name="cal">
			<p:bean class="java.util.GregorianCalendar"></p:bean>
		</p:property>
		<p:property name="user" value="world"></p:property>
	</p:bean>
	<!-- proxy -->
	<p:bean id="hello" class="org.springframework.aop.framework.ProxyFactoryBean">
		<p:property name="target" ref="helloTarget"></p:property>
		<p:property name="interceptorNames">
			<p:list>
				<p:idref bean="timingAdvisor"/>   增加一种服务
				<p:idref bean="xxxAdvisor"/>   增加另一种服务
			</p:list>
		</p:property>
		<p:property name="proxyInterfaces">    要和目标类实现共同的接口
			<p:value>com.kettas.spring.ioc.day1.HelloIF</p:value>
		</p:property>
	</p:bean>
</p:beans>
```
简化配置：有可能只是目标类不一样，其他的都是一样的。解决每一个目标类都需要一个复杂的代理过程配置的问题，可以简化配置的问题 抽象ProxyFactoyBean的方法  如：
```java  
<!--  抽象proxy --定义抽象的类，只是没有目标类，其他的通知和接口都一样>
<p:bean id="helloBase" class="org.springframework.aop.framework.ProxyFactoryBean" abstract=“true”>
		<p:property name="interceptorNames">
			<p:list>
				<p:idref bean="timingAdvisor"/>   增加一种服务
<p:idref bean="xxxAdvisor"/>   增加另一种服务
			</p:list>
		</p:property>
		<p:property name="proxyInterfaces">    要和目标类实现共同的接口
			<p:value>com.kettas.spring.ioc.day1.HelloIF</p:value>
		</p:property>
	</p:bean>
</p:beans>
```
真正的代理
```java  
<!—target 目标 继承抽象方法  只用写目标类就可以了 -->
<!-- proxy -->
<p:bean id="hello" parent=” helloBase”>
	<p:property name="target" ref="helloTarget"></p:property>
</p:bean>
```