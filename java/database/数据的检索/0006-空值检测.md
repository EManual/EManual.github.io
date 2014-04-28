没有添加非空约束列是可以为空值的（也就是NULL），有时我们需要对空值进行检测，比如要查询所有姓名未知的员工信息。既然NULL 代表空值，有的开发人员试图通过下面的SQL语句来实现：
```java  
SELECT * FROM T_Employee WHERE FNAME=null
```
这个语句是可以执行的，不过执行以后我们看不到任何的执行结果，那个Fnumber为“IT002”的数据行中Fname字段为空，但是没有被查询出来。这是因为在SQL语句中对空值的处理有些特别，不能使用普通的等于运算符进行判断，而要使用IS NULL关键字，使用方法为“待检测字段名IS NULL”，比如要查询所有姓名未知的员工信息，则运行下面的SQL语句：
```java  
SELECT * FROM T_Employee WHERE FNAME IS NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
如果要检测“字段不为空”，则要使用IS NOT NULL，使用方法为“待检测字段名IS NOT NULL”，比如要查询所有姓名已知的员工信息，则运行下面的SQL语句：
```java  
SELECT * FROM T_Employee WHERE FNAME IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
IS NULL/IS NOT NULL可以和其他的过滤条件一起使用。比如要查询所有姓名已知且工资小于5000的员工信息，则运行下面的SQL语句：
```java  
SELECT * FROM T_Employee WHERE FNAME IS NOT NULL AND FSalary <5000
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  