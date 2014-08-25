下面这个程序使用一个匿名类执行了一个并不自然的动作。它会打印出什么呢？ 
```java  
public class Twisted {
    private final String name;
    Twisted(String name) {
        this.name = name;
    }
    private String name() {
        return name;
    }
    private void reproduce() {
        new Twisted("reproduce") {
            void printName() {
                System.out.println(name());
            }
        }.printName();
    }
    public static void main(String[] args) {
        new Twisted("main").reproduce();
    }
}
```
根据一个肤浅的分析会判断该程序不能通过编译。reproduce方法中的匿名类试图调用Twisted类中的私有方法name。一个类不能调用另一个类的私有方法，是吗？如果你试图编译这个程序，你会发现它可以成功地通过编译。在顶层的类型（top-level type）中，即本例中的Twisted类，所有的本地的、内部的、嵌套的和匿名的类都可以毫无限制地访问彼此的成员[JLS 6.6.1]。这是一个欢乐的大家庭。 
在了解了这些之后，你可能会希望程序打印出reproduce，因为它在new Twisted(“reproduce”)实例上调用了printName方法，这个实例将字符串”reproduce”传给其超类的构造器使其存储到它的name域中。printName方法调用name方法，name方法返回了name域的内容。但是如果你运行这个程序，你会发现它打印的是main。现在的问题是它为什么会做出这样的事情呢？ 
这种行为背后的原因是私有成员不会被继承[JLS 8.2]。在这个程序中，name方法并没有被继承到reproduce方法中的匿名类中。所以，匿名类中对于printName方法的调用必须关联到外围(“main”)实例而不是当前(“reproduce”)实例。这就是含有正确名称的方法的最小外围范围（enclosing scope）（谜题 71和79）。 
这个程序违反了谜题90中的建议：在”reproduce”中的匿名类即是Twisted类的内部类又扩展了它。单独这一点就足以使程序难以阅读。再加上调用超类的私有方法的复杂度，这个程序就成了纯粹的冗长的废话。这个谜题可以用来强调谜题6中的教训：如果你不能通过阅读代码来分辨程序会做什么，那么它很可能不会做你想让它做的事。要尽量争取程序的清晰。