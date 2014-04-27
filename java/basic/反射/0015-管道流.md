管道流主要可以进行两个线程之间的通信。
```java  
PipedOutputStream 管道输出流
PipedInputStream 管道输入流
```
【例子1】验证管道流
```java  
/**
 * 验证管道流
 * */
import java.io.*;
 
/**
 * 消息发送类
 * */
class Send implements Runnable{
    private PipedOutputStream out=null;
    public Send() {
        out=new PipedOutputStream();
    }
    public PipedOutputStream getOut(){
        return this.out;
    }
    public void run(){
        String message="hello , Rollen";
        try{
            out.write(message.getBytes());
        }catch (Exception e) {
            e.printStackTrace();
        }try{
            out.close();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
 
/**
 * 接受消息类
 * */
class Recive implements Runnable{
    private PipedInputStream input=null;
    public Recive(){
        this.input=new PipedInputStream();
    }
    public PipedInputStream getInput(){
        return this.input;
    }
    public void run(){
        byte[] b=new byte[1000];
        int len=0;
        try{
            len=this.input.read(b);
        }catch (Exception e) {
            e.printStackTrace();
        }try{
            input.close();
        }catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("接受的内容为 "+(new String(b,0,len)));
    }
}
/**
 * 测试类
 * */
class hello{
    public static void main(String[] args) throws IOException {
        Send send=new Send();
        Recive recive=new Recive();
        try{
//管道连接
            send.getOut().connect(recive.getInput());
        }catch (Exception e) {
            e.printStackTrace();
        }
        new Thread(send).start();
        new Thread(recive).start();
    }
}
```
【运行结果】：接受的内容为 hello , Rollen
