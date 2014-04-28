Spring容器,最基本的接口就是BeanFactory 负责创建，配置，管理bean 它有一个子接口ApplicationContext并将功能扩展。
理论上bean装配可以从任何资源获得，包括属性文件，关系数据库等，但xml是最常用的XmlBeanFactory，ClassPathXmlApplicationContext，FileSystemXmlApplicationContext，XmlWebApplicationContext应用系统配置源。Spring中的几种容器都支持使用xml装配bean，包括：
XmlBeanFactory，ClassPathXmlApplicationContext，FileSystemXmlApplicationContext，XmlWebApplicationContext
BeanFactory接口包含如下的基本方法： 
```java  
Boolean containsBean(String name)：判断Spring容器是否包含id为name的bean定义。
Object getBean(String name)：返回容器id为name的bean。
Object getBean(String name, Class requiredType)：返回容器中id为name,并且类型为requiredType的bean。
Class getType(String name)：返回容器中id为name的bean的类型。
```
ApplicationContext有三个实现类实现资源访问:
```java  
FileSystemXmlApplicationContext：基于文件系统的xml配置文件创建ApplicationContext。
ClassPathXmlApplicationContext：以类加载路径下的xml的配置文件创建ApplicationContext（更为常用）。
XmlWebApplicationContext：对使用servletContextResource进行资源访问。
```
获得容器的应用的方式:
```java  
① InputStream is = new FileInputStream("bean.xml");
XmlBeanFactory factory = new XmlBeanFactory(is);
或者BeanFactory factory = new XmlBeanFactory(new ClassPathResource("classpath：bean.xml"))
Action action = (Action) factory.getBean("TheAction");
② ApplicationContext bf=new ClassPathXmlApplicationContext("classpath：bean.xml")
Action action = (Action) factory.getBean("TheAction");
③ ApplicationContext bf=new FileSystemXmlApplicationContext(“classpath：bean.xml”)
```
第一种BeanFactory启动快（启动是不创建实体，到用时才创建实体），
第二种ApplicationContext运行快（在加载时就创建好实体）更为常用，继承BeanFactory。