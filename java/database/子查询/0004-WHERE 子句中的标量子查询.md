标量子查询不仅可以用在SELECT 语句的列表中，它还可以用在WHERE 子句中，而且实际应用中子查询很多的时候都是用在WHERE子句中的。
先来看一个简单的例子，我们要检索喜欢“Story”的读者主键列表，那么这可以使用连接来完成，不过这里我们将使用子查询来完成。
使用子查询的实现思路也比使用连接简单。首先肯定要到T_Category 表中查找FName等于“Story”的记录的FId字段值：
```java  
SELECT FId FROM T_Category WHERE FName=" Story "
```
因为这个查询的返回值是单列且单行的，所以可以当作标量子查询使用。将这个子查询结果来构造外部查询：
```java  
SELECT FReaderId FROM T_ReaderFavorite WHERE FCategoryId=(SELECT FId FROM T_Category WHERE FName="Story")
```
执行这个SQL语句则会得到下面的执行结果：
```java  
FReaderId
1
6
7
12
3
```
下面来看一个稍微复杂一点的例子。假设需要检索每一种书籍类别中出版年份最早的书籍的名称，如果有两本或者多本书籍在同一年出版，则均显示它们的名字。要求检索结果中显示出类型的名字、书的名字和它的出版年份。
检索每种类型图书中出版时间最早的图书非常简单，只要使用GROUP BY 子句以及聚合函数就可以轻松完成这个任务，SQL语句如下：
```java  
SELECT T_Category.FId,MIN(T_Book.FYearPublished) FROM T_Category INNER JOIN T_Book ON T_Category.FId=T_Book.FCategoryId GROUP BY T_Category.FId
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId
1 1999
2 1700
3 1930
4 2003
5 1771
6 1995
```
查询结果是正确的，不过这个查询结果没有提供书名，只提供了类型主键和出版时间最早的图书的出版年份。尝试将图书的名字加入到SELECT语句中，如下：
```java  
SELECT T_Category.FId, T_Book. FName,MIN(T_Book.FYearPublished) FROM T_Category INNER JOIN T_Book ON T_Category.FId=T_Book.FCategoryId GROUP BY T_Category.FId
```
在数据库系统中执行这个SQL语句会报出如下的错误信息：
* 选择列表中的列"T_Book.FName" 无效，因为该列没有包含在聚合函数或GROUP BY子句中。
出现这个错误的原因是所有在SELECT列表中的字段如果没有包含在聚合函数中，则必须放到GROUP BY 子句中，所以将T_Book. FName加入到GROUP BY 子句中，修改后的SQL语句如下：
```java  
SELECT T_Category.FId, T_Book. FName,MIN(T_Book.FYearPublished) FROM T_Category INNER JOIN T_Book ON T_Category.FId=T_Book.FCategoryId GROUP BY T_Category.FId, T_Book. FName
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName
1 Jane Eyre 2001
1 Oliver Twist 2002
1 Two Cites 1999
2 History of America 1700
2 History of China 1982
2 History of England 1860
2 History of TheWorld 2008
3 Astronomy 1971
3 Atom 1930
3 Computer 1970
3 RELATIVITY 1945
4 About J2EE 2005
4 Learning Hibernate 2003
5 How To Singing 1771
6 DaoDeJing 2001
6 Obedience to Authority 1995
```
这个执行结果显然是错误的，因为它们是根据T_Category.FId和T_Book.FName这两个字段进行的分组，所以MIN(T_Book.FYearPublished)返回值不是一个特定书籍类型的最早出版年份，而是每本图书中的最早出版年份。而真正需要的是查询每种书籍类型中的最早出版的书籍，可以使用子查询来轻松完成这个任务。在SQL查询中，需要将一本书籍的出版年份与该类型的所有书籍的出版年份进行比较，并且仅仅在它们匹配时，才返回一个记录，实现SQL语句如下：
```java  
SELECT T_Category.FId, T_Book. FName,T_Book.FYearPublished FROM T_Category INNER JOIN T_Book ON T_Category.FId=T_Book.FCategoryId WHERE T_Book.FYearPublished=(SELECT MIN(T_Book.FYearPublished) FROM T_Book WHERE T_Book.FCategoryId=T_Category.FId)
```
在这个SQL语句中，T_Category表和T_Book表首先进行内部连接，然后使用WHERE子句中使用子查询来进行数据的过滤。这个子查询是一个相关子查询，它返回外部查询中当前图书类别中的图书的最早出版年份。在外部查询的WHERE子句中，T_Book的FYearPublished与子查询的返回值进行比较，这样就可以得到每种书籍类型中的出版最早的书籍了。
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FYearPublished
1 Two Cites 1999
2 History of America 1700
3 Atom 1930
4 Learning Hibernate 2003
5 How To Singing 1771
6 Obedience to Authority 1995
```