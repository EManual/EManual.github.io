在定义数据表的时候，默认情况下所有字段都是允许为空值的，如果需要禁止字段为空，那么就需要在创建表的时候显示指定。指定一个字段为空的方式就是在字段定义后增加NOT NULL，比如下面的SQL语句创建了表T_Person，并且设置FNumber 字段不允许为空：
```java  
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_Person (FNumber VARCHAR(20) NOT NULL ,FName VARCHAR(20),FAge INT)
Oracle：
CREATE TABLE T_Person (FNumber VARCHAR2(20) NOT NULL ,FName VARCHAR2(20),FAge NUMBER (10))
```
创建T_Person表后我们执行下面的SQL语句进行测试：
```java  
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( NULL , "kingchou", 20)
```
因为在定义T_Person 表的时候设定字段FNumber 不能为空，而这个SQL 语句中将FNumber 字段设置为NULL，所以在数据库中执行此SQL 语句后数据库会报出下面错误信息：
* 不能将值NULL 插入列"FNumber"，表 "demo.dbo.T_Person"；列不允许有空值。INSERT 失败。而下面的SQL语句则可以正确的执行：
```java  
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( "1" , "kingchou", 20)
```
非空约束不仅对通过INSERT语句插入的数据起作用，而且对于使用UPDATE语句进行更新时也起作用。执行下面的SQL语句尝试将刚才插入的那条数据的FNumber 字段更新为NULL：
```java  
UPDATE T_Person SET FNumber = NULL
```
在数据库中执行此SQL语句后数据库会报出下面错误信息：
* 不能将值NULL 插入列"FNumber"，表 "demo.dbo.T_Person"；列不允许有空值。UPDATE 失败。