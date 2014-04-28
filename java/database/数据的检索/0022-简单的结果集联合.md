UNION运算符要放置在两个查询语句之间。比如我们要查询公司所有员工（包括临时工）的标识号码、姓名、年龄信息。
查询正式员工信息的SQL语句如下：
```java  
SELECT FNumber,FName,FAge FROM T_Employee
```
而查询临时工信息的SQL语句如下：
```java  
SELECT FIdCardNumber,FName,FAge FROM T_TempEmployee
```
只要用UNION操作符连接这两个查询语句就可以将两个查询结果集联合为一个结果集，SQL语句如下：
```java  
SELECT FNumber,FName,FAge FROM T_Employee
UNION
SELECT FIdCardNumber,FName,FAge FROM T_TempEmployee
```
可以看到UNION操作符将两个独立的结果集联合成为了一个结果集。
UNION可以连接多个结果集，就像“+”可以连接多个数字一样简单，只要在每个结果集之间加入UNION即可，比如下面的SQL语句就连接了三个结果集：
```java  
SELECT FNumber,FName,FAge FROM T_Employee
WHERE FAge<30
UNION
SELECT FIdCardNumber,FName,FAge FROM T_TempEmployee
WHERE FAge>40
UNION
SELECT FIdCardNumber,FName,FAge FROM T_TempEmployee
WHERE FAge<30
```