AOP（Aspect-Oriented Programming，面向切面的编程），它是可以通过预编译方式和运行期动态代理实现在不修改源代码的情况下给程序动态统一添加功能的一种技术。它是一种新的方法论，它是对传统OOP编程的一种补充。
AD：AOP（Aspect-Oriented Programming，面向切面的编程），它是可以通过预编译方式和运行期动态代理实现在不修改源代码的情况下给程序动态统一添加功能的一种技术。它是一种新的方法论，它是对传统OOP编程的一种补充。
OOP是关注将需求功能划分为不同的并且相对独立，封装良好的类，并让它们有着属于自己的行为，依靠继承和多态等来定义彼此的关系；AOP是希望能够将通用需求功能从不相关的类当中分离出来，能够使得很多类共享一个行为，一旦发生变化，不必修改很多类，而只需要修改这个行为即可。
AOP是使用切面（aspect）将横切关注点模块化，OOP是使用类将状态和行为模块化。在OOP的世界中，程序都是通过类和接口组织的，使用它们实现程序的核心业务逻辑是十分合适。但是对于实现横切关注点（跨越应用程序多个模块的功能需求）则十分吃力，比如日志记录，验证。
```java  
/*计算器接口*/ 
public interface Calculator  
{  
    public double add(double num1, double num2) throws Exception;  
    public double sub(double num1, double num2) throws Exception;  
    public double div(double num1, double num2) throws Exception;  
    public double mul(double num1, double num2) throws Exception;  
} 
/*计算器接口的实现类*/ 
public class ArithmeticCalculator implements Calculator  
{  
    @Override 
    public double add(double num1, double num2)  
    {  
        double result = num1 + num2;  
        return result;  
    }  
 
    @Override 
    public double sub(double num1, double num2)  
    {  
        double result = num1 - num2;  
        return result;  
    }  
 
    /*示意代码 暂时不考虑除数0的情况*/ 
    @Override 
    public double div(double num1, double num2)  
    {  
        double result = num1 / num2;  
        return result;  
    }  
 
    @Override 
    public double mul(double num1, double num2)  
    {  
        double result = num1 * num2;  
        return result;  
    }  
} 
```
大多数应用程序都有一个通用的需求，即在程序运行期间追踪正在发生的活动。为了给计算机添加日志功能，ArithmeticCalculator类改变如下：
```java  
/*计算器接口的实现类,添加记录日志功能*/ 
public class ArithmeticCalculator implements Calculator  
{  
    @Override 
    public double add(double num1, double num2)  
    {  
        System.out.println("the method [add()]"+"begin with args ("+num1+","+num2+")");  
        double result = num1 + num2;  
        System.out.println("the method [add()]"+"end with result ("+result+")");  
          
        return result;  
    }  
 
    @Override 
    public double sub(double num1, double num2)  
    {  
        System.out.println("the method [sub()]"+"begin with args ("+num1+","+num2+")");  
        double result = num1 - num2;  
        System.out.println("the method [sub()]"+"end with result ("+result+")");  
          
        return result;  
    }  
 
    /*示意代码 暂时不考虑除数0的情况*/ 
    @Override 
    public double div(double num1, double num2)  
    {  
        System.out.println("the method [div()]"+"begin with args ("+num1+","+num2+")");  
        double result = num1 / num2;  
        System.out.println("the method [div()]"+"end with result ("+result+")");  
          
        return result;  
    }  
 
    @Override 
    public double mul(double num1, double num2)  
    {  
        System.out.println("the method [mul()]"+"begin with args ("+num1+","+num2+")");  
        double result = num1 * num2;  
        System.out.println("the method [mul()]"+"end with result ("+result+")");  
          
        return result;  
    }  
} 
```
若ArithmeticCalculator规定只能计算正数时，又需要添加参数验证方法：
```java  
/*计算器接口的实现类,添加记录日志功能*/ 
public class ArithmeticCalculator implements Calculator  
{  
    @Override 
    public double add(double num1, double num2) throws Exception  
    {  
        this.argsValidatior(num1);  
        this.argsValidatior(num2);  
          
         /*同上*/ 
    }  
 
    @Override 
    public double sub(double num1, double num2) throws Exception  
    {  
        this.argsValidatior(num1);  
        this.argsValidatior(num2);  
          
         /*同上*/ 
    }  
 
    /*示意代码 暂时不考虑除数0的情况*/ 
    @Override 
    public double div(double num1, double num2) throws Exception  
    {  
        this.argsValidatior(num1);  
        this.argsValidatior(num2);  
          
         /*同上*/ 
    }  
 
    @Override 
    public double mul(double num1, double num2) throws Exception  
    {  
        this.argsValidatior(num1);  
        this.argsValidatior(num2);  
          
        /*同上*/ 
    }  
      
    private void argsValidatior(double arg)throws Exception  
    {  
        if(arg < 0)  
            throw new Exception("参数不能为负数");  
    }  
} 
```
上面的程序一个很直观的特点就是，好多重复的代码，并且当加入越来越多的非业务需求（例如日志记录和参数验证），原有的计算器方法变得膨胀冗长。这里有一件非常痛苦的事情，无法使用原有的编程方式将他们模块化，从核心业务中提取出来。例如日志记录和参数验证，AOP里将他们称为横切关注点（crosscutting concern），它们属于系统范围的需求通常需要跨越多个模块。
在使用传统的面向对象的编程方式无法理想化的模块化横切关注点，程序员不能不做的就是将这些横切关注点放置在每一个模块里与核心逻辑交织在一起，这将会导致横切关注点在每一个模块里到处存在。使用非模块化的手段实现横切关注将会导致，代码混乱，代码分散，代码重复。你想想看如果日志记录需要换一种显示方式，那你要改多少代码，一旦漏掉一处（概率很高），将会导致日志记录不一致。这样的代码很维护。种种原因表明，模块只需要关注自己原本的功能需求，需要一种方式来将横切关注点冲模块中提取出来。
忍无可忍的大牛们提出了AOP，它是一个概念，一个规范，本身并没有设定具体语言的实现，也正是这个特性让它变的非常流行，现在已经有许多开源的AOP实现框架了。本次不是介绍这些框架的，我们将不使用这些框架，而是使用底层编码的方式实现最基本的AOP解决上面例子出现的问题。AOP实际是GoF设计模式的延续，设计模式孜孜不倦追求的是调用者和被调用者之间的解耦，AOP可以说也是这种目标的一种实现。AOP可以使用"代理模式"来实现。
  
代理模式的原理是使用一个代理将对象包装起来，然后用该代理对象取代原始的对象，任何对原始对象的调用首先要经过代理。代理对象负责决定是否以及何时将方法调用信息转发到原始对象上。与此同时，围绕着每个方法的调用，代理对象也可以执行一些额外的工作。可以看出代理模式非常适合实现横切关注点。
由于本人只了解Java，所以姑且认为代理模式有两种实现方式，一种是静态代理、另一种是动态代理。他们的区别在于编译时知不知道代理的对象是谁。在模块比较多的系统中，静态代理是不合适也非常低效的，因为静态代理需要专门为每一个接口设计一个代理类，系统比较大成百上千的接口是很正常的，静态代理模式太消耗人力了。动态代理是JDK所支持的代理模式，它可以非常好的实现横切关注点。
```java  
/*使用动态代理需要实现InvocationHandler接口*/ 
public class ArithmeticCalculatorInvocationHandler implements InvocationHandler  
{  
    /*要代理的对象，动态代理只有在运行时才知道代理谁，所以定义为Object类型，可以代理任意对象*/ 
    private Object target = null;  
      
    /*通过构造函数传入原对象*/ 
    public ArithmeticCalculatorInvocationHandler(Object target)  
    {  
        this.target = target;  
    }  
 
    /*InvocationHandler接口的方法，proxy表示代理，method表示原对象被调用的方法，args表示方法的参数*/ 
    @Override 
    public Object invoke(Object proxy, Method method, Object[] args)  
            throws Throwable  
    {  
        /*原对象方法调用前处理日志信息*/ 
        System.out.println("the method ["+method.getName()+"]"+"begin with args ("+Arrays.toString(args)+")");  
          
        Object result = method.invoke(this.target, args);  
          
        /*原对象方法调用后处理日志信息*/ 
        System.out.println("the method ["+method.getName()+"]"+"end with result ("+result+")");  
          
        return result;  
    }  
      
    /*获取代理类*/ 
    public Object getProxy()  
    {  
        return Proxy.newProxyInstance(this.target.getClass().getClassLoader(), this.getClass().getInterfaces(), this);  
    }  
} 
```
场景类调用：
```java  
public class Client  
{  
    public static void main(String[] args) throws Exception  
    {  
        /*获得代理*/ 
        Calculator arithmeticCalculatorProxy = (Calculator)new ArithmeticCalculatorInvocationHandler(  
                 new ArithmeticCalculator()).getProxy();  
 
        /*调用add方法*/ 
        arithmeticCalculatorProxy.add(10, 10);  
    }  
} 
```
控制台的输出：
```java  
the method [add]begin with args ([10.0, 10.0])  
the method [add]end with result (20.0) 
```
可以看到使用动态代理实现了横切关注点。
  
若需要添加参数验证功能，只需要再创建一个参数验证代理即可：
```java  
public class ArithmeticCalculatorArgsInvocationHandler implements 
        InvocationHandler  
{  
    /*要代理的对象，动态代理只有在运行时才知道代理谁，所以定义为Object类型，可以代理任意对象*/ 
    private Object target = null;  
      
    /*通过构造函数传入原对象*/ 
    public ArithmeticCalculatorArgsInvocationHandler(Object target)  
    {  
        this.target = target;  
    }  
 
    /*InvocationHandler接口的方法，proxy表示代理，method表示原对象被调用的方法，args表示方法的参数*/ 
    @Override 
    public Object invoke(Object proxy, Method method, Object[] args)  
            throws Throwable  
    {  
        System.out.println("begin valid method ["+method.getName()+"] with args "+Arrays.toString(args));  
          
        for(Object arg : args)  
        {  
            this.argValidtor((Double)arg);  
        }  
          
        Object result = method.invoke(this.target, args);  
          
        return result;  
    }  
      
    /*获取代理类*/ 
    public Object getProxy()  
    {  
        return Proxy.newProxyInstance(this.target.getClass().getClassLoader(), this.target.getClass().getInterfaces(), this);  
    }  
      
    private void argValidtor(double arg) throws Exception  
    {  
        if(arg < 0)  
            throw new Exception("参数不能为负数！");  
    }  
} 
```
场景类调用：
```java  
public class Client  
{  
    public static void main(String[] args) throws Exception  
    {  
        /*获得代理*/ 
        Calculator arithmeticCalculatorProxy = (Calculator)new ArithmeticCalculatorInvocationHandler(  
                 new ArithmeticCalculator()).getProxy();  
          
        Calculator argValidatorProxy = (Calculator)new ArithmeticCalculatorArgsInvocationHandler(arithmeticCalculatorProxy).getProxy();  
 
        /*调用add方法*/ 
        argValidatorProxy.add(10, 10);  
    }  
} 
```
控制台输出：
```java  
begin valid method [add] with args [10.0, 10.0]  
the method [add]begin with args ([10.0, 10.0])  
the method [add]end with result (20.0) 
```
输入一个负数数据：
```java  
public class Client  
{  
    public static void main(String[] args) throws Exception  
    {  
        /*获得代理*/ 
        Calculator arithmeticCalculatorProxy = (Calculator)new ArithmeticCalculatorInvocationHandler(  
                 new ArithmeticCalculator()).getProxy();  
          
        Calculator argValidatorProxy = (Calculator)new ArithmeticCalculatorArgsInvocationHandler(arithmeticCalculatorProxy).getProxy();  
 
        /*调用add方法*/ 
        argValidatorProxy.add(-10, 10);  
    }  
} 
```
控制台输出：
```java  
begin valid method [add] with args [-10.0, 10.0]  
Exception in thread "main" java.lang.Exception: 参数不能为负数！  
    at com.beliefbetrayal.aop.ArithmeticCalculatorArgsInvocationHandler.argValidtor(ArithmeticCalculatorArgsInvocationHandler.java:46)  
    at com.beliefbetrayal.aop.ArithmeticCalculatorArgsInvocationHandler.invoke(ArithmeticCalculatorArgsInvocationHandler.java:29)  
    at $Proxy0.add(Unknown Source)  
    at com.beliefbetrayal.aop.Client.main(
Client.java:14)
```
  
不知道你有没有使用过Struts2，这个结构和Struts2的拦截器非常相似，一个个Action对象好比我们的原对象业务核心，一个个拦截器好比是这里的代理，通用的功能实现成拦截器，让Action可以共用，Struts2的拦截器也是AOP的优秀实现。