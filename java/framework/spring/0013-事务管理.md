1，事务（见hibernate的ACID）： Spring和EJB一样，不仅提供对程序控制事务管理的支持（手动事务），也对提供声明式事务管理的支持（容器管理事务），但是Spring对程序控制事务管理的支持与EJB很不一样。EJB的事务管理和Java Transaction API(JPA)密不可分。和Ejb不同的是Spring采用的是一种回调机制，把真实的事务从事务代码中抽象出来，那么Spring就不需要JPA的实现。选择手动事务还是容器管理，就是在细微控制和简便操作之间做出选择。想精确控制事务就可以选择手动事务，不用那么精确就可以容器管理事务。
2，事务管理器：不管你是在bean中代码编写事务还是用切面（aspect aop）那样声明事务，都需要Spring的事务管理器连接特定平台的事务实现，每一种访问形式都有一个事务管理器。比如：
```java      
jdbc.datasource.DataSourceTransactionManager：jdbc连接的事务管理，iBATIS也支持。
orm.hibernate3. HibernateTransactionManager：hibernate3的事务支持。
orm.jpa.JpaTransactionManager：jpa的事务支持。
orm.jdo.JdoTransactionManager：Jdo事务管理支持。
```
这些事务管理器分别充当了某个特定的事务实现门面，这样你就只要和Spring的事务打交道，而不用关心实际上的事务是怎么实现的（门面模式）
各种事务管理器的配置，以Hibernate 3为例：
```java  
<bean id="transactionManager" class="org.springframework.
? orm.hibernate3.HibernateTransactionManager">
<property name="sessionFactory" ref="sessionFactory "/>
</bean>
```
3，JDBC事务管理
```java  
<bean id="transactionManager" class="org.springframework.jdbc.
? datasource.DataSourceTransactionManager">  ---? DataSourceTransactionManager调用Connection来管理事务
<property name="dataSource" ref="dataSource"/>  
</bean>
```