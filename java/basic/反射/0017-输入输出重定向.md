【例子1】输入输出重定向
```java  
import java.io.File;  import java.io.FileNotFoundException;  import java.io.FileOutputStream;   import java.io.PrintStream;     

/**   * 为System.out.println()重定向输出   */  
public class systemDemo{
    public static void main(String[] args){
        // 此刻直接输出到屏幕
        System.out.println("hello");
        File file = new File("d:" + File.separator + "hello.txt");
        try{
            System.setOut(new PrintStream(new FileOutputStream(file)));
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }
        System.out.println("这些内容在文件中才能看到哦！");
    }
}
```
【运行结果】：
eclipse的控制台输出的是hello。然后当我们查看d盘下面的hello.txt文件的时候，会在里面看到：这些内容在文件中才能看到哦！
【例子2】
```java  
import java.io.File;   import java.io.FileNotFoundException;   import java.io.FileOutputStream;  import java.io.PrintStream;  

/**   * System.err重定向 这个例子也提示我们可以使用这种方法保存错误信息    */  
public class systemErr{
    public static void main(String[] args){
        File file = new File("d:" + File.separator + "hello.txt");
        System.err.println("这些在控制台输出");
        try{
            System.setErr(new PrintStream(new FileOutputStream(file)));
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }
        System.err.println("这些在文件中才能看到哦！");
    }
}
```
【运行结果】：
你会在eclipse的控制台看到红色的输出：“这些在控制台输出”，然后在d盘下面的hello.txt中会看到：这些在文件中才能看到哦！
【例子3】
```java  
import java.io.File;  import java.io.FileInputStream;  import java.io.FileNotFoundException;  import java.io.IOException;   
/**   * System.in重定向   */  
public class systemIn{
    public static void main(String[] args){
        File file = new File("d:" + File.separator + "hello.txt");
        if(!file.exists()){
            return;
        }else{
            try{
                System.setIn(new FileInputStream(file));
            }catch(FileNotFoundException e){
                e.printStackTrace();
            }
            byte[] bytes = new byte[1024];
            int len = 0;
            try{
                len = System.in.read(bytes);
            }catch(IOException e){
                e.printStackTrace();
            }
            System.out.println("读入的内容为：" + new String(bytes, 0, len));
        }
    }
}
```
【运行结果】：
前提是我的d盘下面的hello.txt中的内容是：“这些文件中的内容哦！”，然后运行程序，输出的结果为：读入的内容为：这些文件中的内容哦！
