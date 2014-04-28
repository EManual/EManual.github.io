关于Cookie，在客户端浏览器保存用户状态的一种机制。
servlet中的Cookie含有三个属性：name, value, maxAge。
maxAge = 60 表示：此cookie在客户端存在1分钟。
两个特殊值：
maxAge = -1 表示：此Cookie生命周期由保存它的浏览器决定 ，(浏览器开则生，关则死)，默认的。
maxAge = 0  表示：删去以前的相应cookie存储。
Cookie应用实例：
```java  
package com.kettas.servlet ;
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
public class CookieServlet extends HttpServlet{
	@Override 
	public void service( HttpServletRequest request , HttpServletResponse response )
		throws ServletException , IOException 
	{// 创建一个新的Cookie对象, 构造参数分别为Cookie的name和value属性
		Cookie c = new Cookie( "test" , "1234567890" );
		// 将Cookie对象加入response中，这样才能被带入客户端
		response.addCookie( c ) ;  
		// 从请求中获取客户端Cookie数组
		Cookie[] cookies = request.getCookies();
		response.setContentType( "text/html" );
		PrintWriter out = response.getWriter();
		out.println("<html>"); 
		out.println( "<body>" ) ; 
		out.println( "<h1>Cookie List</h1><hr/><p></p>" ) ;
		if( cookies != null ){
			for( Cookie cookie : cookies ) {
				out.println( "<h2>" + cookie.getName() + "=" + cookie.getValue() + "</h2>" ) ;
			}
		}else{
			  out.println( "<h2>No cookie</h2>" ) ;
		}
		out.println( "</body>" ) ;
		out.println("</html>");
		out.flush();
	}
}
```