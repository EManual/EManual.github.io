下面的程序在一个类中计算并缓存了一个合计数，并且在另一个类中打印了这个合计数。那么，这个程序将打印出什么呢？这里给一点提示：你可能已经回忆起来了，在代数学中我们曾经学到过，从1到n的整数总和是n(n+1)/2。 
```java  
class Cache {
    static {
        initializeIfNecessary();
    }
    private static int sum;
    public static int getSum() {
        initializeIfNecessary();
        return sum;
    }
    
    private static boolean initialized = false;
    private static synchronized void initializeIfNecessary() {
        if (!initialized) {
            for (int i = 0; i < 100; i++)
                sum += i;
            initialized = true;
        }
    }
}
public class Client {
    public static void main(String[] args) {
        System.out.println(Cache.getSum()); 
    } 
}
```
草草地看一遍，你可能会认为这个程序从1加到了100，但实际上它并没有这么做。再稍微仔细地看一看那个循环，它是一个典型的半开循环，因此它将从0循环到99。有了这个印象之后，你可能会认为这个程序打印的是从0到99的整数总和。用前面提示中给出的公式，我们知道这个总和是99×100/2，即4,950。但是，这个程序可不这么想，它打印的是9900，是我们所预期值的整整两倍。是什么导致它如此热情地翻倍计算了这个总和呢？ 
该程序的作者显然在确保sum在被使用前就已经在初始化这个问题上，经历了众多的麻烦。该程序结合了惰性初始化和积极初始化，甚至还用上了同步，以确保缓存在多线程环境下也能工作。看起来这个程序已经把所有的问题都考虑到了，但是它仍然不能正常工作。它到底出了什么问题呢？ 
与谜题49中的程序一样，该程序受到了类初始化顺序问题的影响。为了理解其行为，我们来跟踪其执行过程。在可以调用Client.main之前，VM必须初始化Client类。这项初始化工作异常简单，我们就不多说什么了。Client.main方法调用了Cache.getsum方法，在getsum方法可以被执行之前，VM必须初始化Cache类。 
回想一下，类初始化是按照静态初始器在源代码中出现的顺序去执行这些初始器的。Cache类有两个静态初始器：在类顶端的一个static语句块，以及静态域initialized的初始化。静态语句块是先出现的，它调用了方法initializeIfNecessary，该方法将测试initialized域。因为该域还没有被赋予任何值，所以它具有缺省的布尔值false。与此类似，sum具有缺省的int值0。因此，initializeIfNecessary方法执行的正是你所期望的行为，将4,950添加到了sum上，并将initialized设置为true。 
在静态语句块执行之后，initialized域的静态初始器将其设置回false，从而完成Cache的类初始化。遗憾的是，sum现在包含的是正确的缓存值，但是initialized包含的却是false：Cache类的两个关键状态并未同步。 
此后，Client类的main方法调用Cache.getSum方法，它将再次调用initializeIfNecessary方法。因为initialized标志是false，所以initializeIfNecessary方法将进入其循环，该循环将把另一个4,950添加到sum上，从而使其值增加到了9,900。getSum方法返回的就是这个值，而程序打印的也是它。 
很明显，该程序的作者认为Cache类的初始化不会以这种顺序发生。由于不能在惰性初始化和积极初始化之间作出抉择，所以作者同时运用这二者，结果产生了大麻烦。要么使用积极初始化，要么使用惰性初始化，但是千万不要同时使用二者。 
如果初始化一个域的时间和空间代价比较低，或者该域在程序的每一次执行中都需要用到时，那么使用积极初始化是恰当的。如果其代价比较高，或者该域在某些执行中并不会被用到，那么惰性初始化可能是更好的选择[EJ Item 48]。另外，惰性初始化对于打破类或实例初始化中的循环也可能是必需的（谜题51）。 
通过重排静态初始化的顺序，使得initialized域在sum被初始化之后不被复位到false，或者通过移除initialized域的显式静态初始化操作，Cache类就可以得到修复。尽管这样所产生的程序可以工作，但是它们仍旧是混乱的和病构的。Cache类应该被重写为使用积极初始化，这样产生的版本很明显是正确的，而且比最初的版本更加简单。
使用这个版本的Cache类，程序就可以打印出我们所期望的4950： 
```java  
class Cache {
    private static final int sum = computeSum();
    private static int computeSum() {
        int result = 0;
        for (int i = 0; i < 100; i++)
            result += i;
        return result;
    }    
    public static int getSum() {
        return sum;
    }    
}
```
请注意，我们使用了一个助手方法来初始化sum。助手方法通常都优于静态语句块，因为它让你可以对计算命名。只有在极少的情况下，你才必须使用一个静态语句块来初始化一个静态域，此时请将该语句块紧随该域声明之后放置。这提高了程序的清晰度，并且消除了像最初的程序中出现的静态初始化与静态语句块互相竞争的可能性。 
总之，请考虑类初始化的顺序，特别是当初始化显得很重要时更是如此。请你执行测试，以确保类初始化序列的简洁。请使用积极初始化，除非你有某种很好的理由要使用惰性初始化，例如性能方面的因素，或者需要打破初始化循环。