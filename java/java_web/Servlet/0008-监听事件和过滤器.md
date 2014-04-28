监听包括三种情况，分别是HttpRequest、Session、ServletContext监听。
常用的是implements  servletContextListener（全局变量）两个方法 
```java   
public void contextInitialized(ServletContextEvent arg0)
arg0.getServletContext()
```
Session监听事件所示：	 
```java   
import javax.servlet.http.HttpSession;
import javax.servlet.http.HttpSessionEvent;
import javax.servlet.http.HttpSessionListener;
import com.kettas.upp02.util.Constant;
public class SessionListener implements HttpSessionListener {
	public void sessionCreated(HttpSessionEvent ent) {
		HttpSession session = ent.getSession();
		synchronized (this) {
			ServletContext ctx = session.getServletContext();
			Integer counter = (Integer) ctx.getAttribute("sessionCount");
			ctx.setAttribute("sessionCount", counter.intValue() + 1);
			System.out.println(Constant.LOGO + "SessionCount:"
					+ (counter.intValue() + 1));
		}}
	public void sessionDestroyed(HttpSessionEvent ent) {
		HttpSession session = ent.getSession();
		synchronized (this) {
			ServletContext ctx = session.getServletContext();
			Integer counter = (Integer) ctx.getAttribute("sessionCount");
			ctx.setAttribute("sessionCount", counter.intValue() - 1);
			System.out.println(Constant.LOGO + "SessionCount:"
					+ (counter.intValue() - 1));
		}
	}
}
```
在web.xml文件中配置如下： 
```java   
<listener>
	<listener-class>shop. SessionListener </listener-class>
</listener>
```
其他两个监听事件的实现同上并无二致。				
过滤器  	// 实现Filter接口
```java   
import java.io.IOException;
import javax.servlet.*;
public class EncodingFilter implements Filter{
//销毁时执行，没必要覆盖
	public void destroy() {}
	//发送请求时执行
	public void doFilter(ServletRequest request, ServletResponse response,
			FilterChain chain) throws IOException, ServletException {
		//设置发送请求和接收请求时的编码方式，统一才能达到过滤作用
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");
		try {
			chain.doFilter(request, response); 请求转发
		} catch (RuntimeException e) {
			e.printStackTrace();
		}}
	//加载时执行，也没必要执行
	public void init(FilterConfig arg0) throws ServletException {}
}
```
web.xml文件中：
//配置当发生什么要的请求时，让那个过滤流执行操作
```java   
 <filter>
	<filter-name>encodingFilter</filter-name>
	<filter-class>filter.EncodingFilter</filter-class>
</filter>
<filter-mapping>
	<filter-name>encodingFilter</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>
```