下面这个程序有两个不可变的值类（value class），值类即其实例表示值的类。第一个类用整数坐标来表示平面上的一个点，第二个类在此基础上添加了一点颜色。主程序将创建和打印第二个类的一个实例。那么，下面的程序将打印出什么呢？ 
```java  
class Point {
    protected final int x, y;
    private final String name; // Cached at construction time
    Point(int x, int y) {
        this.x = x;
        this.y = y;
        name = makeName();
    }
    
    protected String makeName() {
        return "[" + x + "," + y + "]";
    }
    public final String toString() {
        return name;
    }
}

public class ColorPoint extends Point {
    private final String color;
    ColorPoint(int x, int y, String color) {
        super(x, y);
        this.color = color;
    }
    protected String makeName() {
       return super.makeName() + ":" + color;
    }
    public static void main(String[] args) {
        System.out.println(new ColorPoint(4, 2, "purple"));
    }
}
```
main方法创建并打印了一个ColorPoint实例。println方法调用了该ColorPoint实例的toString方法，这个方法是在Point中定义的。toString方法将直接返回name域的值，这个值是通过调用makeName方法在Point的构造器中被初始化的。对于一个Point实例来说，makeName方法将返回[x,y]形式的字符串。对于一个ColorPoint实例来说，makeName方法被覆写为返回[x,y]:color形式的字符串。在本例中，x是4，y是2，color的purple，因此程序将打印[4,2]:purple，对吗？不，如果你运行该程序，就会发现它打印的是[4,2]:null。这个程序出什么问题了呢？ 
这个程序遭遇了实例初始化顺序这一问题。要理解该程序，我们就需要详细跟踪该程序的执行过程。下面是该程序注释过的版本的列表，用来引导我们了解其执行顺序：
```java   
class Point {
    protected final int x, y;
    private final String name; // Cached at construction time
    Point(int x, int y) {
        this.x = x;
        this.y = y;
        name = makeName(); // 3. Invoke subclass method
    }
    
    protected String makeName() {
        return "[" + x + "," + y + "]";
    }
    public final String toString() {
        return name;
    }
}

public class ColorPoint extends Point {
    private final String color;
    ColorPoint(int x, int y, String color) {
        super(x, y);          // 2. Chain to Point constructor
        this.color = color; // 5. Initialize blank final-Too late
    }
    protected String makeName() {
       // 4. Executes before subclass constructor body!
       return super.makeName() + ":" + color;
    }
    public static void main(String[] args) {
        // 1. Invoke subclass constructor
        System.out.println(new ColorPoint(4, 2, "purple"));
    }
}
```
在下面的解释中，括号中的数字引用的就是在上述注释版本的列表中的注释标号。首先，程序通过调用ColorPoint构造器创建了一个ColorPoint实例（1）。这个构造器以链接调用其超类构造器开始，就像所有构造器所做的那样（2）。超类构造器在构造过程中对该对象的x域赋值为4，对y域赋值为2。然后该超类构造器调用makeName，该方法被子类覆写了（3）。 
ColorPoint中的makeName方法（4）是在ColorPoint构造器的程序体之前执行的，这就是问题的核心所在。makeName方法首先调用super.makeName，它将返回我们所期望的[4,2]，然后该方法在此基础上追加字符串“：”和由color域的值所转换成的字符串。但是此刻color域的值是什么呢？由于它仍处于待初始化状态，所以它的值仍旧是缺省值null。因此，makeName方法返回的是字符串“[4,2]:null”。超类构造器将这个值赋给name域（3），然后将控制流返回给子类的构造器。 
这之后子类构造器才将“purple”赋予color域（5），但是此刻已经为时过晚了。color域已经在超类中被用来初始化name域了，并且产生了不正确的值。之后，子类构造器返回，新创建的ColorPoint实例被传递给println方法，它适时地调用了该实例的toString方法，这个方法返回的是该实例的name域的内容，即“[4,2]:null”，这也就成为了程序要打印的东西。 
本谜题说明：在一个final类型的实例域被赋值之前，存在着取用其值的可能，而此时它包含的仍旧是其所属类型的缺省值。在某种意义上，本谜题是谜题49在实例方面的相似物，谜题49是在final类型的静态域被赋值之前，取用了它的值。在这两种情况中，谜题都是因初始化的循环而产生的，在谜题49中，是类的初始化；而在本谜题中，是实例初始化。两种情况都存在着产生极大的混乱的可能性，但是它们之间有一个重要的差别：循环的类初始化是无法避免的灾难，但是循环的实例初始化总是可以且总是应该避免的。 
无论何时，只要一个构造器调用了一个已经被其子类覆写了的方法，那么该问题就会出现，因为以这种方式被调用的方法总是在实例被初始化之前执行。要想避免这个问题，就千万不要在构造器中调用可覆写的方法，直接调用或间接调用都不行[EJ Item 15]。这项禁令应该扩展至实例初始器和伪构造器（pseudoconstructors）readObject与clone。（这些方法之所以被称为伪构造器，是因为它们可以在不调用构造器的情况下创建对象。） 
你可以通过惰性初始化name域来订正该问题，即当它第一次被使用时初始化，以此取代积极初始化，即当Point实例被创建时初始化。 
通过这种修改，该程序就可以打印出我们期望的[4,2]:purple。 
```java  
class Point {
    protected final int x, y;
    private String name; // Lazily initialized
    Point(int x, int y) {
        this.x = x;
        this.y = y;
        // name initialization removed
    }
    
    protected String makeName() {
        return "[" + x + "," + y + "]";
    }
    // Lazily computers and caches name on first use
    public final synchronized String toString() {
        if (name == null)
            name = makeName();
        return name;
    }
}
```
尽管惰性加载可以订正这个问题，但是对于让一个值类去扩展另一个值类，并且在其中添加一个会对euqals比较方法产生影响的域的这种做法仍旧不是一个好主意。你无法在超类和子类上都提供一个基于值的equals方法，而同时又不违反Object.equals方法的通用约定，或者是不消除在超类和子类之间进行有实际意义的比较操作的可能性[EJ Item 7]。 
循环实例初始化问题对语言设计者来说是问题成堆的地方。C++是通过在构造阶段将对象的类型从超类类型改变为子类类型来解决这个问题的。如果采用这种解决方法，本谜题中最开始的程序将打印[4,2]。我们发现没有任何一种流行的语言能够令人满意地解决这个问题。也许，我们值得去考虑，当超类构造器调用子类方法时，通过抛出一个不受检查的异常使循环实例初始化非法。 
总之，在任何情况下，你都务必要记住：不要在构造器中调用可覆 写的方法。在实例初始化中产生的循环将是致命的。该问题的解决方案就是惰性初始化[EJ Items 13,48]。 