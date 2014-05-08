【例子1】
```java  
import java.io.ByteArrayInputStream;  import java.io.IOException;   import java.io.PushbackInputStream;  
/**   * 回退流操作   */  
public class PushBackInputStreamDemo{
    public static void main(String[] args) throws IOException{
        String str = "hello,rollenholt";
        PushbackInputStream push = null;
        ByteArrayInputStream bat = null;
        bat = new ByteArrayInputStream(str.getBytes());
        push = new PushbackInputStream(bat);
        int temp = 0;
        while((temp = push.read()) != -1){
            if(temp == ‘,’){
                push.unread(temp);
                temp = push.read();
                System.out.print("(回退" + (char) temp + ") ");
            }else{
                System.out.print((char) temp);
            }
        }
    }
}
```
【运行结果】：
hello(回退,) rollenholt
【例子2】
```java  
/**   * 取得本地的默认编码   */  
public class CharSetDemo{
    public static void main(String[] args){
        System.out.println("系统默认编码为：" + System.getProperty("file.encoding"));
    }
}
```
【运行结果】：
系统默认编码为：GBK
【例子3】乱码的产生：
```java  
import java.io.File;   import java.io.FileOutputStream;    import java.io.IOException;   import java.io.OutputStream;   
 
/**   * 乱码的产生   */   
public class CharSetDemo2{
    public static void main(String[] args) throws IOException{
        File file = new File("d:" + File.separator + "hello.txt");
        OutputStream out = new FileOutputStream(file);
        byte[] bytes = "你好".getBytes("ISO8859-1");
        out.write(bytes);
        out.close();
    }
}
```
【运行结果】：
??
一般情况下产生乱码，都是由于编码不一致的问题。
