Spring有两种方法提供对EJB的支持：
Spring能让你在Spring的配置文件里，把EJB作为Bean来声明。这样，把EJB引用置入到其他Bean的属性里就成为可能了，好像EJB就是另一个POJO。
Spring能让你写EJB，让EJB成为Spring配置的Bean的代理的工作。
Spring提供了两个代理工厂Bean，来代理EJB的访问：
LocalStatelessSessionProxyFactoryBean——用来访问本地EJB（EJB和它的客户端在同一个容器中）。
SimpleRemoteStatelessSessionProxyFactoryBean——用来访问远程EJB（EJB和它的客户端在独立的容器中）。