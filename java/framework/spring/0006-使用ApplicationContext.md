ApplicationContext覆盖了BeanFactory的所有功能，并提供了更多的特，容器创建时就创建了singleton Bean
相对BeanFactory而言，ApplicationContext提供了以下扩展功能：
1．国际化支持：继承MessageSource接口，提供国际化支持
2．资源访问：支持对文件和URL的访问。
3．事件传播：事件传播特性为系统中状态改变时的检测提供了良好支持。
4．多实例加载：可以在同一个应用中加载多个Context实例，即加多个配置文件。
* 国际化处理的步骤
1）写相应的国家资源文件如：ApplicationResources_zh.properties，注意字符的转化类似struts的国际化
2）bean.xml 的配置
```java  
<p:bean id="messageSource " class="org.springframework.context.support.ResourceBundleMessageSource">
	<p:property name="basename" value="com.kettas.spring.ioc.day3.ApplicationResource" /> 
	</p:bean>
	<p:bean id="msc" class="com.kettas.spring.ioc.day3.MessageSourceConsumer" /> 
</p:beans>
```
3）实现类MessageSourceConsumer
具体的实现类implements MessageSourceAware。注入messageSource ms得到字符：String name = ms.getMessage("name", null, Locale.CHINA);name是资源文件的key值
Locale.CHINA是中文，Locale.ENGLISH英文
* 资源访问：即外部资源文件的获取;资源文件
两种引入外部资源的方式：
①
```java  
<!-- <p:bean class="org.springframework.beans.factory.config.PropertyPlaceholderConfigurer">
	<p:property name="location" value="com/kettas/spring/ioc/day3/jdbc.properties"></p:property>
</p:bean> -->
```
②，引入解析：
```java  
xmlns:context="http://www.springframework.org/schema/context"
<context:property-placeholder location="com/kettas/spring/ioc/day3/jdbc.properties"/>
```
使用<p:property name="driverClassName" value="${jdbc.driver}"></p:property>
jdbc.driver是资源的key值
其它：ApplicationContext.getResource方法提供了对资源文件访问支持，如：
```java  
Resource rs = ctx.getResource("classpath:config.properties");
File file = rs.getFile();
```
* 事件传播：事件机制是观察者模式的实现
事件框架两个重要的成员：
1）ApplicationEvent：容器事件，必须由ApplicationContext发布。
2）ApplicationListener：监听器：可有其他任何监听器bean担任。
3）ApplicationContext是事件源必须由java程序显示的触发。
1)事件流程：
  
2)代码实例：
1，事件源。
```java  
public class LogEventSource implements ApplicationEventPublisherAware 
{
	private ApplicationEventPublisher publisher;   
	public void setApplicationEventPublisher(ApplicationEventPublisher publisher){  
		this.publisher = publisher;
	}
	public void fireEvent(){
		LogEvent evt = new LogEvent(this, "Test message");
		publisher.publishEvent(evt);
	}
}
```
2，事件监听，
```java  
public class Logger implements ApplicationListener {
	private Log logger = LogFactory.getLog(Logger.class);
	public void onApplicationEvent(
	ApplicationEvent evt) {
		logger.info("Event type: " + evt.getClass().getName());
		if(evt instanceof LogEvent){		         
			logger.info(((LogEvent)evt).getMessage());
		}
	}
}
```
3)配置文件
```java  
<p:bean id="les"  class="com.kettas.spring.ioc.day3.LogEventSource"> 有相应的事件方法
</p:bean>
<p:bean class="com.kettas.spring.ioc.day3.Logger"></p:bean> 处理事件的后台
</p:beans>
```
说明：LogEventSourc有相应的事件方法publisher.publishEvent(evt)主动触发容器事件; Logge处理事件的后台
* 多实例加载
BeanPostProcessor bean后处理器 实现BeanPostProcessor接口 对bean实例进一步增加功能，实现两个方法processBeforeInitialization(Object bean，String name)方法（该方法的第一个参数是将进行后处理的实例bean，name是该bean的名字）和ProcessaAfterInitialization(Object bean，String name).在init（）或destory之前做一些处理.Spring的工具类就是通过bean的后处理器完成的。
BeanFactoryPostProcessor 容器后处理器：实现接口BeanFactoryPostProcessor只负责处理容器本身 ，实现的方法是postProcessBeanFactory（ConfigurableListableBeanFactory  beanFactory）参加资源的引入和获取，可以修改bean工厂bean的定义相当一个再配置的过程。类似BeanPostProcessor，ApplicationContext可以自动检测到容器中的容器后处理器，但是BeanFacory必须手动调用。