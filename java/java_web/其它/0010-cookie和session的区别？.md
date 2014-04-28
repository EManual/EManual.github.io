注意cookie有时候禁不掉
```java  
Cookie			session
存储在客户端	存储在服务器端
两种类型		两种实现方式
有声明周期		依赖于cookie
无声明周期		url重写
父路径不能访问子路径的cookie	同一个session的窗口共享一个session
典型应用：		典型应用：
3个月不用再登陆	用户登陆
购物车（http://www.china-pub.com/）	购物车也可以用session实现。?
不可靠			可靠
```