正如“非空约束”表达的意思，如果对一个字段添加了非空约束，那么我们是不能向这个字段中插入NULL值的。T_Debt表的FAmount字段是有非空约束的，如果我们执行下面SQL：
```java  
INSERT INTO T_Debt (FNumber, FPerson) VALUES ("1", "Jim")
```
这句SQL中没有为字段FAmount赋值，也就是说FAmount为空值。我们执行这句SQL以后数据库系统会报出类似如下的错误信息：
不能将值NULL 插入列"FAmount"，表"demo.dbo.T_Debt"；列不允许有空值。INSERT失败。
如果我们为FAmount 设置非空值的话，则会插入成功，执行下面的SQL：
INSERT INTO T_Debt (FNumber,FAmount, FPerson) VALUES ("1",200, "Jim")
此句SQL则可以正常的执行成功。执行SELECT * FROM T_Debt来查看表中的数据：
  