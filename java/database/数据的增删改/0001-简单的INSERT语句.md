INSERT INTO 语句用来向数据表中插入数据，比如执行下面的语句就可以向T_Person表中插入一条数据：
```java  
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("Tom",18,"USA");
```
这句SQL向T_Person表中插入了一条数据，其中FName字段的值为"Tom"，FAge字段的值为18，而FRemark字段的值为"USA"。VALUES 前边的括号中列出的是要设置字段的字段名，字段名之间用逗号隔开；VALUES 后边的括号中列出的是要设置字段的值，各个值同样用逗号隔开。需要注意的是VALUES前列出的字段名和VALUES后边列出的字段值是按顺序一一对应的，也就是第一个值"Tom"设置的是字段FName 的值，第二个值18设置的是字段FAge的值，第三个值"USA"设置的是字段FRemark 的值，不能打乱它们之间的对应关系，而且要保证两边的条数是一致的。由于FName 和FRemark字段是字符串类型的，所以需要用单引号4将值包围起来，而整数类型的FAge 字段的值则不需要用单引号包围起来。
我们来检验一下数据是否真的插入数据表中了，执行下面的SQL语句：
```java  
SELECT * FROM T_Person5
```
执行完毕我们将会看到如下的输出结果（在不同的数据库系统以及管理工具下的显示效果会略有不同）：
  
可以看到插入的数据已经保存在T_Person表中了，我们还可以运行多条SQL语句来插入多条数据：
```java  
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("Jim",20,"USA");
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("Lili",22,"China") ;
INSERT INTO T_Person(FName,FAge,FRemark) VALUES("XiaoWang",17," China ") ;
```
再次执行SELECT * FROM T_Person来查看表中的数据。
INSERT语句中列的顺序可以是任意的，比如我们也可以用下面的SQL来插入数据：
```java  
INSERT INTO T_Person(FAge,FName,FRemark) VALUES(21,"Kimisushi","Korea")
```
执行SELECT * FROM T_Person来查看表中的数据。
可见INSET语句中列的顺序不会影响数据插入的结果。