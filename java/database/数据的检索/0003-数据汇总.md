有时需要对数据库中的数据进行一些统计，比如统计员工总数、统计年龄大于25岁的员工中的最低工资、统计工资大于3800元的员工的平均年龄。SQL中提供了聚合函数来完成计算统计结果集条数、某个字段的最大值、某个字段的最小值、某个字段的平均值以及某个字段的合计值等数据统计的功能，SQL标准中规定了下面几种聚合函数：
```java  
函数名	说明
MAX 	计算字段最大值
MIN 	计算字段最小值
AVG 	计算字段平均值
SUM 	计算字段合计值
COUNT 	统计数据条数
```
这几个聚合函数都有一个参数，这个参数表示要统计的字段名，比如要统计工资总额，那么就需要把FSalary做为SUM函数的参数。通过例子来看一下聚合函数的用法。第一个例子是查询年龄大于25岁的员工的最高工资，执行下面的SQL：
```java  
SELECT MAX(FSalary) FROM T_Employee WHERE FAge>25
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
6200.00
```
为了方面的引用查询的结果，也可以为聚合函数的计算结果指定一个别名，执行下面的SQL：
```java  
SELECT MAX(FSalary) as MAX_SALARY FROM T_Employee WHERE FAge>25
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
MAX_SALARY
6200.00
```
第二个例子我们来统计一下工资大于3800元的员工的平均年龄，执行下面的SQL：
```java  
SELECT AVG(FAge) FROM T_Employee WHERE FSalary>3800
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
25
```
第三个例子我们来统计一下公司每个月应支出工资总额，执行下面的SQL：
```java  
SELECT SUM(FSalary) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
34302.04
```
我们还可以多次使用聚合函数，比如下面的SQL用来统计公司的最低工资和最高工资：
```java  
SELECT MIN(FSalary),MAX(FSalary) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1200.00 8300.00
```
最后一个介绍的函数就是统计记录数量的COUNT，这个函数有一点特别，因为它的即可以像其他聚合函数一样使用字段名做参数，也可以使用星号“*”做为参数。我们执行下面的SQL：
```java  
SELECT COUNT(*),COUNT(FNumber) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
8 8
```
可以看到COUNT(*)、COUNT(FNumber)两种方式都能统计出记录的条数，据此为数不少的开发人员都认为COUNT(*)、COUNT(字段名)这两种使用方式是等价的。下面通过例子来说明，为了看到两种使用方式的区别需要首先向表T_Employee 中插入一条新的数据，执行下面的SQL：
```java  
INSERT INTO T_Employee(FNumber,FAge,FSalary) VALUES("IT002",27,2800)
```
需要注意的就是这句INSERT语句没有为FName字段赋值，也就是说新插入的这条数据的FName 字段值为空，可以执行SELECT * FROM T_Employee 来查看表T_Employee 中的内容：
  
可以看到FNumber为IT002 的行的FName 字段是空值。接着执行下面的SQL：
```java  
SELECT COUNT(*),COUNT(FNumber),COUNT(FName) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
9 9 8
```
可以看到COUNT(*)、COUNT(FNumber)两个表达式的计算结果都是9，而COUNT(FName)的计算结果是8。也就反应出了两种使用方式的区别：COUNT(*)统计的是结果集的总条数，而COUNT(FName)统计的则是除了结果集中FName不为空值（也就是不等于NULL）的记录的总条数。由于FNumber为IT002的行的FName字段是空值，所以COUNT(FName)的计算结果是8。因此在使用聚合函数COUNT的时候一定要区分两种使用方式的区别，以防止出现数据错误。