(1)前言，想要明白hashCode的作用，你必须要先知道Java中的集合。
Java中的集合（Collection）有两类，一类是List，再有一类是Set。 
前者集合内的元素是有序的，元素可以重复；后者元素无序，但元素不可重复。 
那么我们怎么判断两个元素是否重复呢？ 这就是Object.equals方法了。
通常想查找一个集合中是否包含某个对象，就是逐一取出每个元素与要查找的元素进行比较，当发现某个元素与要查找的对象进行equals方法比较的结果相等时，则停止继续查找并返回肯定的信息，否则返回否定的信息，如果一个集合中有很多元素譬如成千上万的元素，并且没有包含要查找的对象时，则意味着你的程序需要从该集合中取出成千上万个元素进行逐一比较才能得到结论，于是，有人就发明了一种哈希算法来提高从集合中查找元素的效率，这种方式将集合分成若干个存储区域，每个对象可以计算出一个哈希码，可以将哈希码分组，每组分别对应某个存储区域，根据一个对象的哈希码就可以确定该对象应该存储的那个区域。
hashCode方法可以这样理解：它返回的就是根据对象的内存地址换算出的一个值。这样一来，当集合要添加新的元素时，先调用这个元素的hashCode方法，就一下子能定位到它应该放置的物理位置上。如果这个位置上没有元素，它就可以直接存储在这个位置上，不用再进行任何比较了；如果这个位置上已经有元素了，就调用它的equals方法与新元素进行比较，相同的话就不存了，不相同就散列其它的地址。这样一来实际调用equals方法的次数就大大降低了，几乎只需要一两次。
(2)首先，equals()和hashcode()这两个方法都是从object类中继承过来的。 
equals()方法在object类中定义如下： 
```java  
public boolean equals(Object obj) { 
	return (this == obj); 
} 
```
很明显是对两个对象的地址值进行的比较（即比较引用是否相同）。但是我们必需清楚，当String、Math、还有Integer、Double。。。。等这些封装类在使用equals()方法时，已经覆盖了object类的equals（）方法。比 如在String类中如下： 
```java  
public boolean equals(Object anObject) { 
	if (this == anObject) { 
	   return true; 
	} 
	if (anObject instanceof String) { 
	   String anotherString = (String)anObject; 
	   int n = count; 
	   if (n == anotherString.count) { 
			char v1[] = value; 
			char v2[] = anotherString.value; 
			int i = offset; 
			int j = anotherString.offset; 
			while (n-- != 0) { 
				if (v1[i++] != v2[j++]) 
					return false; 
				} 
			return true; 
		} 
	} 
	return false; 
} 
```
很明显，这是进行的内容比较，而已经不再是地址的比较。依次类推Double、Integer、Math。。。。等等这些类都是重写了equals()方法的，从而进行的是内容的比较。
我们还应该注意，Java语言对equals()的要求如下，这些要求是必须遵循的： 
1) 对称性：如果x.equals(y)返回是"true"，那么y.equals(x)也应该返回是"true"。 
2) 反射性：x.equals(x)必须返回是"true"。 
3) 类推性：如果x.equals(y)返回是"true"，而且y.equals(z)返回是"true"，那么z.equals(x)也应该返回是"true"。 
4) 还有一致性：如果x.equals(y)返回是"true"，只要x和y内容一直不变，不管你重复x.equals(y)多少次，返回都是"true"。 
5) 任何情况下，x.equals(null)，永远返回是"false"；x.equals(和x不同类型的对象)永远返回是"false"。 
以上这五点是重写equals()方法时，必须遵守的准则，如果违反会出现意想不到的结果，请大家一定要遵守。
(3)其次，hashcode() 方法，在object类中定义如下： 
```java  
public native int hashCode(); 
```
说明它是一个本地方法，它的实现是根据本地机器相关的。当然我们可以在自己写的类中覆盖hashcode()方法，比如String、Integer、Double等这些类都是覆盖了hashcode()方法的。例如在String类中定义的hashcode()方法如下： 
```java  
public int hashCode() { 
	int h = hash; 
	if (h == 0) { 
		int off = offset; 
		char val[] = value; 
		int len = count;   
		for (int i = 0; i < len; i++) { 
			h = 31*h + val[off++]; 
		} 
		hash = h; 
	} 
	return h; 
} 
```
解释一下这个程序（String的API中写到）： 
```java  
s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1] 
```
使用 int 算法，这里 s[i] 是字符串的第 i 个字符，n 是字符串的长度，^ 表示求幂。（空字符串的哈希码为 0。)
(4)谈到hashcode()和equals()就不能不说到hashset,hashmap,hashtable中的使用，具体是怎样呢，请看如下分析：
Hashset是继承Set接口，Set接口又实现Collection接口，这是层次关系。那么hashset是根据什么原理来存取对象的呢？ 
在hashset中不允许出现重复对象，元素的位置也是不确定的。在hashset中又是怎样判定元素是否重复的呢？判断两个对象是否相等的规则是： 
1)，判断两个对象的hashCode是否相等。
如果不相等，认为两个对象也不相等，完毕,如果相等，转入2
2)，判断两个对象用equals运算是否相等。
如果不相等，认为两个对象也不相等 。
如果相等，认为两个对象相等(equals()是判断两个对象是否相等的关键) 。
为什么是两条准则，难道用第一条不行吗？不行，因为前面已经说了，hashcode()相等时，equals()方法也可能不等，所以必须用第2条准则进行限制，才能保证加入的为非重复元素。 
比如下面的代码：
```java  
public static void main(String[] args) {
    String s1 = new String("zhangsan");
    String s2 = new String("zhangsan");
    System.out.println(s1 == s2);// false
    System.out.println(s1.equals(s2));// true
    System.out.println(s1.hashCode());// s1.hashcode()等于s2.hashcode()
    System.out.println(s2.hashCode());
    Set hashset = new HashSet();
    hashset.add(s1);
    hashset.add(s2);
    System.out.println(hashset.size());//1
}
```
再看如下一些示例：
几个很简单的示例，说明一些很简单的道理
例一:
```java  
package com.itsoft;
import java.util.ArrayList;
import java.util.Collection;
public class Point {
private int x;
private int y;
public Point(int x, int y) {
    super();
    this.x = x;
    this.y = y;
}
public static void main(String[] args) {
    Point p1 = new Point(3, 3);
    Point p2 = new Point(5, 5);
    Point p3 = new Point(3, 3);
    Collection<Point> collection = new ArrayList<Point>();
    collection.add(p1);
    collection.add(p2);
    collection.add(p3);
    collection.add(p1);
    System.out.println(collection.size());//4，结果输出4，以为List中可以有重复元素，而且是有序的。
}
}
```
例二(在上例的基础上稍作修改把ArrayList改为HashSet):
```java  
package com.itsoft;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
public class Point {
private int x;
private int y;
public Point(int x, int y) {
    super();
    this.x = x;
    this.y = y;
}
public static void main(String[] args) {
    Point p1 = new Point(3, 3);
    Point p2 = new Point(5, 5);
    Point p3 = new Point(3, 3);
    Collection<Point> collection = new HashSet<Point>();
    collection.add(p1);
    collection.add(p2);
    collection.add(p3);
    collection.add(p1);
    System.out.println(collection.size());//3，因为HashSet中不会保存重复的对象，每添加一个元素，先判断，再添加，如果已经存在，那么就不在添加，无序的！
}
```
}
例三(如果我们需要p1和p3相等呢？就必须重新hashcode()和equal()方法):
```java  
package com.itsoft;
import java.util.Collection;
import java.util.HashSet;
public class Point {
private int x;
private int y;
public Point(int x, int y) {
    super();
    this.x = x;
    this.y = y;
}
@Override
public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + x;
    result = prime * result + y;
    return result;
}
@Override
public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    final Point other = (Point) obj;
    if (x != other.x)
      return false;
    if (y != other.y)
      return false;
    return true;
}
public static void main(String[] args) {
    Point p1 = new Point(3, 3);
    Point p2 = new Point(5, 5);
    Point p3 = new Point(3, 3);
    Collection<Point> collection = new HashSet<Point>();
    collection.add(p1);
    collection.add(p2);
    collection.add(p3);
    collection.add(p1);
    System.out.println(collection.size());//输出2，此时p1和p3是相等的
}
}
```
例四(如果我们把hashcode()方法去掉看下):
```java  
package com.itsoft;
import java.util.Collection;
import java.util.HashSet;
public class Point {
private int x;
private int y;
public Point(int x, int y) {
    super();
    this.x = x;
    this.y = y;
}
@Override
public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    final Point other = (Point) obj;
    if (x != other.x)
      return false;
    if (y != other.y)
      return false;
    return true;
}
public static void main(String[] args) {
    Point p1 = new Point(3, 3);
    Point p2 = new Point(5, 5);
    Point p3 = new Point(3, 3);
    Collection<Point> collection = new HashSet<Point>();
    collection.add(p1);
    collection.add(p2);
    collection.add(p3);
    collection.add(p1);
    System.out.println(collection.size());//输出3，此时p1和p3又不相等了
    //原因：虽然此时p1和p2的equals相等，但是他们的hashcode不相等，所以它们就存储在不同区域，在这两个不同的区域存储着相同的东西，查找的时候只在一个区域查找，就被放进去了。
}
}
```
注：为了避免第四种情况的发生，通常情况下，一个实例的两个对象equals相同，那么他们的hashcode也必须相等，反之，则不成立，当然，只有对象存储在hash算法系列的集合中，hashcode方法才有价值.这样目的就是确保相同的对象存储在相同的位置。
小结：
(1)只有类的实例对象要被采用哈希算法进行存储和检索时，这个类才需要按要求覆盖hashCode方法，即使程序可能暂时不会用到当前类的hashCode方法，但是为它提供一个hashCode方法也不会有什么不好，没准以后什么时候又用到这个方法了，所以，通常要求hashCode方法和equals方法一并被同时覆盖。
(2)equals()相等的两个对象，hashcode()一定相等；equals（）不相等的两个对象，却并不能证明他们的hashcode()不相等。换句话说，equals()方法不相等的两个对象，hashcode()有可能相等。反过来：hashcode()不等，一定能推出equals()也不等；hashcode()相等，equals()可能相等，也可能不等。
提示：
(1)通常来说，一个类的两个实例对象用equal方法比较的结果相等时，它们的哈希码也必须相等，但反之则不成立，即equals方法比较结果不相等的对象可以有相同的哈希码，或者说哈希码相同的两个对象的equal方法比较的结果可以不等。
(2)当一个对象被存储进hashset集合中以后，就不能修改这个对象中的那些参与计算哈希值的字段了，否则，对象修改后的哈希值与最初存储进hashset集合时的哈希值就不同了，这种情况下，即使在contains方法使用该对象的当前引用作为的参数去hashset集合中检索对象，也将返回找不到对象的结果，这也会导致无法从hashset集合中单独删除当前对象，从而造成内存泄露，所谓的内存泄露也就说有一个对象不再被使用，但它一直占有内存空间，没有被释放。