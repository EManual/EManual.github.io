解决乱码问题
```java   
1）response.setContentType(“text/html;charset=gbk2312”)
2)requset.setCharacterEnconding(“gbk”)  ------是post的时候
3)在server.xml中加URLEncoding=“gbk”------是get发送数据的时候
```