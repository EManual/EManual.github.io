SequenceInputStream主要用来将2个流合并在一起，比如将两个txt中的内容合并为另外一个txt。下面给出一个实例：
```java  import java.io.File;  import java.io.FileInputStream;  import java.io.FileOutputStream;  import java.io.IOException;  import java.io.InputStream;  import java.io.OutputStream;  import java.io.SequenceInputStream;  
/**   * 将两个文本文件合并为另外一个文本文件   */  
public class SequenceInputStreamDemo{
    public static void main(String[] args) throws IOException{
        File file1 = new File("d:" + File.separator + "hello1.txt");
        File file2 = new File("d:" + File.separator + "hello2.txt");
        File file3 = new File("d:" + File.separator + "hello.txt");
        InputStream input1 = new FileInputStream(file1);
        InputStream input2 = new FileInputStream(file2);
        OutputStream output = new FileOutputStream(file3);
        // 合并流
        SequenceInputStream sis = new SequenceInputStream(input1, input2);
        int temp = 0;
        while((temp = sis.read()) != -1){
            output.write(temp);
        }
        input1.close();
        input2.close();
        output.close();
        sis.close();
    }
}
```
【运行结果】：
结果会在hello.txt文件中包含hello1.txt和hello2.txt文件中的内容。
