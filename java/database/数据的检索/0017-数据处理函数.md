像普通编程语言一样，SQL也支持使用函数处理数据，函数使用若干字段名或者常量值做为参数；参数的数量是不固定的，有的函数的参数为空，甚至有的函数的参数个数可变；几乎所有函数都有返回值，返回值即为函数的数据处理结果。
其实在前面的章节中我们已经用到函数了，最典型的就是“聚合函数”，“聚合函数”是函数的一种，它们可以对一组数据进行统计计算。除了“聚合函数”，SQL中还有其他类型的函数，比如进行数值处理的数学函数、进行日期处理的日期函数、进行字符串处理的字符串函数等。
我们来演示几个函数使用的典型场景。
主流数据库系统都提供了计算字符串长度的函数，在MYSQL、Oracle、DB2中这个函数名称为LENGTH，而在MSSQLServer中这个函数的名称则为LEN。这个函数接受一个字符串类型的字段值做为参数，返回值为这个字符串的长度。下面的SQL语句计算每一个名称不为空的员工的名字以及名字的长度：
MYSQL、Oracle、DB2：
```java  
SELECT FName, LENGTH(FName) AS namelength FROM T_Employee WHERE FName IS NOT NULL
```
MSSQLServer：
```java  
SELECT FName, LEN(FName) AS namelength FROM T_Employee WHERE FName IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName namelength
Tom 3
Jerry 5
Jane 4
Tina 4
Smith 5
John 4
Kerry 5
Stone 5
```
主流系统都提供了取得字符串的子串的函数，在MYSQL、MSSQLServer中这个函数名称为SUBSTRING，而在Oracle、DB2这个函数名称为SUBSTR。这个函数接受三个参数，第一个参数为要取的主字符串，第二个参数为字串的起始位置（从1开始计数），第三个参数为字串的长度。下面的SQL语句取得每一个名称不为空的员工的名字以及名字中从第二个字符开始、长度为3的字串：
MYSQL、MSSQLServer：
```java  
SELECT FName, SUBSTRING(FName,2,3) FROM T_Employee WHERE FName IS NOT NULL
```
Oracle、DB2：
```java  
SELECT FName, SUBSTR(FName,2,3) FROM T_Employee WHERE FName IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName namelength
Tom om
Jerry er
Jane an
Tina in
Smith mi
John oh
Kerry er
Stone to
```
多个函数还可以嵌套使用。主流系统都提供了计算正弦函数值的函数SIN和计算绝对值的函数ABS，它们都接受一个数值类型的参数。下面的SQL语句取得每个员工的姓名、年龄、年龄的正弦函数值以及年龄的正弦函数值的绝对值，其中计算“年龄的正弦函数值的绝对值”时就要使用嵌套函数，SQL语句如下：
```java  
SELECT FName,FAge, SIN(FAge) , ABS(SIN(FAge)) FROM T_Employee
```