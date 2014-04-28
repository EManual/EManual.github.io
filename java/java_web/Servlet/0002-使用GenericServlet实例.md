使用GenericServlet实例
```java  
package com.kettas.servlet;
import javax.servlet.* ;
import java.io.* ;
public class GenDateServlet extends GenericServlet{
	@Override
	public void service( ServletRequest request , ServletResponse response )
		throws ServletException ,IOException
	{	    	 response.setContentType( "text/html" ) ; // 设置响应内容类型
			 PrintWriter out = response.getWriter();// 获得文本写入流
			 // 给客户端回应的html文本
			 out.println( "<html>" ) ;
			 out.println( "<body>" ) ; 
			 out.println( "<h1>Hello Servlet ！</h1>" );
			 out.println( "</body>" ) ;
			 out.println( "</html>" ) ; 
			 out.flush();// 刷新写入
	}
}
```
配置文件web.xml如下：
```java  
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://java.sun.com/xml/ns/javaee"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"
   version="2.5"> 		
	// Servlet文件路径
	<servlet> 
		<servlet-name>query</servlet-name>
		<servlet-class>com.kettas.servlet.GenDateServlet</servlet-class>
	</servlet>       
	// 指定映射，说明在浏览器中输入".../query"则对应当前Servlet                              
	<servlet-mapping> 
		<servlet-name>query</servlet-name>
		<url-pattern>/query</url-pattern>
	</servlet-mapping>
</web-app>
```