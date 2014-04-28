在实现分页检索、排行榜等功能的时候，需要限制检索的结果集行数，不同的数据库系统对此的支持是不同的。
MYSQL中提供了LIMIT关键字用来限制返回的结果集，比如：
```java  
SELECT * FROM T_Employee ORDER BY FSalary DESC LIMIT 2,5
```
MSSQLServer：MSSQLServer中提供了TOP关键字用来返回结果集中的前N条记录，比如：
```java  
select top 5 * from T_Employee order by FSalary Desc；
```
在MSSQLServer2005中还可以使用窗口函数ROW_NUMBER()实现限制结果集行数，比如：
```java  
SELECT ROW_NUMBER() OVER(ORDER BY FSalary),FNumber,FName,FSalary,FAge FROM T_Employee。
```
Oracle：Oracle中支持窗口函数ROW_NUMBER()，其用法和MSSQLServer2005中相同；除了窗口函数ROW_NUMBER()，Oracle中还提供了更方便的rownum机制，Oracle为每个结果集都增加了一个默认的表示行号的列，这个列的名称为rownum。使用rownum可以很轻松的取得结果集中前N条的数据行，比如：
```java  
SELECT * FROM T_Employee WHERE rownum<=6 ORDER BY FSalary Desc
```
DB2：DB2中支持窗口函数ROW_NUMBER()，其用法和MSSQLServer2005以及Oracle中相同。除此之外，DB2还提供了FETCH关键字用来提取结果集的前N行，比如：
```java  
SELECT * FROM T_Employee ORDER BY FSalary Desc FETCH FIRST 6 ROWS ONLY
```