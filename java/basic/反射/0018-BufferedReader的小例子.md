注意： BufferedReader只能接受字符流的缓冲区，因为每一个中文需要占据两个字节，所以需要将System.in这个字节输入流变为字符输入流，采用：
```java  
BufferedReader buf = new BufferedReader(
                new InputStreamReader(System.in));
```
下面给一个实例：
```java  
import java.io.BufferedReader;  import java.io.IOException;  import java.io.InputStreamReader;  
 
/**  
 * 使用缓冲区从键盘上读入内容   */
public class BufferedReaderDemo{
    public static void main(String[] args){
        BufferedReader buf = new BufferedReader(
                new InputStreamReader(System.in));
        String str = null;
        System.out.println("请输入内容");
        try{
            str = buf.readLine();
        }catch(IOException e){
            e.printStackTrace();
        }
        System.out.println("你输入的内容是：" + str);
    }
}
```
【运行结果】：
```java  
请输入内容
dasdas
你输入的内容是：dasdas
```
