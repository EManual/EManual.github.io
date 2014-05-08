【例子1】向文件中写入数据
现在我们使用字符流
```java  
/**   * 字符流   * 写入数据   */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        Writer out =new FileWriter(f);
        String str="hello";
        out.write(str);
        out.close();
    }
}
```
当你打开hello。txt的时候，会看到hello
其实这个例子上之前的例子没什么区别，只是你可以直接输入字符串，而不需要你将字符串转化为字节数组。
当你如果想问文件中追加内容的时候，可以使用将上面的声明out的哪一行换为：
```java  
Writer out =new FileWriter(f,true);
```
这样，当你运行程序的时候，会发现文件内容变为：
```java  
hellohello如果想在文件中换行的话，需要使用“\r\n”
```
比如将str变为String str="\r\nhello";
这样文件追加的str的内容就会换行了。
【例子2】从文件中读内容：
```java  
/**  
 * 字符流   
 * 从文件中读出内容  
 */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        char[] ch=new char[100];
        Reader read=new FileReader(f);
        int count=read.read(ch);
        read.close();
        System.out.println("读入的长度为："+count);
        System.out.println("内容为"+new String(ch,0,count));
    }
}
```
【运行结果】：
```java  
读入的长度为：17
内容为hellohello
hello
```
当然最好采用循环读取的方式，因为我们有时候不知道文件到底有多大。
```java  
/**  
 * 字符流   
 * 从文件中读出内容   
 */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        char[] ch=new char[100];
        Reader read=new FileReader(f);
        int temp=0;
        int count=0;
        while((temp=read.read())!=(-1)){
            ch[count++]=(char)temp;
        }
        read.close();
        System.out.println("内容为"+new String(ch,0,count));
    }
}
```
【运行结果】：
```java  
内容为hellohello
hello
```
