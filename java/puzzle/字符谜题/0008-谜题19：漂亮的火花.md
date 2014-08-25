下面的程序用一个方法对字符进行了分类。这个程序会打印出什么呢？ 
```java   
public class Classifier {
    public static void main(String[] args) {
        System.out.println(
             classify(‘n’) + classify(‘+’) + classify(‘2’));
    }
    static String classify(char ch) {
        if ("0123456789".indexOf(ch) >= 0)
             return "NUMERAL ";
        if ("abcdefghijklmnopqrstuvwxyz".indexOf(ch) >= 0)
             return "LETTER ";
        /* (Operators not supported yet)
            if ("+-*/&|!=" >= 0)
                 return "OPERATOR ";
        */
        return "UNKNOWN";
    }
}
```
如果你猜想该程序将打印LETTER UNKNOWN NUMERAL，那么你就掉进陷阱里面了。这个程序连编译都通不过。让我们再看一看相关的部分，这一次我们用粗体字突出注释部分： 
```java   
if ("abcdefghijklmnopqrstuvwxyz".indexOf(ch) >= 0)
             return "LETTER ";
        /* (Operators not supported yet)
        if ("+-*/&|!=" >= 0)
                 return "OPERATOR ";
        */
        return "UNKNOWN";
    }
}
```
正如你之所见，注释在包含了字符*/的字符串内部就结束了，结果使得程序在语法上变成非法的了。我们将程序中的一部分注释出来的尝试之所以失败了，是因为字符串字面常量在注释中没有被特殊处理。 
更一般地讲，注释内部的文本没有以任何方式进行特殊处理[JLS 3.7]。因此，块注释不能嵌套。请考虑下面的代码段： 
```java   
/* Add the numbers from 1 to n */
int sum = 0;
for (int i = 1; I <= n; i++)
sum += i;
```
现在假设我们要将该代码段注释成为一个块注释，我们再次用粗体字突出整个注释： 
```java   
/*
/* Add the numbers from 1 to n */
int sum = 0;
for (int i = 1; I <= n; i++)
sum += i;
*/
```
正如你之所见，我们没有能够将最初的代码段注释掉。好在所产生的代码包含了一个语法错误，因此编译器将会告诉我们代码存在着问题。 
你可能偶尔看到过这样的代码段，它被一个布尔表达式为常量false的if语句禁用了： 
```java   
//code commented out with an if statement - doesn‘t always work!
if (false) {
     /* Add the numbers from 1 to n */
     int sum = 0;
     for (int i = 1; i <= n; i++)
            sum += i;
}
```
语言规范建议将这种方式作为一种条件编译技术[JLS 14.21]，但是它不适合用来注释代码。除非要被禁用的代码是一个合法的语句序列，否则就不要使用这项技术。 
注释掉一个代码段的最好的方式是使用单行的注释序列。大多数IDE工具都可以自动化这个过程： 
```java   
//code commented out with an if statement - doesn’t always work!
//     /* Add the numbers from 1 to n */
//     int sum = 0;
//     for (int i = 1; i <= n; i++)
//            sum += i;
```
总之，块注释不能可靠地注释掉代码段，应该用单行的注释序列来代替。对语言设计者来说，应该注意到可嵌套的块注释并不是一个好主意。他们强制编译器去解析块注释内部的文本，而由此引发的问题比它能够解决的问题还要多。