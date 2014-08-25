下面的程序包含了一个简单的不可变类，它表示一个名字，其main方法将一个名字置于一个集合中，并检查该集合是否确实包含了该名字。那么，这个程序到底会打印出什么呢？ 
```java  
import java.util.*;
public class Name {
    private String first, last;
    public Name(String first, String last) {
        this.first = first;
        this.last = last;
    }
    public boolean equals(Object o) {
        if (!(o instanceof Name))
            return false;
        Name n = (Name)o;
        return n.first.equals(first) && n.last.equals(last);
    }
    public static void main(String[] args) {
        Set s = new HashSet();
        s.add(new Name("Mickey", "Mouse"));
        System.out.println(
            s.contains(new Name("Mickey", "Mouse")));
    } 
}
```
一个Name实例由一个姓和一个名构成。两个Name实例在通过equals方法进行计算时，如果它们的姓相等且名也相等，则这两个Name实例相等。姓和名是用在String中定义的equals方法来比较的，两个字符串如果以相同的顺序包含相同的若干个字符，那么它们就相等。因此，两个Name实例如果表示相同的名字，那么它们就相等。例如，下面的方法调用将返回true： 
new Name("Mickey", "Mouse").equals(new Name("Mickey", "Mouse"))
该程序的main方法创建了两个Name实例，它们都表示Mickey Mouse。该程序将第一个实例放置到了一个散列集合中，然后检查该集合是否包含第二个实例。这两个Name实例是相等的，因此看起来该程序似乎应该打印true。如果你运行它，几乎可以肯定它将打印false。那么这个程序出了什么问题呢？ 
这里的bug在于Name违反了hashCode约定。这看起来有点奇怪，因为Name连hashCode都没有，但是这确实是问题所在。Name类覆写了equals方法，而hashCode约定要求相等的对象要具有相同的散列码。为了遵守这项约定，无论何时，只要你覆写了equals方法，你就必须同时覆写hashCode方法[EJ Item 8]。 
因为Name类没有覆写hashCode方法，所以它从Object那里继承了其hashCode实现。这个实现返回的是基于标识的散列码。换句话说，不同的对象几乎总是产生不相等的散列值，即使它们是相等的也是如此。所以说Name没有遵守hashCode的约定，因此包含Name元素的散列集合的行为是不确定的。 
当程序将第一个Name实例放置到散列集合中时，该集合就会在某个散列位置上放置这个实例对应的项。该集合是基于实例的散列值来选择散列位置的，这个散列值是通过实例的hashCode方法计算出来的。 
当该程序在检查第二个Name实例是否包含在散列集合中时，它基于第二个实例的散列值来选择要搜索的散列位置。因为第二个实例有别于第一个实例，因此它极有可能产生不同的散列值。如果这两个散列值映射到了不同的位置，那么contains方法将返回false：我们所喜爱的啮齿动物米老鼠就在这个散列集合中，但是该集合却找不到他。 
假设两个Name实例映射到了相同的位置，那又会怎样呢？我们所了解的所有的HashSet实现都进行了一种优化，即每一项在存储元素本身之外，还存储了元素的散列值。在搜索某个元素时，这种实现通过遍历集合中的项，去拿存储在每一项中的散列值与我们想要查找的元素的散列值进行比较，从而选取适当的散列位置。只有在两个元素的散列值相等的情况下，这种实现才会认为这两个元素相等。这种优化是有实际意义的，因为比较散列码相对于比较元素来说，其代价要小得多。 
对散列集合来说，这项优化并不足以使其能够搜索到正确的位置；两个Name实例必须具有相同的散列值才能让散列集合能够将它们识别为是相等的。该程序偶尔也会打印出true，这是因为被连续创建的两个对象偶尔也会具有相同的标识散列码。一个粗略的实验表明，这种偶然性出现的概率大约是25,000,000分之一。这个实验的结果可能会因所使用的Java实现的不同而有所变化，但是在任何我们所知的JRE上，你基本上是不可能看到该程序打印出true的。 
要想订正该程序，只需在Name类中添加一个恰当的hashCode方法即可。尽管任何其返回值仅有姓和名来确定的方法都可以满足hashCode的约定，但是高质量的散列函数应该尝试着对不同的名字返回不同的散列值。下面的方法就能够很好地实现这一点[EJ Item 8]。只要我们把该方法添加到了程序中，那么该程序就可以打印出我们所期望的true： 
```java  
public int hashCode() {
    return 37 * first.hashCode() + last.hashCode();
}
```
总之，当你覆写equals方法时，一定要记着覆写hashCode方法。更一般地讲，当你在覆写一个方法时，如果它具有一个通用的约定，那么你一定要遵守它。对于大多数在Object中声明的非final的方法，都需要注意这一点[EJ Chapter 3]。不采用这项建议就会导致任意的、不确定的行为。