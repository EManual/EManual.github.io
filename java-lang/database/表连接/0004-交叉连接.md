与内连接比起来，交叉连接非常简单，因为它不存在ON子句。交叉连接会将涉及到的所有表中的所有记录都包含在结果集中。可以采用两种方式来定义交叉连接，分别是隐式的和显式的。
隐式的连接只要在SELECT语句的FROM语句后将要进行交叉连接的表名列出即可，这种方式可以被几乎任意数据库系统支持。比如下面的SQL语句为将T_Customer表和T_Order做交叉连接：
SELECT T_Customer.FId, T_Customer.FName, T_Customer.FAge,T_Order.FId, T_Order.FNumber, T_Order.FPrice FROM T_Customer, T_Order
在交叉连接中同样可以对表使用别名，比如上面的SQL语句来代替：
SELECT c.FId, c.FName, c.FAge,o.FId, o.FNumber, o.FPrice FROM T_Customer c, T_Order o
执行完毕我们就能在输出结果中看到下面的执行结果，可以看到执行结果与上面的一模一样
交叉连接的显式定义方式为使用CROSS JOIN关键字，其语法与INNER JOIN类似，比如下面的SQL将T_Customer表和T_Order做交叉连接：
SELECT T_Customer.FId, T_Customer.FName, T_Customer.FAge,T_Order.FId, T_Order.FNumber, T_Order.FPrice FROM T_Customer CROSS JOIN T_Order
使用CROSS JOIN的方式声明的交叉连接只能被MYSQL、MSSQLServer和Oracle所支持，在DB2中是不被支持的。因为所有的数据库系统都支持隐式的交叉连接，所以它是执行交叉连接的最好方法。