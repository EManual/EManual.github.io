定义抽象类Abstract=“true”抽象bean不能实例化，一个类可以创建多个bean。
抽象bean的配置和一般bean的配置基本一样只是在增加了Abstract=“true”抽象bean是一个bean的模板，容器会忽略抽象bean的定义，不会实例化抽象bean，故不能通过getBean（）显示的获得抽象bean的实例也不能将抽象bean注入其他bean的依赖属性。
抽象bean的配置和继承：
通过Abstract属性配置抽象bean：
```java  
<bean id=”fatherTemple” class=”abstractClass” abstract=”true”>
	<!—注入属性?
	<property name=”name” ref=”xxx”/>
</bean>
<!—通过parent属性定义子bean?
<bean id=”childTemple” parent=”fatherTemple”>
	<property name=”name2” ref=”yyyy”/>  -定义自己的属性
</bean>
```
说明：
子bean配置可以增加新的配置信息，并可以定义新的配置覆盖父类的定义。
子类和父类中至少有一个class属性否则不知道实现类，父类的class可以不写。