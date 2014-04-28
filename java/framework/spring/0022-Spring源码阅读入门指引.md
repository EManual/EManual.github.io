本文大概的对IOC和AOP进行了解，入门先到这一点便已经有了大概的印象了，详细内容请看下文。
AD：
本文说明2点：
1.阅读源码的入口在哪里？
2.入门前必备知识了解：IOC和AOP
一、我们从哪里开始
1.准备工作：在官网上下载了Spring源代码之后，导入Eclipse，以方便查询。
2.打开我们使用Spring的项目工程，找到Web.xml这个网站系统配置文件，在其中找到Spring的初始化信息：
```java  
<listener> 
 <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class> 
</listener> 
```
由配置信息可知，我们开始的入口就这里ContextLoaderListener这个监听器。
在源代码中我们找到了这个类，它的定义是：
```java  
public class ContextLoaderListener extends ContextLoader  
 implements ServletContextListener {  
    …  
 /**  
  * Initialize the root web application context.  
  */ 
 public void contextInitialized(ServletContextEvent event) {  
  this.contextLoader = createContextLoader();  
  if (this.contextLoader == null) {  
   this.contextLoader = this;  
  }  
  this.contextLoader.initWebApplicationContext(event.getServletContext());  
 }  
  ...  
}  
```
该类继续了ContextLoader并实现了监听器，关于Spring的信息载入配置、初始化便是从这里开始了，具体其他阅读另外写文章来深入了解。
二、关于IOC和AOP
关于Spring IOC 网上很多相关的文章可以阅读，那么我们从中了解到的知识点是什么？
1）IOC容器和AOP切面依赖注入是Spring是核心。
IOC容器为开发者管理对象之间的依赖关系提供了便利和基础服务，其中Bean工厂（BeanFactory）和上下文（ApplicationContext）就是IOC的表现形式。
BeanFactory是个接口类，只是对容器提供的最基本服务提供了定义，而DefaultListTableBeanFactory、XmlBeanFactory、ApplicationContext等都是具体的实现。
接口：
```java  
public interface BeanFactory {  
 //这里是对工厂Bean的转义定义，因为如果使用bean的名字检索IOC容器得到的对象是工厂Bean生成的对象，  
 //如果需要得到工厂Bean本身，需要使用转义的名字来向IOC容器检索  
 String FACTORY_BEAN_PREFIX = "&";  
 //这里根据bean的名字，在IOC容器中得到bean实例，这个IOC容器就象一个大的抽象工厂，用户可以根据名字得到需要的bean  
 //在Spring中，Bean和普通的JAVA对象不同在于：  
 //Bean已经包含了我们在Bean定义信息中的依赖关系的处理，同时Bean是已经被放到IOC容器中进行管理了，有它自己的生命周期  
 Object getBean(String name) throws BeansException;  
 //这里根据bean的名字和Class类型来得到bean实例，和上面的方法不同在于它会抛出异常：如果根名字取得的bean实例的Class类型和需要的不同的话。  
 Object getBean(String name, Class requiredType) throws BeansException;  
 //这里提供对bean的检索，看看是否在IOC容器有这个名字的bean  
 boolean containsBean(String name);  
 //这里根据bean名字得到bean实例，并同时判断这个bean是不是单件，在配置的时候，默认的Bean被配置成单件形式,如果不需要单件形式，需要用户在Bean定义信息中标注出来，这样IOC容器在每次接受到用户的getBean要求的时候，会生成一个新的Bean返回给客户使用 - 这就是Prototype形式  
 boolean isSingleton(String name) throws NoSuchBeanDefinitionException;  
 //这里对得到bean实例的Class类型  
 Class getType(String name) throws NoSuchBeanDefinitionException;  
 //这里得到bean的别名，如果根据别名检索，那么其原名也会被检索出来  
 String[] getAliases(String name);  
} 
```
实现：
XmlBeanFactory的实现是这样的：
```java  
public class XmlBeanFactory extends DefaultListableBeanFactory {  
 //这里为容器定义了一个默认使用的bean定义读取器，在Spring的使用中，Bean定义信息的读取是容器初始化的一部分，但是在实现上是和容器的注册以及依赖的注入是分开的，这样可以使用灵活的 bean定义读取机制。  
 private final XmlBeanDefinitionReader reader = new XmlBeanDefinitionReader(this);  
 //这里需要一个Resource类型的Bean定义信息，实际上的定位过程是由Resource的构建过程来完成的。  
 public XmlBeanFactory(Resource resource) throws BeansException {  
 this(resource, null);  
 }  
 //在初始化函数中使用读取器来对资源进行读取，得到bean定义信息。这里完成整个IOC容器对Bean定义信息的载入和注册过程  
 public XmlBeanFactory(Resource resource, BeanFactory parentBeanFactory) throws 
 BeansException {  
 super(parentBeanFactory);  
 this.reader.loadBeanDefinitions(resource);  
} 
```
我们可以看到IOC容器使用的一些基本过程：
如：DefaultListableBeanFactory
```java  
ClassPathResource res = new ClassPathResource("beans.xml");//读取配置文件  
DefaultListableBeanFactory factory = new DefaultListableBeanFactory();  
XmlBeanDefinitionReader reader = new XmlBeanDefinitionReader(factory);  
reader.loadBeanDefinitions(res);  
```
这些代码演示了以下几个步骤：
1. 创建IOC配置文件的抽象资源
2. 创建一个BeanFactory，这里我们使用DefaultListableBeanFactory；
3. 创建一个载入bean定义信息的读取器，这里使用XmlBeanDefinitionReader来载入XML形式的bean定义信息，配置给BeanFactory；
4. 从定义好的资源位置读入配置信息，具体的解析过程由XmlBeanDefinitionReader来完成，这样完成整个载入和注册bean定义的过程。我们的IoC容器就建立起来了。
再简单的说，我的系统在启动时候，会完成的动作就是：
1.由ResourceLoader获取资源文件，也即bean的各种配置文件；
2.由BeanDefintion对配置文件的定义信息的载入；
3.用BeanDefinitionRegistry接口来实现载入bean定义信息并向IOC容器进行注册。
注意，IOC容器和上下文的初始化一般不包含Bean的依赖注入的实现。
2）AOP这个过程并不是在注册bean的过程实现的。
我们只看到在处理相关的Bean属性的时候，使用了RuntimeBeanReference对象作为依赖信息的纪录。
在IOC容器已经载入了用户定义的Bean信息前提下，这个依赖注入的过程是用户第一次向IOC容器索要Bean的时候触发的，或者是我们可以在Bean定义信息中通过控制lazy-init属性来使得容器完成对Bean的预实例化 - 这个预实例化也是一个完成依赖注入的过程。
我们说明一下过程：
1.用户想IOC容器请求Bean。
2.系统先在缓存中查找是否有该名称的Bean（去各个BeanFactory去查找）
3.没有的话就去创建Bean并进行依赖注入，并且这个请求将被记录起来。
请求Bean具体的实现：
代码入口在DefaultListableBeanFactory的基类AbstractBeanFactory中：
```java  
public Object getBean(String name, Class requiredType, final Object[] args) throwsBeansException {  
...  
 Object sharedInstance = getSingleton(beanName);//先去缓存取  
 if (sharedInstance != null) {  
 ...  
  if (containsBeanDefinition(beanName)) {  
   RootBeanDefinition mergedBeanDefinition = getMergedBeanDefinition(beanName, false);  
   bean = getObjectForBeanInstance(sharedInstance, name,mergedBeanDefinition);  
  }  
  else {  
   bean = getObjectForBeanInstance(sharedInstance, name, null);  
  }  
 }  
 else {  
   
 }  
 
...  
} 
```
注入Bean具体的实现：
具体的bean创建过程和依赖关系的注入在createBean中，这个方法在AbstractAutowireCapableBeanFactory中给出了实现：
```java  
protected Object createBean(String beanName, RootBeanDefinition  
mergedBeanDefinition, Object[] args)  
throws BeanCreationException {  
 // Guarantee initialization of beans that the current one depends on.  
 // 这里对取得当前bean的所有依赖bean，确定能够取得这些已经被确定的bean，如果没有被创建，那么这个createBean会被这些IOC  
 // getbean时创建这些bean  
 if (mergedBeanDefinition.getDependsOn() != null) {  
  for (int i = 0; i < mergedBeanDefinition.getDependsOn().length; i++) {  
   getBean(mergedBeanDefinition.getDependsOn()[i]);  
  }  
 }  
 ........  
 // 这里是实例化bean对象的地方，注意这个BeanWrapper类，是对bean操作的主要封装类  
 if (instanceWrapper == null) {  
  instanceWrapper = createBeanInstance(beanName, mergedBeanDefinition,args);  
 }  
 Object bean = instanceWrapper.getWrappedInstance();  
 ......  
 //这个populate方法，是对已经创建的bean实例进行依赖注入的地方，会使用到在loadBeanDefinition的时候得到的那些propertyValue来对bean进行注入。  
 if (continueWithPropertyPopulation) {  
  populateBean(beanName, mergedBeanDefinition, instanceWrapper);  
 }  
 //这里完成客户自定义的对bean的一些初始化动作  
 Object originalBean = bean;  
 bean = initializeBean(beanName, bean, mergedBeanDefinition);  
 // Register bean as disposable, and also as dependent on specified "dependsOn"beans.  
 registerDisposableBeanIfNecessary(beanName, originalBean,mergedBeanDefinition);  
 return bean;  
}  
.........  
} 
```
这就是整个依赖注入的部分处理过程，在这个过程中起主要作用的是WrapperImp ，这个Wrapper不是一个简单的对bean对象的封装，因为它需要处理在beanDefinition中的信息来迭代的处理依赖注入。
到这里，这是简单的，大概的对IOC和AOP进行了解，入门先到这一点便已经有了大概的印象了。