* 基本数据类型(Primitive Data Type)：8种。
1) 整型 
```java  
byte     1B	 8位     -128到127 
short    2B	 16位    -2^15到(2^15)-1 
int      4B	 32位    -2^31到(2^31)-1 
long     8B	 64位    -2^63到(2^63)-1 
```
2) 浮点类型 
```java  
float      4B	  32位       
double     8B	  64位 
```
3) 字符类型 
```java  
char    2B	16位 
```	
4) 布尔型 	1B
```java  
boolean    false/true
```
注：
1、Java中的自动类型提升问题。
正向过程：从低字节到高字节可以自动转换。
byte->short->int->long->float->double
逆向过程：从高字节到低字节用强制类型转换。
例：int a = (int)4.562；
注：逆向转换将丢失精度。
2、boolean：只有true和false。
3、char：Java中用" \u四位十六进制的数字 (即使在注释中出现\u，后面如果跟的不是4个数字，也会报错)"表示将字符转换成对应的unicode编码，字符类型要用单引号括起来。
4、黙认浮点类型为double，float数据类型有一个后缀为"f"或"F"。
5、long类型有一个后缀，为"l"或者"L"。
* 引用数据类型(Reference Type)：
类、接口、数组
引用类型 变量名 = new 引用类型名(参数);		//new后面一般跟的都是类的构造器
成员：写在类体括号里面的
自动类型提升：
```java  
byte a = 1;
byte b = 2;
a = a + b;      //编译出错自动类型提升成int
a += b;       //自加没有自动类型提升问题
```
类型自动提升规则：
a和b作某种运算：
a和b中有double，结果就是double。
a和b中有float，结果就是float。
a和b中有long，结果就是long。
除此之外，结果都是int。
把高字节转成低字节，需要作强制类型转换：byte c =(byte)a + b;
下面是数据类型图：
  