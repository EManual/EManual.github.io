<jsp:include page="/a.jsp" />    
动态包含：包含的是对方的输出结果，分别解释为不同的servlet。
动态包含实例：
(1)header.jsp：
```java  
	<%String text = request.getParameter( "text" );%>
	<center>
		<h1>        
		<font color="blue">
		 <%if( text != null ){ %>                   
			<h1><%=text%></h1>
		 <%}else{ %>
			<h1>Welcome to kettas</h1>
		 <%} %>
		</font>
		</h1>   
	</center>  
```
(2) body.jsp : 
```java  
	<%@page contentType="text/html" %>
		<html> 
		<body> 
<!-- 相当于<jsp:include page="/header.jsp?name=This is param"/> -->                    
	<jsp:include page="/header.jsp">
		<jsp:param name="text" value="This is param"/>
			</jsp:include>  
			<h1>This is body</h1> 
			<% 
				for(int i = 0 ; i< 3 ; i++ ){
			%>
			<h2><%= new java.util.Date() %></h2> 
			<%
				}
			%>					
			<%
				for( int i =0 ; i < 3 ; i++ ){
					out.println( "<h2>" + new java.util.Date() + "</h2>" ) ;
				}
		    %>
			</body>
		</html> 
    <jsp:forward page="/b.jsp" />
    	页面转向 : 相当于servlet中的"接力棒"转向, 是在同一个连接中的页面转向.
    <% response.sendRedirect("/a.jsp"); %>
```
页面转向：连接已经换了一个。