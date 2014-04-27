【例子1】向文件中写入字符串
```java  
/**
 * 字节流
 * 向文件中写入字符串
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        OutputStream out =new FileOutputStream(f);
        String str="你好";
        byte[] b=str.getBytes();
        out.write(b);
        out.close();
    }
}
```
查看hello.txt会看到“你好”。
当然也可以一个字节一个字节的写。
```java  
/**
 * 字节流
 * 向文件中一个字节一个字节的写入字符串
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        OutputStream out =new FileOutputStream(f);
        String str="你好";
        byte[] b=str.getBytes();
        for (int i = 0; i < b.length; i++) {
            out.write(b[i]);
        }
        out.close();
    }
}
```
结果还是：“你好”
【例子2】向文件中追加新内容
```java  
/**
 * 字节流
 * 向文件中追加新内容：
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        OutputStream out =new FileOutputStream(f,true);
        String str="Rollen";
        //String str="\r\nRollen";  可以换行
        byte[] b=str.getBytes();
        for (int i = 0; i < b.length; i++) {
            out.write(b[i]);
        }
        out.close();
    }
}
```
【运行结果】：
你好Rollen
【例子3】读取文件内容
```java  
/**
 * 字节流
 * 读文件内容
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        InputStream in=new FileInputStream(f);
        byte[] b=new byte[1024];
        in.read(b);
        in.close();
        System.out.println(new String(b));
    }
}
```
【运行结果】：
```java  
你好Rollen
Rollen_
```
但是这个例子读取出来会有大量的空格，我们可以利用in.read(b);的返回值来设计程序。如下：
```java  
/**
 * 字节流
 * 读文件内容
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        InputStream in=new FileInputStream(f);
        byte[] b=new byte[1024];
        int len=in.read(b);
        in.close();
        System.out.println("读入长度为："+len);
        System.out.println(new String(b,0,len));
    }
}
```
【运行结果】：
```java  
读入长度为：18
你好Rollen
Rollen
```
读者观察上面的例子可以看出，我们预先申请了一个指定大小的空间，但是有时候这个空间可能太小，有时候可能太大，我们需要准确的大小，这样节省空间，那么我们可以这样干：
```java  
/**
 * 字节流
 * 读文件内容,节省空间
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        InputStream in=new FileInputStream(f);
        byte[] b=new byte[(int)f.length()];
        in.read(b);
        System.out.println("文件长度为："+f.length());
        in.close();
        System.out.println(new String(b));
    }
}
```
【运行结果】：
```java  
文件长度为：18
你好Rollen
Rollen
```
【例子4】将上面的例子改为一个一个读
```java  
/**
 * 字节流
 * 读文件内容,节省空间
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        InputStream in=new FileInputStream(f);
        byte[] b=new byte[(int)f.length()];
        for (int i = 0; i < b.length; i++) {
            b[i]=(byte)in.read();
        }
        in.close();
        System.out.println(new String(b));
    }
}
```
输出的结果和上面的一样。
【例子3】上面的几个例子都是在知道文件的内容多大，然后才展开的，有时候我们不知道文件有多大，这种情况下，我们需要判断是否独到文件的末尾。
```java  
/**
 * 字节流
 *读文件
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        InputStream in=new FileInputStream(f);
        byte[] b=new byte[1024];
        int count =0;
        int temp=0;
        while((temp=in.read())!=(-1)){
            b[count++]=(byte)temp;
        }
        in.close();
        System.out.println(new String(b));
    }
}
```
【运行结果】：
```java  
你好Rollen
Rollen_
```
提醒一下，当读到文件末尾的时候会返回-1.正常情况下是不会返回-1的。