在SQL中ANY和SOME是同义词，所以下面介绍的时候只使用ANY，SOME的用法和功能和ANY一模一样。和IN运算符不同，ANY必须和其他的比较运算符共同使用，而且必须将比较运算符放在ANY 关键字之前，所比较的值需要匹配子查询中的任意一个值，这也就是ANY在英文中所表示的意义。
首先看一个ANY 运算符和等于运算符（=）共同使用的例子，下面的SQL语句检索所有图书出版年份内入会的读者信息：
```java  
SELECT * FROM T_Reader WHERE FYearOfJoin =ANY(select FYearPublished FROM T_Book)
```
外部查询中的WHERE子句指定FYearOfJoin 必须等于子查询select FYearPublished FROM T_Book所返回的集合中的任意一个值。
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FID FNAME FYEAROFBIRTH FCITY FPROVINCE FYEAROFJOIN
1 Tom 1979 TangShan Hebei 2003
2 Sam 1981 LangFang Hebei 2001
3 Jerry 1966 DongGuan GuangDong 1995
4 Lily 1972 JiaXing ZheJiang 2005
5 Marry 1985 BeiJing BeiJing 1999
6 Kelly 1977 ZhuZhou HuNan 1995
7 Tim 1982 YongZhou HuNan 2001
9 John 1979 QingDao ShanDong 2003
11 July 1983 ZhuMaDian HeNan 1999
12 Fige 1981 JinCheng ShanXi 2003
```
这个SQL语句的检索结果与上一节介绍的使用IN 运算符得到的结果是一致的：
```java  
SELECT * FROM T_Reader WHERE FYearOfJoin IN(select FYearPublished FROM T_Book)
```
也就是说“=ANY”等价于IN 运算符，而“<>ANY”则等价于NOT IN 运算符。
除了等于运算符，ANY运算符还可以和大于（>）、小于(<)、大于等于（>=）、小于等于（<=）等比较运算符共同使用。比如下面的SQL语句用于检索在任何一个会员出生之前出版的图书：
```java  
SELECT * FROM T_Book WHERE FYearPublished<ANY(SELECT FYearOfBirth FROM T_Reader)
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FID FNAME FYEARPUBLISHED FCATEGORYID
6 History of China 1982 2
7 History of England 1860 2
8 History of America 1700 2
10 Atom 1930 3
11 RELATIVITY 1945 3
12 Computer 1970 3
13 Astronomy 1971 3
14 How To Singing 1771 5
```
注意，和IN 运算符不同，ANY 运算符不能与固定的集合相匹配，比如下面的SQL 语句是错误的：
```java  
SELECT * FROM T_Book WHERE FYearPublished<ANY(2001,2003,2005)
```
不过这个限制并不会妨碍功能的实现，因为没有对固定的集合进行ANY匹配的必要，因为待匹配的集合是固定的，所以上面的SQL语句完全可以用下面的SQL语句来代替：
```java  
SELECT * FROM T_Book WHERE FYearPublished<2005
```