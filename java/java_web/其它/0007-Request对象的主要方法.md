Request对象的主要方法：
```java  
setAttribute(String name,Object)：设置名字为name的request的参数值 
getAttribute(String name)：返回由name指定的属性值 
getAttributeNames()：返回request对象所有属性的名字集合，结果是一个枚举的实例 
getCookies()：返回客户端的所有Cookie对象，结果是一个Cookie数组 
getCharacterEncoding()：返回请求中的字符编码方式 
getContentLength()：返回请求的Body的长度 
getHeader(String name)：获得HTTP协议定义的文件头信息 
getHeaders(String name)：返回指定名字的request Header的所有值，结果是一个枚举的实例 
getHeaderNames()：返回所以request Header的名字，结果是一个枚举的实例 
getInputStream()：返回请求的输入流，用于获得请求中的数据 
getMethod()：获得客户端向服务器端传送数据的方法 
getParameter(String name)：获得客户端传送给服务器端的有name指定的参数值 
getParameterNames()：获得客户端传送给服务器端的所有参数的名字，结果是一个枚举的实例 
getParametervalues(String name)：获得有name指定的参数的所有值 
getProtocol()：获取客户端向服务器端传送数据所依据的协议名称 
getQueryString()：获得查询字符串 
getRequestURI()：获取发出请求字符串的客户端地址 
getRemoteAddr()：获取客户端的IP地址 
getRemoteHost()：获取客户端的名字 
getSession([Boolean create])：返回和请求相关Session 
getServerName()：获取服务器的名字 
getServletPath()：获取客户端所请求的脚本文件的路径 
getServerPort()：获取服务器的端口号 
removeAttribute(String name)：删除请求中的一个属性
```