主键是在同一张表中必须是唯一的，如果在进行数据插入的时候指定的主键与表中已有的数据重复的话则会导致违反主键约束的异常。T_Debt表中FNumber 字段是主键，如果我们执行下面SQL：
```java  
INSERT INTO T_Debt (FNumber,FAmount, FPerson) VALUES ("1",300, "Jim");
```
由于在上一节中我们已经向表中插入了一条FNumber 字段为1 的记录，所以运行这句SQL的时候会报出类似如下的错误信息：
不能在对象"dbo.T_Debt" 中插入重复键。
而如果我们为FNumber 设置一个不重复值的话，则会插入成功，执行下面的SQL：
```java  
INSERT INTO T_Debt (FNumber,FAmount, FPerson) VALUES ("2",300, "Jim");
```
此句SQL则可以正常的执行成功。执行SELECT * FROM T_Debt来查看表中的数据：
  
可以看到数据已经被正确的插入到表中了。