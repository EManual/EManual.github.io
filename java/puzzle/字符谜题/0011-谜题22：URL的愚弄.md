本谜题利用了Java编程语言中一个很少被人了解的特性。请考虑下面的程序将会做些什么？ 
```java    
public class BrowserTest {
    public static void main(String[] args) {
        System.out.print("iexplore:");
        http://www.google.com;
        System.out.println(":maximize");
    }
}
```
这是一个有点诡异的问题。该程序将不会做任何特殊的事情，而是直接打印iexplore::maximize。在程序中间出现的URL是一个语句标号（statement label）[JLS 14.7]后面跟着一行行尾注释（end-of-line comment）[JLS 3.7]。在Java中很少需要标号，这多亏了Java没有goto语句。在本谜题中所引用的“Java编程语言中很少被人了解的特性”实际上就是你可以在任何语句前面放置标号。这个程序标注了一个表达式语句，它是合法的，但是却没什么用处。 
它的价值所在，就是提醒你，如果你真的想要使用标号，那么应该用一种更合理的方式来格式化程序： 
```java    
public class BrowserTest {
    public static void main(String[] args) {
        System.out.print("iexplore:");
    http:      //www.google.com;
        System.out.println(":maximize");
    }
}
```
这就是说，我们没有任何可能的理由去使用与程序没有任何关系的标号和注释。 
本谜题的教训是：令人误解的注释和无关的代码会引起混乱。要仔细地写注释，并让它们跟上时代；要切除那些已遭废弃的代码。还有就是如果某些东西看起来过于奇怪，以至于不像对的，那么它极有可能就是错的。