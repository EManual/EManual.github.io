ALL在英文中的意思是“所有”，ALL运算符要求比较的值需要匹配子查询中的所有值。ALL运算符同样不能单独使用，必须和比较运算符共同使用。
下面的SQL语句用来检索在所有会员入会之前出版的图书：
```java  
SELECT * FROM T_Book WHERE FYearPublished<ALL(SELECT FYearOfJoin FROM T_Reader)
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FYearPublished FCategoryId
6 History of China 1982 2
7 History of England 1860 2
8 History of America 1700 2
10 Atom 1930 3
11 RELATIVITY 1945 3
12 Computer 1970 3
13 Astronomy 1971 3
14 How To Singing 1771 5
```
与ANY 运算符相同，ALL 运算符同样不能与固定的集合相匹配，比如下面的SQL语句是错误的：
```java  
SELECT * FROM T_Book WHERE FYearPublished<ALL(2001,2003,2005)
```
不过这个限制并不会妨碍功能的实现，因为没有对固定的集合进行ALL匹配的必要，因为待匹配的集合是固定的，所以上面的SQL语句完全可以用下面的SQL语句来代替：
```java  
SELECT * FROM T_Book WHERE FYearPublished<2001
```
另外需要注意的就是，当使用ALL运算符的时候，如果带匹配的集合为空，也就是子查询没有返回任何数据的时候，不论与什么比较运算符搭配使用ALL的返回值将永远是true。比如下面的SQL语句用于检索在所有江苏省会员入会之前出版的图书：
```java  
SELECT * FROM T_Book WHERE FYearPublished<ALL(SELECT FYearOfJoin FROM T_Reader WHERE FProvince = "JiangSu")
```
执行完毕我们就能在输出结果中看到下面的执行结果：
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
这个查询结果将所有的会员都检索出来了，可是根本没有江苏省的会员，应该是返回空结果才对的。看起来这是错误的，其实这完全符合ALL 运算符的语义，因为没有江苏省的会员，所以每本书的出版年份就在所有的江苏省的会员之前，所以每一本书都符合匹配条件。在使用ALL运算符的时候，这一个问题很容易在系统中造成BUG，因此使用时必须注意。