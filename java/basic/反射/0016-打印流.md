打印流
```java  
/**
 * 使用PrintStream进行输出
 * */
import java.io.*;
 
class hello {
    public static void main(String[] args) throws IOException {
        PrintStream print = new PrintStream(new FileOutputStream(new File("d:"
                + File.separator + "hello.txt")));
        print.println(true);
        print.println("Rollen");
        print.close();
    }
}
```
【运行结果】：
```java  
true
Rollen
```
当然也可以格式化输出
```java  
/**
 * 使用PrintStream进行输出
 * 并进行格式化
 * */
import java.io.*;
class hello {
    public static void main(String[] args) throws IOException {
        PrintStream print = new PrintStream(new FileOutputStream(new File("d:"
                + File.separator + "hello.txt")));
        String name="Rollen";
        int age=20;
        print.printf("姓名：%s. 年龄：%d.",name,age);
        print.close();
    }
}
```
【运行结果】：
```java  
姓名：Rollen. 年龄：20.
```
