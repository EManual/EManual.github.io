这个程序创建了一个对象并且检查它是否遵从某个类的不变规则(invariant)。然后该程序序列化这个对象，之后将其反序列化，然后再次检查反序列化得到的副本是否也遵从这个规则。它会遵从这个规则吗？如果不是的话，又是为什么呢？ 
```java  
import java.util.*;
import java.io.*;

public class SerialKiller {
    public static void main(String[] args) {
        Sub sub = new Sub(666); 
        sub.checkInvariant();

        Sub copy = (Sub) deepCopy(sub);
        copy.checkInvariant();
    }

    // Copies its argument via serialization (See Puzzle 80)
    static public Object deepCopy(Object obj) {
        try {
            ByteArrayOutputStream bos = 
                new ByteArrayOutputStream();
            new ObjectOutputStream(bos).writeObject(obj);
            ByteArrayInputStream bin =
                new ByteArrayInputStream(bos.toByteArray());
            return new ObjectInputStream(bin).readObject(); 
        } catch(Exception e) {
            throw new IllegalArgumentException(e); 
        }
    }
}

class Super implements Serializable {
    final Set<Super> set = new HashSet<Super>();
} 

final class Sub extends Super {
    private int id;
    public Sub(int id) {
        this.id = id;
        set.add(this); // Establish invariant
    }

    public void checkInvariant() {
        if (!set.contains(this))
            throw new AssertionError("invariant violated");
    }

    public int hashCode() {
        return id;
    }

    public boolean equals(Object o) {
        return (o instanceof Sub) && (id == ((Sub)o).id);
    }
}
```
程序中除了使用了序列化之外，看起来是很简单的。子类Sub覆写了hashCode方法和equals方法。这些覆写过的方法符合了相关的一般规约[EJ Item 7,8]。Sub的构造器建立了这个类的不变规则，而在它这么做的时候没有调用到可覆写的方法（谜题51）。Super类有一个单独的Set<Super>类型的域，Sub类添加了另外一个int类型的域。Super和Sub都不需要定制的序列化形式。那么什么东西会出错呢？ 
其实有很多。对于5.0版本，运行该程序会得到如下的“堆轨迹”（stack trace）： 
```java  
Exception in thread “main” AssertionError
    at Sub.checkInvariant(SerialKiller.java:41)
    at SerialKiller.main(SerialKiller.java:10)
```
序列化和反序列化一个Sub实例会产生一个被破坏的副本。为什么呢？阅读程序并不会帮助你找出原因，因为真正引起问题的代码在其他地方。错误是由HashSet的readObject方法引起的。在某些情况下，这个方法会间接地调用某个未初始化对象的被覆写的方法。为了组装(populate)正在被反序列化的散列集合，HashSet.readObject调用了HashMap.put方法，而它会去调用每个键(key)的hashCode方法。由于整个对象图（object graph）正在被反序列化，并没有什么可以保证每个键在它的hashCode方法被调用的时候已经被完全初始化了。实际上，这很少会成为一个问题，但是有时候它会造成绝对的混乱。这个缺陷会在正在被反序列化的对象图的某些循环中出现。 
为了更具体一些，让我们看看程序中在反序列化Sub实例的时候发生了什么。首先，序列化系统会反序列化Sub实例中Super的域。唯一的这样的域就是set，它包含了一个对HashSet的引用。在内部，每个HashSet实例包含一个对HashMap的引用，HashMap的键是该散列集合的元素。HashSet类有一个readObject方法，它创建一个空的HashMap，并且使用HashMap的put方法，针对集合中的每个元素在HashMap中插入一个键-值对。put方法会调用键的hashCode方法以确定它所在的单元格（bucket）。在我们的程序中，散列映射表中唯一的键就是Sub的实例，而它的set域正在被反序列化。这个实例的子类域（subclass field），即id，尚未被初始化，所以它的值为0，即所有int域的缺省初始值。不幸的是，Sub的hashCode方法将返回这个值，而不是最后保存在这个域中的值666。因为hashCode返回了错误的值，相应的键-值对条目将会放入错误的单元格中。当id域被初始化为666时，一切都太迟了。当Sub实例在HashMap中的时候，改变这个域的值就会破坏这个域，进而破坏HashSet，破坏Sub实例。程序检测到了这个情况，就报告出了相应的错误。 
这个程序说明，包含了HashMap的readObject方法的序列化系统总体上违背了不能从类的构造器或伪构造器（pseudoconstructor）中调用其可覆写方法的规则[EJ Item 15]。Super类的（缺省的）readObject方法调用了HashSet的(显式的)readObject方法，该方法进而调用了它内部的HashMap的put方法，put方法又调用了Sub实例的hashCode方法，而该实例正处在创建的过程中。现在我们遇到大麻烦了：Super类中，从Object类继承而来的hashCode方法在Sub中被覆写了，但是这个被覆写的方法在Sub的域被初始化之前就被调用了，而该方法需要依赖于Sub的域。 
这个问题和谜题51中的那个本质上几乎是完全相同的。唯一真正不同的是在这个谜题中，readObject伪构造器错误地替代了构造器。HashMap和Hashtable的readObject方法受到的影响是类似的。 
对于平台的实现者来说，也许可以通过牺牲一点性能来订正HashSet、HashMap和HashTable中的这个问题。当针对HashSet时，订正的策略可以是重写readObject方法使其在反序列化期间，将集合的元素保存到一个数组中，而不是将它们放入散列集合中。这样，当被反序列化的散列集合的公共方法首次被调用的时候，数组中的元素将在方法执行之前被插入到集合中。 
这种方法的代价是它需要在与散列集合的每个公共方法相对应的条目上检查是否要组装散列集合。由于HashSet、HashMap以及HashTable都是性能临界（performance-critical）的，所以这个方法看起来是不可取的。更不幸的是，所有的用户都要付出这种代价，甚至当他们不对这些集合（collection）进行序列化时也是如此。这就违背了这样一个原则：你绝不应该为你不使用的功能而付出代价。 
另外一个可能的方法是让HashSet.readObject方法调用ObjectInputStream.registerValidation方法，用以将散列集合的组装延迟到validateObject方法回调时再进行。这个方法看起来更吸引人，因为它仅仅增加了反序列化的开销，但是它会破坏任何在“包含流”（containing stream）的反序列化过程中试图使用HashSet实例的代码。 
上述的2个方法是否可行还有待研究。但是现在，我们必须接受这些类的这种行为。幸运的是，有一个工作区（workaround）：如果一个HashSet、Hashtable或HashMap被序列化，那么请确认它们的内容没有直接或间接地引用到它们自身。这里的内容（content），指的是元素、键和值。 
这里也有一个教训送给那些使用可序列化类型的开发者们：在readObject或readResolve方法中，请避免直接或间接地在正在进行反序列化的对象上调用任何方法。如果你必须在某个类型C的readObject或readResolve方法中违背这条建议，请确定没有C的实例会出现在正在被反序列化的对象图的某个循环内。不幸的是，这不是一个本地的属性：一般说来，你需要考虑到整个系统来验证这一点。 
总之，Java的序列化系统是很脆弱的。为了正确而且高效地序列化大量的类，你必须编写readObject或readResolve方法[EJ Items 55-57]。这个谜题说明了，为了避免破坏反序列化的实例，你必须小心翼翼地编写这些方法。HashSet、HashMap和Hashtable的readObject方法很容易产生这种错误。对于平台设计者来说，如果你决定提供序列化系统，请不要提供如此脆弱的东西。健壮的序列化系统是很难设计的。