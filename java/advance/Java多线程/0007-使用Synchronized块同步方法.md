synchronized关键字有两种用法。第一种就是在《使用Synchronized关键字同步类方法》一文中所介绍的直接用在方法的定义中。另外一种就是synchronized块。我们不仅可以通过synchronized块来同步一个对象变量。也可以使用synchronized块来同步类中的静态方法和非静态方法。
synchronized块的语法如下：
```java  
public void method()  
{  
    … …  
    synchronized(表达式)  
    {  
       … …  
    }  
} 
```
一、非静态类方法的同步    
从《使用Synchronized关键字同步类方法》一文中我们知道使用synchronized关键字来定义方法就会锁定类中所有使用synchronzied关键字定义的静态方法或非静态方法，但这并不好理解。而如果使用synchronized块来达到同样的效果，就不难理解为什么会产生这种效果了。如果想使用synchronized块来锁定类中所有的同步非静态方法，需要使用this做为synchronized块的参数传入synchronized块国，代码如下：
通过synchronized块同步非静态方法
```java  
public class SyncBlock  
{  
    public void method1()  
    {  
        synchronized(this)  // 相当于对method1方法使用synchronized关键字  
        {  
          … …  
		}  
	}  
	public void method2()  
	{  
		synchronized(this)  // 相当于对method2方法使用synchronized关键字  
		{  
			… …  
		}  
	}  
	public synchronized void method3()    
	{  
		… …  
	}  
} 
```
在上面的代码中的method1和method2方法中使用了synchronized块。而第017行的method3方法仍然使用synchronized关键字来定义方法。在使用同一个SyncBlock类实例时，这三个方法只要有一个正在执行，其他两个方法就会因未获得同步锁而被阻塞。在使用synchronized块时要想达到和synchronized关键字同样的效果，必须将所有的代码都写在synchronized块中，否则，将无法使当前方法中的所有代码和其他的方法同步。
除了使用this做为synchronized块的参数外，还可以使用SyncBlock.this作为synchronized块的参数来达到同样的效果。
在内部类（InnerClass）的方法中使用synchronized块来时，this只表示内类，和外类(OuterClass)没有关系。但内类的非静态方法可以和外类的非静态方法同步。如在内类InnerClass中加一个method4方法，并使method4方法和SyncBlock的三个方法同步，代码如下：
使内类的非静态方法和外类的非静态方法同步 
```java  
public class SyncBlock  
{  
    … …  
    class InnerClass  
    {  
        public void method4()  
        {  
            synchronized(SyncBlock.this)  
            {  
                … …   
            }  
        }  
    }  
    … …  
} 
```
在上面SyncBlock类的新版本中，InnerClass类的method4方法和SyncBlock类的其他三个方法同步，因此，method1、method2、method3和method4四个方法在同一时间只能有一个方法执行。
Synchronized块不管是正常执行完，还是因为程序出错而异常退出synchronized块，当前的synchronized块所持有的同步锁都会自动释放。
因此，在使用synchronized块时不必担心同步锁的释放问题。
二、静态类方法的同步
由于在调用静态方法时，对象实例不一定被创建。因此，就不能使用this来同步静态方法，而必须使用Class对象来同步静态方法。代码如下：
通过synchronized块同步静态方法 
```java  
public class StaticSyncBlock  
{  
    public static void method1()  
	{  
		synchronized(StaticSyncBlock.class)    
    {  
		… …  
    }  
}  
	public static synchronized void method2()    
    {  
		… …  
	}  
} 
```
在同步静态方法时可以使用类的静态字段class来得到Class对象。在上例中method1和method2方法同时只能有一个方法执行。除了使用class字段得到Class对象外，还可以使用实例的getClass方法来得到Class对象。上例中的代码可以修改如下：
使用getClass方法得到Class对象
```java  
public class StaticSyncBlock  
{  
	public static StaticSyncBlock instance;   
    public StaticSyncBlock()  
    {  
        instance = this;  
    }  
    public static void method1()  
    {  
       synchronized(instance.getClass())  
       {  
              
       }  
    }  
}  
```
在上面代码中通过一个public的静态instance得到一个StaticSyncBlock类的实例，并通过这个实例的getClass方法得到了Class对象（一个类的所有实例通过getClass方法得到的都是同一个Class对象，因此，调用任何一个实例的getClass方法都可以）。我们还可以通过Class对象使不同类的静态方法同步，如Test类的静态方法method和StaticSyncBlock类的两个静态方法同步，代码如下：
Test类的method方法和StaticSyncBlock类的method1、method2方法同步
```java  
public class Test  
{  
    public static void method()  
    {  
        synchronized(StaticSyncBlock.class)  
        {  
               
        }  
    }  
} 
```
注意：在使用synchronized块同步类方法时，非静态方法可以使用this来同步，而静态方法必须使用Class对象来同步。它们互不影响。当然，也可以在非静态方法中使用Class对象来同步静态方法。但在静态方法中不能使用this来同步非静态方法。这一点在使用synchronized块同步类方法时应注意。