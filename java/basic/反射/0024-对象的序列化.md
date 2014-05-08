对象序列化就是把一个对象变为二进制数据流的一种方法。
一个类要想被序列化，就行必须实现java.io.Serializable接口。虽然这个接口中没有任何方法，就如同之前的cloneable接口一样。实现了这个接口之后，就表示这个类具有被序列化的能力。
先让我们实现一个具有序列化能力的类吧：
【例子1】
```java  
import java.io.*;  /**   * 实现具有序列化能力的类    */   
public class SerializableDemo implements Serializable{
    public SerializableDemo(){
         
    }
    public SerializableDemo(String name, int age){
        this.name=name;
        this.age=age;
    }
    @Override
    public String toString(){
        return "姓名："+name+"  年龄："+age;
    }
    private String name;
    private int age;
}
```
这个类就具有实现序列化能力，在继续将序列化之前，先将一下ObjectInputStream和ObjectOutputStream这两个类
先给一个ObjectOutputStream的例子吧：
【例子2】
```java  
import java.io.Serializable;   import java.io.File;    import java.io.FileOutputStream;      import java.io.IOException;     import java.io.ObjectOutputStream;     
/**    * 实现具有序列化能力的类   */   
public class Person implements Serializable{
    public Person(){
    }
 
    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }
 
    @Override
    public String toString(){
        return "姓名：" + name + "  年龄：" + age;
    }
 
    private String name;
    private int age;
}
/**
 * 示范ObjectOutputStream
 * */
public class ObjectOutputStreamDemo{
    public static void main(String[] args) throws IOException{
        File file = new File("d:" + File.separator + "hello.txt");
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(
                file));
        oos.writeObject(new Person("rollen", 20));
        oos.close();
    }
}
```
【运行结果】：
当我们查看产生的hello.txt的时候，看到的是乱码，呵呵。因为是二进制文件。
虽然我们不能直接查看里面的内容，但是我们可以使用ObjectＩｎｐｕｔＳｔｒｅａｍ类查看：
【例子3】
```java  
import java.io.File;import java.io.FileInputStream;import java.io.ObjectInputStream;
/**   * ObjectInputStream示范    */   
public class ObjectInputStreamDemo{
    public static void main(String[] args) throws Exception{
        File file = new File("d:" + File.separator + "hello.txt");
        ObjectInputStream input = new ObjectInputStream(new FileInputStream(
                file));
        Object obj = input.readObject();
        input.close();
        System.out.println(obj);
    }
}
```
【运行结果】：
姓名：rollen  年龄：20
到底序列化什么内容呢？
其实只有属性会被序列化。
* Externalizable接口
被Serializable接口声明的类的对象的属性都将被序列化，但是如果想自定义序列化的内容的时候，就需要实现Externalizable接口。
当一个类要使用Externalizable这个接口的时候，这个类中必须要有一个无参的构造函数，如果没有的话，在构造的时候会产生异常，这是因为在反序列话的时候会默认调用无参的构造函数。
现在我们来演示一下序列化和反序列话：
【例子4】
```java  
package IO;
import java.io.Externalizable;    import java.io.File;   import java.io.FileInputStream;   import java.io.FileOutputStream;   import java.io.IOException;   import java.io.ObjectInput;   import java.io.ObjectInputStream;   import java.io.ObjectOutput;   import java.io.ObjectOutputStream;   
 
/**   * 序列化和反序列化的操作    */   
public class ExternalizableDemo{
    public static void main(String[] args) throws Exception{
        ser(); // 序列化
        dser(); // 反序列话
    }
 
    public static void ser() throws Exception{
        File file = new File("d:" + File.separator + "hello.txt");
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(
                file));
        out.writeObject(new Person("rollen", 20));
        out.close();
    }
 
    public static void dser() throws Exception{
        File file = new File("d:" + File.separator + "hello.txt");
        ObjectInputStream input = new ObjectInputStream(new FileInputStream(
                file));
        Object obj = input.readObject();
        input.close();
        System.out.println(obj);
    }
}
 
class Person implements Externalizable{
    public Person(){
    }
 
    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }
 
    @Override    public String toString(){
        return "姓名：" + name + "  年龄：" + age;
    }
 
    // 复写这个方法，根据需要可以保存的属性或者具体内容，在序列化的时候使用
    @Override    public void writeExternal(ObjectOutput out) throws IOException{
        out.writeObject(this.name);
        out.writeInt(age);
    }
 
    // 复写这个方法，根据需要读取内容 反序列话的时候需要
    @Override    public void readExternal(ObjectInput in) throws IOException,
            ClassNotFoundException{
        this.name = (String) in.readObject();
        this.age = in.readInt();
    }
    private String name;
    private int age;
}
```
【运行结果】：
姓名：rollen  年龄：20
本例中，我们将全部的属性都保留了下来，
Serializable接口实现的操作其实是吧一个对象中的全部属性进行序列化，当然也可以使用我们上使用是Externalizable接口以实现部分属性的序列化，但是这样的操作比较麻烦，
当我们使用Serializable接口实现序列化操作的时候，如果一个对象的某一个属性不想被序列化保存下来，那么我们可以使用transient关键字进行说明：
下面举一个例子：
【例子5】
```java  
package IO;
import java.io.File;  import java.io.FileInputStream;  import java.io.FileOutputStream;  import java.io.ObjectInputStream;  import java.io.ObjectOutputStream;  import java.io.Serializable;   
/**   * 序列化和反序列化的操作    */   
public class serDemo{
    public static void main(String[] args) throws Exception{
        ser(); // 序列化
        dser(); // 反序列话
    }
 
    public static void ser() throws Exception{
        File file = new File("d:" + File.separator + "hello.txt");
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(
                file));
        out.writeObject(new Person1("rollen", 20));
        out.close();
    }
 
    public static void dser() throws Exception{
        File file = new File("d:" + File.separator + "hello.txt");
        ObjectInputStream input = new ObjectInputStream(new FileInputStream(
                file));
        Object obj = input.readObject();
        input.close();
        System.out.println(obj);
    }
}
 
class Person1 implements Serializable{
    public Person1(){
    }
    public Person1(String name, int age){
        this.name = name;
        this.age = age;
    }
 
    @Override    public String toString(){
        return "姓名：" + name + "  年龄：" + age;
    }
 
    // 注意这里    private transient String name;
    private int age;
}
```
【运行结果】：
姓名：null  年龄：20
最后在给一个序列化一组对象的例子吧：
【例子6】
```java  
import java.io.File;   import java.io.FileInputStream;   import java.io.FileOutputStream;   import java.io.ObjectInputStream;   import java.io.ObjectOutputStream;   import java.io.Serializable;  

/**   * 序列化一组对象   */  
public class SerDemo1{
    public static void main(String[] args) throws Exception{
        Student[] stu = { new Student("hello", 20), new Student("world", 30),
                new Student("rollen", 40) };
        ser(stu);
        Object[] obj = dser();
        for(int i = 0; i < obj.length; ++i){
            Student s = (Student) obj[i];
            System.out.println(s);
        }
    }
 
    // 序列化    public static void ser(Object[] obj) throws Exception{
        File file = new File("d:" + File.separator + "hello.txt");
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(
                file));
        out.writeObject(obj);
        out.close();
    }
 
    // 反序列化    public static Object[] dser() throws Exception{
        File file = new File("d:" + File.separator + "hello.txt");
        ObjectInputStream input = new ObjectInputStream(new FileInputStream(
                file));
        Object[] obj = (Object[]) input.readObject();
        input.close();
        return obj;
    }
}
 
class Student implements Serializable{
    public Student(){ 
    }
    public Student(String name, int age){
        this.name = name;
        this.age = age;
    }
 
    @Override    public String toString(){
        return "姓名：  " + name + "  年龄：" + age;
    }
    private String name;
    private int age;
}
```
【运行结果】：
```java  
姓名：  hello  年龄：20
姓名：  world  年龄：30
姓名：  rollen  年龄：40
```
