与标量子查询不同，列值子查询可以返回一个多行多列的结果集。这样的子查询又被称为表子查询，表子查询可以看作一个临时的表，表子查询可以用在SELECT 语句的FROM子句中、INSERT语句、连接、IN 子句等很多场合。
首先来看一个在FROM子句中使用的最简单的表子查询。SQL语句如下：
```java  
SELECT T_Reader.FName,t2.FYearPublished,t2.FName FROM T_Reader,(SELECT * FROM T_Book WHERE FYearPublished < 1800) t2
```
这里将T_Reader表和表子查询做交叉连接，并且将“SELECT * FROM T_Book WHERE FYearPublished < 1800”做为表子查询，还可以为表子查询执行表别名，在SELECT的列表中也可以使用和表一样的列名饮用方式，这与使用一个普通的数据表没有什么区别。
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName FYearPublished FName
Tom 1700 History of America
Sam 1700 History of America
Jerry 1700 History of America
Lily 1700 History of America
Marry 1700 History of America
Kelly 1700 History of America
Tim 1700 History of America
King 1700 History of America
John 1700 History of America
Lucy 1700 History of America
July 1700 History of America
Fige 1700 History of America
Tom 1771 How To Singing
Sam 1771 How To Singing
Jerry 1771 How To Singing
Lily 1771 How To Singing
Marry 1771 How To Singing
Kelly 1771 How To Singing
Tim 1771 How To Singing
King 1771 How To Singing
John 1771 How To Singing
Lucy 1771 How To Singing
July 1771 How To Singing
```
表子查询可以看作一张临时的表，所以引用子查询中列的时候必须使用子查询中定义的列名，也就是如果子查询中为列定义了别名，那么在引用的时候也要使用别名。比如下面的SQL语句：
```java  
SELECT T_Reader.FName,t2.FYear,t2.FName ,t2.F3 FROM T_Reader,(SELECT FYearPublished AS FYear,FName,1+2 as F3 FROM T_Book WHERE FYearPublished < 1800) t2
```
这里的表子查询为FYearPublished列取了一个别名FYear，这样在引用它的时候就必须使用FYear而不能继续使用FYearPublished这个名字，这里子查询中还增加了一个新列F3，同样可以在SELECT列表中引用它。
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName FYear FName F3
Tom 1700 History of America 3
Sam 1700 History of America 3
Jerry 1700 History of America 3
Lily 1700 History of America 3
Marry 1700 History of America 3
Kelly 1700 History of America 3
Tim 1700 History of America 3
King 1700 History of America 3
John 1700 History of America 3
Lucy 1700 History of America 3
July 1700 History of America 3
Fige 1700 History of America 3
Tom 1771 How To Singing 3
Sam 1771 How To Singing 3
Jerry 1771 How To Singing 3
Lily 1771 How To Singing 3
Marry 1771 How To Singing 3
Kelly 1771 How To Singing 3
Tim 1771 How To Singing 3
King 1771 How To Singing 3
John 1771 How To Singing 3
Lucy 1771 How To Singing 3
July 1771 How To Singing 3
```