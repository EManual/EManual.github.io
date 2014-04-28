(1) 关于javabean要求： 
1，具有无参的构造函数。
2，针对每一个成员变量，因改提供相应get/set。 
3，implments Serializable（实现才能对象序列化）。
(2) <jsp:useBean /> 
使用一个保存在某个作用域(pagecontext, request, session, application)中的javabean。
<jsp:useBean id="user" class="beijing.User" scope="session"/> 
实际上执行的代码为：User u = session.getAttribute("user"); 
id的含义：
1，为要使用的javabean取个名字。   
2，javabean在session作用域中的命名属性。
class：java bean 的类型。
scope：指定一个作用域(page,request,session,application)，若不指定，则由小到大。
(3) <jsp:setProperty /> 五种设置属性的方法：
<jsp:setProperty name="" property="" value=""/>
	name：被操作的javabean 的名字，即useBean中的id。
	property：属性名称id,name,phone
	value：值  
<jsp:setProperty name="" property="" param=""/>
	param:表示该属性的值来自于客户端提交的参数。param用来指定这个参数的名字。    
<jsp:setProperty name="" property=""/>
	客户端提交的参数名称和成员变量的名称正好一致。省略param。
<jsp:setProperty name="" property="*"/>
	用一个标签为所有的属性赋值，属性的值来自于客户端提交的参数， 
	参数名字和属性名字 一一对应。
(4) <jsp:getProperty />
使用javabean中的属性，可用于页面显示。
<jsp:getProperty name="" property=""/>  
name：被操作的javabean 的名字，即useBean中的id。
property：属性名称id,name,phone。
使用片段如下：
```java   	
<html> 
	<body>            
		<h2><jsp:getProperty name="user" property="name" /></h2>
		<h2><jsp:getProperty name="user" property="id"/></h2>
		<h2><jsp:getProperty name="user" property="phone"/></h2> 
		<h2><jsp:getProperty name="user" property="password"/></h2>
	</body>
</html>
```