主键是在同一张表中必须是唯一的，如果在进行数据更新的时候指定的主键与表中已有的数据重复的话则会导致违反主键约束的异常。T_Debt表中FNumber 字段是主键，如果我们执行下面SQL：
```java  
UPDATE T_Debt set FNumber = "2" WHERE FPerson="Tom"
```
由于表中已经存在一条FNumber 字段为2 的记录，所以运行这句SQL 的时候会报出类似如下的错误信息：
违反了PRIMARY KEY 约束"PK__T_Debt__1920BF5C"。不能在对象"dbo.T_Debt" 中插入重复键。
而如果我们为FNumber设置一个不重复值的话，则会插入成功，执行下面的SQL：
```java  
UPDATE T_Debt set FNumber = "8" WHERE FPerson="Tom"
```
此句SQL则可以正常的执行成功。执行SELECT * FROM T_Debt来查看表中的数据：
  
可以看到数据已经被正确的更新到表中了。