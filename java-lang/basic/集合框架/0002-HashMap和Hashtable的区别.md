HashMap：JDK1.2之后推出，是新的类。采用异步处理方式，性能较高，但是属于非线程安全。允许设置null。
Hashtable:JDK1.0时推出，是旧的类。采用同步处理方式，性能较低，但是属于非线程安全。允许设置null。
HashMap是Hashtable的轻量级实现（非线程安全的实现），他们都完成了Map接口，主要区别在于HashMap允许空（null）键值（key）,由于非线程安全，在只有一个线程访问的情况下，效率要高于Hashtable。 
HashMap允许将null作为一个entry的key或者value，而Hashtable不允许。 
HashMap把Hashtable的contains方法去掉了，改成containsvalue和containsKey。因为contains方法容易让人引起误解。 
Hashtable继承自Dictionary类，而HashMap是Java1.2引进的Map interface的一个实现。 
最大的不同是，Hashtable的方法是Synchronize的，而HashMap不是，在多个线程访问Hashtable时，不需要自己为它的方法实现同步，而HashMap 就必须为之提供外同步。 
Hashtable和HashMap采用的hash/rehash算法都大概一样，所以性能不会有很大的差异。
就HashMap与HashTable主要从三方面来说。 
一，历史原因:Hashtable是基于陈旧的Dictionary类的，HashMap是Java 1.2引进的Map接口的一个实现 
二，同步性:Hashtable是线程安全的，也就是说是同步的，而HashMap是线程序不安全的，不是同步的 
三，值：只有HashMap可以让你将空值作为一个表的条目的key或value 。