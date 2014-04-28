和IN、ANY、ALL等运算符不同，EXISTS运算符是单目运算符，它不与列匹配，因此它也不要求待匹配的集合是单列的。EXISTS运算符用来检查每一行是否匹配子查询，可以认为EXISTS就是用来测试子查询的结果是否为空，如果结果集为空则匹配结果为false，否则匹配结果为true。
先来看一个简单的SQL语句：
```java  
SELECT * FROM T_Book WHERE EXISTS(SELECT * FROM T_Reader WHERE FProvince="ShanDong")
```
这句SQL语句对T_Book表中的每行数据进行匹配，测试是否存在山东省的读者，因为系统中存在山东省的读者，所以这个SQL语句将检索出所有的图书。执行结果如下：
```java  
FId FName FYearPublished FCategoryId
1 About J2EE 2005 4
2 Learning Hibernate 2003 4
3 Two Cites 1999 1
4 Jane Eyre 2001 1
5 Oliver Twist 2002 1
6 History of China 1982 2
7 History of England 1860 2
8 History of America 1700 2
9 History of TheWorld 2008 2
10 Atom 1930 3
11 RELATIVITY 1945 3
12 Computer 1970 3
13 Astronomy 1971 3
14 How To Singing 1771 5
15 DaoDeJing 2001 6
16 Obedience toAuthority 1995 6
```
再来看另外一个SQL语句：
```java  
SELECT * FROM T_Book WHERE EXISTS(SELECT * FROM T_Reader WHERE FProvince="YunNan")
```
这句SQL语句对T_Book表中的每行数据进行匹配，测试是否存在云南省的读者，因为系统中不存在云南省的读者，所以这个SQL语句的执行结果为空。
从前面几个例子来看，使用EXISTS运算符要么就是匹配返回表中所有数据，要么就是不匹配不返回任何数据，好像EXISTS运算符并没有太大意义，其实上面这两个例子在实际中并不常用，EXISTS运算符的真正意义只有和相关子查询一起使用才更有意义。相关子查询中引用外部查询中的这个字段，这样在匹配外部子查询中的每行数据的时候相关子查询就会根据当前行的信息来进行匹配判断了，这样就可以完成非常丰富的功能。
下面的SQL语句用来检索存在1950 年以前出版的图书的图书类别：
```java  
SELECT * FROM T_Category WHERE EXISTS(SELECT * FROM T_Book WHERE T_Book. FCategoryId = T_Category.FId AND T_Book.FYearPublished<1950)
```
在EXISTS后的子查询中，SQL对T_Category表中的每一行数据到子查询中进行匹配，测试T_Book 表中是否存在FCategoryId 字段值等于当前类别主键值且出版年份在1950年之前的书籍。执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName
2 History
3 Theory
5 Art
```