外键是指向另一个表中已有数据的约束，因此外键值必须是在目标表中存在的。如果更新后的数据在目标表中不存在的话则会导致违反外键约束异常。T_Debt 表中FPerson 字段是指向表T_Person的FName 字段的外键，如果我们执行下面SQL：
```java  
UPDATE T_Debt set FPerson = "Merry" WHERE FNumber="1"
```
由于在T_Person表中不存在FName字段等于“Merry”的数据行，所以会数据库系统会报出类似如下的错误信息：
UPDATE 语句与FOREIGN KEY 约束"FK__T_Debt__FPerson__1A14E395"冲突。该冲突发生于数据库"demo"，表"dbo.T_Person", column "FName"。
而如果我们为FPerson字段设置已经在T_Person表中存在的FName字段值的话则会插入成功，执行下面的SQL：
```java  
UPDATE T_Debt set FPerson = "Lili" WHERE FNumber="1"
```
此句SQL则可以正常的执行成功。执行SELECT * FROM T_Debt来查看表中的数据：
  
可以看到数据已经被正确的更新到表中了。