Spring的aop机制提供两类方式实现类代理。一种是单个代理，一种是自动代理。
单个代理通过ProxyFactoryBean来实现（就如上面的配置）。
自动代理：自动代理能够让切面定义来决定那个bean需要代理，不需要我们为特定的bean明确的创建代理从而提供一个更完整的aop实现 通过BeanNameAutoProxyCreator或者 DefaultAdvisorAutoProxyCreator实现。
◆采用单个代理方式 （费时费力,配置复杂臃肿）
下面就采用自动代理 
实现代理bean的两种方式：
1，“基于Spring上下文的里声明的通知者bean的基本自动代理”：通知者的切点表达式用于决定哪个bean和那些方法需要被代理
2,”基于@AspectJ注释驱动切面的自动代理”：切面里包含的通知里指定的切点将用于选择哪个bean和哪个方法要被代理
第一种：<！——自动代理增加此行，容器会自动根据通知要匹配的切入点，为包含切入点的类创建　代理。注意这个bean没有id，因为永远都不会直接引用它——> 
<bean class="org.springframework.aop.framework.autoproxy.DefaultAdvisorAutoProxyCreator"/> feedom.net 　　   
第二种 自动代理@AspectJ切面
然而aspectJ提供可一种基于jdk1.5注解技术的方式，使得配置文件更少，更方便。能够把POJO类注释为切面这通常称为
@AspectJ.我们利用@AspectJ注释，我们不需要声明任何额外的类或Bean就可以把POJO转换成一个切面例如：  
@Aspect  定义切面不再是普通的POJO了 在POJO类中加注释
```java  
public class AspectJMixAspect {	
	private Log logger = LogFactory.getLog(AspectJMixAspect.class);	
	@Pointcut("execution(* *..HelloIF.*(..)) || execution(* *..TestBeanIF.*(..))")定义切入点那些类的那些方法添加
	public void allMethods() {	}	
	@Pointcut("execution(* *..TestBeanIF.toDate(..)) && args(dateStr)")	
	public void toDate(String dateStr) {	
	}	
	@Around("allMethods()")	环绕通知
	public Object timing(ProceedingJoinPoint pjp) throws Throwable {	
		long begin = System.currentTimeMillis();	
		Object ret = pjp.proceed();	
		long end = System.currentTimeMillis();	
		String methodName = pjp.getSignature().getName();	
		String targetClass = pjp.getTarget().getClass().getName();	
		logger.info("Around advice: It took " + (end - begin) + "ms to call "
						+ methodName + " on " + targetClass);
		return ret;
	}
	@Before("allMethods()")
	public void logBefore(JoinPoint jp) {
		logger.info("Before advice: " + jp.getSignature().toLongString());	
	}	
	@AfterReturning(value="toDate(dateStr)", returning = "date", argNames = "date, dateStr")	
	public void afterReturning(Date date, String dateStr) {
		logger.info("call method toDate(" + dateStr + ") and return " + date);	
	}	
	@AfterThrowing(value="toDate(dateStr)", throwing="ex", argNames="dateStr, ex")	
	public void afterThrowing(String dateStr, ParseException ex){方法名任意但参数要和argNames=""中的参数顺序一样，
	}
}
```
配置文件
```java  
<?xml version="1.0" encoding="UTF-8"?>
<p:beans xmlns:aop="http://www.springframework.org/schema/aop"
	xmlns:p="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.5.xsd http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-2.5.xsd ">
	<!-- target -->
	<p:bean id="hello" class="com.kettas.spring.ioc.day1.HelloIFImpl">
		<p:property name="cal">
			<p:bean class="java.util.GregorianCalendar"></p:bean>
		</p:property>
		<p:property name="user" value="world"></p:property>
	</p:bean>
	<p:bean id="testBean" class="com.kettas.spring.aop.day5.TestBean">
		<p:property name="pattern" value="yyyy-MM-dd"></p:property>
	</p:bean>
	<!-- apsect bean -->
	<p:bean id="aspectJAspect" class="com.kettas.spring.aop.day5.AspectJMixAspect"></p:bean>
<aop:aspectj-autoproxy></aop:aspectj-autoproxy> 声明自动代理bean需要命名空间:aop="http://www.springframework.org/schema/aop"
</p:beans>
```