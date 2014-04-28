Java 2集合框架图：
  
简化图：
  
Java平台提供了一个全新的集合框架。“集合框架”主要由一组用来操作对象的接口组成。不同接口描述一组不同数据类型。
集合接口：6个接口（短虚线表示），表示不同集合类型，是集合框架的基础。
抽象类：5个抽象类（长虚线表示），对集合接口的部分实现。可扩展为自定义集合类。
实现类：8个实现类（实线表示），对接口的具体实现。
在很大程度上，一旦您理解了接口，您就理解了框架。虽然您总要创建接口特定的实现，但访问实际集合的方法应该限制在接口方法的使用上；因此，允许您更改基 本的数据结构而不必改变其它代码。
Collection 接口是一组允许重复的对象。
Set 接口继承 Collection，但不允许重复，使用自己内部的一个排列机制。
List 接口继承 Collection，允许重复，以元素安插的次序来放置元素，不会重新排列。
Map接口是一组成对的键－值对象，即所持有的是key-value pairs。Map中不能有重复的key。拥有自己的内部排列机制。
容器中的元素类型都为Object。从容器取得元素时，必须把它转换成原来的类型。
集合接口 
1.Collection 接口
用于表示任何对象或元素组。想要尽可能以常规方式处理一组元素时，就使用这一接口。
  
(1) 单元素添加、删除操作：
```java  
boolean add(Object o):将对象添加给集合
boolean remove(Object o): 如果集合中有与o相匹配的对象，则删除对象o
```
(2) 查询操作：
```java  
int size() ：返回当前集合中元素的数量
boolean isEmpty() ：判断集合中是否有任何元素
boolean contains(Object o) ：查找集合中是否含有对象o
Iterator iterator() ：返回一个迭代器，用来访问集合中的各个元素
```
(3) 组操作：作用于元素组或整个集合
boolean containsAll(Collection c)：查找集合中是否含有集合c 中所有元素
boolean addAll(Collection c)：将集合c 中所有元素添加给该集合
void clear(): 删除集合中所有元素
void removeAll(Collection c)：从集合中删除集合c 中的所有元素
void retainAll(Collection c)：从集合中删除集合c 中不包含的元素
(4) Collection转换为Object数组：
Object[] toArray()：返回一个内含集合所有元素的array
Object[] toArray(Object[] a)：返回一个内含集合所有元素的array。运行期返回的array和参数a的型别相同，需要转换为正确型别。
此外，您还可以把集合转换成其它任何其它的对象数组。但是，您不能直接把集合转换成基本数据类型的数组，因为集合必须持有对象。
“斜体接口方法是可选的。因为一个接口实现必须实现所有接口方法，调用程序就需要一种途径来知道一个可选的方法是不是不受支持。如果调用一种可选方法 时，一个 UnsupportedOperationException 被抛出，则操作失败，因为方法不受支持。此异常类继承 RuntimeException 类，避免了将所有集合操作放入 try-catch 块。”
Collection不提供get()方法。如果要遍历Collectin中的元素，就必须用Iterator。
1.1.AbstractCollection 抽象类
AbstractCollection 类提供具体“集合框架”类的基本功能。虽然您可以自行实现 Collection 接口的所有方法，但是，除了iterator()和size()方法在恰当的子类中实现以外，其它所有方法都由 AbstractCollection 类来提供实现。如果子类不覆盖某些方法，可选的如add()之类的方法将抛出异常。
1.2.Iterator 接口
Collection 接口的iterator()方法返回一个 Iterator。Iterator接口方法能以迭代方式逐个访问集合中各个元素，并安全的从Collection 中除去适当的元素。
  
(1) boolean hasNext(): 判断是否存在另一个可访问的元素
Object next()：返回要访问的下一个元素。如果到达集合结尾，则抛出NoSuchElementException异常。
(2) void remove()：删除上次访问返回的对象。本方法必须紧跟在一个元素的访问后执行。如果上次访问后集合已被修改，方法将抛出IllegalStateException。
“Iterator中删除操作对底层Collection也有影响。”
迭代器是 故障快速修复（fail-fast）的。这意味着，当另一个线程修改底层集合的时候，如果您正在用 Iterator 遍历集合，那么，Iterator就会抛出 ConcurrentModificationException （另一种 RuntimeException异常）异常并立刻失败
2.List接口
List 接口继承了 Collection 接口以定义一个允许重复项的有序集合。该接口不但能够对列表的一部分进行处理，还添加了面向位置的操作。
  
(1) 面向位置的操作包括插入某个元素或 Collection 的功能，还包括获取、除去或更改元素的功能。在 List 中搜索元素可以从列表的头部或尾部开始，如果找到元素，还将报告元素所在的位置：
void add(int index, Object element)：在指定位置index上添加元素element。
boolean addAll(int index, Collection c)：将集合c的所有元素添加到指定位置index。
Object get(int index)：返回List中指定位置的元素。
int indexOf(Object o)：返回第一个出现元素o的位置，否则返回-1。
int lastIndexOf(Object o)：返回最后一个出现元素o的位置，否则返回-1。
Object remove(int index)：删除指定位置上的元素。
Object set(int index, Object element)：用元素element取代位置index上的元素，并且返回旧的元素。
(2) List 接口不但以位置序列迭代的遍历整个列表，还能处理集合的子集：
ListIterator listIterator() : 返回一个列表迭代器，用来访问列表中的元素。
ListIterator listIterator(int index) : 返回一个列表迭代器，用来从指定位置index开始访问列表中的元素。
List subList(int fromIndex, int toIndex) ：返回从指定位置fromIndex（包含）到toIndex（不包含）范围中各个元素的列表视图。
“对子列表的更改（如 add()、remove() 和 set() 调用）对底层 List 也有影响。”。
2.1.ListIterator接口
ListIterator 接口继承 Iterator 接口以支持添加或更改底层集合中的元素，还支持双向访问。ListIterator没有当前位置，光标位于调用previous和next方法返回的值之 间。一个长度为n的列表，有n+1个有效索引值：
  
(1) void add(Object o)：将对象o添加到当前位置的前面。
void set(Object o)：用对象o替代next或previous方法访问的上一个元素。如果上次调用后列表结构被修改了，那么将抛出IllegalStateException 异常。
(2) boolean hasPrevious()：判断向后迭代时是否有元素可访问。
Object previous()：返回上一个对象。
int nextIndex()：返回下次调用next方法时将返回的元素的索引。
int previousIndex()：返回下次调用previous方法时将返回的元素的索引。
“正常情况下，不用ListIterator改变某次遍历集合元素的方向 — 向前或者向后。虽然在技术上可以实现，但previous() 后立刻调用next()，返回的是同一个元素。把调用 next()和previous()的顺序颠倒一下，结果相同。”
“我们还需要稍微再解释一下 add() 操作。添加一个元素会导致新元素立刻被添加到隐式光标的前面。因此，添加元素后调用 previous() 会返回新元素，而调用 next() 则不起作用，返回添加操作之前的下一个元素。”
2.2.AbstractList和AbstractSequentialList抽象类
有两个抽象的 List 实现类：AbstractList 和 AbstractSequentialList。像 AbstractSet 类一样，它们覆盖了 equals() 和 hashCode() 方法以确保两个相等的集合返回相同的哈希码。若两个列表大小相等且包含顺序相同的相同元素，则这两个列表相等。这里的 hashCode() 实现在 List 接口定义中指定，而在这里实现。
除了equals()和hashCode()，AbstractList和 AbstractSequentialList实现了其余 List方法的一部分。因为数据的随机访问和顺序访问是分别实现的，使得具体列表实现的创建更为容易。需要定义的一套方法取决于您希望支持的行为。您永远不必亲自 提供的是 iterator方法的实现。
2.3. LinkedList类和ArrayList类
在“集合框架 ”中有两种常规的 List 实现：ArrayList 和 LinkedList。使用两种 List 实现的哪一种取决于您特定的需要。如果要支持随机访问，而不必在除尾部的任何位置插入或除去元素，那么，ArrayList提供了可选的集合。但如果，您要频繁的从列表的中间位置添加和除去元素，而只要顺序的访问列表元素，那么，LinkedList 实现更好。
“ArrayList 和 LinkedList 都实现 Cloneable 接口，都提供了两个构造函数，一个无参的，一个接受另一个Collection”
2.3.1. LinkedList类
LinkedList类添加了一些处理列表两端元素的方法。
  
(1) void addFirst(Object o)：将对象o添加到列表的开头。
void addLast(Object o)：将对象o添加到列表的结尾。
(2) Object getFirst()：返回列表开头的元素。
Object getLast()：返回列表结尾的元素。
(3) Object removeFirst()：删除并且返回列表开头的元素。
Object removeLast()：删除并且返回列表结尾的元素。
(4) LinkedList()：构建一个空的链接列表。
LinkedList(Collection c)：构建一个链接列表，并且添加集合c的所有元素。
“使用这些新方法，您就可以轻松的把 LinkedList 当作一个堆栈、队列或其它面向端点的数据结构。”
2.3.2. ArrayList类
ArrayList类封装了一个动态再分配的Object[]数组。每个ArrayList对象有一个capacity。这个capacity表示存储列表中元素的数组的容量。当元素添加到ArrayList时，它的capacity在常量时间内自动增加。
在向一个ArrayList对象添加大量元素的程序中，可使用ensureCapacity方法增加capacity。这可以减少增加重分配的数量。
(1) void ensureCapacity(int minCapacity)：将ArrayList对象容量增加minCapacity。
(2) void trimToSize()：整理ArrayList对象容量为列表当前大小。程序可使用这个操作减少ArrayList对象存储空间。
2.3.2.1. RandomAccess接口
一个特征接口。该接口没有任何方法，不过你可以使用该接口来测试某个集合是否支持有效的随机访问。ArrayList和Vector类用于实现该接口。
3.Set接口
Set 接口继承 Collection 接口，而且它不允许集合中存在重复项，每个具体的 Set 实现类依赖添加的对象的 equals()方法来检查独一性。Set接口没有引入新方法，所以Set就是一个Collection，只不过其行为不同。
  
3.1. Hash表
Hash表是一种数据结构，用来查找对象。Hash表为每个对象计算出一个整数，称为Hash Code(哈希码)。Hash表是个链接式列表的阵列。每个列表称为一个buckets(哈希表元)。对象位置的计算　index = HashCode % buckets (HashCode为对象哈希码，buckets为哈希表元总数)。
当你添加元素时，有时你会遇到已经填充了元素的哈希表元，这种情况称为Hash Collisions(哈希冲突)。这时，你必须判断该元素是否已经存在于该哈希表中。
如果哈希码是合理地随机分布的，并且哈希表元的数量足够大，那么哈希冲突的数量就会减少。同时，你也可以通过设定一个初始的哈希表元数量来更好地控制哈 希表的运行。初始哈希表元的数量为　buckets = size * 150% + 1 (size为预期元素的数量)。
如果哈希表中的元素放得太满，就必须进行rehashing(再哈希)。再哈希使哈希表元数增倍，并将原有的对象重新导入新的哈希表元中，而原始的哈希表元被删 除。load factor(加载因子)决定何时要对哈希表进行再哈希。在Java编程语言中，加载因子默认值为0.75，默认哈希表元为101。
3.2. Comparable接口和Comparator接口
在“集合框架”中有两种比较接口：Comparable接口和Comparator接口。像String和Integer等Java内建类实现 Comparable接口以提供一定排序方式，但这样只能实现该接口一次。对于那些没有实现Comparable接口的类、或者自定义的类，您可以通过 Comparator接口来定义您自己的比较方式。
3.2.1. Comparable接口
在java.lang包中，Comparable接口适用于一个类有自然顺序的时候。假定对象集合是同一类型，该接口允许您把集合排序成自然顺序。
(1) int compareTo(Object o)： 比较当前实例对象与对象o，如果位于对象o之前，返回负值，如果两个对象在排序中位置相同，则返回0，如果位于对象o后面，则返回正值
在 Java 2 SDK版本1.4中有二十四个类实现Comparable接口。下表展示了8种基本类型的自然排序。虽然一些类共享同一种自然排序，但只有相互可比的类才 能排序。
  
利用Comparable接口创建您自己的类的排序顺序，只是实现compareTo()方法的问题。通常就是依赖几个数据成员的自然排序。同时类也应该 覆盖equals()和hashCode()以确保两个相等的对象返回同一个哈希码。
3.2.2. Comparator接口
若一个类不能用于实现java.lang.Comparable，或者您不喜欢缺省的Comparable行为并想提供自己的排序顺序(可能多种排序方 式)，你可以实现Comparator接口，从而定义一个比较器。
(1)int compare(Object o1, Object o2)：对两个对象o1和o2进行比较，如果o1位于o2的前面，则返回负值，如果在排序顺序中认为o1和o2是相同的，返回0，如果o1位于o2的后面，则返回 正值
“与Comparable相似，0返回值不表示元素相等。一个0返回值只是表示两个对象排在同一位置。由Comparator用户决定如何处理。如果两个 不相等的元素比较的结果为零，您首先应该确信那就是您要的结果，然后记录行为。”
(2)boolean equals(Object obj): 指示对象obj是否和比较器相等。
“该方法覆写Object的equals()方法，检查的是Comparator实现的等同性，不是处于比较状态下的对象。”
3.3. SortedSet接口
“集合框架”提供了个特殊的Set接口：SortedSet，它保持元素的有序顺序。SortedSet接口为集的视图(子集)和它的两端（即头和尾） 提供了访问方法。当您处理列表的子集时，更改视图会反映到源集。此外，更改源集也会反映在子集上。发生这种情况的原因在于视图由两端的元素而不是下标元素 指定，所以如果您想要一个特殊的高端元素（toElement）在子集中，您必须找到下一个元素。
添加到SortedSet实现类的元素必须实现Comparable接口，否则您必须给它的构造函数提供一个Comparator接口的实现。 TreeSet类是它的唯一一份实现。
“因为集必须包含唯一的项，如果添加元素时比较两个元素导致了0返回值（通过Comparable的compareTo()方法或Comparator 的compare()方法），那么新元素就没有添加进去。如果两个元素相等，那还好。但如果它们不相等的话，您接下来就应该修改比较方法，让比较方法和 equals() 的效果一致。”
  
(1) Comparator comparator(): 返回对元素进行排序时使用的比较器，如果使用Comparable接口的compareTo()方法对元素进行比较，则返回null。
(2) Object first()：返回有序集合中第一个(最低)元素。
(3) Object last()：返回有序集合中最后一个(最高)元素。
(4) SortedSet subSet(Object fromElement, Object toElement)： 返回从fromElement(包括)至toElement(不包括)范围内元素的SortedSet视图(子集)。
(5) SortedSet headSet(Object toElement)：返回SortedSet的一个视图，其内各元素皆小于toElement。
(6) SortedSet tailSet(Object fromElement)：返回SortedSet的一个视图，其内各元素皆大于或等于fromElement。
3.4. AbstractSet抽象类
AbstractSet类覆盖了Object类的equals()和hashCode()方法，以确保两个相等的集返回相同的哈希码。若两个集大小相等且包含相同元素，则这两个集相等。按定义，集的哈希码是集中元素哈希码的总和。因此，不论集的内部顺序如何，两个相等的集会有相同的哈希码。
3.4.1. Object类
(1) boolean equals(Object obj)：对两个对象进行比较，以便确定它们是否相同。
(2) int hashCode()：返回该对象的哈希码，相同的对象必须返回相同的哈希码。
3.5. HashSet类类和TreeSet类
“集合框架”支持Set接口两种普通的实现：HashSet和TreeSet(TreeSet实现SortedSet接口)。在更多情况下，您会使用 HashSet 存储重复自由的集合。考虑到效率，添加到 HashSet 的对象需要采用恰当分配哈希码的方式来实现hashCode()方法。虽然大多数系统类覆盖了 Object中缺省的hashCode()和equals()实现，但创建您自己的要添加到HashSet的类时，别忘了覆盖 hashCode()和equals()。
当您要从集合中以有序的方式插入和抽取元素时，TreeSet实现会有用处。为了能顺利进行，添加到TreeSet的元素必须是可排序的。
3.5.1.HashSet类
(1) HashSet()：构建一个空的哈希集。
(2) HashSet(Collection c)：构建一个哈希集，并且添加集合c中所有元素。
(3) HashSet(int initialCapacity)：构建一个拥有特定容量的空哈希集。
(4) HashSet(int initialCapacity, float loadFactor)：构建一个拥有特定容量和加载因子的空哈希集。LoadFactor是0.0至1.0之间的一个数。
3.5.2. TreeSet类
(1) TreeSet()：构建一个空的树集。
(2) TreeSet(Collection c)：构建一个树集，并且添加集合c中所有元素。
(3) TreeSet(Comparator c)：构建一个树集，并且使用特定的比较器对其元素进行排序。
“comparator比较器没有任何数据，它只是比较方法的存放器。这种对象有时称为函数对象。函数对象通常在“运行过程中”被定义为匿名内部类的一个 实例。”
TreeSet(SortedSet s): 构建一个树集，添加有序集合s中所有元素，并且使用与有序集合s相同的比较器排序
3.6. LinkedHashSet类
LinkedHashSet扩展HashSet。如果想跟踪添加给HashSet的元素的顺序，LinkedHashSet实现会有帮助。 LinkedHashSet的迭代器按照元素的插入顺序来访问各个元素。它提供了一个可以快速访问各个元素的有序集合。同时，它也增加了实现的代价，因为 哈希表元中的各个元素是通过双重链接式列表链接在一起的。
(1) LinkedHashSet()：构建一个空的链接式哈希集。
(2) LinkedHashSet(Collection c)：构建一个链接式哈希集，并且添加集合c中所有元素。
(3) LinkedHashSet(int initialCapacity)：构建一个拥有特定容量的空链接式哈希集。
(4) LinkedHashSet(int initialCapacity, float loadFactor)：构建一个拥有特定容量和加载因子的空链接式哈希集。LoadFactor是0.0至1.0之间的一个数。
“为优化HashSet空间的使用，您可以调优初始容量和负载因子。TreeSet不包含调优选项，因为树总是平衡的。”
4. Map接口
Map接口不是Collection接口的继承。Map接口用于维护键/值对(key/value pairs)。该接口描述了从不重复的键到值的映射。
  
(1) 添加、删除操作：
Object put(Object key, Object value： 将互相关联的一个关键字与一个值放入该映像。如果该关键字已经存在，那么与此关键字相关的新值将取代旧值。方法返回关键字的旧值，如果关键字原先并不存 在，则返回null。
Object remove(Object key)：从映像中删除与key相关的映射。
void putAll(Map t)：将来自特定映像的所有元素添加给该映像。
void clear()：从映像中删除所有映射。
“键和值都可以为null。但是，您不能把Map作为一个键或值添加给自身。”
(2) 查询操作：
Object get(Object key)：获得与关键字key相关的值，并且返回与关键字key相关的对象，如果没有在该映像中找到该关键字，则返回null。
boolean containsKey(Object key)：判断映像中是否存在关键字key。
boolean containsValue(Object value)：判断映像中是否存在值value。
int size()：返回当前映像中映射的数量。
boolean isEmpty()：判断映像中是否有任何映射。
(3) 视图操作：处理映像中键/值对组。
Set keySet()：返回映像中所有关键字的视图集。
“因为映射中键的集合必须是唯一的，您用Set支持。你还可以从视图中删除元素，同时，关键字和它相关的值将从源映像中被删除，但是你不能添加任何元素。”
Collection values():返回映像中所有值的视图集
“因为映射中值的集合不是唯一的，您用Collection支持。你还可以从视图中删除元素，同时，值和它的关键字将从源映像中被删除，但是你不能添加任何元素。”
Set entrySet(): 返回Map.Entry对象的视图集，即映像中的关键字/值对
“因为映射是唯一的，您用Set支持。你还可以从视图中删除元素，同时，这些元素将从源映像中被删除，但是你不能添加任何元素。”
4.1. Map.Entry接口
Map的entrySet()方法返回一个实现Map.Entry接口的对象集合。集合中每个对象都是底层Map中一个特定的键/值对。
  
通过这个集合的迭代器，您可以获得每一个条目(唯一获取方式)的键或值并对值进行更改。当条目通过迭代器返回后，除非是迭代器自身的remove()方 法或者迭代器返回的条目的setValue()方法，其余对源Map外部的修改都会导致此条目集变得无效，同时产生条目行为未定义。
(1) Object getKey()：返回条目的关键字。
(2) Object getValue()：返回条目的值。
(3) Object setValue(Object value)：将相关映像中的值改为value，并且返回旧值。
4.2. SortedMap接口
“集合框架”提供了个特殊的Map接口：SortedMap，它用来保持键的有序顺序。
  
SortedMap接口为映像的视图(子集)，包括两个端点提供了访问方法。除了排序是作用于映射的键以外，处理SortedMap和处理 SortedSet一样。
添加到SortedMap实现类的元素必须实现Comparable接口，否则您必须给它的构造函数提供一个Comparator接口的实现。 TreeMap类是它的唯一一份实现。
“因为对于映射来说，每个键只能对应一个值，如果在添加一个键/值对时比较两个键产生了0返回值（通过Comparable的compareTo()方 法或通过Comparator的compare()方法），那么，原始键对应值被新的值替代。如果两个元素相等，那还好。但如果不相等，那么您就应该修改 比较方法，让比较方法和 equals() 的效果一致。”
(1) Comparator comparator()：返回对关键字进行排序时使用的比较器，如果使用Comparable接口的compareTo()方法对关键字进行比较，则返回null。
(2) Object firstKey()：返回映像中第一个(最低)关键字。
(3) Object lastKey()：返回映像中最后一个(最高)关键字。
(4) SortedMap subMap(Object fromKey, Object toKey)：返回从fromKey(包括)至toKey(不包括)范围内元素的SortedMap视图(子集)。
(5) SortedMap headMap(Object toKey)：返回SortedMap的一个视图，其内各元素的key皆小于toKey。
(6) SortedSet tailMap(Object fromKey)：返回SortedMap的一个视图，其内各元素的key皆大于或等于fromKey。
4.3. AbstractMap抽象类
和其它抽象集合实现相似，AbstractMap类覆盖了equals()和hashCode()方法以确保两个相等映射返回相同的哈希码。如果两个映射大小相等、包含同样的键且每个键在这两个映射中对应的值都相同，则这两个映射相等。映射的哈希码是映射元素哈希码的总和，其中每个元素是Map.Entry接口的一个实现。因此，不论映射内部顺序如何， 两个相等映射会报告相同的哈希码。
4.4. HashMap类和TreeMap类
“集合框架”提供两种常规的 Map实现：HashMap和TreeMap (TreeMap实现SortedMap接口)。在Map中插入、删除和定位元素，HashMap是最好的选择。但如果您要按自然顺序或自定义顺序遍历键，那么TreeMap会更好。使用HashMap要求添加的键类明确定义了hashCode()和 equals()的实现。
这个TreeMap没有调优选项，因为该树总处于平衡状态。
4.4.1. HashMap类
为了优化HashMap空间的使用，您可以调优初始容量和负载因子。
(1) HashMap()：构建一个空的哈希映像。
(2) HashMap(Map m)：构建一个哈希映像，并且添加映像m的所有映射。
(3) HashMap(int initialCapacity)：构建一个拥有特定容量的空的哈希映像。
(4) HashMap(int initialCapacity, float loadFactor)：构建一个拥有特定容量和加载因子的空的哈希映像。
4.4.2. TreeMap类
TreeMap没有调优选项，因为该树总处于平衡状态。
(1) TreeMap()：构建一个空的映像树。
(2) TreeMap(Map m)：构建一个映像树，并且添加映像m中所有元素。
(3) TreeMap(Comparator c)：构建一个映像树，并且使用特定的比较器对关键字进行排序。
(4) TreeMap(SortedMap s)：构建一个映像树，添加映像树s中所有映射，并且使用与有序映像s相同的比较器排序。
4.5. LinkedHashMap类
LinkedHashMap扩展HashMap，以插入顺序将关键字/值对添加进链接哈希映像中。象LinkedHashSet一 样，LinkedHashMap内部也采用双重链接式列表。
(1) LinkedHashMap()：构建一个空链接哈希映像。
(2) LinkedHashMap(Map m)：构建一个链接哈希映像,并且添加映像m中所有映射。
(3) LinkedHashMap(int initialCapacity)：构建一个拥有特定容量的空的链接哈希映像。
(4) LinkedHashMap(int initialCapacity, float loadFactor)：构建一个拥有特定容量和加载因子的空的链接哈希映像。
(5) LinkedHashMap(int initialCapacity, float loadFactor,
boolean accessOrder)：构建一个拥有特定容量、加载因子和访问顺序排序的空的链接哈希映像。
“如果将accessOrder设置为true,那么链接哈希映像将使用访问顺序而不是插入顺序来迭代各个映像。每次调用get或者put方法时，相关的映射便从它的当前位置上删除，然后放到链接式映像列表的结尾处（只有链接式映像列表中的位置才会受到影响，哈希表元则不受影响。哈希表映射总是待在对应于关键字的哈希码的哈希表元中）。”
“该特性对于实现高速缓存的“删除最近最少使用”的原则很有用。例如，你可以希望将最常访问的映射保存在内存中，并且从数据库中读取不经常访问的对象。当你在表中找不到某个映射，并且该表中的映射已经放得非常满时，你可以让迭代器进入该表，将它枚举的开头几个映射删除掉。这些是最近最少使用的映射。”
(6) protected boolean removeEldestEntry(Map.Entry eldest): 如果你想删除最老的映射，则覆盖该方法，以便返回true。当某个映射已经添加给映像之后，便调用该方法。它的默认实现方法返回false，表示默认条件下老的映射没有被删除。但是你可以重新定义本方法，以便有选择地在最老的映射符合某个条件，或者映像超过了某个大小时，返回true。
4.6. WeakHashMap类
WeakHashMap是Map的一个特殊实现，它使用WeakReference(弱引用)来存放哈希表关键字。使用这种方式时，当映射的键在 WeakHashMap 的外部不再被引用时，垃圾收集器会将它回收，但它将把到达该对象的弱引用纳入一个队列。WeakHashMap的运行将定期检查该队列，以便找出新到达的 弱应用。当一个弱引用到达该队列时，就表示关键字不再被任何人使用，并且它已经被收集起来。然后WeakHashMap便删除相关的映射。
(1) WeakHashMap(): 构建一个空弱哈希映像。
(2) WeakHashMap(Map t): 构建一个弱哈希映像,并且添加映像t中所有映射。
(3) WeakHashMap(int initialCapacity): 构建一个拥有特定容量的空的弱哈希映像。
(4) WeakHashMap(int initialCapacity, float loadFactor): 构建一个拥有特定容量和加载因子的空的弱哈希映像。
4.6. IdentityHashMap类
IdentityHashMap也是Map的一个特殊实现。在这个类中，关键字的哈希码不应该由hashCode()方法来计算，而应该由 System.identityHashCode方法进行计算(即使已经重新定义了hashCode方法)。这是Object.hashCode根据对象 的内存地址来计算哈希码时使用的方法。另外，为了对各个对象进行比较，IdentityHashMap将使用==，而不使用equals方法。
换句话说，不同的关键字对象，即使它们的内容相同，也被视为不同的对象。IdentityHashMap类可以用于实现对象拓扑结构转换 (topology-preserving object graph transformations)(比如实现对象的串行化或深度拷贝)，在进行转换时，需要一个“节点表”跟踪那些已经处理过的对象的引用。即使碰巧有对象相等，“节点表”也不应视其相等。另一个应用是维护代理对象。比如，调试工具希望在程序调试期间维护每个对象的一个代理对象。
“IdentityHashMap类不是一般意义的Map实现！它的实现有意的违背了Map接口要求通过equals方法比较对象的约定。这个类仅使用在很少发生的需要强调等同性语义的情况。”
(1) IdentityHashMap ()：构建一个空的全同哈希映像，默认预期最大尺寸为21“预期最大尺寸是映像期望把持的键/值映射的最大数目”。
(2) IdentityHashMap (Map m)：构建一个全同哈希映像,并且添加映像m中所有映射。
(3) IdentityHashMap (int expectedMaxSize)：构建一个拥有预期最大尺寸的空的全同哈希映像。放置超过预期最大尺寸的键/值映射时，将引起内部数据结构的增长，有时可能很费时。