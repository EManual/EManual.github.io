* 一致资源定位器URL
URL(Uniform Resource Locator)是一致资源定位器的简称，它表示Internet上某一资源的地址。通过URL我们可以访问Internet上的各种网络资源，比如最常见的WWW，FTP站点。浏览器通过解析给定的URL可以在网络上查找相应的文件或其他资源。
* URL的组成
protocol://resourceName
协议名（protocol）指明获取资源所使用的传输协议，如http、ftp、gopher、file等，资源名（resourceName）则应该是资源的完整地址，包括主机名、端口号、文件名或文件内部的一个引用。例如：
```java  
http://www.sun.com/ 协议名://主机名
http://home.netscape.com/home/welcome.html 协议名://机器名＋文件名
http://www.gamelan.com:80/Gamelan/network.html#BOTTOM 协议名://机器名＋端口号＋文件名＋内部引用。
```
* 创建一个URL
为了表示URL， java.net中实现了类URL。我们可以通过下面的构造方法来初始化一个URL对象：
（1） public URL (String spec);
通过一个表示URL地址的字符串可以构造一个URL对象。
```java  
URL urlBase=new URL("http://www. 263.net/") 
```
（2） public URL(URL context, String spec);
通过基URL和相对URL构造一个URL对象。
```java  
URL net263=new URL ("http://www.263.net/");
URL index263=new URL(net263, "index.html")
```
（3） public URL(String protocol, String host, String file);
```java  
new URL("http", "www.gamelan.com", "/pages/Gamelan.net. html");
```
（4） public URL(String protocol, String host, int port, String file);
```java  
URL gamelan=new URL("http", "www.gamelan.com", 80, "Pages/Gamelan.network.html");
```
注意：类URL的构造方法都声明抛弃非运行时例外（MalformedURLException），因此生成URL对象时，我们必须要对这一例外进行处理，通常是用try-catch语句进行捕获。格式如下：
```java  
	try{
　　　	URL myURL= new URL(…)
　　}catch (MalformedURLException e){
　　…　　}
```
* 解析一个URL
一个URL对象生成后，其属性是不能被改变的，但是我们可以通过类URL所提供的方法来获取这些属性：
```java  
public String getProtocol() 获取该URL的协议名。
public String getHost() 获取该URL的主机名。
public int getPort() 获取该URL的端口号，如果没有设置端口，返回-1。
public String getFile() 获取该URL的文件名。
public String getRef() 获取该URL在文件中的相对位置。
public String getQuery() 获取该URL的查询信息。
public String getPath() 获取该URL的路径。
public String getAuthority() 获取该URL的权限信息。
public String getUserInfo() 获得使用者的信息。
public String getRef() 获得该URL的锚。
```
* 从URL读取WWW网络资源
当我们得到一个URL对象后，就可以通过它读取指定的WWW资源。这时我们将使用URL的方法openStream()，其定义为：
```java  
InputStream openStream();
```
方法openSteam()与指定的URL建立连接并返回InputStream类的对象以从这一连接中读取数据。
```java  
public class URLReader {
　　public static void main(String[] args) throws Exception { 
　　　　　　　　　　　　　　　　　　　　　　//声明抛出所有例外
　　　　URL tirc = new URL("http://www.tirc1.cs.tsinghua.edu.cn/"); 
　　　　　　　　　　　　　　　　　　　　　　//构建一URL对象
　　　　BufferedReader in = new BufferedReader(new InputStreamReader(tirc.openStream()));
　　　　//使用openStream得到一输入流并由此构造一个BufferedReader对象
　　　　String inputLine;
　　　　while ((inputLine = in.readLine()) != null) 
　　　　　　　　　　　　　　　　　//从输入流不断的读数据，直到读完为止
　　　　　　　System.out.println(inputLine); //把读入的数据打印到屏幕上
　　　　in.close(); //关闭输入流
　　}
}
```
* 通过URLConnetction连接WWW
通过URL的方法openStream()，我们只能从网络上读取数据，如果我们同时还想输出数据，例如向服务器端的CGI程序发送一些数据，我们必须先与URL建立连接，然后才能对其进行读写，这时就要用到类URLConnection了。CGI是公共网关接口（Common Gateway Interface）的简称，它是用户浏览器和服务器端的应用程序进行连接的接口，有关CGI程序设计，请读者参考有关书籍。
类URLConnection也在包java.net中定义，它表示Java程序和URL在网络上的通信连接。当与一个URL建立连接时，首先要在一个URL对象上通过方法openConnection()生成对应的URLConnection对象。例如下面的程序段首先生成一个指向地址http://edu.chinaren.com/index.shtml的对象，然后用openConnection（）打开该URL对象上的一个连接，返回一个URLConnection对象。如果连接过程失败，将产生IOException.
```java  
　　Try{
　　　　URL netchinaren = new URL ("http://edu.chinaren.com/index.shtml");
　　　　URLConnectonn tc = netchinaren.openConnection();
　　}catch(MalformedURLException e){ //创建URL()对象失败
　　…
　　}catch (IOException e){ //openConnection()失败
　　…
　　}
```
类URLConnection提供了很多方法来设置或获取连接参数，程序设计时最常使用的是getInputStream()和getOurputStream(),其定义为：
```java  
InputSteram getInputSteram();
OutputSteram getOutputStream();
```
通过返回的输入/输出流我们可以与远程对象进行通信。看下面的例子：
```java  
　　URL url =new URL ("http://www.javasoft.com/cgi-bin/backwards"); 
　　//创建一URL对象
　　URLConnectin con=url.openConnection(); 
　　//由URL对象获取URLConnection对象
　　DataInputStream dis=new DataInputStream (con.getInputSteam()); 
　　//由URLConnection获取输入流，并构造DataInputStream对象
　　PrintStream ps=new PrintSteam(con.getOutupSteam());
　　//由URLConnection获取输出流，并构造PrintStream对象
　　String line=dis.readLine(); //从服务器读入一行
　　ps.println("client…"); //向服务器写出字符串 "client…"
```
其中backwards为服务器端的CGI程序。实际上，类URL的方法openSteam（）是通过URLConnection来实现的。它等价于
```java  
openConnection().getInputStream();
```
基于URL的网络编程在底层其实还是基于下面要讲的Socket接口的。WWW，FTP等标准化的网络服务都是基于TCP协议的，所以本质上讲URL编程也是基于TCP的一种应用。