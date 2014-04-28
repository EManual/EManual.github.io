1. ArrayList概述：
ArrayList是List接口的可变数组的实现。实现了所有可选列表操作，并允许包括 null 在内的所有元素。除了实现List接口外，此类还提供一些方法来操作内部用来存储列表的数组的大小。
每个ArrayList实例都有一个容量，该容量是指用来存储列表元素的数组的大小。它总是至少等于列表的大小。随着向ArrayList中不断添加元 素，其容量也自动增长。自动增长会带来数据向新数组的重新拷贝，因此，如果可预知数据量的多少，可在构造ArrayList时指定其容量。在添加大量元素 前，应用程序也可以使用ensureCapacity操作来增加ArrayList实例的容量，这可以减少递增式再分配的数量。 
注意，此实现不是同步的。如果多个线程同时访问一个ArrayList实例，而其中至少一个线程从结构上修改了列表，那么它必须保持外部同步。
2. ArrayList的实现：
对于ArrayList而言，它实现List接口、底层使用数组保存所有元素。其操作基本上是对数组的操作。下面我们来分析ArrayList的源代码：
1) 底层使用数组实现：
```java  
private transient Object[] elementData;  
private transient Object[] elementData; 
``` 
2) 构造方法： 
ArrayList提供了三种方式的构造器，可以构造一个默认初始容量为10的空列表、构造一个指定初始容量的空列表以及构造一个包含指定collection的元素的列表，这些元素按照该collection的迭代器返回它们的顺序排列的。
```java   
public ArrayList() {  
    this(10);  
}  
  
public ArrayList(int initialCapacity) {  
    super();  
    if (initialCapacity < 0)  
        throw new IllegalArgumentException("Illegal Capacity: "+ initialCapacity);  
    this.elementData = new Object[initialCapacity];  
}  
  
public ArrayList(Collection<? extends E> c) {  
    elementData = c.toArray();  
    size = elementData.length;  
    // c.toArray might (incorrectly) not return Object[] (see 6260652)  
    if (elementData.getClass() != Object[].class)  
        elementData = Arrays.copyOf(elementData, size, Object[].class);  
}  

public ArrayList() {  
    this(10);  
}  
  
public ArrayList(int initialCapacity) {  
    super();  
    if (initialCapacity < 0)  
        throw new IllegalArgumentException("Illegal Capacity: "+ initialCapacity);  
    this.elementData = new Object[initialCapacity];  
}  
  
public ArrayList(Collection<? extends E> c) {  
    elementData = c.toArray();  
    size = elementData.length;  
    // c.toArray might (incorrectly) not return Object[] (see 6260652)  
    if (elementData.getClass() != Object[].class)  
        elementData = Arrays.copyOf(elementData, size, Object[].class);  
}
```  
3) 存储： 
ArrayList提供了set(int index, E element)、add(E e)、add(int index, E element)、addAll(Collection<? extends E> c)、addAll(int index, Collection<? extends E> c)这些添加元素的方法。下面我们一一讲解：
```java  
// 用指定的元素替代此列表中指定位置上的元素，并返回以前位于该位置上的元素。  
public E set(int index, E element) {  
    RangeCheck(index);  
  
    E oldValue = (E) elementData[index];  
    elementData[index] = element;  
    return oldValue;  
}  

// 用指定的元素替代此列表中指定位置上的元素，并返回以前位于该位置上的元素。  
public E set(int index, E element) {  
    RangeCheck(index);  
  
    E oldValue = (E) elementData[index];  
    elementData[index] = element;  
    return oldValue;  
}  

// 将指定的元素添加到此列表的尾部。  
public boolean add(E e) {  
    ensureCapacity(size + 1);   
    elementData[size++] = e;  
    return true;  
}  

// 将指定的元素添加到此列表的尾部。  
public boolean add(E e) {  
    ensureCapacity(size + 1);   
    elementData[size++] = e;  
    return true;  
}  
 
// 将指定的元素插入此列表中的指定位置。  
// 如果当前位置有元素，则向右移动当前位于该位置的元素以及所有后续元素（将其索引加1）。  
public void add(int index, E element) {  
    if (index > size || index < 0)  
        throw new IndexOutOfBoundsException("Index: "+index+", Size: "+size);  
    // 如果数组长度不足，将进行扩容。  
    ensureCapacity(size+1);  // Increments modCount!!  
    // 将 elementData中从Index位置开始、长度为size-index的元素，  
    // 拷贝到从下标为index+1位置开始的新的elementData数组中。  
    // 即将当前位于该位置的元素以及所有后续元素右移一个位置。  
    System.arraycopy(elementData, index, elementData, index + 1, size - index);  
    elementData[index] = element;  
    size++;  
}  

// 将指定的元素插入此列表中的指定位置。  
// 如果当前位置有元素，则向右移动当前位于该位置的元素以及所有后续元素（将其索引加1）。  
public void add(int index, E element) {  
    if (index > size || index < 0)  
        throw new IndexOutOfBoundsException("Index: "+index+", Size: "+size);  
    // 如果数组长度不足，将进行扩容。  
    ensureCapacity(size+1);  // Increments modCount!!  
    // 将 elementData中从Index位置开始、长度为size-index的元素，  
    // 拷贝到从下标为index+1位置开始的新的elementData数组中。  
    // 即将当前位于该位置的元素以及所有后续元素右移一个位置。  
    System.arraycopy(elementData, index, elementData, index + 1, size - index);  
    elementData[index] = element;  
    size++;  
}  
 
// 按照指定collection的迭代器所返回的元素顺序，将该collection中的所有元素添加到此列表的尾部。  
public boolean addAll(Collection<? extends E> c) {  
    Object[] a = c.toArray();  
    int numNew = a.length;  
    ensureCapacity(size + numNew);  // Increments modCount  
    System.arraycopy(a, 0, elementData, size, numNew);  
    size += numNew;  
    return numNew != 0;  
}  

// 按照指定collection的迭代器所返回的元素顺序，将该collection中的所有元素添加到此列表的尾部。  
public boolean addAll(Collection<? extends E> c) {  
    Object[] a = c.toArray();  
    int numNew = a.length;  
    ensureCapacity(size + numNew);  // Increments modCount  
    System.arraycopy(a, 0, elementData, size, numNew);  
    size += numNew;  
    return numNew != 0;  
}  
 
// 从指定的位置开始，将指定collection中的所有元素插入到此列表中。  
public boolean addAll(int index, Collection<? extends E> c) {  
    if (index > size || index < 0)  
        throw new IndexOutOfBoundsException(  
            "Index: " + index + ", Size: " + size);  
  
    Object[] a = c.toArray();  
    int numNew = a.length;  
    ensureCapacity(size + numNew);  // Increments modCount  
  
    int numMoved = size - index;  
    if (numMoved > 0)  
        System.arraycopy(elementData, index, elementData, index + numNew, numMoved);  
  
    System.arraycopy(a, 0, elementData, index, numNew);  
    size += numNew;  
    return numNew != 0;  
}  

// 从指定的位置开始，将指定collection中的所有元素插入到此列表中。  
public boolean addAll(int index, Collection<? extends E> c) {  
    if (index > size || index < 0)  
        throw new IndexOutOfBoundsException(  
            "Index: " + index + ", Size: " + size);  
  
    Object[] a = c.toArray();  
    int numNew = a.length;  
    ensureCapacity(size + numNew);  // Increments modCount  
  
    int numMoved = size - index;  
    if (numMoved > 0)  
        System.arraycopy(elementData, index, elementData, index + numNew, numMoved);  
  
    System.arraycopy(a, 0, elementData, index, numNew);  
    size += numNew;  
    return numNew != 0;  
}  
```
4) 读取：
```java   
// 返回此列表中指定位置上的元素。  
public E get(int index) {  
    RangeCheck(index);  
  
    return (E) elementData[index];  
}  
[java] view plaincopy
// 返回此列表中指定位置上的元素。  
public E get(int index) {  
    RangeCheck(index);  
  
    return (E) elementData[index];  
}  
```
5) 删除： 
ArrayList提供了根据下标或者指定对象两种方式的删除功能。如下：
```java   
// 移除此列表中指定位置上的元素。  
public E remove(int index) {  
    RangeCheck(index);  
  
    modCount++;  
    E oldValue = (E) elementData[index];  
  
    int numMoved = size - index - 1;  
    if (numMoved > 0)  
        System.arraycopy(elementData, index+1, elementData, index, numMoved);  
    elementData[--size] = null; // Let gc do its work  
  
    return oldValue;  
}  

// 移除此列表中指定位置上的元素。  
public E remove(int index) {  
    RangeCheck(index);  
  
    modCount++;  
    E oldValue = (E) elementData[index];  
  
    int numMoved = size - index - 1;  
    if (numMoved > 0)  
        System.arraycopy(elementData, index+1, elementData, index, numMoved);  
    elementData[--size] = null; // Let gc do its work  
  
    return oldValue;  
}  
 
// 移除此列表中首次出现的指定元素（如果存在）。这是应为ArrayList中允许存放重复的元素。  
public boolean remove(Object o) {  
    // 由于ArrayList中允许存放null，因此下面通过两种情况来分别处理。  
    if (o == null) {  
        for (int index = 0; index < size; index++)  
            if (elementData[index] == null) {  
                // 类似remove(int index)，移除列表中指定位置上的元素。  
                fastRemove(index);  
                return true;  
            }  
} else {  
    for (int index = 0; index < size; index++)  
        if (o.equals(elementData[index])) {  
            fastRemove(index);  
            return true;  
        }  
    }  
    return false;  
}  

// 移除此列表中首次出现的指定元素（如果存在）。这是应为ArrayList中允许存放重复的元素。  
public boolean remove(Object o) {  
    // 由于ArrayList中允许存放null，因此下面通过两种情况来分别处理。  
    if (o == null) {  
        for (int index = 0; index < size; index++)  
            if (elementData[index] == null) {  
                // 类似remove(int index)，移除列表中指定位置上的元素。  
                fastRemove(index);  
                return true;  
            }  
} else {  
    for (int index = 0; index < size; index++)  
        if (o.equals(elementData[index])) {  
            fastRemove(index);  
            return true;  
        }  
    }  
    return false;  
}  
```
注意：从数组中移除元素的操作，也会导致被移除的元素以后的所有元素的向左移动一个位置。
6) 调整数组容量： 
从上面介绍的向ArrayList中存储元素的代码中，我们看到，每当向数组中添加元素时，都要去检查添加后元素的个数是否会超出当前数组的长度，如果超 出，数组将会进行扩容，以满足添加数据的需求。数组扩容通过一个公开的方法ensureCapacity(int minCapacity)来实现。在实际添加大量元素前，我也可以使用ensureCapacity来手动增加ArrayList实例的容量，以减少递增 式再分配的数量。
```java  
public void ensureCapacity(int minCapacity) {  
    modCount++;  
    int oldCapacity = elementData.length;  
    if (minCapacity > oldCapacity) {  
        Object oldData[] = elementData;  
        int newCapacity = (oldCapacity * 3)/2 + 1;  
            if (newCapacity < minCapacity)  
                newCapacity = minCapacity;  
      // minCapacity is usually close to size, so this is a win:  
      elementData = Arrays.copyOf(elementData, newCapacity);  
    }  
}  

public void ensureCapacity(int minCapacity) {  
    modCount++;  
    int oldCapacity = elementData.length;  
    if (minCapacity > oldCapacity) {  
        Object oldData[] = elementData;  
        int newCapacity = (oldCapacity * 3)/2 + 1;  
            if (newCapacity < minCapacity)  
                newCapacity = minCapacity;  
      // minCapacity is usually close to size, so this is a win:  
      elementData = Arrays.copyOf(elementData, newCapacity);  
    }  
} 
``` 
从上述代码中可以看出，数组进行扩容时，会将老数组中的元素重新拷贝一份到新的数组中，每次数组容量的增长大约是其原容量的1.5倍。这种操作的代价是很 高的，因此在实际使用时，我们应该尽量避免数组容量的扩张。当我们可预知要保存的元素的多少时，要在构造ArrayList实例时，就指定其容量，以避免 数组扩容的发生。或者根据实际需求，通过调用ensureCapacity方法来手动增加ArrayList实例的容量。
ArrayList还给我们提供了将底层数组的容量调整为当前列表保存的实际元素的大小的功能。它可以通过trimToSize方法来实现。代码如下：
```java  
public void trimToSize() {  
    modCount++;  
    int oldCapacity = elementData.length;  
    if (size < oldCapacity) {  
        elementData = Arrays.copyOf(elementData, size);  
    }  
}  

public void trimToSize() {  
    modCount++;  
    int oldCapacity = elementData.length;  
    if (size < oldCapacity) {  
        elementData = Arrays.copyOf(elementData, size);  
    }  
}  
```
7) Fail-Fast机制： 
ArrayList也采用了快速失败的机制，通过记录modCount参数来实现。在面对并发的修改时，迭代器很快就会完全失败，而不是冒着在将来某个不确定时间发生任意不确定行为的风险。具体介绍请参考我之前的文章深入Java集合学习系列：HashMap的实现原理 中的Fail-Fast机制。
8) 关于其他 的一些方法的实现都很简单易懂，读者可参照API文档和源代码，一看便知，这里就不再多说。