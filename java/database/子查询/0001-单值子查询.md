单值子查询的语法和普通的SELECT语句没有什么不同，唯一的限制就是子查询的返回值必须只有一行记录，而且只能有一个列。这样的子查询又被称为标量子查询，标量子查询可以用在SELECT语句的列表中、表达式中、WHERE 语句中等很多场合。
首先来看一个在SELECT语句列表中使用的最简单的标量子查询。SQL语句如下：
```java  
MYSQL,MSSQLServer：
SELECT 1 AS f1,2,(SELECT MIN(FYearPublished) FROM T_Book),(SELECT MAX(FYearPublished) FROM T_Book) AS f4
Oracle：
SELECT 1 AS f1,2,(SELECT MIN(FYearPublished) FROM T_Book),(SELECT MAX(FYearPublished) FROM T_Book) AS f4 FROM DUAL
DB2：
SELECT 1 AS f1,2,(SELECT MIN(FYearPublished) FROM T_Book),(SELECT MAX(FYearPublished) FROM T_Book) AS f4 FROM SYSIBM.SYSDUMMY1
```
这个SQL语句一共返回四列，第一列是数字1，第二列是数字2，第三列则是一个标量子查询，它返回最早出版图书的年份，第四列也是一个标量子查询，它返回最晚出版图书的年份。这里完全可以将标量子查询当成一个普通的列，而且还可以为标量子查询列取一个别名。
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
f1 f4
1 2 1700 2008
```
如果一个子查询返回值不止一行记录或者有多个列的话都不能当作标量子查询使用，否则会出错。比如下面SQL语句是错的：
SELECT 1 AS f1,2,(SELECT FYearPublished FROM T_Book)
由于这句SQL 语句中的子查询会返回多行记录，所以在执行的时候数据库会提示如下的错误信息：
* 子查询返回的值不止一个。
当子查询跟随在 =、!=、<、<=、>、>= 之后，或子查询用作表达式时，这种情况是不允许的。
下面的SQL 语句也是错误的：
```java  
SELECT 1 AS f1,2,(SELECT MAX(FYearPublished),MIN(FYearPublished) FROM T_Book)
```
由于这句SQL语句中的子查询会返回包含两列数据的结果集，所以在执行的时候数据库会提示如下的错误信息：
* 当没有用EXISTS 引入子查询时，在选择列表中只能指定一个表达式。
上面举的例子都是在执行前就能确定是否正确的，但是有的时候一个子查询是否使用正确是要到运行时才能确定的。比如在数据库系统中执行下面的SQL语句：
```java  
SELECT 1 AS f1,2,(SELECT FYearPublished FROM T_Book where FYearPublished<2000)
```
在数据库系统中执行后这句SQL语句会报错，因为发行日期小于2000年的书有不止一本，所以子查询的返回结果集也就有不止一条记录。如果我们调整这句SQL 语句，转而查询发行日期小于1750年的书，SQL语句如下：
```java  
SELECT 1 AS f1,2,(SELECT FYearPublished FROM T_Book where FYearPublished<1750)
```
因为数据库中发行日期小于1750年的书恰恰只有一本，所以这句SQL语句能够执行成功，执行结果如下：
```java  
f1
1 2 1700
```