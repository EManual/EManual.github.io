有的时候我们需要查询一些不能从任何实体表中能够取得的数据，比如将数字1作为结果集或者计算字符串“abc”的长度。
有的开发人员尝试使用下面的SQL来完成类似的功能：
```java  
SELECT 1 FROM T_Employee
```
可是执行以后却得到了下面的执行结果集
```java  
1
1
1
1
1
1
1
1
1
```
结果集中出现了不止一个1，这时因为通过这种方式得到的结果集数量是取决于T_Employee表中的数据条目数的，必须要借助于DISTINCT关键字来将结果集条数限定为一条，SQL语句如下：
```java  
SELECT DISTINCT 1 FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1
```
就能在输出结果中看到下面的执行结果：
```java  
1
```
还可以在不带FROM子句的SELECT语句中使用函数，比如下面的SQL将字符串“abc”
的长度作为结果集：
MYSQL:
```java  
SELECT LENGTH("abc")
```
MSSQLServer:
```java  
SELECT LEN("abc")
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
3
```
还可以在SELECT语句中同时计算多个表达式，比如下面的SQL语句将1、2、3、’a’、’b’、’c’作为结果集：
```java  
SELECT 1,2,3,"a","b","c"
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1 2 3 a b c
```
在Oracle中是不允许使用这种不带FROM子句的SELECT语句，不过我们可以使用Oracle的系统表来作为FROM子句中的表名，系统表是Oracle内置的特殊表，最常用的系统表为DUAL。比如下面的SQL将1以及字符串"abc"的长度作为结果集：
```java  
SELECT 1, LENGTH("abc") FROM DUAL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1 LENGTH(ABC)
1 3
```
在DB2中也同样不支持不带FROM子句的SELECT语句，它也是采用和Oracle类似的系统表，最常用的系统表为SYSIBM.SYSDUMMY1。比如下面的SQL将1以及字符串"abc"的长度作为结果集：
```java  
SELECT 1, LENGTH("abc") FROM SYSIBM.SYSDUMMY1
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1 2
1 3
```