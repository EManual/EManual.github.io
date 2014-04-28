jsp中的隐含9对象
```java  
request ----> HttpServletRequest。
response ---> HttpServletResponse。
session ----> HttpSession。
application -> ServletContext。 
			   |-> web.xml。
			   |-> setAttribute, getAttribute。
			   |-> 全局唯一。 
```			   
以下四个用的很少，知道有这个东西即可。   
```java  
out  ---------> response.getWriter();<% out.println()%>。
config -------> ServletConfig <在xml中也可以配置servlet，可以配置初始化参数>。
exception  ---> Exception。
page    ------> Object。
```
相当重要的隐含对象，重点说明
pageContext --> javax.serlvet.jsp.PageContext
关于pageContext：
1，本身也是一个能存储命名属性的作用域。
```java  
setAttribute("name", data)
getAttribute("name")
```
pageContext作用域和声明周期。
声明周期只局限在本页面。
在同一页面的不同标签之间传递数据。（本页面共享数据）
同时保证数据不流传到其他页面上。	            
2，可以管理其他作用域中的命名属性。
```java  
pageContext.getAttribute("name");
pageContext.getAttribute("name",int scope); 
```
scope值为：
```java  
PAGE_SCOPE 
REQUEST_SCOPE
SESSION_SCOPE
APPLICATION_SCOPE
```
为了选择作用域：
```java  
pageContext.setAttribute( "name" , value );
pageContext.setAttribute( "name" , value , int scope );   
pageContext.findAttribute( "name" );
```
按照从小到大的顺序依次查找作用域中的命名属性。
```java  
pageCOntext --> request ---> session  --> application
pageCOntext.findAttribute("a");
```
3，获得其他所有的隐含对象。
```java  
pageContext.getRequest() ---> request
pageCOntext.getSession()
pageCOntext.getConfig()
pageCOntext.getOut()
```
注意：隐含对象在表达式标签和普通脚本中都可以使用：
```java  
<%= request.getParameter("name") %> 
<%  sesison.getAttribute() %>
```
但是在声明脚本中不能用，比如：
```java   
<%!
void fn(){
	session.getAtrreibute();
}
%>
```