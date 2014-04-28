下面将会列出了一些常用的优化手法，注意这些优化手法只是一些常规条件下的优化手法，具体的优化效果是与使用的DBMS以及数据的特点密切相关的，需要根据具体情况来使用不同的优化手法，如果使用不当的话有可能会适得其反。
* 创建必要的索引
在经常需要进行检索的字段上创建索引，比如经常要按照图书名称进行检索，那么就应该在图书名称字段上创建索引，如果经常要按照员工部门和员工岗位级别进行检索，那么就应该在员工部门和员工岗位级别这两个字段上创建索引。创建索引给检索带来的性能提升往往是巨大的，因此在发现检索速度过慢的时候应该首先想到的就是创建索引。
* 使用预编译查询
程序中通常是根据用户的输入来动态执行SQL语句，这时应该尽量使用参数化SQL，这样不仅可以避免SQL注入漏洞攻击，最重要数据库会对这些参数化SQL执行预编译，这样第一次执行的时候DBMS会为这个SQL语句进行查询优化并且执行预编译，这样以后再执行这个SQL的时候就直接使用预编译的结果，这样可以大大提高执行的速度。
* 调整WHERE 子句中的连接顺序
DBMS 一般采用自下而上的顺序解析WHERE 子句，根据这个原理,表连接最好写在其他WHERE条件之前，那些可以过滤掉最大数量记录。
比如下面的SQL语句性能较差：
```java  
SELECT * FROM T_Person WHERE FSalary > 50000 AND FPosition= ‘MANAGER’ AND 25 < (SELECT COUNT(*) FROM T_Manager WHERE FManagerId=2);
```
我们将子查询的条件放到最前面，下面的SQL语句性能比较好：
```java  
SELECT * FROM T_Person WHERE 25 < (SELECT COUNT(*) FROM T_Manager WHERE FManagerId=2) AND FSalary > 50000 AND FPosition= ‘MANAGER’ ;
```
* SELECT语句中避免使用‘*’
SELECT*比较简单，但是除非确实需要检索所有的列，否则将会检索出不需要的列，这回增加网络的负载和服务器的资源消耗；即使确实需要检索所有列，也不要使用SELECT *，因为这是一个非常低效的方法，DBMS在解析的过程中，会将*依次转换成所有的列名，这意味着将耗费更多的时间。
* 尽量将多条SQL语句压缩到一句SQL中
每次执行SQL的时候都要建立网络连接、进行权限校验、进行SQL语句的查询优化、发送执行结果，这个过程是非常耗时的，因此应该尽量避免过多的执行SQL语句，能够压缩到一句SQL执行的语句就不要用多条来执行。
比如T_Person表中有如下的初始数据：
```java  
FId FName FGroupId
0 ABC
1 CBA
2 NBA
3 WTO
4 WHO
5 Tom
6 Jim
7 Ham
8 Mam
9 Lily
10 Lucy
11 Linda
12 Robert
13 John
14 Wiki
15 SVN
```
T_Person表中保存是人员信息，FId字段为主键，FName字段为姓名，FGroupId为分组号。我们需要将这些人员进行分组，每三人一组，将组号更新到FGroupId 字段中。
可以在宿主语言中通过代码来实现这个功能：
```java  
//当前组号
int groupid=0;
//计数器
int counter=0;
rs = ExecuteQuery("SELECT FId FROM T_Person");
while(rs.next())
{
	//计数器增加1
	counter = counter+1;
	if(counter==3)
	{
	//计数器清零
	counter=0;
	//组号加一
	groupid = groupid+1;
	}
	id = rs.Get("FId");
	//将主键为id的记录的FGroupId字段更新为组号groupid
	update = CreateUpdate("UPDATE T_Person SET FGroupId =:groupId WHERE FId =:id");
	update.SetParameter(":groupId ", groupid);
	update.SetParameter(":id", id);
	ExecuteUpdate(update);
}
```
这个算法非常简单，逐条处理T_Person表中数据，这在数据量小的时候并没有什么问题，但是当表中的数据有大量的数据时性能就非常差了。假设表中1 万条数据，那么一共就需要执行10001 次数据库操作，速度将会让人无法忍受。
我们分析T_Person表中数据特点，发现FId字段是主键，因此每条记录中FId字段都是唯一的，同时FId字段的值是连续递增的，因此可以更新FGroupId的值为FId与3整除后的值。根据整除运算的特性，FId等于0的记录的FGroupId字段被更新为0，FId等于1的记录的FGroupId字段被更新为0，FId等于2的记录的FGroupId字段被更新为0；FId等于3的记录的FGroupId字段被更新为1，FId等于4的记录的FGroupId字段被更新为1，FId等于5的记录的FGroupId字段被更新为1；FId等于6的记录的FGroupId字段被更新为2……，以此类推，这样所有的记录就被很快的分组了。实现这样的分组操作只要一个UPDATE 语句即可完成：
```java  
UPDATE T_Person SET FGroupId =FId/3;
```
* 用Where子句替换HAVING 子句
避免使用HAVING子句，因为HAVING只会在检索出所有记录之后才对结果集进行过滤。如果能通过WHERE子句限制记录的数目，那就能减少这方面的开销。HAVING 中的条件一般用于聚合函数的过滤，除此而外，应该将条件写在WHERE 子句中。
* 使用表的别名
当在SQL语句中连接多个表时，请使用表的别名并把别名前缀于每个列名上。这样就可以减少解析的时间并减少那些由列名歧义引起的语法错误。
* 用EXISTS替代IN
在查询中，为了满足一个条件，往往需要对另一个表进行联接，在这种情况下，使用EXISTS而不是IN 通常将提高查询的效率，因为IN 子句将执行一个子查询内部的排序和合并。下面的语句2 就比语句1 效率更加高。
语句1：
```java  
SELECT * FROM T_Employee WHERE FNumber> 0 AND FDEPTNO IN (SELECT FNumber FROM T_Department WHERE FMangerName = ‘Tome’)
```
语句 2：
```java  
SELECT * FROM T_Employee WHERE FNumber > 0 AND EXISTS (SELECT 1 FROM T_Department WHERE T_Department. FDEPTNO = EMP.FNumber
AND FMangerName = ‘MELB’)
```
* 用表连接替换EXISTS
通常来说，表连接的方式比EXISTS 更有效率，因此如果可能的话尽量使用表连接替换EXISTS。下面的语句2 就比语句1 效率更加高。
语句1：
```java  
SELECT FName FROM T_Employee
WHERE EXISTS
(
	SELECT 1 FROM T_Department
	WHERE T_Employee.FDepartNo= FNumber
	AND FKind=‘A’
);
```
语句2：
```java  
SELECT FName FROM T_Department, T_Employee WHERE T_Employee. FDepartNo = T_Departmen. FNumber AND FKind = ‘A’ ;
```
* 避免在索引列上使用计算
在 WHERE 子句中，如果索引列是计算或者函数的一部分，DBMS 的优化器将不会使用索引而使用全表扫描。
例如下面的SQL语句用于检索月薪的12倍大于两万五千元的员工：
```java  
SELECT *FROM T_Employee WHERE FSalary * 12 >25000;
```
由于在大于号左边的是FSalary与12的成绩表达式，这样DBMS的优化器将不会使用字段FSalary的索引，因为DBMS必须对T_Employee表进行全表扫描，从而计算FSalary * 12 的值，然后与25000进行比较。将上面的SQL语句修改为下面的等价写法后DBMS将会使用索引查找，从而大大提高了效率：
```java  
SELECT *FROM T_Employee WHERE FSalary >25000/12;
```
同样的，不能在索引列上使用函数，因为函数也是一种计算，会造成全表扫描。下面的语句2就比语句1 效率更加高。
```java  
语句1：
SELECT * FROM T_Example WHERE ABS(FAmount)=300
语句2：
SELECT * FROM T_Example WHERE FAmount=300 OR FAmount=-300
```
* 用UNION ALL 替换UNION
当SQL语句需要UNION两个查询结果集合时，即使检索结果中不会有重复的记录，如果使用UNION这两个结果集同样会尝试进行合并，然后在输出最终结果前进行排序。
因此，如果检索结果中不会有重复的记录的话，应该用UNION ALL替代UNION，这样效率就会因此得到提高。下面的语句2 就比语句1效率更加高。
```java  
语句1：
SELECTACCT_NUM, BALANCE_AMT FROM DEBIT_TRANSACTIONS1 WHERE TRAN_DATE = ‘20010101’
UNION
SELECTACCT_NUM, BALANCE_AMT FROM DEBIT_TRANSACTIONS2 WHERE TRAN_DATE =‘20010102’
语句2：
SELECTACCT_NUM, BALANCE_AMT FROM DEBIT_TRANSACTIONS1 WHERE TRAN_DATE =‘20010101’
UNION ALL
SELECTACCT_NUM, BALANCE_AMT FROM DEBIT_TRANSACTIONS2 WHERE TRAN_DATE = ‘20010102’
```
* 避免隐式类型转换造成的全表扫描
T_Person 表的字符串类型字段FLevel 为人员的级别，在FAge 字段上建有索引。
我们执行下面的SQL语句用于检索所有级别等于10的员工：
SELECT FId,FAge,FName FROM T_Person WHERE FAge=10
在这个SQL语句中，将字符串类型字段FLevel与数值10进行比较，由于在大部分数据库中隐式转换类型中数值类型的优先级高于字符串类型，因此DBMS会对FAge字段进行隐式类型转换，相当于执行了下面的SQL语句：
```java  
SELECT FId,FAge,FName FROM T_Person WHERE TO_INT(FAge)=10
```
由于在索引字段上进行了计算，所以造成了索引失效而使用全表扫描。因此应将
SQL语句做如下修改：
```java  
SELECT FId,FAge,FName FROM T_Person WHERE FAge=‘10’
```
* 防止检索范围过宽
如果DBMS 优化器认为检索范围过宽，那么它将放弃索引查找而使用全表扫描。
下面是几种可能造成检索范围过宽的情况：
使用IS NOT NULL或者不等于判断，可能造成优化器假设匹配的记录数太多。
使用LIKE 运算符的时候，"a%"将会使用索引，而"a%c"和"%c"则会使用全表扫描，因此"a%c"和"%c"不能被有效的评估匹配的数量。