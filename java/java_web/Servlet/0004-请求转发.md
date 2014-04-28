实现不同servlet之间的数据传递，这样便可实现业务逻辑和显示逻辑的分离
实例：
(1) 第一个servlet，负责业务
```java  
package com.kettas.servlet ;
import javax.servlet.* ;
import javax.servlet.http.*;
import java.io.*; 
import java.util.* ;
public class ForwardA extends HttpServlet{
	@Override
	public void service( HttpServletRequest request , HttpServletResponse response )
		throws ServletException , IOException
	{	   System.out.println( "=== This is forward A ===" ) ;
		   // 将业务部分的数据存储在request对象中，传递给下一个servlet使用
		   Date d = new Date();
		   request.setAttribute( "date" , d ) ;
		   /* 注意转发的过程
			* 首先获得一个知道下一棒地址的"接力棒"对象，然后将这个"接力棒"传给下一个
			* servlet，这样便将请求转发了。
			*/
		   RequestDispatcher disp = request.getRequestDispatcher( "/forwardB" ) ;
		   disp.forward( request , response ) ;
	}
}
```
注意：
1，这种请求转发的方式是共用一个连接的，不管你中途经过了多少个servlet，正因如此，这些servlet才能共享request中存储的数据。
2，只有最后一个servlet，才能在客户端浏览器中显示。
(2) 第二个servlet，负责显示
```java  
package com.kettas.servlet ;
import javax.servlet.* ;
import javax.servlet.http.*;
import java.io.*; 
import java.util.* ;
public class ForwardB extends HttpServlet{
	@Override
	public void service( HttpServletRequest request , HttpServletResponse response )
		throws ServletException , IOException
	{       response.setContentType( "text/html" ); 
		   PrintWriter out = response.getWriter();
		   out.println( "<h2>This is forwared B</h2>" ) ;
		   // 通过getAttribute方法，从request中取得数据
		   // 由于此方法返回的是Object对象，故要强转
		   Date d = (Date)request.getAttribute( "date" ) ;
		   out.println( "<h2>" + d + "</h2>" ) ;
		   System.out.println( "=== This is forward B ===" ) ;
		   out.flush();
	}
}
```
(3) web.xml片段：
```java  
<servlet> 
	<servlet-name>a</servlet-name>
	<servlet-class>com.kettas.servlet.ForwardA</servlet-class>
</servlet>                                  
<servlet-mapping> 
	<servlet-name>a</servlet-name>  
	<url-pattern>/forwardA</url-pattern>
</servlet-mapping>
<servlet> 
	<servlet-name>b</servlet-name>
	<servlet-class>com.kettas.servlet.ForwardB</servlet-class>
</servlet>                                  
<servlet-mapping> 
	<servlet-name>b</servlet-name>  
	<url-pattern>/forwardB</url-pattern>
</servlet-mapping>
```
页面跳转的两种方式：
1）request.getRequestDispatcher(“/forwardA”).forward(request , response); 这种跳转是在服务器内部是servlet之间跳转，显示的总是最后一个servlet  A-?B--?----?D
2)response.sendRedirect(“mayservlet/query”)它其实是在客户端的url发生改变,相当一次新的请求，故不能传递数据，但能在不同的应用中跳转