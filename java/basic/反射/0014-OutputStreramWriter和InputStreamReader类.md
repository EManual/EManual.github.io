整个IO类中除了字节流和字符流还包括字节和字符转换流。
OutputStreramWriter将输出的字符流转化为字节流
InputStreamReader将输入的字节流转换为字符流
但是不管如何操作，最后都是以字节的形式保存在文件中的。
【例子1】将字节输出流转化为字符输出流
```java  
/**
 * 将字节输出流转化为字符输出流
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName= "d:"+File.separator+"hello.txt";
        File file=new File(fileName);
        Writer out=new OutputStreamWriter(new FileOutputStream(file));
        out.write("hello");
        out.close();
    }
}
```
【运行结果】：文件中内容为：hello
【例子2】将字节输入流变为字符输入流
```java  
/**
 * 将字节输入流变为字符输入流
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName= "d:"+File.separator+"hello.txt";
        File file=new File(fileName);
        Reader read=new InputStreamReader(new FileInputStream(file));
        char[] b=new char[100];
        int len=read.read(b);
        System.out.println(new String(b,0,len));
        read.close();
    }
}
```
【运行结果】：
```java  
hello
```
前面列举的输出输入都是以文件进行的，现在我们以内容为输出输入目的地，使用内存操作流
ByteArrayInputStream 主要将内容写入内容
ByteArrayOutputStream  主要将内容从内存输出
【例子3】使用内存操作流将一个大写字母转化为小写字母
```java  
/**
 * 使用内存操作流将一个大写字母转化为小写字母
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String str="ROLLENHOLT";
        ByteArrayInputStream input=new ByteArrayInputStream(str.getBytes());
        ByteArrayOutputStream output=new ByteArrayOutputStream();
        int temp=0;
        while((temp=input.read())!=-1){
            char ch=(char)temp;
            output.write(Character.toLowerCase(ch));
        }
        String outStr=output.toString();
        input.close();
        output.close();
        System.out.println(outStr);
    }
}
```
【运行结果】：
```java  
rollenholt
```
内容操作流一般使用来生成一些临时信息采用的，这样可以避免删除的麻烦。
