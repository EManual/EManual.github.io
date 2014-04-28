目前演示的几个UPDATE语句都是一次性更新所有行的数据，这无法满足只更新符合特定条件的行的需求，比如“将Tom 的年龄修改为12 岁”。要实现这样的功能只要使用WHERE 子句就可以了，在WHERE 语句中我们设定适当的过滤条件，这样UPDATE 语句只会更新符合WHERE子句中过滤条件的行，而其他行的数据则不被修改。
执行下边的UPDATE语句：
```java  
UPDATE T_Person SET FAge = 12 WHERE FNAME="Tom"
```
执行完此SQL语句后执行SELECT * FROM T_Person来查看表中的数据的变化：
  
可以看到只有第一行中的FAGE 被更新了。WHERE子句“WHERE FNAME="Tom"”表示我们只更新FNAME字段等于"Tom"的行。由于FNAME 字段等于"Tom"的只有一行，所以仅有一行记录被更新，但是如果有多个符合条件的行的话将会有多行被更新，比如下面UPDATE 语句将所有年龄为25 的人员的备注信息修改为“BlaBla”：
```java  
UPDATE T_Person SET FRemark = "BlaBla" WHERE FAge =25
```
执行完此SQL语句后执行SELECT * FROM T_Person来查看表中的数据的变化。
目前为止我们演示的都是非常简单的WHERE 子句，我们可以使用复杂的WHERE 语句来满足更加复杂的需求，比如下面的UPDATE 语句就用来将FNAME 等于’Jim’或者’LXF’的行的FAge字段更新为22：
```java  
UPDATE T_Person SET FAge = 22 WHERE FName ="jim" OR FName="LXF"
```
执行完此SQL语句后执行SELECT * FROM T_Person来查看表中的数据的变化。
这里我们使用OR逻辑运算符来组合两个条件来实现复杂的过滤逻辑，我们还可以使用OR、NOT等运算符实现更加复杂的逻辑，甚至能够使用模糊查询、子查询等实现高级的数据过滤。