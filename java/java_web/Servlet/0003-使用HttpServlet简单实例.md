使用HttpServlet简单实例
```java  
package com.kettas.servlet ;
import javax.servlet.* ;
import javax.servlet.http.* ;
import java.io.* ;
public class LoginServlet extends HttpServlet{
	@Override 
	public void service( HttpServletRequest request , HttpServletResponse response )
		throws ServletException , IOException 
	{   response.setContentType("text/html; charset=GB2312"); // 注意设置编码的方式
		request.setCharacterEncoding("GB2312");
		PrintWriter out = response.getWriter();
		// 取得客户端提交的数据 
		String name = request.getParameter( "userName" ) ;
		String pwd = request.getParameter( "password" ) ;
		out.println("<html>");
		out.println("<body>");
		out.println("<h1>");
		out.println("Name : " + name + "   " + "Password : " + pwd);
		out.println("</h1>");
		out.println("</body>");
		out.println("</html>");
		out.flush();
	}
}
```
配置文件web.xml片段：
```java  
<servlet> 
	<servlet-name>login</servlet-name>
	<servlet-class>com.kettas.servlet.LoginServlet</servlet-class>
</servlet>                                      
<servlet-mapping>       
	<servlet-name>login</servlet-name>
	<url-pattern>/login</url-pattern>
</servlet-mapping>
```