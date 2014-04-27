* Socket通讯
网络上的两个程序通过一个双向的通讯连接实现数据的交换，这个双向链路的一端称为一个Socket。Socket通常用来实现客户方和服务方的连接。Socket是TCP/IP协议的一个十分流行的编程界面，一个Socket由一个IP地址和一个端口号唯一确定。
在传统的UNIX环境下可以操作TCP/IP协议的接口不止Socket一个，Socket所支持的协议种类也不光TCP/IP一种，因此两者之间是没有必然联系的。在Java环境下，Socket编程主要是指基于TCP/IP协议的网络编程。
* Socket通讯的一般过程
使用Socket进行Client/Server程序设计的一般连接过程是这样的：Server端Listen(监听)某个端口是否有连接请求，Client端向Server端发出Connect(连接)请求，Server端向Client端发回Accept（接受）消息。一个连接就建立起来了。Server端和Client端都可以通过Send，Write等方法与对方通信。
对于一个功能齐全的Socket，都要包含以下基本结构，其工作过程包含以下四个基本的步骤：
（1） 创建Socket；
（2） 打开连接到Socket的输入/出流；
（3） 按照一定的协议对Socket进行读/写操作；
（4） 关闭Socket。
* 创建Socket
java在包java.net中提供了两个类Socket和ServerSocket，分别用来表示双向连接的客户端和服务端。这是两个封装得非常好的类，使用很方便。其构造方法如下：
```java  
Socket(InetAddress address, int port);
Socket(InetAddress address, int port, boolean stream);
Socket(String host, int prot);
Socket(String host, int prot, boolean stream);
Socket(SocketImpl impl)
Socket(String host, int port, InetAddress localAddr, int localPort)
Socket(InetAddress address, int port, InetAddress localAddr, int localPort)
ServerSocket(int port);
ServerSocket(int port, int backlog);
ServerSocket(int port, int backlog, InetAddress bindAddr).
```
其中address、host和port分别是双向连接中另一方的IP地址、主机名和端口号，stream指明socket是流socket还是数据报socket，localPort表示本地主机的端口号，localAddr和bindAddr是本地机器的地址（ServerSocket的主机地址），impl是socket的父类，既可以用来创建serverSocket又可以用来创建Socket。count则表示服务端所能支持的最大连接数。例如：
```java  
Socket client = new Socket("127.0.01.", 80);
ServerSocket server = new ServerSocket(80);
```
注意，在选择端口时，必须小心。每一个端口提供一种特定的服务，只有给出正确的端口，才能获得相应的服务。0~1023的端口号为系统所保留，例如http服务的端口号为80,telnet服务的端口号为21,ftp服务的端口号为23, 所以我们在选择端口号时，最好选择一个大于1023的数以防止发生冲突。
在创建socket时如果发生错误，将产生IOException，在程序中必须对之作出处理。所以在创建Socket或ServerSocket是必须捕获或抛出例外。
* 简单的Client/Server程序设计
下面我们给出一个用Socket实现的客户和服务器交互的典型的C/S结构的演示程序，读者通过仔细阅读该程序，会对前面所讨论的各个概念有更深刻的认识。程序的意义请参考注释。
1. 客户端程序
```java  
　　import java.io.*;
　　import java.net.*;
　　public class TalkClient {
　　　　public static void main(String args[]) {
　　　　　　try{
　　　　　　　　Socket socket=new Socket("127.0.0.1",4700); 
　　　　　　　　//向本机的4700端口发出客户请求
　　　　　　　　BufferedReader sin=new BufferedReader(new InputStreamReader(System.in));
　　　　　　　　//由系统标准输入设备构造BufferedReader对象
　　　　　　　　PrintWriter os=new PrintWriter(socket.getOutputStream());
　　　　　　　　//由Socket对象得到输出流，并构造PrintWriter对象
　　　　　　　　BufferedReader is=new BufferedReader(new InputStreamReader(socket.getInputStream()));
　　　　　　　　//由Socket对象得到输入流，并构造相应的BufferedReader对象
　　　　　　　　String readline;
　　　　　　　　readline=sin.readLine(); //从系统标准输入读入一字符串
　　　　　　　　while(!readline.equals("bye")){ 
　　　　　　　　//若从标准输入读入的字符串为 "bye"则停止循环
　　　　　　　　　　os.println(readline); 
　　　　　　　　　　//将从系统标准输入读入的字符串输出到Server
　　　　　　　　　　os.flush(); 
　　　　　　　　　　//刷新输出流，使Server马上收到该字符串
　　　　　　　　　　System.out.println("Client:"+readline); 
　　　　　　　　　　//在系统标准输出上打印读入的字符串
　　　　　　　　　　System.out.println("Server:"+is.readLine()); 
　　　　　　　　　　//从Server读入一字符串，并打印到标准输出上
　　　　　　　　　　readline=sin.readLine(); //从系统标准输入读入一字符串
　　　　　　　　} //继续循环
　　　　　　　　os.close(); //关闭Socket输出流
　　　　　　　　is.close(); //关闭Socket输入流
　　　　　　　　socket.close(); //关闭Socket
　　　　　　}catch(Exception e) {
　　　　　　　　System.out.println("Error"+e); //出错，则打印出错信息
　　　　　　}
　　}
}
```
2. 服务器端程序
```java  
　　import java.io.*;
　　import java.net.*;
　　import java.applet.Applet;
　　public class TalkServer{
　　　　public static void main(String args[]) {
　　　　　　try{
　　　　　　　　ServerSocket server=null;
　　　　　　　　try{ 
　　　　　　　　　　server=new ServerSocket(4700); 
　　　　　　　　//创建一个ServerSocket在端口4700监听客户请求
　　　　　　　　}catch(Exception e) {
　　　　　　　　　　System.out.println("can not listen to:"+e); 
　　　　　　　　//出错，打印出错信息
　　　　　　　　}
　　　　　　　　Socket socket=null;
　　　　　　　　try{
　　　　　　　　　　socket=server.accept(); 
　　　　　　　　　　//使用accept()阻塞等待客户请求，有客户
　　　　　　　　　　//请求到来则产生一个Socket对象，并继续执行
　　　　　　　　}catch(Exception e) {
　　　　　　　　　　System.out.println("Error."+e); 
　　　　　　　　　　//出错，打印出错信息
　　　　　　　　}
　　　　　　　　String line;
　　　　　　　　BufferedReader is=new BufferedReader(new InputStreamReader(socket.getInputStream()));
　　　　　　　　　//由Socket对象得到输入流，并构造相应的BufferedReader对象
　　　　　　　　PrintWriter os=newPrintWriter(socket.getOutputStream());
　　　　　　　　　//由Socket对象得到输出流，并构造PrintWriter对象
　　　　　　　　BufferedReader sin=new BufferedReader(new InputStreamReader(System.in));
　　　　　　　　　//由系统标准输入设备构造BufferedReader对象
　　　　　　　　System.out.println("Client:"+is.readLine()); 
　　　　　　　　//在标准输出上打印从客户端读入的字符串
　　　　　　　　line=sin.readLine(); 
　　　　　　　　//从标准输入读入一字符串
　　　　　　　　while(!line.equals("bye")){ 
　　　　　　　　//如果该字符串为 "bye"，则停止循环
　　　　　　　　　　os.println(line); 
　　　　　　　　　　//向客户端输出该字符串
　　　　　　　　　　os.flush(); 
　　　　　　　　　　//刷新输出流，使Client马上收到该字符串
　　　　　　　　　　System.out.println("Server:"+line); 
　　　　　　　　　　//在系统标准输出上打印读入的字符串
　　　　　　　　　　System.out.println("Client:"+is.readLine());
　　　　　　　　　　//从Client读入一字符串，并打印到标准输出上
　　　　　　　　　　line=sin.readLine(); 
　　　　　　　　　　//从系统标准输入读入一字符串
　　　　　　　　} 　//继续循环
　　　　　　　　os.close(); //关闭Socket输出流
　　　　　　　　is.close(); //关闭Socket输入流
　　　　　　　　socket.close(); //关闭Socket
　　　　　　　　server.close(); //关闭ServerSocket
　　　　　　}catch(Exception e){
　　　　　　　　System.out.println("Error:"+e); 
　　　　　　　　//出错，打印出错信息
　　　　　　}
　　　　}
　　}
```