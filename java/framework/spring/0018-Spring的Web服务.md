Spring支持：使用JAX-RPC暴露服务，访问Web服务
除了上面所说的支持方法，你还可以用XFire xfire.codehaus.org 来暴露你的服务。XFire是一个轻量级的SOAP库，目前在Codehaus开发。
使用JAXI-RPC暴露服务 
Spring对JAX-RPC Servlet的端点实现有个方便的基类-ServletEndpointSupport。为暴露我们的Account服务，我们继承了Spring的ServletEndpointSupport类来实现业务逻辑，这里通常把调用委托给业务层。
访问服务：
Spring有两个工厂bean用来创建Web服务代理，LocalJaxRpcServiceFactoryBean 和 JaxRpcPortProxyFactoryBean。前者只返回一个JAX-RPT服务类供我们使用。后者是一个全功能的版本，可以返回一个实现我们业务服务接口的代理。本例中，我们使用后者来为前面段落中暴露的AccountService端点创建一个代理。你将看到Spring对Web服务提供了极好的支持，只需要很少的代码 - 大多数都是通过类似下面的Spring配置文件： 
```java  
<bean id="accountWebService" class="org.springframework.remoting.jaxrpc.JaxRpcPortProxyFactoryBean">
	<property name="serviceInterface" value="example.RemoteAccountService"/>
	<property name="wsdlDocumentUrl" value="http://localhost:8080/account/services/accountService?WSDL"/>
	<property name="namespaceUri" value="http://localhost:8080/account/services/accountService"/>
	<property name="serviceName" value="AccountService"/>
	<property name="portName" value="AccountPort"/>
</bean>
```
XFire是一个Codehaus提供的轻量级SOAP库。在写作这个文档时（2005年3月）XFire还处于开发阶段。虽然Spring提供了稳定的支持，但是在未来应该会加入更多特性。暴露XFire是通过XFire自身带的context，这个context将和RemoteExporter风格的bean相结合，后者需要被加入到在你的WebApplicationContext中。