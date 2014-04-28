Servlet是最顶层的接口，其提供的方法有：
```java  
init(ServletConfig config)：void   // 初始化   
getServletConfig()：ServletConfig  // 取得该Servlet配置信息
getServletInfo()：String		   // 取得相关信息
service(ServletRequest req, ServletResponse res)：void   //核心方法
destroy()：void   // Servlet生命周期结束时候执行的方法
```
显然我们最关心的是service方法，其他的几个方法在实现的时候是千篇一律、无关痛痒的。故提供了GenericServlet类，此类实现了Servlet接口，我们在使用Servlet的时候，只需继承这个类然后覆盖其中的service方法(抛出ServletException、IOException异常)即可。
由于Servlet基本上是在http协议下使用的，故提供了HttpServlet这个类，此类继承自GenericServlet类，我们在使用Servlet时，只需继承HttpServlet类然后覆盖以下方法：
```java  
service( HttpServletRequest request ,
		 HttpServletResponse response )
		 throws ServletException , IOException : void
```
注意：HttpServletRequest和HttpServletResponse分别是从ServletRequest和ServletResponse继承
此外，HttpServlet还提供了doPost和doGet方法，参数和返回值与service方法一样。只是service方法可以针对客户端的任何请求类型(GET和POST)，而doPost和doGet方法分别只能对应客户端的POST方式请求和GET方式的请求。