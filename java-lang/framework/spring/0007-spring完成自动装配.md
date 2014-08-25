让spring完成自动装配 Autowiring 解决<ref>标签为javaBean注入时难以维护而实现的
下面是几种autowire type的说明：
1，byname：试图在容器中寻找和需要自动装配的属性名相同的bean或id，如果没有找到相应的bean，则这个属性未被装配上。配置文件中的id/name中查找
2，byType：试图在容器中寻找一个与需要自动装配的属性类型相同的bean或id，如果没有找到，则该属性未被装配上。相当set方法注入。
3，constructor：试图在容器中寻找与需要自动装配的bean的构造函数参数一致的一个或多个bean，如果没找到则抛出异常。构造方法注入。
4，autodetect：首先尝试使用constructor来自动装配，然后再使用byType方式。
Dependeney_cheching 依赖检查 一般和自动装配配套使用四种类型：name，simple，object ，all
缺点：spring不一定能很准确的找到javaBean的依赖对象，大型应用一般不用，且配置文件可读性差。