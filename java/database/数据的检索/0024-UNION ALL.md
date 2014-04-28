我们想列出公司中所有员工（包括临时工）的姓名和年龄信息，那么我们可以执行下面的SQL语句：
```java  
SELECT FName,FAge FROM T_Employee
UNION
SELECT FName,FAge FROM T_TempEmployee
```
的是不一致的，在正式员工中有姓名为Tom、年龄为26以及姓名为Tina、年龄为26的两名员工，而临时工中也有姓名为Tom、年龄为26以及姓名为Tina、年龄为26的两名员工，也就是说正式员工的临时工中存在重名和年龄重复的现象，但是在查询结果中却将重复的信息只保留了一条，也就是只有一个姓名为Tom、年龄为26的员工和一个姓名为Tina、年龄为26的员工。
这时因为默认情况下，UNION运算符合并了两个查询结果集，其中完全重复的数据行被合并为了一条。如果需要在联合结果集中返回所有的记录而不管它们是否唯一，则需要在UNION运算符后使用ALL操作符，比如下面的SQL语句：
```java  
SELECT FName,FAge FROM T_Employee
UNION ALL
SELECT FName,FAge FROM T_TempEmployee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName FAge
Tom 26
Jerry 29
Jane 24
Tina 26
Smith 29
<NULL> 28
John 24
Kerry 29
Stone 23
Sarani 33
Tom 26
Yalaha 38
Tina 26
Konkaya 29
Fotifa 46
```