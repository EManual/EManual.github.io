联合结果集不必受被联合的多个结果集之间的关系限制，不过使用UNION仍然有两个基本的原则需要遵守：一是每个结果集必须有相同的列数；二是每个结果集的列必须类型相容。
首先看第一个原则，每个结果集必须有相同的列数，两个不同列数的结果集是不能联合在一起的。比如下面的SQL语句是错误的：
```java  
SELECT FNumber,FName,FAge,FDepartment FROM T_Employee
UNION
SELECT FIdCardNumber,FName,FAge FROM T_TempEmployee
```
执行以后数据库系统会报出如下的错误信息：
使用UNION、INTERSECT 或EXCEPT 运算符合并的所有查询必须在其目标列表中有相同数目的表达式。
因为第一个结果集返回了4列数据，而第二个结果集则返回了3列数据，数据库系统并不会用空值将第二个结果集补足为4列。如果需要将未知列补足为一个默认值，那么可以使用常量字段，比如下面的SQL语句就将第二个结果集的与FDepartment对应的字段值设定为“临时工，不属于任何一个部门”：
```java  
SELECT FNumber,FName,FAge,FDepartment FROM T_Employee
UNION
SELECT FIdCardNumber,FName,FAge,"临时工，不属于任何一个部门" FROM T_TempEmployee
```
联合结果集的第二个原则是：每个结果集的列必须类型相容，也就是说结果集的每个对应列的数据类型必须相同或者能够转换为同一种数据类型。比如下面的SQL语句在MYSQL中可以正确的执行：
```java  
SELECT FIdCardNumber,FAge,FName FROM T_TempEmployee
UNION
SELECT FNumber,FName,FAge FROM T_Employee
```
可以看到MYSQL将FAge转换为了文本类型，以便于与FName字段值匹配。不过这句SQL语句在MSSQLServer、Oracle、DB2中执行则会报出类似如下的错误信息：
表达式必须具有与对应表达式相同的数据类型。
因为这些数据库系统不会像MYSQL那样进行默认的数据类型转换。由于不同数据库系统中数据类型转换规则是各不相同的，因此如果开发的应用程序要考虑跨多数据库移植的话最好保证结果集的每个对应列的数据类型完全相同。