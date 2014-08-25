下面的程序被设计用来打印它的类文件的名称。如果你不熟悉类字面常量，那么我告诉你Me.class.getName()将返回Me类完整的名称，即“com.javapuzzlers.Me”。那么，这个程序会打印出什么呢？ 
```java   
package com.javapuzzlers;
public class Me {
    public static void main(String[] args){
        System.out.println(
             Me.class.getName().
                replaceAll(".","/") + ".class");
    }
}
```
该程序看起来会获得它的类名（“com.javapuzzlers.Me”），然后用“/”替换掉所有出现的字符串“.”，并在末尾追加字符串“.class”。你可能会认为该程序将打印com/javapuzzlers/Me.class，该程序正式从这个类文件中被加载的。如果你运行这个程序，就会发现它实际上打印的是///////////////////.class。到底怎么回事？难道我们是斜杠的受害者吗？ 
问题在于String.replaceAll接受了一个正则表达式作为它的第一个参数，而并非接受了一个字符序列字面常量。（正则表达式已经被添加到了Java平台的1.4版本中。）正则表达式“.”可以匹配任何单个的字符，因此，类名中的每一个字符都被替换成了一个斜杠，进而产生了我们看到的输出。 
要想只匹配句点符号，在正则表达式中的句点必须在其前面添加一个反斜杠（\）进行转义。因为反斜杠字符在字面含义的字符串中具有特殊的含义——它标识转义字符序列的开始——因此反斜杠自身必须用另一个反斜杠来转义，这样就可以产生一个转义字符序列，它可以在字面含义的字符串中生成一个反斜杠。把这些合在一起，就可以使下面的程序打印出我们所期望的com/javapuzzlers/Me.class： 
```java   
package com.javapuzzlers;
public class Me {
    public static void main(String[] args){
        System.out.println(
            Me.class.getName().replaceAll("\\.","/") + ".class");
    }
}
```
为了解决这类问题，5.0版本提供了新的静态方法java.util.regex.Pattern.quote。它接受一个字符串作为参数，并可以添加必需的转义字符，它将返回一个正则表达式字符串，该字符串将精确匹配输入的字符串。下面是使用该方法之后的程序： 
```java   
package com.javapuzzlers;
import java.util.regex.Pattern;
public class Me {
    public static void main(String[] args){
        System.out.println(Me.class.getName().
			replaceAll(Pattern.quote("."),"/") + ".class");
    }
}
```
该程序的另一个问题是：其正确的行为是与平台相关的。并不是所有的文件系统都使用斜杠符号来分隔层次结构的文件名组成部分的。要想获取一个你正在运行的平台上的有效文件名，你应该使用正确的平台相关的分隔符号来代替斜杠符号。这正是下一个谜题所要做的。