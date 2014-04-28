正如“非空约束”表达的意思，如果对一个字段添加了非空约束，那么我们是不能将这个字段中的值更新为NULL的。T_Debt表的FAmount字段是有非空约束的，如果我们执行下面SQL：
```java  
UPDATE T_Debt set FAmount = NULLWHERE FPerson="Tom"
```
这句SQL为FAmount 设置空值。我们执行这句SQL以后数据库系统会报出类似如下的错误信息：
不能将值NULL 插入列"FAmount"，表"demo.dbo.T_Debt"；列不允许有空值。UPDATE失败。
如果我们为FAmount 设置非空值的话，则会插入成功，执行下面的SQL：
```java  
UPDATE T_Debt set FAmount =123WHERE FPerson="Tom"
```
此句SQL则可以正常的执行成功。执行SELECT * FROM T_Debt来查看表中的数据：
  
可以看到数据已经被正确的更新到表中了。