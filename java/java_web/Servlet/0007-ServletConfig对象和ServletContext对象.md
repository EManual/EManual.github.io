(1)ServletConfig：用来保存一个Servlet的配置信息的(比如 : name, class, url ... )
这些配置信息没什么大用处，我们还可以在ServletConfig中保存自己在web.xml文件中定义的数据
此时的web.xml文件片段如下：
```java   
<servlet>
	<!-- 自己定义的，要保存在ServletConfig对象中的数据 -->
	<init-param> 
		<param-name>jdbc.driver</param-name>
		<param-value>oracle.jdbc.driver.OracleDriver</param-value>
	</init-param>  
	<init-param> 
		<param-name>jdbc.user</param-name>
		<param-value>yinkui</param-value>
	</init-param>
	...
	<servlet-name>query</servlet-name>
	<servlet-class>com.kettas.servlet.Query</servlet-class>
</servlet>  
```
在Servlet中取得这些数据：
```java   
// getServletConfig方法继承自父类GenericServlet
ServletConfig sc = this.getServletConfig();
// 显然，getInitParameter方法返回的只能是字符串类型数据
String driver = sc.getInitParameter("jdbc.driver");
String user = sc.getInitParameter("jdbc.user");
```
注意：
1 ServletConfig对象只能从web.xml文件中获取自定义数据(字符串数据)，不存在setAttribute方法去存入自定义数据。
2 在Servlet中，若要覆盖父类的init(ServletConfig config)方法，必须这么做：
```java   
public void init( ServletConfig config ){ 
	// 覆盖之前调用父类的这个方法, 否则ServletConfig对象会丢失
	// 此时this.getServletConfig()返回的是null, 那样我们就不能使用它了
	super.init( config ) ;
	...   }			   
```
(2)ServletContext：用来保存数据的全局唯一对象，一个应用中只有一个ServletContext对象
1：通过web.xml文件，在ServletContext对象中存入数据
此时的web.xml文件片段如下所示： 
```java   
<!-- 在此处写入我们要存入ServletContext对象中的数据 -->
<context-param> 
	<param-name>jdbc.driver</param-name>
	<param-value>oracle.jdbc.driver.OracleDriver</param-value>
</context-param>
<context-param> 
	<param-name>jdbc.url</param-name>
	<param-value>jdbc:oracle:thin:@192.168.0.201:1521:kettas</param-value>
</context-param>  
...
<servlet> 
	<servlet-name>...</servlet-name>
	<servlet-class>...</servlet-class>
</servlet>  
```   
取得其中的数据：String driver = servletContext.getInitParameter("jdbc.driver"); 
2：通过setAttribute方法，在ServletContext对象中存入数据
servletContext.setAttribute("name", data); // 两个参数分别为命名属性以及对应的数据
// 取得ServletContext对象中的数据, 参数为命名属性
// 返回的是Object对象, 故要强转
servletContext.getAttribute("name");
3：取得ServletContext对象的三种方法(this指代当前Servlet) 
```java  
(1) ServletContext sc = this.getServletContext();
(2) ServletContext sc = this.getServletConfig().getServletContext();
(3) ServletContext sc = request.getSession(true).getServletContext();
``` 
ServletContext对象的一个重要方法：
```java         				     
InputStream is = sc.getResourceAsStream( "fileName" ) ;
```
fileName：使用的是虚拟目录, 不依赖于实际路径/books/ajax.pdf
最左边一个"/"：web 应用的根目录  
// 获得实际路径  String path = ctx.getRealPath( "/books/ajax.pdf" )