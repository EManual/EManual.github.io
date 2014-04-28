关于HttpSession, 在服务器端保存用户状态的一种机制
(1) 获取HttpSession对象的方法：
```java  
// 参数为true，表示若存在对应的HttpSession对象，则返回。若不存在，则创建一个新的。
// 若参数为false，表示若存在对应的HttpSession对象，则返回。若不存在，则返回null。
HttpSession session = request.getSession(true);
```
(2) 对HttpSession对象, 进行存取数据的操作
```java  
// 两个参数，分别为命名属性和对应的数据
session.setAttribute("name", data);
// 一个参数，命名属性，注意返回的为Object对象，要强转
session.getAttribute("name");
```
(3) 比较Session和request：
request：
创建：当用户请求到达服务器的时候。
销毁：当本次请求的应答回到客户端的时候。
	  客户端的一次请求应答之间。
session：
创建：当用户第一次调用request.getSession( true ) 
销毁：超时 ( 两级超时限制 )
		1) 内存 ---> 文件。
		2) 从文件系统销毁。
session的原理： 
给每个浏览器一个cookie，这个cookie的name属性为"jsessionid"，value属性为这个session对应的ID值。
(4) 当浏览器拒绝cookie时可以用URL把session的id提交给服务器
如：
http://localhost:8989/servletapp/forwardB;jsessionid=37D50D093CCD4A37CC1118785E38F438
"url;jessionid="+ session.getId()
response.encodeURL("url")：对url进行编码