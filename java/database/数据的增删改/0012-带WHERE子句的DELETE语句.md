由于前面我们执行“DELETE FROM T_Person”语句将数据表T_Person中的数据全部
删除了，为了演示带WHERE 子句的DELETE 语句，我们需要重新插入一些数据到T_Person
中。请执行下面的SQL语句：
```java  
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("Jim",20,"USA");
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("Lili",22,"China");
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("XiaoWang",17," China ");
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("Sam",16,"China");
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("BlueFin",12,"Mars");
```
执行完此SQL语句后执行SELECT * FROM T_Person来查看T_Person表中新插入的数据。
我们要删除年龄大于20 岁或者来自火星（Mars）的人员，因此使用带复合逻辑WHERE子句，如下：
```java  
DELETE FROM T_Person WHERE FAge > 20 or FRemark = "Mars"
```
执行完此SQL语句后执行SELECT * FROM T_Person来查看表中的数据的变化：
  
可以看到年龄为22 岁的Lili和来自火星的BlueFin被删除了。
本章已经结束，我们不再需要T_Person、T_Debt这两张表，因此需要将它们删除，执行下面的SQL即可：
```java  
DROP TABLE T_Debt;
DROP TABLE T_Person;
```