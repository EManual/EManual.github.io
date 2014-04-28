1） Servlet在容器中运行，其实例的创建及销毁等都不是由程序员决定的，而是由容器进行控制的。
创建Servlet实例有两个时机：
1，客户端第一次请求某个Servlet时，系统创建该Servlet的实例：大部分的Servlet都是这种Servlet。
2，Web应用启动时立即创建Servlet实例，即load-on-startup  <load-on-startup>1</load-on-startup>
Servlet的生命周期通过javax.servlet.Servlet接口中的init()、service()和destroy()方法来表示。
每个Servlet的运行都遵循如下生命周期。
（1）加载和实例化：找到servlet类的位置通过类加载器加载Servlet类，成功加载后，容器通过Java的反射API来创建Servlet实例，调用的是Servlet的默认构造方法（即不带参数的构造方法），
（2）初始化： 容器将调用Servlet的init()方法初始化这个对象。初始化的目的是为了让Servlet对象在处理客户端请求前完成一些初始化的工作，如建立数据库的连接，获取配置信息等。对于每一个Servlet实例，init()方法只被调用一次
（3）请求处理：Servlet容器调用Servlet的service()方法对请求进行处理。要注意的是，在service()方法调用之前，init()方法必须成功执行
（4）服务终止：容器就会调用实例的destroy()方法，以便让该实例可以释放它所使用的资源
2）从始至终只有一个对象，多线程通过线程池访问同一个servlet
Servlet采用多线程来处理多个请求同时访问，Servelet容器维护了一个线程池来服务请求。
线程池实际上是等待执行代码的一组线程叫做工作者线程(WorkerThread)，Servlet容器使用一个调度线程来管理工作者线程(DispatcherThread)。
当容器收到一个访问Servlet的请求，调度者线程从线程池中选出一个工作者线程，将请求传递给该线程，然后由该线程来执行Servlet的service方法。
当这个线程正在执行的时候，容器收到另外一个请求，调度者线程将从池中选出另外一个工作者线程来服务新的请求，容器并不关系这个请求是否访问的是同一个Servlet还是另外一个Servlet。
当容器同时收到对同一Servlet的多个请求，那这个Servlet的service方法将在多线程中并发的执行。
3）如何现实servlet 的单线程模式
```java  
<%@ page isThreadSafe=”false”%>
```