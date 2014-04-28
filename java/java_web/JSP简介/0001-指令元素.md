用来说明一个jsp文件自身的一些特点。以便服务器(tomcat)作出正确的处理。
页面指令：
```java  
<%@page contentType="text/html;charset=utf-8" %> 
<%@page import="java.util.*" %> 
```
标签库指令：
```java  
<%@taglib %>  
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
```
包含指令：静态包含。
用来包含其他jsp的源代码 (静态包含)。
所谓静态包含, 就是先将引入的jsp页包含入本页面中， 然后解释为同一个servlet。
<%@include file="xxx"%> 静态包含包含的是源代码，考虑变量冲突，并且xxx后面不能传参数。