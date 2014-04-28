在数据库中存在一种特殊的值：NULL（空值）。一个字段如果没有被赋值，那么它的值就是NULL，NULL并不代表没有值而是表示值未知。员工信息表中存储着身份证号、姓名、年龄等信息，其中某条记录中年龄字段的值为NULL，并不表示这个员工没有年龄，而只是他的年龄暂时不知道。因此，在数据库中NULL 主要用于标识一个字段的值为“未知”。
由于NULL在数据库中是比较特殊的，所以在涉及到NULL的一些处理中也会存在一些需要特别注意的地方。为了更加清晰的讲解我们将创建一张表，执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_Employee
(
FId VARCHAR(20),
FName VARCHAR(20),
FSalary INT
)
Oracle：
CREATE TABLE T_Employee
(
FId VARCHAR2(20),
FName VARCHAR2(20),
FSalary NUMBER (10)
)
```
T_Employee表保存了员工信息，FId字段为主键，FName字段为员工姓名，FSalary字段为员工工资。请在相应的DBMS 中执行相应的SQL 语句，然后执行下面的SQL语句向T_Employee表中插入一些演示数据：
```java  
INSERT INTO T_Employee(FId,FName,FSalary)VALUES(‘1’,‘Tom’,3000);
INSERT INTO T_Employee(FId,FName,FSalary)VALUES(‘2’,‘Jim’,NULL);
INSERT INTO T_Employee(FId,FName,FSalary)VALUES(‘3’,NULL,8000);
INSERT INTO T_Employee(FId,FName,FSalary)VALUES(‘4’,‘Lily’,9000);
INSERT INTO T_Employee(FId,FName,FSalary)VALUES(‘5’,‘Robert’,2000);
```
执行完毕查看T_Employee表中的内容：
```java  
FId FName FSalary
1 Tom 3000
2 Jim <NULL>
3 <NULL> 8000
4 Lily 9000
5 Robert 2000
```
* NULL与比较运算符
NULL 表示未知的值，因此在使用比较运算符的时候就需要注意NULL 值可能造成的BUG。比如有的开发人员认为下面的SQL 语句将返回Jim、Robert、Tom 三个人的工资，因为他认为NULL等于0：
```java  
SELECT * FROM T_Employee WHERE FSalary<5000
```
可是执行上面的查询语句后却得到了下面的结果：
```java  
FId FName FSalary
1 Tom 3000
5 Robert 2000
```
Jim并没有像预想的那样被检索出来。这是因为NULL不等于0，它代表“未知”，Jim的工资未知，所以DBMS不会认为它的工资小于5000，所以它并不会被检索出来。有的开发人员认为下面的SQL 语句将返回所有员工的工资，因为所有员工的工资肯定不是大于5000 就是小于等于5000：
```java  
SELECT * FROM T_Employee WHERE FSalary<5000 OR FSalary>=5000
```
可是执行上面的查询语句后却得到了下面的结果：
```java  
FId FName FSalary
1 Tom 3000
3 <NULL> 8000
4 Lily 9000
5 Robert 2000
```
同样，Jim并没有像预想的那样被检索出来。因为貌似这个查询条件包含了所有的工资金额，可以DBMS是无法确认NULL 值是不是在这个范围之内的，因此Jim并不会被检索出来。
因此为了检索所有工资小于5000 元的员工，包括工资额未知的员工，必须使用ISNULL运算符，SQL语句如下：
```java  
SELECT * FROM T_Employee WHERE FSalary<5000 OR FSalary IS NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FSalary
1 Tom 3000
2 Jim <NULL>
5 Robert 2000
```
* NULL和计算字段
如果NULL 值出现在任何计算字段中，那么计算结果永远是NULL。为了验证这一点请执行下面的SQL语句：
```java  
SELECT FId,FName, FSalary ,FSalary+2000 FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FSalary FSalary+2000
1 Tom 3000 5000
2 Jim <NULL> <NULL>
3 <NULL> 8000 10000
4 Lily 9000 11000
5 Robert 2000 4000
```
第二行记录的FSALARY 字段为NULL，为一个未知的工资增加2000 元得到的仍然是未知工资NULL，这是完全符合逻辑的。
如果这个结果不符合业务系统的要求可以通过两种方式来解决这个问题，一个是过滤掉NULL值，一个是将NULL值转换为业务系统认为的值。
第一种解决方式例子如下，这里用IS NOT NULL运算符将NULL值过滤掉：
```java  
SELECT FId,FName, FSalary ,FSalary+2000 FROM T_Employee WHERE FSalary IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FSalary FSalary+2000
1 Tom 3000 5000
3 <NULL> 8000 10000
4 Lily 9000 11000
5 Robert 2000 4000
```
第二种解决方式例子如下，这里使用CASE 函数将NULL值转换为0，也就是认为工资未知的工资为0：
```java  
SELECT FId,FName, FSalary ,
(	CASE
	WHEN FSalary IS NULL THEN 0
	ELSE FSalary
	END
)+2000 FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FSalary
1 Tom 3000 5000
2 Jim <NULL> 2000
3 <NULL> 8000 10000
4 Lily 9000 11000
5 Robert 2000 4000
```
* NULL和字符串
如果NULL值出现在任何和字符串相关计算字段中，那么计算结果永远是NULL。为了验证这一点请执行下面的SQL语句：
```java  
MYSQL,Oracle：
SELECT FId,FName,FName||‘LOL’,FSalary FROM T_Employee
MSSQLServer：
SELECT FId,FName,FName+‘LOL’,FSalary FROM T_Employee
DB2：
SELECT FId,FName,CONCAT(FName,‘LOL’),FSalary FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FSalary
1 Tom TomLOL 3000
2 Jim JimLOL <NULL>
3 <NULL> <NULL> 8000
4 Lily LilyLOL 9000
5 Robert RobertLOL 2000
```
第三行记录的FName 字段为NULL，为一个未知姓名的员工的名字后增加“LOL”得到的仍然是未知姓名NULL，这是完全符合逻辑的。
如果这个结果不符合业务系统的要求，同样可以采用10.6.2 的解决方案，这里不再赘述。
* NULL和函数
如果NULL 值出现在普通函数中，那么计算结果永远是NULL。为了验证这一点请执行下面的SQL语句：
```java  
SELECT FId,FName, FSalary ,ABS(FSalary-5000) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName FSalary
1 Tom 3000 2000
2 Jim <NULL> <NULL>
3 <NULL> 8000 3000
4 Lily 9000 4000
5 Robert 2000 3000
```
第二行记录的FSalary字段为NULL，对一个未知值进行函数计算得到的仍然是未知NULL，这是完全符合逻辑的。
如果这个结果不符合业务系统的要求，同样可以采用10.6.2 的解决方案，这里不再赘述。
* NULL和聚合函数
和普通的函数不同，如果NULL值出现在聚合函数中，那么NULL值将会被忽略。
为了验证这一点请执行下面的SQL语句：
```java  
SELECT MAX(FSalary) AS MAXSALARY,MIN(FSalary) AS MINSALARY,COUNT(FSalary) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
MAXSALARY MINSALARY
9000 2000 4
```
按照前面的分析，一个包含NULL值在内的所有员工工资的的最大值和最小值应该是未知NULL，不过聚合函数是一个例外，NULL值将会被忽略。这是需要特别注意的。
* 诀窍
处理含有NULL值的运算是非常麻烦的，不过只要记住“NULL代表未知”这一原则就可以灵活应对很多问题。下面举几个例子：条件表达式“NULL=3”的返回值为NULL，因为无法确认3是否与一个未知值相等；“NULL=NULL”的返回值也为NULL，因为无法确认两个未知值是否相等；“NULL<>NULL”的返回值也为NULL，因为同样无法确认两个未知值是否不相等。
表达式“NULLAND TRUE”的返回值为NULL，因为无法确认一个未知值与TRUE进行AND运算的结果；表达式“NULLAND FALSE”的返回值为TRUE，因为任何一个布尔值与FALSE 进行AND 运算的结果都为TRUE，虽然NULL 表示未知值，但是NULL同样不是TRUE 就是FALSE；表达式“NULL OR TRUE”的返回值为TRUE，因为任何一个布尔值与TRUE进行OR运算的结果都为TRUE，虽然NULL表示未知值，但是NULL同样不是TRUE就是FALSE；表达式“NULL OR FALSE”的返回值为TRUE，因为无法确认一个未知值与FALSE 进行OR运算的结果。