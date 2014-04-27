* 接口的定义：接口从本质上说是一种特殊的抽象类。
关键字interface。
在接口中，所有的方法为公开、抽象的方法：public abstract。
在接口中，所有的属性都是公开、静态的常量：public static final。
接口与接口之间可以多继承，用extends，多个之间用逗号隔开。
接口中没有构造方法，不能用“new 接口名”来实例化一个接口，但可以声明一个接口。
例如，定义一个用于计算的接口，在该接口中定义了一个常量PI和两个方法，具体代码如下：
```java  
public interface CalInterface 
{
    final float PI=3.14159f;//定义用于表示圆周率的常量PI
    float getArea(float r);//定义一个用于计算面积的方法getArea()
    float getCircumference(float r);//定义一个用于计算周长的方法getCircumference()
}
```
* 接口的实现：
关键字implements
一个类实现一个接口必须实现接口中所有的方法，否则其为抽象类，并且在实现类中的方法要加上public(不能省略)。
类中的默认修饰符：default。
接口中的默认修饰符：public。
一个类除了继承另一个类外（只能继承一个类），还可以实现多个接口(接口之间用逗号分隔)。
```java  
public class Cire implements CalInterface 
{
    public float getArea(float r) 
    {
        float area=PI*r*r;//计算圆面积并赋值给变量area
        return area;//返回计算后的圆面积
    }
    public float getCircumference(float r) 
    {
        float circumference=2*PI*r;      //计算圆周长并赋值给变量circumference
        return circumference;           //返回计算后的圆周长
    }
    public static void main(String[] args) 
    {
        Cire c = new Cire();
        float f = c.getArea(2.0f);
        System.out.println(Float.toString(f));
    }
}
```
* 接口的作用：
间接实现多继承：用接口来实现多继承并不会增加类关系的复杂度。因为接口不是类，与类不在一个层次上，是在类的基础上进行再次抽象。
接口可以抽象出次要类型，分出主、次关系类型，符合看世界的一般方法。
接口隔离，与封装性有关。一个对象都有多个方面，可以只展示其中几个方面，其他的都隐藏。因此可以看为“更高层次的封装”，把一个大接口做成若干个小接口。
通过接口制定标准（最重要的作用）。
接口：制定标准。
接口的调用者：使用标准。
接口的实现类：实现标准。
解耦合作用：把使用标准和实现标准分开，使得标准的制定者和实现者解除偶合关系，具有极强的可移植性。
例：sun公司提供一套访问数据库的接口（标准），java程序员访问数据库时针对数据库接口编程。接口由各个数据库厂商负责实现。
* 接口编程的原则
尽量针对接口编程（能用接口就尽量用接口）。
接口隔离原则（用若干个小接口取代一个大接口）。
* 注意：
接口中没有构造器，也没有main方法。
在类的继承中，只能做单重继承，而实现接口时，一次则可以实现多个接口，每个接口间使用逗号“,”分隔。这时就可能出现常量或方法名冲突的情况，解决该问题时，如果常量冲突，则需要明确指定常量的接口，这可以通过“接口名.常量”实现。如果出现方法冲突时，则只要实现一个方法就可以了。