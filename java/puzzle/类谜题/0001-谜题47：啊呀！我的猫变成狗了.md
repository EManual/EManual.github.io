下面的程序使用了一个Counter类来跟踪每一种家庭宠物叫唤的次数。那么该程序会打印出什么呢？ 
```java  
class Counter {
    private static int count = 0;
    public static final synchronized void increment() {
        count++;
    }
    public static final synchronized int getCount() {
        return count; 
    } 
}

class Dog extends Counter {
    public Dog() { }
    public void woof() { increment(); }
} 

class Cat extends Counter {
    public Cat() { } 
    public void meow() { increment(); }
}

public class Ruckus {
    public static void main(String[] args) { 
        Dog dogs[] = { new Dog(), new Dog() };
        for (int i = 0; i < dogs.length; i++)
            dogs[i].woof();
        Cat cats[] = { new Cat(), new Cat(), new Cat() };
        for (int i = 0; i < cats.length; i++)
            cats[i].meow();
        System.out.print(Dog.getCount() + " woofs and ");
        System.out.println(Cat.getCount() + " meows");
    }
}
```
我们听到两声狗叫和三声猫叫——肯定是好一阵喧闹——因此，程序应该打印2 woofs and 3 meows，不是吗？不：它打印的是5 woofs and 5 meows。所有这些多出来的吵闹声是从哪里来的？我们做些什么才能够阻止它？ 
该程序打印出的犬吠声和猫叫声的数量之和是10，它是实际总数的两倍。问题在于Dog和Cat都从其共同的超类那里继承了count域，而count又是一个静态域。每一个静态域在声明它的类及其所有子类中共享一份单一的拷贝，因此Dog和Cat使用的是相同的count域。每一个对woof或meow的调用都在递增这个域，因此它被递增了5次。该程序分别通过调用Dog.getCount和Cat.getCount读取了这个域两次，在每一次读取时，都返回并打印了5。 
在设计一个类的时候，如果该类构建于另一个类的行为之上，那么你有两种选择：一种是继承，即一个类扩展另一个类；另一种是组合，即在一个类中包含另一个类的一个实例。选择的依据是，一个类的每一个实例都是另一个类的一个实例，还是都有另一个类的一个实例。在第一种情况应该使用继承，而第二种情况应该使用组合。当你拿不准时，优选组合而不是继承[EJ Item 14]。 
一条狗或是一只猫都不是一种计数器，因此使用继承是错误的。Dog和Cat不应该扩展Counter，而是应该都包含一个计数器域。每一种宠物都需要有一个计数器，但并非每一只宠物都需要有一个计数器，因此，这些计数器域应该是静态的。我们不必为Counter类而感到烦恼；一个int域就足够了。 
下面是我们重新设计过的程序，它会打印出我们所期望的2 woofs, 3 meows： 
```java  
class Dog {
    private static int woofCounter;
    public Dog() { }
    public static int woofCount() { return woofCounter; };
    public void woof() { woofCounter++; }
} 

class Cat {
    private static int meowCounter;
    public Cat() { } 
    public static int meowCount() { return meowCounter; };
    public void meow() { meowCounter++; }
}
```
Ruckus类除了两行语句之外没有其它的变化，这两行语句被修改为使用新的方法名来访问计数器： 
System.out.print(Dog.woofCount() + " woofs and ");
System.out.println(Cat.meowCount() + " meows");
总之，静态域由声明它的类及其所有子类所共享。如果你需要让每一个子类都具有某个域的单独拷贝，那么你必须在每一个子类中声明一个单独的静态域。如果每一个实例都需要一个单独的拷贝，那么你可以在基类中声明一个非静态域。还有就是，要优选组合而不是继承，除非导出类真的需要被当作是某一种基类来看待。