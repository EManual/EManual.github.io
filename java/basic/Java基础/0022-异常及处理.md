一、异常的定义
在《java编程思想》中这样定义 异常：阻止当前方法或作用域继续执行的问题。虽然java中有异常处理机制，但是要明确一点，决不应该用"正常"的态度来看待异常。绝对一点说异常就是某种意义上的错误，就是问题，它可能会导致程序失败。之所以java要提出异常处理机制，就是要告诉开发人员，你的程序出现了不正常的情况，请注意。
记得当初学习java的时候，异常总是搞不太清楚，不知道这个异常是什么意思，为什么会有这个机制？但是随着知识的积累逐渐也对异常有一点感觉了。举一个例子来说明一下异常的用途。
```java  
public class Calculator {
    public int devide(int num1, int num2) {
        //判断除数是否为0
        if(num2 == 0) {
            throw new IllegalArgumentException("除数不能为零");
        }              return num1/num2;
    }
}
```
看一下这个类中关于除运算的方法，如果你是新手你可能会直接返回计算结果，根本不去考虑什么参数是否正确，是否合法（当然可以原谅，谁都是这样过来的）。但是我们应尽可能的考虑周全，把可能导致程序失败的"苗头"扼杀在摇篮中，所以进行参数的合法性检查就很有必要了。其中执行参数检查抛出来的那个参数非法异常，这就属于这个方法的不正常情况。正常情况下我们会正确的使用计算器，但是不排除粗心大意把除数赋值为0。如果你之前没有考虑到这种情况，并且恰巧用户数学基础不好，那么你完了。但是如果你之前考虑到了这种情况，那么很显然错误已在你的掌控之中。
二、异常扫盲行动
今天和别人聊天时看到一个笑话：世界上最真情的相依，是你在try我在catch。无论你发神马脾气，我都默默承受，静静处理。 大多数新手对java异常的感觉就是：try...catch...。没错，这是用的最多的，也是最实用的。我的感觉就是：java异常是从"try...catch..."走来。
首先来熟悉一下java的异常体系：
Throwable 类是 Java 语言中所有错误或异常的超类（这就是一切皆可抛的东西）。它有两个子类：Error和Exception。
Error：用于指示合理的应用程序不应该试图捕获的严重问题。这种情况是很大的问题，大到你不能处理了，所以听之任之就行了，你不用管它。比如说VirtualMachineError：当Java虚拟机崩溃或用尽了它继续操作所需的资源时，抛出该错误。好吧，就算这个异常的存在了，那么应该何时，如何处理它呢？？交给JVM吧，没有比它更专业的了。
Exception：它指出了合理的应用程序想要捕获的条件。Exception又分为两类：一种是CheckedException，一种是UncheckedException。这两种Exception的区别主要是CheckedException需要用try...catch...显示的捕获，而UncheckedException不需要捕获。通常UncheckedException又叫做RuntimeException。《effective java》指出：对于可恢复的条件使用被检查的异常（CheckedException），对于程序错误（言外之意不可恢复，大错已经酿成）使用运行时异常（RuntimeException）。
我们常见的RuntimeExcepiton有IllegalArgumentException、IllegalStateException、NullPointerException、IndexOutOfBoundsException等等。对于那些CheckedException就不胜枚举了，我们在编写程序过程中try...catch...捕捉的异常都是CheckedException。io包中的IOException及其子类，这些都是CheckedException。
三、异常的使用
在异常的使用这一部分主要是演示代码，都是我们平常写代码的过程中会遇到的（当然只是一小部分），抛砖引玉吗！
例1. 这个例子主要通过两个方法对比来演示一下有了异常以后代码的执行流程。 
```java  
public static void testException1() {
        int[] ints = new int[] { 1, 2, 3, 4 };
        System.out.println("异常出现前");
        try {
            System.out.println(ints[4]);
            System.out.println("我还有幸执行到吗");// 发生异常以后，后面的代码不能被执行
        } catch (IndexOutOfBoundsException e) {
            System.out.println("数组越界错误");
        }
        System.out.println("异常出现后");
    }
    /*output:
    异常出现前
    数组越界错误
    4
    异常出现后
    */
public static void testException2() {
        int[] ints = new int[] { 1, 2, 3, 4 };
        System.out.println("异常出现前");
        System.out.println(ints[4]);
        System.out.println("我还有幸执行到吗");// 发生异常以后，他后面的代码不能被执行
    }
```
首先指出例子中的不足之处，IndexOutofBoundsException是一个非受检异常，所以不用try...catch...显示捕捉，但是我的目的是对同一个异常用不同的处理方式，看它会有什么不同的而结果（这里也就只能用它将就一下了）。异常出现时第一个方法只是跳出了try块，但是它后面的代码会照样执行的。但是第二种就不一样了直接跳出了方法，比较强硬。从第一个方法中我们看到，try...catch...是一种"事务性"的保障，它的目的是保证程序在异常的情况下运行完毕，同时它还会告知程序员程序中出错的详细信息（这种详细信息有时要依赖于程序员设计）。
例2. 重新抛出异常
```java  
public class Rethrow {
    public static void readFile(String file) throws FileNotFoundException {
        try {
            BufferedInputStream in = new BufferedInputStream(new FileInputStream(file));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.err.println("不知道如何处理该异常或者根本不想处理它，但是不做处理又不合适，这是重新抛出异常交给上一级处理");
            //重新抛出异常
            throw e;
        }
    }    
    public static void printFile(String file) {
        try {
            readFile(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }   
    public static void main(String[] args) {
        printFile("D:/file");
    }
}
```
异常的本意是好的，让我们试图修复程序，但是现实中我们修复的几率很小，我们很多时候就是用它来记录出错的信息。如果你厌倦了不停的处理异常，重新抛出异常对你来说可能是一个很好的解脱。原封不动的把这个异常抛给上一级，抛给调用这个方法的人，让他来费脑筋吧。这样看来，java异常（当然指的是受检异常）又给我们平添很多麻烦，尽管它的出发点是好的。
例3. 异常链的使用及异常丢失
定义三个异常类：ExceptionA,ExceptionB,ExceptionC
```java  
public class ExceptionA extends Exception {
    public ExceptionA(String str) {
        super();
    }
}
 
public class ExceptionB extends ExceptionA {
 
    public ExceptionB(String str) {
        super(str);
    }
}
public class ExceptionC extends ExceptionA {
    public ExceptionC(String str) {
        super(str);
    }
}
```
异常丢失的情况：
```java  
public class NeverCaught {
    static void f() throws ExceptionB{
        throw new ExceptionB("exception b");
    }
    static void g() throws ExceptionC {
        try {
            f();
        } catch (ExceptionB e) {
            ExceptionC c = new ExceptionC("exception a");
            throw c;
        }
    }
 
    public static void main(String[] args) {
            try {
                g();
            } catch (ExceptionC e) {
                e.printStackTrace();
            }
    }
}
/*  exception.ExceptionC   at exception.NeverCaught.g(NeverCaught.java:12)    at exception.NeverCaught.main(NeverCaught.java:19)    */  
```
为什么只是打印出来了ExceptionC而没有打印出ExceptionB呢？这个还是自己分析一下吧！
上面的情况相当于少了一种异常，这在我们排错的过程中非常的不利。那我们遇到上面的情况应该怎么办呢？这就是异常链的用武之地：保存异常信息，在抛出另外一个异常的同时不丢失原来的异常。
```java  
public class NeverCaught {
    static void f() throws ExceptionB{
        throw new ExceptionB("exception b");
    }
    static void g() throws ExceptionC {
        try {
            f();
        } catch (ExceptionB e) {
            ExceptionC c = new ExceptionC("exception a");
            //异常 
            c.initCause(e);
            throw c;
        }
    }
    public static void main(String[] args) {
            try {
                g();
            } catch (ExceptionC e) {
                e.printStackTrace();
            }
    }
}
/*
exception.ExceptionC
at exception.NeverCaught.g(NeverCaught.java:12)
at exception.NeverCaught.main(NeverCaught.java:21)
Caused by: exception.ExceptionB
at exception.NeverCaught.f(NeverCaught.java:5)
at exception.NeverCaught.g(NeverCaught.java:10)
... 1 more
*/
```
这个异常链的特性是所有异常均具备的，因为这个initCause()方法是从Throwable继承的。
例4. 清理工作
清理工作对于我们来说是必不可少的，因为如果一些消耗资源的操作，比如IO,JDBC。如果我们用完以后没有及时正确的关闭，那后果会很严重，这意味着内存泄露。异常的出现要求我们必须设计一种机制不论什么情况下，资源都能及时正确的清理。这就是finally。
```java  
public void readFile(String file) {
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new InputStreamReader(
                    new FileInputStream(file)));
            // do some other work
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
```
例子非常的简单，是一个读取文件的例子。这样的例子在JDBC操作中也非常的常见。（所以，我觉得对于资源的及时正确清理是一个程序员的基本素质之一。）
Try...finally结构也是保证资源正确关闭的一个手段。如果你不清楚代码执行过程中会发生什么异常情况会导致资源不能得到清理，那么你就用try对这段"可疑"代码进行包装，然后在finally中进行资源的清理。举一个例子：
```java  
public void readFile() {
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new InputStreamReader(
                    new FileInputStream("file")));
            // do some other work
            //close reader
            reader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } 
    }
```
我们注意一下这个方法和上一个方法的区别，下一个人可能习惯更好一点，及早的关闭reader。但是往往事与愿违，因为在reader.close()以前异常随时可能发生，这样的代码结构不能预防任何异常的出现。因为程序会在异常出现的地方跳出，后面的代码不能执行（这在上面应经用实例证明过）。这时我们就可以用try...finally来改造：
```java  
public void readFile() {
        BufferedReader reader = null;
        try {
            try {
                reader = new BufferedReader(new InputStreamReader(
                        new FileInputStream("file")));
                // do some other work
                // close reader
            } finally {
                reader.close();            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
```
及早的关闭资源是一种良好的行为，因为时间越长你忘记关闭的可能性越大。这样在配合上try...finally就保证万无一失了(不要嫌麻烦，java就是这么中规中矩)。
再说一种情况，假如我想在构造方法中打开一个文件或者创建一个JDBC连接，因为我们要在其他的方法中使用这个资源，所以不能在构造方法中及早的将这个资源关闭。那我们是不是就没辙了呢？答案是否定的。看一下下面的例子：
```java  
public class ResourceInConstructor {
    BufferedReader reader = null;
    public ResourceInConstructor() {
        try {
            reader = new BufferedReader(new InputStreamReader(new FileInputStream("")));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    public void readFile() {
        try {
            while(reader.readLine()!=null) {
                //do some work
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }    
    public void dispose() {
        try {
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
这一部分讲的多了一点，但是异常确实是看起来容易用起来难的东西呀，java中还是有好多的东西需要深挖的。
四、异常的误用
对于异常的误用着实很常见，上一部分中已经列举了几个，大家仔细的看一下。下面再说两个其他的。
例1. 用一个Exception来捕捉所有的异常，颇有"一夫当关万夫莫开"的气魄。不过这也是最傻的行为。
```java  
public void readFile(String file) {
        BufferedReader reader = null;
        Connection conn = null;
        try {
            reader = new BufferedReader(new InputStreamReader(
                    new FileInputStream(file)));
            // do some other work                conn = DriverManager.getConnection("");
            //...
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
                conn.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
```
从异常角度来说这样严格的程序确实是万无一失，所有的异常都能捕获。但是站在编程人员的角度，万一这个程序出错了我们该如何分辨是到底是那引起的呢，IO还是JDBC...所以，这种写法很值得当做一个反例。大家不要以为这种做法很幼稚，傻子才会做。我在公司实习时确实看见了类似的情况：只不过是人家没有用Exception而是用了Throwable。
例2. 这里就不举例子了，上面的程序都是反例。异常是程序处理意外情况的机制，当程序发生意外时，我们需要尽可能多的得到意外的信息，包括发生的位置，描述，原因等等。这些都是我们解决问题的线索。但是上面的例子都只是简单的printStackTrace()。如果我们自己写代码，就要尽可能多的对这个异常进行描述。比如说为什么会出现这个异常，什么情况下会发生这个异常。如果传入方法的参数不正确，告知什么样的参数是合法的参数，或者给出一个sample。
例3. 将try block写的简短，不要所有的东西都扔在这里，我们尽可能的分析出到底哪几行程序可能出现异常，只是对可能出现异常的代码进行try。尽量为每一个异常写一个try...catch，避免异常丢失。在IO操作中，一个IOException也具有"一夫当关万夫莫开"的气魄。
五、总结
总结非常简单，不要为了使用异常而使用异常。异常是程序设计的一部分，对它的设计也要考究点。