【例子1】创建一个新文件。
```java  
import java.io.*;
class hello{
    public static void main(String[] args) {
        File f=new File("D:\\hello.txt");
        try{
            f.createNewFile();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
【运行结果】：
程序运行之后，在d盘下会有一个名字为hello.txt的文件。
【例子2】File类的两个常量
```java  
import java.io.*;
class hello{
    public static void main(String[] args) {
        System.out.println(File.separator);
        System.out.println(File.pathSeparator);
    }
}
```
【运行结果】：
```java  
\
;
```
此处多说几句：我直接在windows下使用\进行分割不行吗？当然是可以的。但是在linux下就不是\了。所以，要想使得我们的代码跨平台，更加健壮，所以，大家都采用这两个常量吧，其实也多写不了几行。
现在我们使用File类中的常量改写上面的代码：
```java  
import java.io.*;
class hello{
    public static void main(String[] args) {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        try{
            f.createNewFile();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
【例子3】删除一个文件
```java  
/**
 * 删除一个文件
 * */
import java.io.*;
class hello{
    public static void main(String[] args) {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        if(f.exists()){
            f.delete();
        }else{
            System.out.println("文件不存在");
        }
         
    }
}
```
【例子4】创建一个文件夹
```java  
/**
 * 创建一个文件夹
 * */
import java.io.*;
class hello{
    public static void main(String[] args) {
        String fileName="D:"+File.separator+"hello";
        File f=new File(fileName);
        f.mkdir();
    }
}
```
【运行结果】：
D盘下多了一个hello文件夹
【例子5】列出指定目录的全部文件（包括隐藏文件）：
```java  
/**
 * 使用list列出指定目录的全部文件
 * */
import java.io.*;
class hello{
    public static void main(String[] args) {
        String fileName="D:"+File.separator;
        File f=new File(fileName);
        String[] str=f.list();
        for (int i = 0; i < str.length; i++) {
            System.out.println(str[i]);
        }
    }
}
```
【运行结果】：
D盘下所有文件(每个人的运行结果不同)
【例子6】判断一个指定的路径是否为目录
```java  
/**
 * 使用isDirectory判断一个指定的路径是否为目录
 * */
import java.io.*;
class hello{
    public static void main(String[] args) {
        String fileName="D:"+File.separator;
        File f=new File(fileName);
        if(f.isDirectory()){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
}
```
【运行结果】：YES
【例子7】搜索指定目录的全部内容
```java  
/**
 * 列出指定目录的全部内容
 * */
import java.io.*;
class hello{
    public static void main(String[] args) {
        String fileName="D:"+File.separator;
        File f=new File(fileName);
        print(f);
    }
    public static void print(File f){
        if(f!=null){
            if(f.isDirectory()){
                File[] fileArray=f.listFiles();
                if(fileArray!=null){
                    for (int i = 0; i < fileArray.length; i++) {
                        //递归调用
                        print(fileArray[i]);
                    }
                }
            }
            else{
                System.out.println(f);
            }
        }
    }
}
```
【运行结果】：
指定目录的全部内容(每个人的运行结果不同)
【例子8】使用RandomAccessFile写入文件
```java  
/**
 * 使用RandomAccessFile写入文件
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        String fileName="D:"+File.separator+"hello.txt";
        File f=new File(fileName);
        RandomAccessFile demo=new RandomAccessFile(f,"rw");
        demo.writeBytes("asdsad");
        demo.writeInt(12);
        demo.writeBoolean(true);
        demo.writeChar('A');
        demo.writeFloat(1.21f);
        demo.writeDouble(12.123);
        demo.close();   
    }
}
```
如果你此时打开hello。txt查看的话，会发现那是乱码。
【例子9】文件的复制
基本思路还是从一个文件中读入内容，边读边写入另一个文件，就是这么简单。、
首先编写下面的代码：
```java  
/**
 * 文件的复制
 * */
import java.io.*;
class hello{
    public static void main(String[] args) throws IOException {
        if(args.length!=2){
            System.out.println("命令行参数输入有误，请检查");
            System.exit(1);
        }
        File file1=new File(args[0]);
        File file2=new File(args[1]);
         
        if(!file1.exists()){
            System.out.println("被复制的文件不存在");
            System.exit(1);
        }
        InputStream input=new FileInputStream(file1);
        OutputStream output=new FileOutputStream(file2);
        if((input!=null)&&(output!=null)){
            int temp=0;
            while((temp=input.read())!=(-1)){
                output.write(temp);
            }
        }
        input.close();
        output.close(); 
    }
}
```
然后在命令行下面
```java  
javac hello.java
java hello d:\hello.txt d:\rollen.txt
```
现在你就会在d盘看到rollen。txt了。