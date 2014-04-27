String：不可改变的Unicode字符序列。
池化思想，把需要共享的数据放在池中，用一个存储区域来存放一些公用资源以减少存储空间的开销。
在String类中，以字面值创建时，会到Java方法空间的串池中去查找，如果没有则会在串池里创建一个字符串对象，并返回其地址赋给对象变量，如果有就返回串池中字符串的地址，并把这个地址赋给对象变量。
如果是new，则会在堆空间中创建String类的对象，不会有上述的过程。
如：
```java  
String s1 = “abc”;//新创建，字符串常量池中没有该串，则会在池中创建一个串“abc”
String s2 = “abc”;//串池中已经存在“abc”，则s2会去指向“abc”而不会去创建一个新的
String s3 = new String(“abc”);//直接在堆中去开辟一个新的空间，而不会去池中查找
```
类中的具体方法查看下Api文档。
调用任何String中的方法，不会改变String自身，除非重新赋值。
StringBuffer：可改变的Unicode字符序列。
允许并发操作，是线程安全的。
String类在进行字符串连接时会显得效率很低，就是因为它所产生的对象的属性是不能够修改的，当连接字符串时也就只能创建新的对象。
对于很多字符串连接时，应当使用StringBuffer类，使用这个类的对象来进行字符串连接时就不会有多余的中间对象生成，从而优化了效率。
例：对于字符串连接String str = “A” + “B” + “C” + “D”;
产生：“AB”、“ABC”、“ABCD”。
在串池中产生的“AB”、“ABC”明显是多余对象，浪费空间。
解决方案：
```java  
String s = null;
StringBuffer sb = new StringBuffer(“A”);
sb.append(“B”);
sb.append(“C”);
sb.append(“D”);
s = sb.toString();
```
StringBulder：可改变的Unicode字符序列。
操作同StringBuffer，只是不支持并发操作，非线程安全的。