字节输入流：InputStream类为所有字节输入流的父类。
三个基本的read()方法： 
```java  
	int read()
		从流里读出的一个字节。不推荐使用
	int read(byte[] b)
		将数据读入到字节数组中，并返回所读的字节数
	int read(byte[] b, int off, int len)
		off  从哪里开始读。
		len  读取多少。
		将输入流中最多 len 个数据字节读入字节数组。
```
其它方法： 
```java  
	void close() 
		关闭此输入流并释放与该流关联的所有系统资源。
	int available()
		返回不受阻塞地从此输入流读取的字节数。
	long skip(long n)
		跳过和放弃此输入流中的n个数据字节，该方法有可能失效。
	boolean markSupported()
		测试此输入流是否支持 mark 和 reset 方法。
	void mark(int n)
		在此输入流中标记当前的位置
	void reset()
		将此流重新定位到对此输入流最后调用 mark 方法时的位置。 
```
字节输出流：OutputStream类是所有字节输入流的父类。
三个基本的write()方法： 
```java  
	void write(int n)
		将指定的字节写入此输出流。
	void write(byte[] b) 
		将 b.length 个字节从指定的字节数组写入此输出流。
	void write(byte[] b, int off, int len)
		将指定字节数组中从偏移量off开始的len个字节写入此输出流。
```
其它方法： 
```java  
	void close()
			关闭此输出流并释放与此流有关的所有系统资源。
	void flush()
			刷新此输出流并强制写出所有缓冲的输出字节。 
```		
文件输入输出流：FileInputStream和FileOutputStream
要构造一个FileInputStream，所关联的文件必须存在而且是可读的。
如：
```java  
	FileInputStream fis = new FileInputStream("myfile.dat"); 
```
要构造一个FileOutputStream，而输出文件已经存在，则它将被覆盖。		 	
如：
```java  			
	FIleOutputStream fos = new FileOutputStream("results.dat"); 
```
要想以追加的方式写，则需要一个额外的参数，如：
```java  	
	FileOutputStream outfile = new FileOutputStream("results.dat" ,true);	//参数为true时输出为追加，为false时为覆盖。
```
字符流：Reader和Writer所有字符流的父类型。
Java技术使用Unicode来表示字符串和字符，而且提供16位版本的流，以便用类似的方法处理字符。 
如果构造了一个连接到流的Reader和Writer，转换规则会在使用缺省平台所定义的字节编码和Unicode之间切换。 
桥梁流：InputStreamReader和OutputStreamWriter（字节流转化成字符流的桥转换器）
这两个类不是用于直接输入输出的，他是将字节流转换成字符流的桥转换器，并可以指定编解码方式。
逐行读写流：BufferedReader/BufferedWriter
以上两个都是过滤流，需要用其他的节点流来作参数构造对象。
BufferedReader的方法：readLine():String ，当他的返回值是null时，就表示读取完毕了。要注意，再写入时要注意写换行符，否则会出现阻塞。
BufferedWriter的方法：newLine() ，这个方法会写出一个换行符。
管道流：线程交互的时候使用
PipedInputStream/PipedOutputStream
传送输出流可以连接到传送输入流，以创建通信管道。传送输出流是管道的发送端。通常，数据由某个线程写入 PipedOutputStream 对象，并由其他线程从连接的 PipedInputStream 读取。
注意：管道输出流和管道输入流需要对接。
数据流：DataInputStream和DataOutputStream
通过流来读写Java基本类，注意DataInputStream和DataOutputStream的方法是成对的。 
支持直接输出输入各种数据类型。
注意：使用DataOutputStream/DataInputStream时，要注意写入顺序和读取顺序相同，否则会将没有分割写入的信息分割不正确而读取出错误的数据。
对象流：ObjectInputStream和ObjectOutputStream（实现对象序列化）。
对象流是过滤流，需要节点流作参数来构造对象，用于直接把对象写入文件和从文件中读取对象。
只有实现了Serializable接口的类型的对象才可以被读写，Serializable接口是个标记接口，其中没有定义方法。
对象会序列化成一个二进制代码，文件中保存对象的属性。
writeObject(o)、readObject()这两个是对象读写操作时用的方法。
```java  
	Object o = new Object();	
	FileOutputStream fos=new FileOutputStream(“Object.txt”);
	ObjectOutputStream oos=new ObjectOutputStream(fos);
	oos.writeObject(o);
	oos.close();

	FileInputStream fis =new FileInputStream(“Object.txt”);
	ObjectInputStream ois =new ObjectInputStream(fis);
	Object o = (Object)Ois.readObject();
	ois.close();
```
一个类中有其他类型的对象，那么，这个类实现了Serializable接口，在对象序列化时，也同样要求这个类中属性都能够对象序列化（基本类型除外）。
注意：
对于对象流的操作，在写对象时要一次写入完毕，如果使用追加模式写入，只会读取到上一次写入的对象，使用对象流写入时，会先写入一个头部，然后写入数据，最后加上结束符号，如果使用追加方式写入的话，那就会在结束符号继续向下写入，但是在读取时只会读到结束符为止，以后再次写入的数据就会丢失。
包名、类名和属性可以被序列化，方法和构造器不会被序列化的。
静态属性不会被序列化的。
属性会被递归序列化的，也就是一个类中有引用类型的属性，如果这个属性对应的类实现了Serializable接口，在对象序列化时，也同样会对这个类中的属性进行对象序列化，如果没有实现Serializable接口，则会抛出异常。
所有属性必须都是可序列化的，特别是当有些属性本身也是对象的时候，要尤其注意这一点。
网络中传递对象必须实现序列化。