集合：保存多个其他对象的对象，不能保存简单类型。
Collection框架的结构如下：
```java  
Collection 
├List 
│├LinkedList 
│├ArrayList 
│└Vector 
│　└Stack 
└Set 
Map 
├Hashtable 
├HashMap 
└WeakHashMap
```
Collection是最基本的集合接口，一个Collection代表一组Object，即Collection的元素（Elements） 。
Map提供key到value的映射 。
List：有序(存放元素的顺序)，可重复的集合。
ArrayList：实质就是一个会自动增长的数组。
查询效率比较高，增删的效率比较低，适用于查询比较频繁，增删动作较少的元素管理的集合。
加载大批量的数据时，先进行手动扩容(就是调用ensureCapacity(int minCapacity)方法)，这样可以提高效率。
LinkedList：底层是用双向循环链表来实现的
查询效率低，但是增删效率很高，适用于增删动作的比较频繁，查询次数较少的元素管理的集合。
Set：无序的，不允许有重复元素的集合
HashSet：
Object类中的hashCode()的方法是所有类都会继承的方法，这个方法会算出一个Hash码值返回，HashSet会用Hash码值去和数组长度取模，对象的模值(这个模值就是对象要存放在数组中的位置，和数组的下标相同)相同时才会判断数组中的元素和要加入的对象的内容是否相同，如果不同才会再找位置添加进去，相同则不允许添加。
如果数组中的元素和要加入的对象的hashCode()返回了相同的Hash码值，才会用equals()方法来判断两个对象的内容是否相同。	
注意：要存入HashSet的集合对象中的自定义类必须覆盖hashCode()、equals()两个方法，才能保证集合中元素不重复。
TreeSet：可排序的Set
SortedSet接口是Set的子接口，TreeSet是SortedSet接口的实现类，他可以对集合中的元素进行排序。
将自定义类的对象存放在TreeSet中，这个类需要实现了Comparable接口，TreeSet可以自动过滤掉重复元素所以不在需要重载hashCode()方法，TreeSet会根据比较规则判断元素内容是否相同，不同则会存入，TreeSet会在元素存入时就进行排序。
Comparable接口：
也叫做可比较接口，这个接口在java.lang包下，只要根据指定类型的排序规则实现了这个接口，就是可排序的。
这个接口中只定义了一个 compareTo(Object o)方法，该方法的返回值类型是整型，如果当前对象大于参数对象就返回正数，当前对象等于参数对象就返回0，当前对象小于参数对象就返回负值，这样写就是升序排列，反之则是进行降序排列。
Comparator接口：
比较器Comparator接口，是另一种对自定义类型对象的集合整体排序的方法，存在于java.util包下。
这个接口中定义了一个 compare(Object o1,Object o2) 方法来比较两个对象，这个方法的返回值定义和上面介绍的那个方法是一样。
利用这种方式，则在创建集合的时候把定义好的比较器作为参数，构造一个集合。
Map：存放key-value对(有关系的两个对象，一个做key，一个做value，同时存入)。
HashMap：基于哈希表的 Map 接口的实现，此实现提供所有可选的映射操作，并允许使用 null 值和 null 键。
遍历：
先调用keySet()得到key的set集合，
再迭代遍历key的set集合，
根据key得到value。
Hashtable：同HashMap，一般不使用。
HashMap与Hashtable的区别：
HashMap：非线程安全，不支持并发控制，允许空的键值对。
Hashtable：是线程安全，支持并发控制，不允许有空的键值对。
SortedMap接口：Map的子接口，按某一特定排序规则来存放所加入的键值对。
实现类：TreeMap类。
Key值的排序规则，同SortedSet接口实现类TreeSet。
* 注意：
key一般是8种基本类型的封装类或者是String类，拿自己自定义的类作为Key没有意义。
key不可重复，value可以重复。