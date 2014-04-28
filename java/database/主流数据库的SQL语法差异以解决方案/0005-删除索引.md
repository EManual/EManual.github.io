索引的定义在各个数据库系统中基本相同，但是删除索引的语法则各有不同，比如删除T_Person表中定义的名称为idx1的索引在不同数据库系统下的SQL语句如下：
```java  
MYSQL：
DROP INDEX idx1 ON T_Person
MSSQLServer：
DROP INDEX T_Person.idx1
Oracle,DB2：
DROP INDEX idx1
```