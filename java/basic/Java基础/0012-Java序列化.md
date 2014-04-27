Java 串行化技术可以使你将一个对象的状态写入一个Byte 流里，并且可以从其它地方把该Byte 流里的数据读出来，重新构造一个相同的对象。这种机制允许你将对象通过网络进行传播，并可以随时把对象持久化到数据库、文件等系统里。Java的串行化机制是RMI、EJB等技术的技术基础。用途：利用对象的串行化实现保存应用程序的当前工作状态，下次再启动的时候将自动地恢复到上次执行的状态。
序列化就是一种用来处理对象流的机制，所谓对象流也就是将对象的内容进行流化。可以对流化后的对象进行读写操作，也可将流化后的对象传输于网络之间。序列化是为了解决在对对象流进行读写操作时所引发的问题。
序列化的实现：将需要被序列化的类实现Serializable接口，然后使用一个输出流(如：FileOutputStream)来构造一个ObjectOutputStream(对象流)对象，接着，使用ObjectOutputStream对象的writeObject(Object obj)方法就可以将参数为obj的对象写出(即保存其状态)，要恢复的话则用输入流。
* 串行化的特点：
1、如果某个类能够被串行化，其子类也可以被串行化。如果该类有父类，则分两种情况来考虑，如果该父类已经实现了可串行化接口。则其父类的相应字段及属性的处理和该类相同；如果该类的父类没有实现可串行化接口，则该类的父类所有的字段属性将不会串行化。
2、声明为static和transient类型的成员数据不能被串行化。因为static代表类的状态， transient代表对象的临时数据；
3、相关的类和接口：在java.io包中提供的涉及对象的串行化的类与接口有ObjectOutput接口、ObjectOutputStream类、ObjectInput接口、ObjectInputStream类。
A：ObjectOutput接口：它继承DataOutput接口并且支持对象的串行化，其内的writeObject()方法实现存储一个对象。ObjectInput接口：它继承DataInput接口并且支持对象的串行化，其内的readObject()方法实现读取一个对象。
B：ObjectOutputStream类：它继承OutputStream类并且实现ObjectOutput接口。利用该类来实现将对象存储（调用ObjectOutput接口中的writeObject()方法）。ObjectInputStream类：它继承InputStream类并且实现ObjectInput接口。利用该类来实现读取一个对象（调用ObjectInput接口中的readObject()方法）。
对于父类的处理，如果父类没有实现串行化接口，则其必须有默认的构造函数（即没有参数的构造函数）。否则编译的时候就会报错。在反串行化的时候，默认构造函数会被调用。但是若把父类标记为可以串行化，则在反串行化的时候，其默认构造函数不会被调用。这是为什么呢？这是因为Java对串行化的对象进行反串行化的时候，直接从流里获取其对象数据来生成一个对象实例，而不是通过其构造函数来完成。
```java  
import java.io.*;
public class Cat implements Serializable {
	private String name;
	public Cat () {
		this.name = "new cat";
	}
	public String getName() {
		return this.name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public static void main(String[] args) {         
		Cat cat = new Cat();
		try {
			FileOutputStream fos = new FileOutputStream("catDemo.out");
			ObjectOutputStream oos = new ObjectOutputStream(fos);
			System.out.println(" 1> " + cat.getName());
			cat.setName("My Cat");                       
			oos.writeObject(cat);
			oos.close();                       
		} catch (Exception ex) {  ex.printStackTrace();   }
		try {
			FileInputStream fis = new FileInputStream("catDemo.out");
			ObjectInputStream ois = new ObjectInputStream(fis);
			cat = (Cat) ois.readObject();
			System.out.println(" 2> " + cat.getName());
			ois.close();
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}
}//writeObject和readObject本身就是线程安全的，传输过程中是不允许被并发访问的。所以对象能一个一个接连不断的传过来
```