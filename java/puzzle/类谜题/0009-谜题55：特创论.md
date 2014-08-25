某些时候，对于一个类来说，跟踪其创建出来的实例个数会非常用有，其典型实现是通过让它的构造器递增一个私有静态域来完成的。在下面的程序中，Creature类展示了这种技巧，而Creator类对其进行了操练，将打印出已经创建的Creature实例的数量。那么，这个程序会打印出什么呢？
```java   
public class Creator {
    public static void main(String[] args) {
        for (int i = 0; i < 100; i++)
            Creature creature = new Creature();
        System.out.println(Creature.numCreated());
    }
}

class Creature {
    private static long numCreated = 0;
    public Creature() {
        numCreated++;
    }
    public static long numCreated() {
        return numCreated;
    }
}
```
这是一个捉弄人的问题。该程序看起来似乎应该打印100，但是它没有打印任何东西，因为它根本就不能编译。如果你尝试着去编译它，你就会发现编译器的诊断信息基本没什么用处。下面就是javac打印的东西： 
```java  
Creator.java:4: not a statement
            Creature creature = new Creature();
            ^
Creator.java:4: ‘;’ expected
            Creature creature = new Creature();
                            ^
```
一个本地变量声明看起来像是一条语句，但是从技术上说，它不是；它应该是一个本地变量声明语句（local variable declaration statement）[JLS 14.4]。Java语言规范不允许一个本地变量声明语句作为一条语句在for、while或do循环中重复执行[JLS 14.12-14]。一个本地变量声明作为一条语句只能直接出现在一个语句块中。（一个语句块是由一对花括号以及包含在这对花括展中的语句和声明构成的。） 
有两种方式可以订正这个问题。最显而易见的方式是将这个声明至于一个语句块中： 
```java  
for (int i = 0; i < 100; i++) {
     Creature creature = new Creature();
}
```
然而，请注意，该程序没有使用本地变量creature。因此，将该声明用一个无任何修饰的构造器调用来替代将更具实际意义，这样可以强调对新创建对象的引用正在被丢弃： 
```java  
for (int i = 0; i < 100; i++) 
     new Creature();
```
无论我们做出了上面的哪种修改，该程序都将打印出我们所期望的100。 
请注意，用于跟踪Creature实例个数的变量（numCreated）是long类型而不是int类型的。我们很容易想象到，一个程序创建出的某个类的实例可能会多余int数值的最大值，但是它不会多于long数值的最大值。 
int数值的最大值是231-1，即大约2.1×109，而long数值的最大值是263-1，即大约9.2×1018。当前，每秒钟创建108个对象是可能的，这意味着一个程序在long类型的对象计数器溢出之前，不得不运行大约三千年。即使是面对硬件速度的提升，long类型的对象计数器也应该足以应付可预见的未来。 
还要注意的是，本谜题中的创建计数策略并不是线程安全的。如果多个线程可以并行地创建对象，那么递增计数器的代码和读取计数器的代码都应该被同步：
```java   
// Thread-safe creation counter
class Creature {
    private static long numCreated;
    public Creature() {
        synchronized (Creature.class) {
            numCreated++;
        }
    }
    public static synchronized long numCreated() {
        return numCreated;
    }
}
```
或者，如果你使用的是5.0或更新的版本，你可以使用一个AtomicLong实例，它在面临并发时可以绕过对同步的需求。 
```java  
// Thread-safe creation counter using AtomicLong;
import java.util.concurrent.atomic.AtomicLong;
class Creature {
    private static AtomicLong numCreated = new AtomicLong();
    public Creature() {
        numCreated.incrementAndGet();
    }
    public static long numCreated() {
        return numCreated.get();
    }
}
```
请注意，把numCreated声明为瞬时的是不足以解决问题的，因为volatile修饰符可以保证其他线程将看到最近赋予该域的值，但是它不能进行原子性的递增操作。 
总之，一个本地变量声明不能被用作for、while或do循环中的重复执行语句，它作为一条语句只能出现在一个语句块中。另外，在使用一个变量来对实例的创建进行计数时，要使用long类型而不是int类型的变量，以防止溢出。最后，如果你打算在多线程中创建实例，要么将对实例计数器的访问进行同步，要么使用一个AtomicLong类型的计数器。