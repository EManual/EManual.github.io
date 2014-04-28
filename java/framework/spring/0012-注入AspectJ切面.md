为什么要用AspectJ：AspectJ提供了Spring AOP很多不能实现的多种切点类型（比如属性，构造方法切入，由于不能实现构造方法的切入spring aop就不能实现对象创建过程的通知）
AspectJ是一个代码生成工具（Code Generator）。AspectJ有自己的语法编译工具，编译的结果是Java Class文件，运行的时候，classpath需要包含AspectJ的一个jar文件。AspectJ是AOP最早成熟的Java实现，它稍微扩展了一下Java语言，增加了一些Keyword等。
```java  
public aspect TestAspectJ {  
    public TestAspectJ();
　　public pointcut writeOperations(): 
　　　　execution(public boolean Worker.createData()) ||
　　　　execution(public boolean Worker.updateData()) ||
　　　　execution(public boolean AnotherWorker.updateData()) ;
　　before() : writeOperations() { 
　　　　XXXXXX;　advice body
　　}
　　after() : writeOperations() {
　　 　XXXX;// advice body
　　}
}
```
配置文件
```java  
<bean class=”xxx/TeatAspectJ” factory-method=”aspectof”>
  <property name=”” ref=””/></bean>
```
说明机制：这个<bean>和其他的bean并没有太多区别，只是多了 factory-nmthod属性 要想获得切面的实例，就必须使用factory-method来调用 aspectof（）方法，而不是调用TestAspectJ的构造方法，简单来说Spring不使用《bean》声明来创建TestAspectJ实例，它已经被AspectJ运行时创建了，Spring通过aspectof（）工厂方法获得切面的引用，然后利用<bean>元素对她执行属性注入。
上述代码关键点是pointcut，意味切入点或触发点，那么在那些条件下该点会触发呢？是后面红字标识的一些情况，在执行
Worker的createData()方法，Worker的update方法等时触发Pointcut类似触发器，是事件Event发生源，一旦pointcut被触发，将会产生相应的动作Action，这部分Action称为Advice。
Advice在AspectJ有三种：before、 after、Around之分，上述aspect Lock代码中使用了Advice的两种before和after。
所以AOP有两个基本的术语：Pointcut和Advice。你可以用事件机制的Event和Action来类比理解它们
其中advice部分又有：
Interceptor - 解释器并没有在AspectJ出现，在使用JDK动态代理API实现的AOP框架中使用，解释有方法调用或对象构造或者字段访问等事件，是调用者和被调用者之间的纽带，综合了Decorator/代理模式甚至职责链等模式。
Introduction - 修改一个类，以增加字段、方法或构造或者执行新的接口，包括Mixin实现。