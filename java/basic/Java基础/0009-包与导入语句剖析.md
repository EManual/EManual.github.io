1、包(package)。用于将完成不同功能的类分门别类，放在不同的目录（包）下。包的命名规则：将公司域名反转作为包名。比如www.shengsiyuan.com，则包名字就可以写成com.shengsiyuan（包名），对于包名：每个字母都需要小写。
```java  
package com.shengsiyuan;
public class PackageTest{
	public static void main(String[] args){
		System.out.println("Helloworld");
	}
}
```
编译通过执行出现如下错误：
```java  
D:\src>javac PackageTest.java
D:\src>java PackageTest
Exception in thread "main" java.lang.NoClassDefFoundError: PackageTest (wrong name: com/shengsiyuan/PackageTest)
        at java.lang.ClassLoader.defineClass1(Native Method)
        at java.lang.ClassLoader.defineClass(Unknown Source)
        at java.security.SecureClassLoader.defineClass(Unknown Source)
        at java.net.URLClassLoader.defineClass(Unknown Source)
        at java.net.URLClassLoader.access$100(Unknown Source)
        at java.net.URLClassLoader$1.run(Unknown Source)
        at java.net.URLClassLoader$1.run(Unknown Source)
        at java.security.AccessController.doPrivileged(Native Method)
        at java.net.URLClassLoader.findClass(Unknown Source)
        at java.lang.ClassLoader.loadClass(Unknown Source)
        at sun.misc.Launcher$AppClassLoader.loadClass(Unknown Source)
        at java.lang.ClassLoader.loadClass(Unknown Source)
        at sun.launcher.LauncherHelper.checkAndLoadMain(Unknown Source)
```
【说明】：NoClassDefFoundError 没有类定义发现错误，找不到这个com/shengsiyuan/PackageTest这个类，所以这个是错误时因为包的路径出现的错误，所以要使用包这个概念，必须要建立好包的这个目录结构，然后把这个编译生成的.class文件放在里面，执行命令java com.shengsiyuan.PackageTest，如下执行成功。
```java  
D:\src>java com.shengsiyuan.PackageTest
Helloworld
```
【说明】：此时这个类的全名是com.shengsiyuan.PackageTest，如果定义类的时候没有使用package，那么Java就认为我们所定义的类位于默认包里（default package）。
2、编译带有package声明的Java源文件有两种方式： 
a) 直接编译，然后根据类中所定义的包名，逐一手工建立目录结构，最后将生成的.class文件放到该目录结构中（很少使用，比较麻烦）。 
b) 使用编译参数 –d，方式为 javac –d . 源文件.java，这样在编译后，编译器会自动帮助我们建立好包所对应的目录结构。
如上一个例子用以下命令则编译器就会自动将我们的类文件放在定义的包目录下，当然编译的时候要写全名：
```java  
D:\src>javac -d . PackageTest.java
D:\src>java com.shengsiyuan.PackageTest
Helloworld
```
3、有两个包名，分别是 aa.bb.cc 与 aa.bb.cc.dd，那么我们称后者为前者的子包。 
4、导入（import），将使用package分离的各个类导入回来，让编译器能够找到所需要的类。
程序一：
```java  
package com.shengsiyuan;
public class PackageTest{
	public static int i = 100;
}
```
程序二：
```java  
import com.shengsiyuan.PackageTest;

public class ImportTest{
	public static void main(String[] args){
		System.out.println(PackageTest.i);	
	}
}
```
编译结果：
```java  
D:\src>javac -d . PackageTest.java
D:\src>javac ImportTest.java
D:\src>java ImportTest
100
```
5、import 的语法：import  com.shengsiyuan.PackageTest; 
6、import com.shengsiyuan.*，表示导入 com.shengsiyuan 包下面的所有类。*表示通配符。匹配任何字符。
7、import aa.bb.*并不会导入 aa.bb.cc 包下面的类。这时需要这样写：
```java  
import aa.bb.*; 
import aa.bb.cc.*;
```
8、关于 package、import、class 的顺序问题： 
a) 首先需要定义包（package），可选 
b) 接下来使用 import 进行导入，可选 
c) 然后才是 class 或 interface 的定义。 
9、如果两个类在同一个包下面，那么则不需要导入，直接使用即可。