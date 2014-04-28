(1) 构思，比如写一个对指定名字说hello的标签，应该是<前缀:hello user="zhangsan"/>
(2) 写类
要实现的基础接口：javax.serlvet.jsp.tagext.SimpleTag 
其中含有五个方法：
```java   
	doTag         ---> 实现标签的功能 .
	setJspContext ---> pageContext .
	setParent     ---> 父标签的实现类                          
	setJspBody    ---> JspFragement 
	getParent  
```	
要实现五个方法，显得很繁琐，javax.servlet.jsp.tagext.SimpleTagSupport类实现了这个
基础接口，我们在写类时只需要继承这个类，然后覆盖doTag方法即可。
类如下：
```java  
package com.kettas.tag;
import javax.servlet.http.*;
import javax.servlet.jsp.tagext.*; 
import javax.servlet.jsp.*;
import java.io.*;
public class HelloHandler extends SimpleTagSupport{
	private String user;
	public void setUser( String user ){
		this.user = user;
	}                   
	public String getUser(){
		return user;
	}              
	@Override
	public void doTag() throws JspException , IOException{
		PageContext ctx = (PageContext)this.getJspContext();
		ctx.getOut().println( "hello " + user );
		ctx.getOut().flush();	
	}
}
```
(3) 写tld配置文件(位置为 : /WEB-INF/***.tld)
```java  
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" 
	"http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd">
<taglib>
	<tlibversion>1.0</tlibversion>
	<jspversion>2.0</jspversion>
	<shortname>mytag</shortname>
	<!-- 指定命名空间 引入标签时使用 -->
	<uri>liucy@cernet.com</uri> 
	<tag>
		<!-- 标签名 -->
		<name>hello</name>
		<!-- 标签对应的类 -->
		<tag-class>com.kettas.tag.HelloHandler</tag-class>    
		<!-- 标签体之中是否含有内容 -->
		<body-content>empty</body-content>
		<!-- 标签属性 -->
		<attribute> 
			<name>user</name>
			<type>java.lang.String</type>
			<required>true</required>
			<rtexprvalue>true</rtexprvalue>
		</attribute>
	</tag> 
</taglib>
```
(4) 在jsp文件中使用：
```java  
<%@page contentType="text/html"%>
<%-- 注意引入自定义标签的方式, prefix属性指定标签前缀, 前缀解决不同标签库标签重名 --%>
<%@taglib uri="liucy@cernet.com" prefix="liucy"%>
<html>                                        
	<body> 
		<h2> 
			<liucy:hello user="<%= request.getParameter( "name" )%>"/>
		</h2>
	</body>
</html>
```
自定义一个循环标签 : 
类 : ===================================
```java  
package com.kettas.tag;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import javax.servlet.jsp.tagext.*;
import java.io.*;
public class LoopHandler extends SimpleTagSupport{
	private int begin;
	private int end;
	public void setBegin( int begin ){
		this.begin = begin;
	}                     
	public int getBegin( ){
		return begin;
	}               
	public void setEnd(int end ){
		this.end = end;
	}                 
	public int getEnd( ){
		return end;
	}
	@Override
	public void doTag()throws JspException ,IOException{
		// JspFragment对象可以获取标签体内部的内容
		JspFragment f = this.getJspBody();
		PageContext ctx = (PageContext)this.getJspContext();
		for( int i = begin ; i < end ; i++){
			f.invoke( ctx.getOut() );
		}
	}
}
```
配置文件如下 :============================
```java  	 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" 
		"http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd">
	<taglib>
		<tlibversion>1.0</tlibversion>
		<jspversion>2.0</jspversion>
		<shortname>mytag</shortname>
		<uri>liucy@cernet.com</uri> 
		<tag>
		<name>hello</name>
		<tag-class>com.kettas.tag.HelloHandler</tag-class>    
		<body-content>empty</body-content>
		<attribute> 
		<name>user</name>
		<type>java.lang.String</type>
		<required>true</required>
		<rtexprvalue>true</rtexprvalue>
		</attribute>
		</tag> 
		<tag> 
		<name>loop</name>
		<tag-class>com.kettas.tag.LoopHandler</tag-class>
		<!-- 标签体内含有内容, 并且是非脚本的内容 -->
			<body-content>scriptless</body-content>
		<attribute>
		<name>begin</name>
		<type>int</type>
	<required>true</required>						<rtexprvalue>true</rtexprvalue>
		</attribute> 
		<attribute>
		<name>end</name>
	<type>int</type>
	<required>true</required>
	<rtexprvalue>true</rtexprvalue>
	</attribute> 
	</tag>
</taglib>
```
使用如下 :=====================================
```java  
<%@taglib uri="liucy@cernet.com" prefix="liucy"%>
<liucy:loop begin="0" end="3">
	<h2>Hello!</h2>
</liucy:loop>
```
如此便可连续在网页上输出三个"Hello !"