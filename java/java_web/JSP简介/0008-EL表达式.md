EL表达式( ${ } )
(1) 完成一些简单运算. 
数学运算：
```java  
+ - *　% /	  ${ a + b }
```
布尔运算：
```java  
>     gt  ( great than )
<     lt  ( less than )
>=    ge  ( great equal )
<=    le  ( less equal )
!=    ne  ( not equal )
==    eq  ( equal )
${ a > b }   ${ a gt b }
```
逻辑运算：
```java  
&& || !
and or not  
```
非空运算：
```java  
a == null
${ not empty a }
	|-> a 不存在返回true
	|-> a 存在 返回false  
```
(2) 通过EL表达式,快捷的访问作用域中的命名属性
<%= session.getAttribute( "name" )%>
用EL表达式 : ${ name }
(3) 快速访问javabean的属性.
<jsp:getProperty name="user" property="name"/>
用EL表达式 : ${ user.name }
(4) 常用隐含对象。 
${ param }  
${ param.age }
${ param.name }
相当于：<%= request.getParameter( "name" ) %> 
用来访问客户端提交的参数.
${ cookie.age } 
实际要执行的代码：
```java  
Cookie[] c = request.getCookies();
for( Cookie a : c ){
  if(a.getName() == "age"){
	  a.getValue();
	  ...
  }
}
```