AOP是OOP的延续，是Aspect Oriented Programming的缩写，意思是面向切面的编程。并不是全部的AOP框架都是一样的。他们连接点模型的功能可能有强弱之分，有些可以字段，方法，构造函数级别的，有些只能是方法的比如spring aop 最主要的三种aop框架：AspectJ，Jboss AOP，Spring Aop  前面两种都可以对字段方法构造函数的支持。Sping和AspectJ有大量的协作 。
Aop添加的主要功能有：事务管理，安全，日志，检查，锁等。
Spring对Aop支持的4种情况：
★经典的基于代理的Aop（各个版本的spring） 
★@AspectJ注解驱动的切面（spring 2.0）
★纯POJO切面（spring 2.0）                
★注入式AspectJ切面（各个版本的spring）
* 名词解释：
☆关注点 (Concern)：关注点就是我们要考察或解决的问题。如订单的处理，用户的验证、用户日志记录等都属于关注点。
关注点中的核心关注点 (Core Concerns)，是指系统中的核心功能，即真正的商业逻辑。如在一个电子商务系统中，订单处理、客户管理、库存及物流管理都是属于系统中的核心关注点。
还有一种关注点叫横切关注点 (Crosscutting Concerns)，他们分散在每个各个模块中解决同一样的问题，跨越多个模块。如用户验证、日志管理、事务处理、数据缓存都属于横切关注点。
在 AOP 的编程方法中，主要在于对关注点的提起及抽象。我们可以把一个复杂的系统看作是由多个关注点来有机组合来实现，一个典型的系统可能会包括几个方面的关注点，如核心业务逻辑、性能、数据存储、日志、授权、安全、线程及错误检查等，另外还有开发过程中的关注点，如易维护、易扩展等。
☆切面 (Aspect)：切面是通知和切入点的结合，通知和写入点定义了切面的全部内容—它的功能，在何时何地完成功能。在Spring 2.0 AOP中，切面可以使用通用类（基于模式的风格XML Schema 的风格） 或者在普通类中以 @Aspect 注解（@AspectJ风格）来实现。
下面的例子是基于 xml schema 风格来定义一个 Aspect(红字部分)： 
```java  
<aop:aspect id="aspectDemo" ref="aspectBean"> 
	<aop:pointcut id = "myPointcut" expression = "execution(* package1.Foo.handle*(..)" /> 
	<aop:before pointcut -ref = "myPointcut" method = "doLog" /> 
</aop:aspect > 
```
这个定义的意思是：每执行到 package1.Foo 类的以 handle 开头的方法前，就会先执行 aspectBean 的 doLog 方法
☆连接点 (Join point)：连接点就是在程序执行过程中某个特定的点，比如某方法调用的时候或者处理异常的时候。这个点可以是一个方法、一个属性、构造函数、类静态初始化块，甚至一条语句。切面代码可以通过这些点插入到程序的一般流程之中，从而添加新的行为。 而对于 SPRING 2.0 AOP来说他是基于动态代理的，故只支持方法连接点，这个一定要记住～！每一个方法都可以看成为一个连接点，（AspectJ和Jboss可以提供其他aop的实现如，字段构造函数等）只有被纳入某个Point Cut的 JointPoint 才有可能被 Advice 。 通过声明一个org.aspectj.lang.JoinPoint 
类型的参数可以使通知（Advice）的主体部分获得连接点信息。JoinPoint 与CutPoint 之间的关系见下面的CutPoint 的讲解。
☆切入点 (Pointcut)：如果说通知定义了切面的“什么”和“何时”那么切入点就定义了“何地”。切入点指一个或多个连接点，可以理解成连接电点的集合 。我们通常使用明确的类和方法或是利用正则表达式定义这些切入点。 Advice 是通过 Pointcut 来连接和介入进你的 JointPoint 的。 
比如在前面的例子中，定义了<aop:pointcut id = "myPointcut" expression = "execution(* package1.Foo.handle*(..)" />  那个类的那个方法使用。
那么这就是定义了一个PointCut，该Pointcut 表示“在package1.Foo类所有以handle开头的方法”
假设package1.Foo类里类似于：
```java  
Public class Foo { 
   public handleUpload(){..} 
   public handleReadFile(){..} 
}
```
那么handleUpload 是一个JointPoint ，handleReadFile 也是一个Joint，那么上面定义的id=”myPointcut” 的PointCut 则是这两个JointPoint 的集合
☆通知 (Advice)：通知定义了切面是什么，以及何时使用，去了描述切面要完成的工作，通知还要解决何时执行这个工作的问题。它应该在某个方法之前调用还是之后调用，或者抛出一个异常。故通知有各种类型Advice。定义了切面中的实际逻辑(即实现)，比如日志的写入的实际代码。换一种说法Advice 是指在定义好的切入点处，所要执行的程序代码。
通知有以下几种：
1，前置通知（Before advice） ：在切入点匹配的方法执行之前运行使用@Before 注解来声明。implements MethodBeforeAdvice实现的方法是public void before(Method method, Object[] args, Object target)。
2，返回后通知（After returning advice）：在切入点匹配的方法返回的时候执行。使用 @AfterReturning 注解来声明。
3，抛出后通知（After throwing advice）: 在切入点匹配的方法执行时抛出异常的时候运行。使用 @AfterThrowing 注解来声明
4，后通知（After (finally) advice）：不论切入点匹配的方法是正常结束的，还是抛出异常结束的，在它结束后（finally）后通知（After (finally) advice）都会运行。使用 @After 注解来声明。这个通知必须做好处理正常返 回和异常返回两种情况。通常用来释放资源。
5，环绕通知（Around Advice）：环绕通知既在切入点匹配的方法执行之前又在执行之后运行。并且，它可以决定这个方法在什么时候执行，如何执行，甚至是否执行。在环绕通知中，除了可以自由添加需要的横切功能以外，还需要负责主动调用连接点 ( 通过 proceed) 来执行激活连接点的程序。 请尽量使用最简单的满足你需求的通知。（比如如果前置通知也可以适用的情况下，就不要使用环绕通知） 
6，环绕通知使用@Around注解来声明。而且该通知对应的方法的第一个参数必须是ProceedingJoinPoint类型。在通知体内（即通知的具体方法内），调用 ProceedingJoinPoint 的 proceed() 方法来执行连接点方法。
☆引入 (Introduction)：引入是指给一个现有类添加方法或字段属性，引入还可以在不改变现有类代码的情况下，让现有的Java类实现新的接口 （以及一个对应的实现 ）。相对于 Advice 可以动态改变程序的功能或流程来说，引入 (Introduction) 则用来改变一个类的静态结构 。比如你可以使用一个引入来使bean实现IsModified接口，以便简化缓存机制。举例来说，我们可以创建一个Audiable通知类，记录对象在最后一次被修改是时的状态，这很简单，只要一个方法，setLastModified(Date)，和一个实例变量来保存这个状态，这个新的方法和实例变量然后就可以引入到现在的类，从而在不修改他们的情况下让他们有新的行为和状态。
☆目标对象（ Target Object ）被一个或者多个切面（aspect）所通知（advise）的对象。也有人把它叫做 被通知（advised）对象。 既然Spring AOP是通过运行时代理实现的，这个对象永远是一个 被代理（proxied ）对象。
☆AOP 代理（AOP Proxy）“代理”是向目标对象应用通知之后被创建的对象，对客户端来说目标对象和代理对象是一样的。AOP框架创建的对象，用来实现切面契约（aspect contract）（包括通知方法执行等功能）。 在Spring中，AOP生成被代理的类有两种：如果目标对象实现的是一个接口则是用JDK的  java.lang.reflect.Proxy动态代理;如果不是接口则用CGLIB库生成目标生成目标类的子类在创建这个子类的时候spring织入通知，并且把这个子类的调用委托给子类，这样就要注意两点，1，最好是用接口实现代理，cglib只是实现没有接口也可以通知的情况。2，被标记final的方法和类不能通知因为无法创建子类。。
☆织入（Weaving）把切面（aspect）连接到其它的应用程序类型或者对象上，并创建一个被通知（advised）的对象，这样一个行为就叫做Weaving。 这些可以在编译时（例如使用AspectJ 编译器），类加载时和运行时完成。 Spring 和其他纯 Java AOP 框架一样，在运行时完成织入 。
其实织入的方式有3种：
1、编译器织入： 切面在目标类编译时植入，这需要特殊的编译器。AspectJ 主要就是是使用这种织入方式 。
2、类加载器织入： －切面在目标类加载到JVM的时候进行织入，这需要特殊的ClassLoader。它可以在目标类被加载到程序之前增强类的字节代码。比如AspectWerkz (已并入 AspecJ)及JBoss就使用这种方式 。 
3、运行时织入： －即在java运行的过程中，使用Java提供代理来实现织入。根据代理产生方式的不同，运行时织入又可以进一步分为J2SE动态代理及动态字节码生成两种方式。由于J2SE动态代理只能代理接口，因此，需要借助于一些动态字节码生成器来实现对类的动态代理。大多数AOP实现都是采用这种运行时织入的方式，包括Spring 。