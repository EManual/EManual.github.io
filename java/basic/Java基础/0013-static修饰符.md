把对象相关的变成类相关的，它可以修饰属性、方法、代码块和内部类。
* static修饰属性（类变量）：
那么这个属性就可以用" 类名.属性名 "来访问，也就是使这个属性成为本类的类变量，为本类对象所共享。
类加载的过程，类本身也是保存在文件中（字节码文件保存着类的信息）的，java会通过I/O流把类的文件读入JVM（java虚拟机），这个过程称为类的加载。JVM会通过类路径（CLASSPATH）来找字节码文件。需要的时候才会进行类加载，生成对象时是先加载后构造。
类变量，会在加载时自动初始化，初始化规则和实例变量相同。
* 注意：
类中的实例变量是在创建对象时被初始化的。
static修饰的属性，是在类加载时被创建并进行初始化，类加载的过程只进行一次，也就是类变量只会被创建一次。
* static修饰方法（静态方法）：
会使这个方法成为整个类所公有的方法，可以用" 类名.方法名 "访问。
static修饰的方法，不能直接访问本类中的非静态成员，但本类的非静态方法可以访问本类的静态成员。
在静态方法中不能出现this关键字。
父类中是静态方法，子类中不能覆盖为非静态方法，在符合覆盖规则的前提下，在父子类中，父类中的静态方法可以被子类中的静态方法覆盖，但是没有多态。（在使用对象调用静态方法时其实是调用编译时类型的静态方法）
java中的main方法必须写成static的原因：在类加载时无法创建对象，而静态方法可以不通过对象调用，所以在类加载时就可以通过main方法入口来运行程序。
* static修饰初始代码块：
这时这个初始代码块就叫做静态初始代码块，这个代码块只在类加载时被执行一次。
可以用静态初始代码块初始化一个类。
动态初始代码块，写在类体中的“{}”，这个代码块是在生成对象时运行，这种代码块叫动态初始代码块。
下面的例子显示的类有一个static方法，一些static变量，以及一个static 初始化块：
```java  
// Demonstrate static variables，methods，and blocks.
class UseStatic {
	static int a = 3;
	static int b;
	static void meth(int x) {
		System.out.println("x = " + x);
		System.out.println("a = " + a);
		System.out.println("b = " + b);
	}
	static {
		System.out.println("Static block initialized.");
		b = a * 4;
	}
	public static void main(String args[]) {
		meth(42);
	}
}
```
一旦UseStatic 类被装载，所有的static语句被运行。首先，a被设置为3，接着static 块执行(打印一条消息)，最后，b被初始化为a*4 或12。然后调用main()，main() 调用meth() ，把值42传递给x。3个println ( ) 语句引用两个static变量a和b，以及局部变量x 。
注意：在一个static 方法中引用任何实例变量都是非法的。
下面是该程序的输出：
```java  
Static block initialized.
x = 42
a = 3
b = 12
```
在定义它们的类的外面，static方法和变量能独立于任何对象而被使用。这样，你只要在类的名字后面加点号运算符即可。例如，如果你希望从类外面调用一个static方法，你可以使用下面通用的格式：
```java  
classname.method( )
```
这里，classname是类的名字，在该类中定义static方法。可以看到，这种格式与通过对象引用变量调用非static方法的格式类似。一个static变量可以以同样的格式来访问——类名加点号运算符。这就是Java 如何实现全局功能和全局变量的一个控制版本。
下面是一个例子。在main() 中，static方法callme() 和static 变量b在它们的类之外被访问。
```java  
class StaticDemo {
	static int a = 42;
	static int b = 99;
	static void callme() {
		System.out.println("a = " + a);
	}
}

class StaticByName {
	public static void main(String args[]) {
		StaticDemo.callme();
		System.out.println("b = " + StaticDemo.b);
	}
}
```
下面是该程序的输出：
```java  
a = 42
b = 99
```
解释的很透彻，还想补充点，就是static成员是不能被其所在class创建的实例访问的。
```java  
Example: Class MyClass { public static str = "this is for test purpose"; } 
MyClass instanceClass = new MyClass(); Console.WriteLine(MyClass.str); // Runs well 
Console.WriteLine(instanceClass.str); // Error,lack of accessor
```
通俗点的解释如下：
1、如果不加static修饰的成员是对象成员，也就是归每个对象所有的。
2、加static修饰的成员是类成员，就是可以由一个类直接调用，为所有对象共有的。