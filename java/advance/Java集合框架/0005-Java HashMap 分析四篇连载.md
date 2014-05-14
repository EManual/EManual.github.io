Java的HashMap非常的常用，本篇研究它的实现算法，最后希望计算出内存占用，性能的量化数据，然后得出什么时候使用HashMap，什么时候不能滥用的结论。
HashMap实际上是一个数组，数组里面的每个元素都是一个链表。每个元素在通过put方法放入HashMap中的时候，要按照如下步骤进行：
1.根据该元素自身提供的hashcode计算出散列值，该散列值就是数组的下标。
2.将新元素放入该数组位置的链表中。
先来看一下数组的定义：
```java  
	 /**     
     * The table, resized as necessary. Length MUST Always be a power of two.   
     */     
    transient Entry[] table;  
```
这是一个数组，transient关键字告诉我们它不会参与序列化。既然是一个数组，总有数目上限，也就意味着如果存入HashMap的元素太多，导致数组大小不能够存放所有的链表的时候，数组大小必须要能够调整。所以首先来考察一下数组容量的相关算法。
第一，Entry是什么类型？
```java  
static class Entry<K,V> implements Map.Entry<K,V> {  
        final K key;  
        V value;  
        Entry<K,V> next;  
        final int hash;  
  
        /**    
         * Creates new entry.    
         */    
        Entry(int h, K k, V v, Entry<K,V> n) {  
            value = v;  
            next = n;  
            key = k;  
            hash = h;  
        }  
        ....  
        public final boolean equals(Object o) {  
            if (!(o instanceof Map.Entry))  
                return false;  
            Map.Entry e = (Map.Entry)o;  
            Object k1 = getKey();  
            Object k2 = e.getKey();  
            if (k1 == k2 || (k1 != null && k1.equals(k2))) {  
                Object v1 = getValue();  
                Object v2 = e.getValue();  
                if (v1 == v2 || (v1 != null && v1.equals(v2)))  
                    return true;  
            }  
            return false;  
        }  
  
        public final int hashCode() {  
            return (key==null   ? 0 : key.hashCode()) ^  
                   (value==null ? 0 : value.hashCode());  
        }  
        ....  
```
这是一个HashMap类的内部静态类。实现了Map.Entry接口。接受两个模板参数K和V。key和hash一旦在构造函数中被初始化，就不可改变，并且由于有next的存在，Entry可以构成一个单向链表。
比较重要的是equals和hashCode方法。代码先列出来，后面再解释。
第二，初始容量的设定
大多数都在下面的构造函数里面.用于指定的initialCapacity不准小于0，也不能超过最大值。并且最终的capicity必须是2的n次方。还有如果使用了无参数的构造函数，默认会创建一个拥有16个元素的数组。
```java  
public HashMap(int initialCapacity, float loadFactor) {  
        if (initialCapacity < 0)  
            throw new IllegalArgumentException("Illegal initial capacity: " +  
                                               initialCapacity);  
        if (initialCapacity > MAXIMUM_CAPACITY)  
            initialCapacity = MAXIMUM_CAPACITY;  
        if (loadFactor <= 0 || Float.isNaN(loadFactor))  
            throw new IllegalArgumentException("Illegal load factor: " +  
                                               loadFactor);  
  
        // Find a power of 2 >= initialCapacity  
        int capacity = 1;  
        while (capacity < initialCapacity)  
            capacity <<= 1;  
  
        this.loadFactor = loadFactor;  
        threshold = (int)(capacity * loadFactor);  
        table = new Entry[capacity];  
        init();  
    }  
```
第三,什么时候应该调整数组的大小？
算法是这样，有一个变量size保存了实际数组已经使用了多少个元素，并且如果size的值达到了变量threshold的值，就必须扩充数组的容量。threshold=capicity*loadFactor.capicity是数组最大的容纳元素个数，loadFactor可以在构造函数中制定，否则采用默认值0.75f。capicity的最大值是1<<30(也就是2的30次方,1073741824).由此我们可以看到HashMap最多存放10亿多个链表。
第四，如何调整数组大小？
答案是2倍，很像C++里面的vector的分配策略。
```java   
void addEntry(int hash, K key, V value, int bucketIndex) {  
        Entry<K,V> e = table[bucketIndex];  
        table[bucketIndex] = new Entry<K,V>(hash, key, value, e);  
        if (size++ >= threshold)  
            resize(2 * table.length);  
    }  
```