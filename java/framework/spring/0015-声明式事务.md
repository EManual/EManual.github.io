可以把事务想成一个切面，那么就可以用事务性边界包裹Biz层的方法，然后注入事务
Spring提供了三种在配置文件声明事务性边界的方式：
★常用的Spring aop代理 bean来支持事务。
★但在Spring 2中增加了两种新的方式：简单的XML声明（xml-declared）事务。
★注释驱动事务。
1）代理事务：声明式事务管理通过使用Spring的TransactionProxyFactoryBean代理POJO来完成。TransactionProxyFactoryBean是ProxyFactoryBean的一个特化，他知道如何通过事务性边界包裹一个POJO的方法来代理他们。
```java  
<bean id="rantService" class="org.springframework.transaction.interceptor.TransactionProxyFactoryBean">
<property name="target" ref="rantServiceTarget" />      --?装配事务目标，相当给biz层的方法加事务
<property name="proxyInterfaces" value="com.roadrantz.service.RantService" />
<property name="transactionManager" ref="transactionManager" />   --?提供适当的事务管理器
<property name="transactionAttributes ">
	<props>
		<prop key="add*">PROPAGATION_REQUIRED</prop>
		<prop key="*">PROPAGATION_SUPPORTS,readOnly</prop>
	</props>
</property>
</bean>
```
事务传播行为：
```java  
PROPAGATION_REQUIRED ：当前方法必须有一个事务，有事务则运行该事务，没有则开始新的事务。---?最常用
PROPAGATION_MANDATORY：该方法必须有事务，没有事务则抛出异常
PROPAGATION_NESTED :该方法运行在嵌套事务中。如果封装事务不存在则就像第一种PROPAGATION_REQUIRED
PROPAGATION_NEVER  ：该方法不能有事务，有事务则抛出异常。
PROPAGATION_NOT_SUPPORTED：该方法不能有事务，如果有事务，则将该方法在运行期间挂起。
PROPAGATION_REQUIRES_NEW：方法必须运行在事务里，
PROPAGATION_SUPPORTS：表示当前方法不需要事务性上下文，但是如果有一个事务已经在运行的话，他可以在这个事务里运行。
PROPAGATION,   ISOLATION,     readOnly,     -Exception, +Exception
(传播行为)    （隔离级别 可选）  （事务只读 可选）  （回滚规则  可选）
```
可以创建事务模板简化配置：建立事务的抽象声明 
```java  
<bean id="TXServiceTemplate" class="org.springframework.transaction.interceptor.TransactionProxyFactoryBean"
 abstract=“true”> 
	<property name="transactionManager" ref="transactionManager" />   --?提供适当的事务管理器
	<property name="transactionAttributes ">
	<props>
		<prop key="add*">PROPAGATION_REQUIRED</prop>
		<prop key="*">PROPAGATION_SUPPORTS,readOnly</prop>
	</props>
	</property>
</bean>
<bean id=”ranBiz” parent=” TXServiceTemplate ”>
<property name="proxyInterfaces" value="com.roadrantz.service.RantService" />
<property name="transactionManager" ref="transactionManager" />   --?提供适当的事务管理器
</bean>
```
2）在Spring2.0声明事务 <tx>上面的方法会导致配置很臃肿，下面就是更简单的配置
在Spring2.0中专门为声明事务提供了一些新的标签 tx名称空间下
```java  
xmlns:tx=http://www.springframework.org/schema/tx
xmlns:aop ="http://www.springframework.org/schema/aop"
     http://www.springframework.org/schema/tx
http://www.springframework.org/schema/tx/spring-tx-2.0.xsd">
<tx:advice  id="txAdvice" transaction-manager="txManager">
<tx:attributes>
<tx:method name="get*" read-only="true"/>
<tx:method name="create*" />
<tx:method name="join*"/>
</tx:attributes>
</tx:advice>
<aop:config>
	<aop:advisor  pointcut="execution(* *..Roster.*(..))" advice-ref="txAdvice"/>
</aop:config>
```
3）定义注释驱动的事务，@Transactional可以在源代码中注释来进一步简化配置
```java  
@Transactional (propagation=Propagation.SUPPORTS, readOnly=true)
@Service("roster")
public class RosterImpl implements Rosterpublic
@Transactional                  ---------------	--------?方法层面的事务
Public  Player createPlayer(Player p) {
	playerDao.save(p);
	return p;
}
<context:component-scan 
base-package="com.kettas.spring.dao.day5.roster.dao,com.kettas.spring.dao.day5.roster.biz">
</context:component-scan>
<tx:annotation-driven/>  自动搜索@Transactional的bean 然后把事务通知告诉它。
```