在进行数据检索的时候有时候需要只检索结果集中的部分行，比如说“检索成绩排前三名的学生”、“检索工资水平排在第3位到第7位的员工信息”，这种功能被称为“限制结果集行数”。在虽然主流的数据库系统中都提供了限制结果集行数的方法，但是无论是语法还是使用方式都存在着很大的差异，即使是同一个数据库系统的不同版本（比如
MSSQLServer2000和MSSQLServer2005）也存在着一定的差异。因此本节将按照数据库系统来讲解每种数据库系统对限制结果集行数的特性支持。
* MYSQL
MYSQL中提供了LIMIT关键字用来限制返回的结果集，LIMIT放在SELECT语句的最后位置，语法为“LIMIT 首行行号，要返回的结果集的最大数目”。比如下面的SQL语句将返回按照工资降序排列的从第二行开始（行号从0开始）的最多五条记录：
```java  
SELECT * FROM T_Employee ORDER BY FSalary DESC LIMIT 2,5
```
很显然，下面的SQL语句将返回按照工资降序排列的前五条记录：
```java  
SELECT * FROM T_Employee ORDER BY FSalary DESC LIMIT 0,5
```
* MSSQLServer2000
MSSQLServer2000中提供了TOP关键字用来返回结果集中的前N条记录，其语法为“SELECT TOP 限制结果集数目字段列表SELECT语句其余部分”，比如下面的SQL语句用来检索工资水平排在前五位（按照工资从高到低）的员工信息：
```java  
select top 5 * from T_Employee order by FSalary Desc
```
MSSQLServer2000没有直接提供返回提供“检索从第5行开始的10条数据”、“检索第五行至第十二行的数据”等这样的取区间范围的功能，不过可以采用其他方法来变通实现，最常使用的方法就是用子查询9，比如要实现检索按照工资从高到低排序检索从第六名开始一共三个人的信息，那么就可以首先将前五名的主键取出来，在检索的时候检索排除了这五名员工的前三个人，SQL如下：
```java  
SELECT top 3 * FROM T_Employee WHERE FNumber NOT IN(SELECT TOP 5 FNumber FROM T_Employee ORDER BY FSalary DESC) ORDER BY FSalary DESC 
```
* MSSQLServer2005
MSSQLServer2005兼容几乎所有的MSSQLServer2000的语法，所以可以使用上个小节提到的方式来在MSSQLServer2005中实现限制结果集行数，不过MSSQLServer2005提供了新的特性来帮助更好的限制结果集行数的功能，这个新特性就是窗口函数ROW_NUMBER()。
ROW_NUMBER()函数可以计算每一行数据在结果集中的行号（从1开始计数），其使用语法如下：
ROW_NUMBER OVER(排序规则)
比如我们执行下面的SQL语句：
```java  
SELECT ROW_NUMBER() OVER(ORDER BY FSalary),FNumber,FName,FSalary,FAge FROM T_Employee
```
可以看到第一列中的数据就是通过ROW_NUMBER()计算出来的行号。有的开发人员想使用如下的方式来实现返回第3行到第5行的数据（按照工资降序）：
```java  
SELECT ROW_NUMBER() OVER(ORDER BY FSalary DESC),FNumber,FName,FSalary,FAge FROM T_Employee WHERE (ROW_NUMBER() OVER(ORDER BY FSalary DESC))>=3 AND (ROW_NUMBER() OVER(ORDER BY FSalary DESC))<=5
```
但是在运行的时候数据库系统会报出下面的错误信息：
开窗函数只能出现在SELECT 或ORDER BY 子句中。
也就是说ROW_NUMBER()不能用在WHERE语句中。我们可以用子查询来解决这个问题，下面
的SQL语句用来返回第3行到第5行的数据：
```java  
SELECT * FROM(SELECT ROW_NUMBER() OVER(ORDER BY FSalary DESC) AS rownum,FNumber,FName,FSalary,FAge FROM T_Employee) AS a
WHERE a.rownum>=3 AND a.rownum<=5
```
* Oracle
Oracle中支持窗口函数ROW_NUMBER()，其用法和MSSQLServer2005中相同，比如我们
执行下面的SQL语句：
```java  
SELECT * FROM(SELECT ROW_NUMBER() OVER(ORDER BY FSalary DESC) row_num,FNumber,FName,FSalary,FAge FROM T_Employee) a
WHERE a.row_num>=3 AND a.row_num<=5
```
注意：rownum在Oracle中为保留字，所以这里将MSSQLServer2005中用到的rownum替换为row_num；Oracle中定义表别名的时候不能使用AS关键字，所以这里也去掉了AS。
Oracle支持标准的函数ROW_NUMBER()，不过Oracle中提供了更方便的特性用来计算行号，也就在Oracle中可以无需自行计算行号，Oracle为每个结果集都增加了一个默认的表示行号的列，这个列的名称为rownum。比如我们执行下面的SQL语句：
```java  
SELECT rownum,FNumber,FName,FSalary,FAge FROM T_Employee
```
使用rownum我们可以很轻松的取得结果集中前N条的数据行，比如我们执行下面的SQL语句可以得到按工资从高到底排序的前6名员工的信息：
```java  
SELECT * FROM T_Employee WHERE rownum<=6 ORDER BY FSalary Desc
```
看到这里，您可能认为下面的SQL就可以非常容易的实现“按照工资从高到低的顺序取出第三个到第五个员工信息”的功能了：
```java  
SELECT rownum,FNumber,FName,FSalary,FAge FROM T_Employee WHERE rownum BETWEEN 3 AND 5 ORDER BY FSalary DESC
```
检索结果为空！！！这非常出乎我们的意料。让我们来回顾一下rownum的含义：rownum为结果集中每一行的行号（从1开始计数）。对于下面的SQL：
```java  
SELECT * FROM T_Employee WHERE rownum<=6 ORDER BY FSalary Desc
```
当进行检索的时候，对于第一条数据，其rownum为1，因为符合“WHERE rownum<=6”所以被放到了检索结果中；当检索到第二条数据的时候，其rownum为2，因为符合“WHERE
rownum<=6”所以被放到了检索结果中……依次类推，直到第七行。所以这句SQL语句能够实现“按照工资从高到低的顺序取出第三个到第五个员工信息”的功能。而对于这句SQL语句：
```java  
SELECT rownum,FNumber,FName,FSalary,FAge FROM T_Employee WHERE rownum BETWEEN 3 AND 5 ORDER BY FSalary DESC
```
当进行检索的时候，对于第一条数据，其rownum为1，因为不符合“WHERE rownum BETWEEN 3 AND 5”，所以没有被放到了检索结果中；当检索到第二条数据的时候，因为第一条数据没有放到结果集中，所以第二条数据的rownum仍然为1，而不是我们想像的2，所以因为不符合“WHERE rownum<=6”，没有被放到了检索结果中；当检索到第三条数据的时候，因为第一、二条数据没有放到结果集中，所以第三条数据的rownum仍然为1，而不是我们想像的3，所以因为不符合“WHERE rownum<=6”，没有被放到了检索结果中……依此类推，这样所有的数据行都没有被放到结果集中。
因此如果要使用rownum来实现“按照工资从高到低的顺序取出第三个到第五个员工信息”的功能，就必须借助于窗口函数ROW_NUMBER()。
* DB2
DB2中支持窗口函数ROW_NUMBER()，其用法和MSSQLServer2005以及Oracle中相同，
比如我们执行下面的SQL语句：
```java  
SELECT * FROM(SELECT ROW_NUMBER() OVER(ORDER BY FSalary DESC) row_num,FNumber,FName,FSalary,FAge FROM T_Employee) a
WHERE a.row_num>=3 AND a.row_num<=5
```
除此之外，DB2还提供了FETCH关键字用来提取结果集的前N行，其语法为“FETCH FIRST 条数ROWS ONLY”，比如我们执行下面的SQL语句可以得到按工资从高到底排序的前6名员工的信息：
```java  
SELECT * FROM T_Employee ORDER BY FSalary Desc FETCH FIRST 6 ROWS ONLY
```
需要注意的是FETCH子句要放到ORDER BY语句的后面DB2没有直接提供返回提供“检索从第5行开始的10条数据”、“检索第五行至第十二行的数据”等这样的取区间范围的功能，不过可以采用其他方法来变通实现，最常使用的方法就是用子查询，比如要实现检索按照工资从高到低排序检索从第六名开始一共三个人的信息，那么就可以首先将前五名的主键取出来，在检索的时候检索排除了这五名员工的前三个人，SQL如下：
```java  
SELECT * FROM T_Employee WHERE FNumber NOT IN(SELECT FNumber FROM T_Employee ORDER BY FSalary DESC FETCH FIRST 5 ROWS ONLY) ORDER BY FSalary DESC FETCH FIRST 3 ROWS ONLY
```