到目前为止，本书中所有的连接几乎都是等值连接，也就是在这种连接的ON子句的条件包含一个等号运算。等值连接是最常用的连接，因为它指定的连接条件是一个表中的一个字段必须等于另一个表中的一个字段。
处理等值连接，还存在另外一种不等值连接，也就是在连接的条件中可以使用小于（<）、大于（>）、不等于（<>）等运算符，而且还可以使用LIKE、BETWEEN AND等运算符，甚至还可以使用函数。
例如，如果需要检索价格小于每个客户的年龄的五倍值的订单列表，那么就可以使用不等值连接，实现的SQL语句如下所示：
```java  
SELECT T_Order.FNumber,T_Order.FPrice,T_Customer.FName,T_Customer.FAge FROM T_Order INNER JOIN T_Customer ON T_Order.FPrice< T_Customer.FAge*5
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FNumber FPrice FName FAge
K001 100.00 TOM 21
K001 100.00 MIKE 24
K001 100.00 JACK 30
K001 100.00 TOM 25
N002 100.00 TOM 21
N002 100.00 MIKE 24
N002 100.00 JACK 30
N002 100.00 TOM 25
T002 100.00 TOM 21
T002 100.00 MIKE 24
T002 100.00 JACK 30
T002 100.00 TOM 25
```
不等值连接产生了大量的查询结果，因为它是对被连接的两张表做了笛卡尔运算，所以如果只想查看与客户对应的订单，那么就要在不等值连接后添加等值连接匹配条件。实现的SQL语句如下：
```java  
SELECT T_Order.FNumber,T_Order.FPrice,T_Customer.FName,T_Customer.FAge FROM T_Order INNER JOIN T_Customer ON T_Order.FPrice< T_Customer.FAge*5 and T_Order.FCustomerId=T_Customer.FId
```
这里添加了“and T_Order.FCustomerId=T_Customer.FId”这个条件来限制匹配规则。执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FNumber FPrice FName FAge
K001 100.00 TOM 21
N002 100.00 MIKE 24
```