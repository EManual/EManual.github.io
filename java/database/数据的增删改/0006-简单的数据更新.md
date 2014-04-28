UPDATE 语句用来对数据表中的数据进行更新。下边的语句用来将表T_Person 中所有人员的FREMARK 字段值更新为“SuperMan”：
```java  
UPDATE T_Person SET FRemark = "SuperMan"
```
执行SELECT * FROM T_Person来查看表中的数据：
  
可以看到所有行的FRemark字段值都被设置成了“SuperMan”。
来看一下刚才执行的SQL语句，首先它声明了要更新的表为T_Person：
```java  
UPDATE T_Person
```
在SET子句中，我们指定将FRemark字段更新为新值"SuperMan"：
```java  
SET FRemark = "SuperMan"
```
我们还可以在SET 语句中定义多个列，这样就可以实现多列同时更新了，比如下面的
UPDATE 语句用来将所有人员的FRemark字段更新为“Sonic”，并且将年龄更新为25：
```java  
UPDATE T_Person SET FRemark = "Sonic",FAge=25
```
多个列之间需要使用逗号分隔开。执行完此SQL语句后执行SELECT * FROM T_Person来查看表中的数据的变化。