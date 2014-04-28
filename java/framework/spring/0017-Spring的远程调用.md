Spring远程支持是由普通（Spring）POJO实现的，这使得开发具有远程访问功能的服务变得相当容易
四种远程调用技术：
◆ 远程方法调用（RMI）       
◆ Caucho的Hessian和Burlap  
◆Spring自己的Http invoker    
◆使用SOAP和JAX-RPC的web Services
Spring对上面的远程服务调用都有支持
Spring远程调用支持6种不同的RPC模式：远程方法调用（RMI）、Caucho的Hessian和Burlap、Spring自己的HTTP invoker、EJB和使用JAX-RPC 的Web Services。表6.1概括地论述了每个模式，并简略讨论它们在不同情况下的用处。
  
远程方法调用（RMI）。通过使用RmiProxyFactoryBean和RmiServiceExporter，Spring同时支持传统的RMI（使用java.rmi.Remote接口和java.rmi.RemoteException）和通过RMI调用器实现的透明远程调用（支持任何Java接口）。
Spring的HTTP调用器。Spring提供了一种特殊的允许通过HTTP进行Java串行化的远程调用策略，支持任意Java接口（就像RMI调用器）。相对应的支持类是 HttpInvokerProxyFactoryBean 和 HttpInvokerServiceExporter。
Hessian。通过 HessianProxyFactoryBean 和 HessianServiceExporter，可以使用Caucho提供的基于HTTP的轻量级二进制协议来透明地暴露服务。
Burlap。Burlap是Caucho的另外一个子项目，可以作为Hessian基于XML的替代方案。Spring提供了诸如BurlapProxyFactoryBean和BurlapServiceExporter 的支持类。
JAX RPC。Spring通过JAX-RPC为远程Web服务提供支持。
客户端发起对代理的调用，好像是代理提供了这些服务的功能一样。代理代表客户端和远程服务交流。它处理连接的具体情况，并向远程服务发起远程调用。在Spring里，远程服务是被代理的，所以他们能像一般的Bean那样置入到客户端的代码里。
  