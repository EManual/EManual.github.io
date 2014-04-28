内部连接要求组成连接的两个表必须具有匹配的记录，T_Order表中的数据如下：
```java  
FId FNumber FPrice FCustomerId FTypeId
1 K001 100.00 1 1
2 K002 200.00 1 1
3 T003 300.00 1 2
4 N002 100.00 2 2
5 N003 500.00 3 4
6 T001 300.00 4 3
7 T002 100.00 <NULL> 1
```
使用内部连接可以查询每张订单的订单号、价格、对应的客户姓名以及客户年龄，SQL语句如下：
```java  
SELECT o.FNumber,o.FPrice,o.FCustomerId,c.FName,c.FAge FROM T_Order o INNER JOIN T_Customer c ON o.FCustomerId=c.FId
```
执行以后我们在输出结果中看到下面的执行结果：
```java  
FNumber FPrice FCustomerId FName FAge
K001 100.00 1 TOM 21
K002 200.00 1 TOM 21
T003 300.00 1 TOM 21
N002 100.00 2 MIKE 24
N003 500.00 3 JACK 30
T001 300.00 4 TOM 25
```
仔细观察我们可以看到T_Order表中有7行数据，而通过上面的内部连接查询出来的结果只有6条，其中订单号为T002的订单没有显示到结果集中。这是因为订单号为T002的订单的FCustomerId字段值为空，显然是无法与T_Customer表中的任何行匹配了，所以它没有显示到结果集中。在一些情况下这种处理方式能够满足要求，但是有时我们要求无法匹配的NULL值也要显示到结果集中，比如“查询每张订单的订单号、价格、对应的客户姓名以及客户年龄，如果没有对应的客户，则在客户信息处显示空格”，希望的查询结果是这样的：
```java  
FNumber FPrice FCustomerId FName FAge
K001 100.00 1 TOM 21
K002 200.00 1 TOM 21
T003 300.00 1 TOM 21
N002 100.00 2 MIKE 24
N003 500.00 3 JACK 30
T001 300.00 4 TOM 25
T002 100.00 <NULL> <NULL> <NULL>
```
使用内部连接是很难达到这种效果的，可以使用外部连接来实现。外部连接主要就是用来解决这种空值匹配问题的。外部连接的语法与内部连接几乎是一样的，主要区别就是对于空值的处理。外部连接不需要两个表具有匹配记录，这样可以指定某个表中的记录总是放到结果集中。根据哪个表中的记录总是放到结果集中，外部连接分为三种类型：右外部连接（RIGHT OUTER JOIN）、左外部连接（LEFT OUTER JOIN）和全外部连接（FULLOUTER JOIN）。
三者的共同点是都返回符合连接条件的数据，这一点是和内部连接是一样的，不同点在于它们对不符合连接条件的数据处理，三者不同点说明如下：
1，左外部连接还返回左表中不符合连接条件的数据；
2，左外部连接还返回右表中不符合连接条件的数据；
3，全外部连接还返回左表中不符合连接条件的数据以及右表中不符合连接条件的数据，它其实是左外部连接和左外部连接的合集。
这里的左表和右表是相对于JOIN关键字来说的，位于JOIN关键字左侧的表即被称为左表，而位于JOIN关键字右侧的表即被称为右表。比如：
```java  
SELECT o.FNumber,o.FPrice,o.FCustomerId,c.FName,c.FAge FROM T_Order o INNER JOIN T_Customer c ON o.FCustomerId=c.FId
```
这里的T_Order就是左表，而T_Customer则是右表。
* 左外部连接
在左外部连接中，左表中所有的记录都会被放到结果集中，无论是否在右表中存在匹配记录。比如下面的SQL语句用来实现“查询每张订单的订单号、价格、对应的客户姓名以及客户年龄，如果没有对应的客户，则在客户信息处显示空格”：
```java  
SELECT o.FNumber,o.FPrice,o.FCustomerId,c.FName,c.FAge FROM T_Order o LEFT OUTER JOIN T_Customer c ON o.FCustomerId=c.FId
```
执行以后我们在输出结果中看到下面的执行结果：
```java  
FNumber FPrice FCustomerId FName FAge
K001 100.00 1 TOM 21
K002 200.00 1 TOM 21
T003 300.00 1 TOM 21
N002 100.00 2 MIKE 24
N003 500.00 3 JACK 30
T001 300.00 4 TOM 25
T002 100.00 <NULL> <NULL> <NULL>
```
在T_Order表中有7条记录，其中最后一条不满足连接条件，但是也放到了结果集中，只是在不存在匹配条件的列中显示为NULL。
虽然左外部连接包含左表中的所有记录，但是它只提供出示的结果集，WHERE语句仍然会改变最终的结果集。比如为上面的SQL语句添加一个WHERE子句，使得结果中不包含价格小于150元的订单：
```java  
SELECT o.FNumber,o.FPrice,o.FCustomerId,c.FName,c.FAge FROM T_Order o LEFT OUTER JOIN T_Customer c ON o.FCustomerId=c.FId WHERE o.FPrice>=150
```
执行以后我们在输出结果中看到下面的执行结果：
```java  
FNumber FPrice FCustomerId FName FAge
K002 200.00 1 TOM 21
T003 300.00 1 TOM 21
N003 500.00 3 JACK 30
T001 300.00 4 TOM 25
```
尽管左外部连接返回了T_Order表中的所有记录，但是由于WHERE语句的过滤，包括订单号为T002在内的所有价格小于150元的订单全部被排除在了结果集之外。
* 右外部连接
与左外部连接正好相反，在右外部连接中不管是否成功匹配连接条件都会返回右表中的所有记录。比如下面的SQL语句使用右外部连接查询每张订单的信息以及对应的客户信息：
```java  
SELECT o.FNumber,o.FPrice,o.FCustomerId,c.FName,c.FAge FROM T_Order o RIGHT OUTER JOIN T_Customer c ON o.FCustomerId=c.FId
```
执行以后我们在输出结果中看到下面的执行结果：
```java  
FNumber FPrice FCustomerId FName FAge
K001 100.00 1 TOM 21
K002 200.00 1 TOM 21
T003 300.00 1 TOM 21
N002 100.00 2 MIKE 24
N003 500.00 3 JACK 30
T001 300.00 4 TOM 25
<NULL> <NULL> <NULL> LINDA <NULL>
```
可以看到前6条记录都是符合连接条件的，而T_Customer表中姓名为LINDA的客户没有对应的订单，但是仍然被放到了结果集中，其无法匹配的字段填充的都是NULL。