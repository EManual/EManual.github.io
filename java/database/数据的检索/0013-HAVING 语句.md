有的时候需要对部分分组进行过滤，比如只检索人数多余1个的年龄段，有的开发人员会使用下面的SQL语句：
```java  
SELECT FAge,COUNT(*) AS CountOfThisAge FROM T_Employee GROUP BY FAge WHERE COUNT(*)>1
```
可以在数据库系统中执行下面的SQL的时候，数据库系统会提示语法错误，这是因为聚合函数不能在WHERE语句中使用，必须使用HAVING子句来代替，比如：
```java  
SELECT FAge,COUNT(*) AS CountOfThisAge FROM T_Employee GROUP BY FAge HAVING COUNT(*)>1
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FAge CountOfThisAge
23 		2
25 		2
28 		3
```
HAVING语句中也可以像WHERE语句一样使用复杂的过滤条件，比如下面的SQL用来检索人数为1个或者3个的年龄段，可以使用下面的SQL：
```java  
SELECT FAge,COUNT(*) AS CountOfThisAge FROM T_Employee GROUP BY FAge HAVING COUNT(*) =1 OR COUNT(*) =3
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FAge CountOfThisAge
22 		1
27 		1
28 		3
```
也可以使用IN操作符来实现上面的功能，SQL语句如下：
```java  
SELECT FAge,COUNT(*) AS CountOfThisAge FROM T_Employee GROUP BY FAge HAVING COUNT(*) IN (1,3)
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FAge CountOfThisAge
22 		1
27 		1
28 		3	
```
HAVING语句能够使用的语法和WHERE几乎是一样的，不过使用WHERE的时候GROUP BY子句要位于WHERE子句之后，而使用HAVING子句的时候GROUP BY子句要位于HAVING子句之后，比如下面的SQL是错误的：
```java  
SELECT FAge,COUNT(*) AS CountOfThisAge FROM T_Employee HAVING COUNT(*) IN (1,3) GROUP BY FAge
```
需要特别注意，在HAVING语句中不能包含未分组的列名，比如下面的SQL语句是错误的：
```java  
SELECT FAge,COUNT(*) AS CountOfThisAge FROM T_Employee GROUP BY FAge HAVING FName IS NOT NULL
```
执行的时候数据库系统会提示类似如下的错误信息：
HAVING 子句中的列"T_Employee.FName" 无效，因为该列没有包含在聚合函数或GROUP BY 子句中。
需要用WHERE语句来代替HAVING，修改后的SQL语句如下：
```java  
SELECT FAge,COUNT(*) AS CountOfThisAge FROM T_Employee WHERE FName IS NOT NULL GROUP BY FAge
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FAge CountOfThisAge
22 1
23 2
25 2
28 3
```