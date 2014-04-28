通过 CREATE TABLE 语句创建的数据表的结构并不是永远不变的，很多因素决定我们需要对数据表的结构进行修改，比如我们需要在T_Person表中记录一个人的个人爱好信息，那么就需要在T_Person中增加一个记录个人爱好的字段，再如我们不再需要记录一个人的年龄，那么我们就可以将FAge字段删除。这些操作都可以使用ALTER TABLE 语句来完成。
ANSI-SQL中为ALTER TABLE 语句规定了两种修改方式：添加字段和删除字段，有的数据库系统中还提供了修改表名、修改字段类型、修改字段名称的语法。
首先来看添加字段的语法：
```java  
ALTER TABLE 待修改的表名ADD 字段名字段类型
```
在语句中需要指定要修改的表的表名、要增加的字段名以及字段的数据类型，其使用方式和创建表的非常类似。下面是为T_Person表增加个人爱好字段的SQL语句：
```java  
ALTER TABLE T_PERSON ADD FFavorite VARCHAR(20)
```
注意：上边的SQL在MYSQL、MSSQLServer 以及DB2 下可以正常运行，不过由于各个主流数据库系统中数据类型的差异，所以在其他数据库中可能需要改写。
下面是此SQL在Oracle下的写法：
```java  
ALTER TABLE T_PERSON ADD FFavorite VARCHAR2(20)
```
接下来看删除字段的语法：
```java  
ALTER TABLE 待修改的表名DROP 待删除的字段名
```
在语句中需要指定要修改的表的表名以及要删除字段的名称。下面是删除T_Person 表中年龄字段的SQL语句：
```java  
ALTER TABLET_Person DROP FAge
```
注意：DB2 中不能删除字段，所以这个SQL语句在DB2 中是无法正确执行的。