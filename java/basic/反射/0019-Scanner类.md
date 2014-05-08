其实我们比较常用的是采用Scanner类来进行数据输入，下面来给一个Scanner的例子吧。
```java  
BufferedReader buf = new BufferedReader(
                new InputStreamReader(System.in));
```
【例子1】
```java  
import java.util.Scanner;
/**   * Scanner的小例子，从键盘读数据   *   
 */  
public class ScannerDemo{
    public static void main(String[] args){
        Scanner sca = new Scanner(System.in);
        // 读一个整数
        int temp = sca.nextInt();
        System.out.println(temp);
        //读取浮点数
        float flo=sca.nextFloat();
        System.out.println(flo);
        //读取字符
        //...等等的，都是一些太基础的，就不师范了。
    }
}
```
其实Scanner可以接受任何的输入流
下面给一个使用Scanner类从文件中读出内容
【例子2】
```java  
import java.io.File;  import java.io.FileNotFoundException;  import java.util.Scanner;     
/**  
 * Scanner的小例子，从文件中读内容  
 */  
public class ScannerDemo{
    public static void main(String[] args){
        File file = new File("d:" + File.separator + "hello.txt");
        Scanner sca = null;
        try{
            sca = new Scanner(file);
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }
        String str = sca.next();
        System.out.println("从文件中读取的内容是：" + str);
    }
}
```
【运行结果】：
从文件中读取的内容是：这些文件中的内容哦！
