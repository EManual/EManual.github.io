【例子1】
[code=java]
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
 
public class DataOutputStreamDemo{
    public static void main(String[] args) throws IOException{
        File file = new File("d:" + File.separator + "hello.txt");
        char[] ch = { "A", "B", "C" };
        DataOutputStream out = null;
        out = new DataOutputStream(new FileOutputStream(file));
        for(char temp : ch){
            out.writeChar(temp);
        }
        out.close();
    }
}
[/code]
【运行结果】：
[code=java]
A B C
[/code]
现在我们在上面例子的基础上，使用DataInputStream读出内容。
【例子2】
[code=java]
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
 
public class DataOutputStreamDemo{
    public static void main(String[] args) throws IOException{
        File file = new File("d:" + File.separator + "hello.txt");
        DataInputStream input = new DataInputStream(new FileInputStream(file));
        char[] ch = new char[10];
        int count = 0;
        char temp;
        while((temp = input.readChar()) != "C"){
            ch[count++] = temp;
        }
        System.out.println(ch);
    }
}
[/code]
【运行结果】：
[code=java]
AB
[/code]
