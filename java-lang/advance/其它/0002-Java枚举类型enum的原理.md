1. 关于Java Enum:
学过C/C++等语言的人，应该都对Enum类型略知一二。Enum一般用来表示一组相同类型的常量。如性别、日期、月份、颜色等。对这些属性用常量的好处是显而易见的，不仅可以保证单例，且比较时候可以用 ”==” 来替换 equals是一种好的习惯。 JDK1.5之前没有Enum这个类型，那时候一般用接口常量来替代。有了 JavaEnum 之后，可以更贴近的表示这种常量。
2. 如何使用Java Enum
简单的用法：JavaEnum简单的用法一般用于代表一组常用常量，可用来代表一类相同类型的常量值。如：
性别：
[code=java]
public enum SexEnum {
  male , female ;
}
[/code]
颜色：
[code=java]
public enum Color {
  RED , BLUE,GREEN,BLACK ;
}
[/code]
枚举对象里面的值都必须是唯一的。
可以通过 Enum 类型名直接引用该常量，如 SexEnum.male,Color.RED.
复杂用法：Java 为枚举类型提供了一些内置的方法，同事枚举常量还可以有自己的方法。可以很方便的遍历枚举对象，看个下面的例子：
1. 代码一 WeekDay.java：
[code=java]
 /** 
 * @author yubing.linyb 
 * 2009.7.29 
 * 定义一个枚举类型，代表星期一到星期日的7个缩写常量 
 * 同时还定义了枚举类型的属性day，该属性可以是final,也可是变量 
 * 同时还定义了该枚举类型的一个方法printDay 
 */  
public enum WeekDay {  
Mon("Monday"), Tue("Tuesday"), Wed("Wednesday"), Thu("Thursday"), Fri(  
        "Friday"), Sat("Saturday"), Sun("Sunday");  
  
/**定义枚举类型自己的属性**/  
private final String day;  
   
private WeekDay(String day) {  
     this.day = day;  
}  
  
/**定义枚举类型自己的方法**/  
public static void printDay(int i){  
     switch(i){  
     case 1: System.out.println(WeekDay.Mon); break;  
     case 2: System.out.println(WeekDay.Tue);break;  
     case 3: System.out.println(WeekDay.Wed);break;  
     case 4: System.out.println(WeekDay.Thu);break;  
     case 5: System.out.println(WeekDay.Fri);break;  
     case 6: System.out.println(WeekDay.Sat);break;  
     case 7: System.out.println(WeekDay.Sun);break;  
     default:System.out.println("wrong number!");  
     }  
}  
   
public String getDay() {  
     return day;  
}  
}  
[/code]
2. 代码二 WeekDayTest.java：
[code=java]
/** 
 * @author yubing.linyb 
 * 2009.7.29 
 * 测试枚举类型WeekDay. 
 */  
public class WeekDayTest {  
  public static void main(String args[]) {  
      for (WeekDay day : WeekDay.values()) {  
         System.out.println(day + "====>" + day.getDay());  
      }  
      WeekDay.printDay(5);  
  }  
}  
输出结果为：
Mon====>Monday
Tue====>Tuesday
Wed====>Wednesday
Thu====>Thursday
Fri====>Friday
Sat====>Saturday
Sun====>Sunday
Fri
[/code]
3. Java Enum原理
Java Enum 类型的语法结构尽管和 java 类的语法不一样，应该说差别比较大。但是经过编译器编译之后产生的是一个 class 文件。该 class 文件经过反编译可以看到实际上是生成了一个类，该类继承了 java.lang.Enum<E>.WeekDay (javap WeekDay 命令 之后得到的内容如下 ( 去掉了汇编代码 )：
[code=java]
public final class WeekDay extends java.lang.Enum{  
    public static final WeekDay Mon;  
    public static final WeekDay Tue;  
    public static final WeekDay Wed;  
    public static final WeekDay Thu;  
    public static final WeekDay Fri;  
    public static final WeekDay Sat;  
    public static final WeekDay Sun;  
    static {};  
    public static void printDay(int);  
    public java.lang.String getDay();  
    public static WeekDay[] values();  
    public static WeekDay valueOf(java.lang.String);  
}  
[/code]
所以实际上Enum类型就是以Java类来实现的，没有什么新的特点，只不过java编译器帮我们做了语法的解析和编译。完全也可以自己实现。但是既然有这样方便一个东西，当然会去用了。