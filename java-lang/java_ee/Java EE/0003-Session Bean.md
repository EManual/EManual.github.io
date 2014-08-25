主要用来实现单次使用的服务，该服务能被启用许多次，但是由于无状态会话Bean 并不保留任
何有关状态的信息，其效果是每次调用提供单独的使用。在很多情况下，无状态会话Bean 提供可重用的单次使
用服务。无状态就意味着共享，多客户端，可以构建pooling池  
注意：单例bean一定是无状态的。通过配置文件sun-ejb-jar.xml(netbeans环境 glassfish服务器)来配置这个池。
配置文件举例如下：
[code=java] 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE sun-ejb-jar PUBLIC "-//Sun Microsystems, 
	Inc.//DTD Application Server 9.0 EJB 3.0//EN" 
	"http://www.sun.com/software/appserver/dtds/sun-ejb-jar_3_0-0.dtd">
<sun-ejb-jar>
  <enterprise-beans>
	  <ejb>
		  <ejb-name>SllcBean</ejb-name><!-- 指定ejb的名字 -->
		  <!-- 对池的配置 -->
		  <bean-pool>
			 <steady-pool-size>2</steady-pool-size>    <!-- 稳定状态下 池中ejb数量 -->
			 <resize-quantity>2</resize-quantity>     <!-- 创建ejb的步长 一次新创建两个 -->
			 <max-pool-size>6</max-pool-size>         <!-- 池中容许的ejb最大数目 -->
		  </bean-pool>
	  </ejb>
  </enterprise-beans>
</sun-ejb-jar>
[/code]
2）无状态session bean的生命周期
1，构造方法(只能无参)
2，属性的依赖注入
3，@PostConstruct标记的方法
(被销毁 时间容器决定  销毁前执行@PreDestroy标记的方法)
由不存在到存在，并非在用户调用此ejb时才转换，容器对ejb的加载分为懒汉式和非懒汉式，若为
后者，则在ejb容器启动时就完成了对ejb的加载，就是说容器启动后ejb就是存在的状态了。
[color=blue]有状态的session bean  
有状态Bean是一个可以维持自身状态的会话Bean。每个用户都有自己的一个实例，在用户的生存期内，StatefulSession Bean保持了用户的信息，即“有状态”；一旦用户灭亡（调用结束或实例结束），Stateful Session Bean的生命期也告结束。即每个用户最初都会得到一个初始的Stateful Session Bean。Stateful Session Bean 的开发步骤与Stateless Session Bean 的开发步骤相同。Stateful Session Bean跟踪用户的状态，一个bean只能被一个用户所使用。此类bean不是管理在 bean pool 中，是比较消耗资源的，一般的时候要尽量避免使用。
Stateless Session Bean 与Stateful Session Bean 的区别。这两种Session Bean 都可以将系统逻辑放在方法之中执行，不同的是Stateful Session Bean 可以记录呼叫者的状态，因此一个使用者会有自己的一个实例。Stateless Session Bean 虽然也是逻辑组件，但是他却不负责记录使用者状态，也就是说当使用者呼叫Stateless Session Bean 的时候，EJB 容器并不会寻找特定的Stateless Session Bean 的实体来执行这个method。换言之，很可能数个使用者在执行某个Stateless Session Bean 的methods 时，会是同一个Bean的实例在执行。从内存方面来看，Stateful Session Bean 与Stateless Session Bean 比较，Stateful Session Bean 会消耗J2EE Server 较多的内存，然而Stateful Session Bean 的优势却在于他可以维持使用者的状态。