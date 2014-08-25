本谜题试图从前一个谜题中吸取教训。下面的程序还是由一个Name类和一个main方法构成，这个main方法还是将一个名字放置到一个散列集合中，然后检查该集合是否包含了这个名字。然而，这一次Name类已经覆写了hashCode方法。那么下面的程序将打印出什么呢？ 
```java  
import java.util.*;
public class Name {
    private String first, last;
    public Name(String first, String last) {
        this.first = first; this.last = last;
    }
    public boolean equals(Name n) {
        return n.first.equals(first) && n.last.equals(last);
    }    
    public int hashCode() {
        return 31 * first.hashCode() + last.hashCode(); 
    }
    public static void main(String[ ] args) {
        Set s = new HashSet();
        s.add(new Name("Donald", "Duck"));
        System.out.println(
            s.contains(new Name("Donald", "Duck")));
    }
}
```
与谜题57一样，该程序的main方法创建了两个Name实例，它们表示的是相同的名字。这一次使用的名字是Donald Duck而不是Mickey Mouse，但是它们不应该有很大的区别。main方法同样还是将第一个实例置于一个散列集合中，然后检查该集合中是否包含了第二个实例。这一次hashCode方法明显是正确的，因此看起来该程序应该打印true。但是，表象再次欺骗了我们：它总是打印出false。这一次又是哪里出错了呢？ 
这个程序的缺陷与谜题57中的缺陷很相似，在谜题57中，Name覆写了equals方法，但是没有覆写hashCode方法；而在本谜题中，Name覆写了hashCode方法，但是没有覆写equals方法。这并不是说Name没有声明一个equals方法，它确实声明了，但是那是个错误的声明。Name类声明了一个参数类型是Name而不是Object的equals方法。这个类的作者可能想要覆写equals方法，但是却错误地重载了它[JLS 8.4.8.1, 8.4.9]。 
HashSet类是使用equals(Object)方法来测试元素的相等性的；Name类中声明一个equals(Name)方法对HashSet不造成任何影响。那么Name是从哪里得到了它的equals(Object)方法的呢？它是从Object哪里继承而来的。这个方法只有在它的参数与在其上调用该方法的对象完全相同时才返回true。我们的程序中的main方法将一个Name实例插入到了散列集合中，并且测试另一个实例是否存在于该散列集合中，由此可知该测试一定是返回false的。对我们而言，两个实例可以代表那令人惊奇的水禽唐老鸭，但是对散列映射表而言，它们只是两个不相等的对象。 
订正该程序只需用可以在谜题57中找到的覆写的equals方法来替换重载的equals方法即可。通过使用这个equals方法，该程序就可以打印出我们所期望的true： 
```java  
public boolean equals(Object o) {
    if (!(o instanceof Name))
        return false;
    Name n = (Name)o;
    return n.first.equals(first) && n.last.equals(last);
}
```
要让该程序可以正常工作，你只需增加一个覆写的equals方法即可。你不必剔除那个重载的版本，但是你最好是删掉它。重载为错误和混乱提供了机会[EJ Item 26]。如果兼容性要求强制你必须保留一个自身类型的equals方法，那么你应该用自身类型的重载去实现Object的重载，以此来确保它们具有相同的行为： 
public boolean equals(Object o) { return o instanceof Name && equals((Name) o); } 
本谜题的教训是：当你想要进行覆写时，千万不要进行重载。为了避免无意识地重载，你应该机械地对你想要覆写的每一个超类方法都拷贝其声明，或者更好的方式是让你的IDE帮你去做这些事。这样做除了可以保护你免受无意识的重载之害，而且还可以保护你免受拼错方法名之害。如果你使用的5.0或者更新的版本，那么对于那些意在覆写超类方法的方法，你可以将@Override注释应用于每一个这样的方法的声明上： 
@Override public Boolean equals(Object o) { ... }
在使用这个注释时，除非被注释的方法确实覆写了一个超类方法，否则它将不能编译。对语言设计者来说，值得去考虑在每一个覆写超类方法的方法声明上都添加一个强制性的修饰符。