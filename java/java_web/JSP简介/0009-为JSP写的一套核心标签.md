为JSP写的一套核心标签, 有了这套标签, 根本不需要自定义标签了
(1) 准备
需要standard.jar，jstl.jar两个jar包，放入Tomcat 6.0/lib目录中(或者是/WEB-INF/lib)。
(2)core
<%@tagliburi="http://java.sun.com/jsp/jstl/core" prefix="c"%>
forEach循环：
①一般用法，相当普通的for循环：
```java  
<c:forEach begin =”1” end=”10” varstatas="st">
	${ st.count }
</c:forEach>
```
② 迭代循环，集合： 
```java  
<c:forEach var="u" items="${ users }">
	${ u.name}
</c:forEach>
```
若是map集合${ user.key}得到值的集合
set  
```java  
(1)	<c:set var="a" value="1234"/>   
(2)	<c:set var="a">
		xxxxx
	</c:set>  
```
把标签体内所有的输出都当作var的值，不直接显示在网页上
使用需要调用${a}
```java  
remove     
<c:remove var="a"/>
	${a}
url
<c:url var="date" value="/jspapp/date.jsp">
	<c:param name="age" value="23"/>
	<c:param name="name" value="lisi"/>
	<c:param name="passwd" value="ffff"/>
</c:url> 
<a href="${date}">test</a>
	 /jspapp/xxx.jsp?age=23   
<a href="/jspapp/xxx.jsp?age=23&name=lsis&passwd=123">
   test
</a>
同if swith
   <c:if test=”s{4>2}”>xxxxx</c:if>
   <c:choose> 
		<c:when test="a">
			cccccccc
		</c:when>
	<c:when test="b"></c:when>
		....
   </c:choose>
   <c:choose> 
		<c:when test="">
			cddddddd
		</c:when>
		<c:when test="">
		 sssss
		</c:when>
		<c"when test="">
		 xxxxxx
		</c:when>
	<c:otherwise>
	
	</c:otherwise>
   </c:choose> 
```