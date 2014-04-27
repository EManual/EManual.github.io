Java提供了public, private, protected 三个访问权限修饰词，提供了以下四种访问权限控制机制：
1、包访问权限；
2、Public访问权限；
3、Private访问权限；
4、Protected访问权限；
1、包访问权限
包访问权限是Java为了便于程序员开发而给定的一种权限选择。
当方法或域未给定访问权限限制符时，其默认具有该权限。具有该权限的方法和域成员，在包内是完全可见的（注意要与其对象依附在一起
），而包外则不可见。
这有点类似于C++中友元类，友元类见彼此可见，以简化访问。
```java  
Package accesscontrol
//Animal.java
public class Animal
{
　　void bark()
}

Package accesscontrol
//Test.java
public class Test
{
　　main()
　　{
　　Animal a= new Animal();
     a.bark();//此处直接访问了Animal类中的bark（）方法
　　}
}
```
由于Animal类和Test类都被打包在了同一个Package下，Animal中的bark（）方法为包访问权限，故对类Test可见。
对java文件中的类也是如此，若未指定限制符，其默认为包访问权限，只能在包内被使用。包外是无法利用其生成对象的（不可见）。
注意：当决定一个类对包外可见的时候，除了要将类得访问限定符改为public意外，自定义的构造器限定符也必须修改为public，不然将导
致外部不可见。
2、public 权限
当在方法或域前面显式的给定public限定符的时候，其具有该权限控制。
public权限是最为宽松的一种权限控制，对包的内、外部都是完全可见的。
java最多只允许一个java文件中出现一个public类（该类向外提供接口，并与该java文件的名称完全一致）。
当一个java文件中无一个Public类时，表明其仅供包内使用，对外界不可见！
注意：类只有包访问权限和public访问权限两类。
3、Private访问权限
Private是访问限定最为严格一种权限。
当方法或域为private权限时，表明其只针对该类的内部可见，类的外部（包括同一包内的其它类）是不可见的。
```java  
//Animal.java
public class Animal
{
　　private void bark()
}

Package accesscontrol
//Test.java
public class Test
{
　　main()
　　{
　　Animal a= new Animal();
     a.bark();//此处将造成编译错误，bark（）方法为private方法，仅对Animal类 内部可见，现在在Test类内部。
　　}
}
```
4、protected访问权限
protected权限是一种严格程度介于public和private之间的权限，具有prtoected权限的域和方法只能对其自身和导出类可见。
在面向对象的设计当中，最常用的为public和private访问权限两种。
一般情况下将域定义为private，将方法定义为public。外界使用该类时，通过public方法使用其接口，而具体的域成员则对外部屏蔽，只
能通过类提供的接口间接访问。
```java  
public class Dog {
　　private int age=0;
    public setAge(int num)
    {
　　	age=num+1;
    }
}
```
此处，age域对外部不可见，要想对其进行操作，必须使用Dog类提供的接口setAge（int num）。
注意到setAge的方法体age=num+1;对用户给出的年龄加1了以后再修改了age属性，这种修改对使用者是不可见的，有时又是非常的必要的！
  