内连接组合两张表，并且基于两张表中的关联关系来连接它们。使用内连接需要指定表中哪些字段组成关联关系，并且需要指定基于什么条件进行连接。内连接的语法如下：
```java  
INNER JOIN table_name ON condition
```
其中table_name 为被关联的表名，condition则为进行连接时的条件。
下面的SQL语句检索所有的客户姓名为MIKE的客户的订单号以及订单价格：
```java  
SELECT FNumber,FPrice FROM T_Order INNER JOIN T_Customer ON FCustomerId= T_Customer.FId WHERE T_Customer.FName="TOM"
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FNumber FPrice
K001 100.00
K002 200.00
T003 300.00
T001 300.00
```
在这个SQL 语句中，首先列出了组成结果集所需要的列名，而后则是在FROM 关键字后指定需要的表，在INNER JOIN关键字后指明要被连接的表，而在ON关键字后则指定了进行连接时所使用的条件。由于T_Customer和T_Order表中都有名称为FId的列，所以在ON关键字后的条件中使用FId字段的时候必须显示的指明这里使用FId字段属于哪个表。比如下面的SQL语句在执行的时候则会报出“列名FId不明确”的错误信息：
```java  
SELECT FNumber,FPrice FROM T_Order INNER JOIN T_Customer ON FCustomerId= FId WHERE T_Customer.FName="TOM"
```
同样如果在SELECT语句后的字段列表中也不能存在有歧义的字段，比如下面的SQL语句执行会出错：
```java  
SELECT FId,FNumber,FPrice FROM T_Order INNER JOIN T_Customer ON FCustomerId= T_Customer.FId WHERE T_Customer.FName="TOM"
```
必须为FId字段显式的指定所属的表，修正后的SQL语句如下：
```java  
SELECT T_Order.FId,FNumber,FPrice FROM T_Order INNER JOIN T_Customer ON FCustomerId= T_Customer.FId WHERE T_Customer.FName="TOM"
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FNumber FPrice
1 K001 100.00
2 K002 200.00
3 T003 300.00
6 T001 300.00
```
为了避免列名歧义并且提高可读性，这里建议使用表连接的时候要显式列所属的表，如下：
```java  
SELECT T_Order.FId,T_Order.FNumber,T_Order.FPrice FROM T_Order INNER JOIN T_Customer ON T_Order.FCustomerId= T_Customer.FId WHERE T_Customer.FName="TOM"
```
指定列所属的表后，我们就可以很轻松的引用同名的字段了，比如下面的SQL语句检索所有的订单以及它们对应的客户的相关信息：
```java  
SELECT T_Order.FId,T_Order.FNumber,T_Order.FPrice,T_Customer.FId,T_Customer.FName,T_Customer.FAge FROM T_Order INNER JOIN T_Customer ON T_Order.FCustomerId= T_Customer.FId
```
在大多数数据库系统中，INNER JOIN中的INNER是可选的，INNER JOIN是默认的连接方式。也就是下面的SQL语句同样可以完成和检索所有的订单以及它们对应的客户的相关信息的功能：
```java  
SELECT T_Order.FId,T_Order.FNumber,T_Order.FPrice,T_Customer.FId,T_Customer.FName,T_Customer.FAge FROM T_Order JOIN T_Customer
ON T_Order.FCustomerId= T_Customer.FId
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FNumber FPrice FId FName FAge
1 K001 100.00 1 TOM 21
2 K002 200.00 1 TOM 21
3 T003 300.00 1 TOM 21
4 N002 100.00 2 MIKE 24
5 N003 500.00 3 JACK 30
6 T001 300.00 4 TOM 25
```
为了明确指定字段所属的表，上面的SQL语句中多次出现了T_Order、T_Customer，当字段比较多的时候这样的SQL语句看起来非常繁杂，为此可以使用表别名来简化SQL语句的编写，比如下面的SQL语句就与上面的SQL语句是等价的：
```java  
SELECT o.FId,o.FNumber,o.FPrice,c.FId,c.FName,c.FAge FROM T_Order o JOIN T_Customer c ON o.FCustomerId= c.FId
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FNumber FPrice FId FName FAge
1 K001 100.00 1 TOM 21
2 K002 200.00 1 TOM 21
3 T003 300.00 1 TOM 21
4 N002 100.00 2 MIKE 24
5 N003 500.00 3 JACK 30
6 T001 300.00 4 TOM 25
```
在使用表连接的时候可以不局限于只连接两张表，因为有很多情况下需要联系许多表。
例如，我们需要检索每张订单的订单号、价格、客户姓名、订单类型等信息，由于客户信息和订单类型信息是保存在另外的表中的，因此需要同时连接T_Customer和T_OrderType两张表才能检索到所需要的信息，编写如下SQL语句即可：
```java  
INNER JOIN T_OrderType ON T_Order.FTypeId= T_OrderType.FId
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FNumber FPrice FName FName
K001 100.00 TOM MarketOrder
K002 200.00 TOM MarketOrder
T003 300.00 TOM LimitOrder
N002 100.00 MIKE LimitOrder
N003 500.00 JACK StopLimit Order
T001 300.00 TOM Stop Order
```