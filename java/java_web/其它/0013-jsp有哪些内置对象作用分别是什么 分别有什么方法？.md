JSP共有以下9个内置的对象： 
```java  
request 用户端请求，此请求会包含来自GET/POST请求的参数 
response 网页传回用户端的回应 
pageContext 网页的属性是在这里管理 
session 与请求有关的会话期 
application servlet 正在执行的内容 
out 用来传送回应的输出 
config servlet的构架部件 
page JSP网页本身 
exception 针对错误网页，未捕捉的例外 
request：表示HttpServletRequest对象。它包含了有关浏览器请求的信息，并且提供了几个用于获取cookie, header, 和session数据的有用的方法。 
response：表示HttpServletResponse对象，并提供了几个用于设置送回 浏览器的响应的方法（如cookies,头信息等） 
out：对象是javax.jsp.JspWriter的一个实例，并提供了几个方法使你能用于向浏览器回送输出结果。 
pageContext：表示一个javax.servlet.jsp.PageContext对象。它是用于方便存取各种范围的名字空间、servlet相关的对象的API，并且包装了通用的servlet相关功能的方法。 
session：表示一个请求的javax.servlet.http.HttpSession对象。Session可以存贮用户的状态信息 
applicaton ：表示一个javax.servle.ServletContext对象。这有助于查找有关servlet引擎和servlet环境的信息 
config：表示一个javax.servlet.ServletConfig对象。该对象用于存取servlet实例的初始化参数。 
page：表示从该页面产生的一个servlet实例
```