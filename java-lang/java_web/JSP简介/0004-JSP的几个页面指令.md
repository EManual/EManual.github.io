页面指令：向服务器说明页面自身的特征,以便服务器。
1，<%@page contentType="text/xml;charset=utf-8" %> 客户端--->>服务端的编码。
2，<%@page import="" %> 引入名字空间。
3，<%@page pageEncoding="GBK/GB2312/utf-8"%>(网页的静态内容乱码想到pageEncoding， 
jsp文件文本编辑器所采用的编码)--->服务器内部使用的用来指定jsp 源文件所采用的编码方式。   	  
4，<%@page isELIgnored="false" %> EL一种表达式语言，默认值不同的服务器不一样，最好明确写出：	   
${ 1+1 } (false：显示结果。true：显示 ${ 1+1 }源代码)。 
5，<%@page errorPage="/error.jsp"%>
指定错误页面。
jsp ---> 业务代码。
6，<%@page isErrorPage="true|false"%> 当是TRUE时就会有exception的隐含对象。
<%@page isErrorPage="true" errorPage="/other.jsp"%> 不能这样转。
A(源页面) -------------------------> B(错误页面)
errorPage="B"           isErrorPage="true"	      
7，<%@page session="true"%>--默认值, 表示本页面是否需要session对象。
在servlet中只有直接调用才能得到，而jsp中默认是有的：
<%@page language="java"%>默认的语言。
<%@page extends="XXX" %>服务器自己决定。
<%@page buffer=""%> 服务器自己决定调节。