使用OutputStream向屏幕上输出内容
```java  
/**    * 使用OutputStream向屏幕上输出内容     */   
import java.io.*;
class hello {
    public static void main(String[] args) throws IOException {
        OutputStream out=System.out;
        try{
            out.write("hello".getBytes());
        }catch (Exception e) {
            e.printStackTrace();
        }
        try{
            out.close();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
【运行结果】：
hello
