几乎所有的数据库系统都支持左外部连接和右外部连接，但是全外部连接则不是所有数据库系统都支持，特别是最常使用的MYSQL就不支持全外部连接。全外部连接是左外部连接和右外部连接的合集，因为即使在右表中不存在匹配连接条件的数据，左表中的所有记录也将被放到结果集中，同样即使在左表中不存在匹配连接条件的数据，右表中的所有记录也将被放到结果集中。
比如下面的SQL语句使用全外部连接查询每张订单的信息以及对应的客户信息：
```java  
SELECT o.FNumber,o.FPrice,o.FCustomerId,c. FROM T_Order o FULL OUTER JOIN T_Customer c ON o.FCustomerId=c.FId
```
执行以后我们在输出结果中看到下面的执行结果：
```java  
FNUMBER FPRICE FCUSTOMERID FNAME FAGE
K001 100.00 1 TOM 21
K002 200.00 1 TOM 21
T003 300.00 1 TOM 21
N002 100.00 2 MIKE 24
N003 500.00 3 JACK 30
T001 300.00 4 TOM 25
<NULL> <NULL> <NULL> LINDA <NULL>
T002 100.00 <NULL> <NULL> <NULL>
```
可以看到前6条记录都是符合连接条件的，而T_Customer表中姓名为LINDA的客户没有对应的订单，但是仍然被放到了结果集中，其无法匹配的字段填充的都是NULL，同样订单号为T002的订单没有匹配任何一个客户，但是仍然被放到了结果集中。
虽然在MYSQL中不支持全外部连接，不过由于全外部连接是左外部连接和右外部连接的合集，所以可以使用左外部连接和右外部连接来模拟实现全外部连接：使用左外部连接和右外部连接分别进行匹配查询，然后使用UNION运算符来取两个查询结果集的合集。比如可以在MYSQL中执行下面的SQL来实现T_Order表和T_Customer表的全外部连接：
```java  
SELECT o.FNumber,o.FPrice,o.FCustomerId,c.FName,c.FAge FROM T_Order o LEFT OUTER JOIN T_Customer c ON o.FCustomerId=c.FId
UNION
SELECT o.FNumber,o.FPrice,o.FCustomerId,c.FName,c.FAge FROM T_Order o RIGHT OUTER JOIN T_Customer c ON o.FCustomerId=c.FId
```
执行以后我们在输出结果中看到下面的执行结果：
```java  
FNUMBER FPRICE FCUSTOMERID FNAME FAGE
K001 100.00 1 TOM 21
K002 200.00 1 TOM 21
T003 300.00 1 TOM 21
N002 100.00 2 MIKE 24
T001 300.00 4 TOM 25
N003 500.00 3 JACK 30
<NULL> <NULL> <NULL> LINDA <NULL>
T002 100.00 <NULL> <NULL> <NULL>
```
可以看到和全外部连接的执行结果是完全一致的。