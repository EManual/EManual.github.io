(1) 第一个程序HelloWorld：
```java  
package mypack;		//相当于一个目录
public class HelloWorld{
    public static void main(String[] args){
	   System.out.println("Hello World"); 
	}
}
```
注：
1、文件名必须和public修饰的类名一致，以.java作为文件后缀，如果定义的类不是public的，则文件名与类名可以不同。
2、一个.java文件中可以有多个class，但是只有一个public修饰的类。
3、java源代码文件编译后，一个类对应生成一个.class文件。
4、一个java应用程序应该包含一个main()方法，而且其签名是固定的，它是应用程序的入口方法，可以定义在任意一个类中，不一定是public修饰的类。
编译：javac -d . HelloWorld.java
含有包的类，在编译的时候最好用上面的格式，-d指的是让该类生成的时候按照包结构去生成，“.”指的是在当前路径下生成。
如果不用上面的格式，也可以用javac HelloWorld.java，但是需要注意的是包结构就要由自己去建立，然后将生成的.class文件放到该目录下。
执行：java mypack.HelloWorld
将字节码文件交给Java虚拟机去解释执行。
需要注意的事，必须使用包名.类名去解释执行。
(2) Java的运行过程
编译：生成可执行文件，如C++中利用g++生成a.out，效率高，但不跨平台。
解释：解释器把源文件逐行解释，跨平台但效率不高。
在java中，先编译后解释，把.java文件编译成.class字节码文件：
```java  
Java源代码文件(.java文件)   
Java编译器(javac)  
Java字节码文件(.class文件，平台无关的)   
Java解释器(java)，执行Java字节码
```
Java是跨平台的语言，真正执行的不是二进制代码，而是字节码。
Java程序的执行实际上是在JVM（Java Virtual Machine，Java虚拟机）上解释执行的，Java是跨平台的，而JVM不是跨平台的（JVM是由C语言编写的），Java之所以能够做到跨平台，本质原因在于JVM不是跨平台的。