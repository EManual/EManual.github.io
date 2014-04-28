1) 建立连接。
2) 执行SQL。
3) 处理结果。
4) 释放资源。    
Connection pool：连接池
DataSource：  
LDAP ( Light directory access protocal )轻量级目录访问协议。
JNDI ( java naming director interface ) Java 命名目录接口。
使用连接池：
1)配置连接池：
改配置文件 conf/context.xml   
```java  
<Resource driverClassName="oracle.jdbc.driver.OracleDriver"  
注：jar包应该放在外边的lib包中，因为它是给tomcat用的。
	url="jdbc:oracle:thin:@127.0.0.1:1521:XE"
	username="kettas"
	password="kettas"
	maxActive="2"  最大连接数
	type="javax.sql.DataSource" 连接类型
	auth="Container"  一般不改
	name="oracle/ds"  
	/>
```
2)使用DataSource：
```java      
用法：%@page import="javax.naming.*"%> 
<%
	Context ctx = new InitialContext();
	DataSource ds = (DataSource)ctx.lookup("java:comp/env/oracle/ds");tomcat特点：必须加java:comp/env/*
	Connection conn = ds.getConnection();
	out.println( "<h1>get connection!</h1>" );
	conn.close();
%>
```