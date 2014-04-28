当点击一个链接时,浏览器首先找到站点的IP地址,这是通过DNS来实现的,在找到IP地址后就可以建立TCP连接了,连接建立后我们就可以发送请求了.但这个请求是什么样子的呢 ? 我们现在假设点击了一个从 www.webmonkey.com/HTML/96/47/Index2A , HTML 点击了WWW.GRIPY.ORG/MATTARG/  这时浏览器会发出下面的请求:
```java  
Get/MATTARG/HTML/1.0
User-Agent: Mozilla/2.0(macitosh;1;PPC)
Accept: text/html: */*
Cookie: name = value
Refetet: http://www.webmonkey.com/html/96/47/index2a.html
Host: www.gtippy.org
```
第一行称为请求,它告诉服务器从MATTMARG 取得文件,这是的目录一般是要加 / 的,下面几行通知服务器你所使用的浏览器是什么类型,你所接收的数据是什么类型,如果你以前访问过这个站点,站点可能向你发送了Cookie ,如果你已经有了一个这样的 Cookie ,浏览器会将这个 Cookie 返回给服务器, referer 行通知服务器用户从哪一页到达此页的.
下面服务器就要返回文件了,每次服务器返回文件时,都要返回一个 Http/1.0 响应,同进带有状态码,在此之后是述内部的头信息,下面就是一个响应:
```java  
HTTP/1.0 200 Pound
Data: Mon 10 Feb 1997 23:48:22 GMT
Server: Apache/1.1 1 Hot&ired/1.0
Content-type: text/html
Last-Moditied: Tues,11 Feb 1997 22:45:55 GMT
```
不同的数据可能返回不同的Content-type ，因此不同的内容需要不同的 Content-type ，因此有时候这个过程是很慢的。