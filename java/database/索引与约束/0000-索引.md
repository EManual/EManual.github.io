前面的章节我们讲解了数据表的创建以及数据的增删改查，掌握了这些知识我们已经可以对数据库进行基本的操作了，但是在使用一段时间后我们就发现很多问题，比如按照年龄进行数据检索的时候速度非常快但是按照姓名进行数据检索的时候则非常慢、一个人的姓名不应该是未知的但是还是录入了大量的值为NULL的姓名到系统中、注册会员的Email地址不应该重复的可是在数据表中却能够插入重复的Email地址。在数据库系统中解决这些问题的技术就是索引与约束，索引用来提高数据的检索速度，而约束则用来保证数据的完整性。
索引是建立在数据表上的，因此需要首先创建一张数据表，创建SQL语句如下：
```java  
MYSQL、MSSQLServer、DB2:
CREATE TABLE T_Person (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT)
Oracle:
CREATE TABLE T_Person (FNumber VARCHAR2(20),FName VARCHAR2(20),FAge NUMBER (10))
```
请在不同的数据库系统中运行相应的SQL语句。T_Person为记录人员信息的数据表，其中字段FNumber为人员的编号，FName为人员姓名，FAge为人员年龄。
索引是针对字段的，因此创建索引索引的时候需要指定要在那个字段上创建索引，还可以为多个字段创建一个索引，这样还可以指定索引相关的字段列表。创建索引的SQL语句是CREATE INDEX，其语法如下：
```java  
CREATE INDEX 索引名ON 表名(字段1, 字段2,……字段n)
```
其中【索引名】为被创建的索引的名称，这个名称必须是唯一的；【表名】为要创建索引的表；【字段1,字段2,……字段n】为组成这个索引的字段列表，允许一到多个。
下面的SQL语句在T_Person表的FName字段上创建索引，索引名为idx_person_name：
```java  
CREATE INDEX idx_person_name ON T_Person(FName)
```
下面的SQL 语句在T_Person 表的FName 和FAge 字段上创建索引，索引名为idx_person_nameage：
```java  
CREATE INDEX idx_person_nameage ON T_Person(FName,FAge)
```
索引创建后是可以被删除的，删除索引使用的语句为DROP INDEX。不同的数据库系统的DROP INDEX 语法是不同的，下面分别介绍：
MYSQL中的DROP INDEX 语法如下：
```java  
DROP INDEX 索引名ON 表名
```
比如下面的SQL语句用来删除刚才我们创建了两个索引：
```java  
DROP INDEX idx_person_name ON T_Person;
DROP INDEX idx_person_nameage ON T_Person;
```
MSSQLServer 中的DROP INDEX 语法如下：
```java  
DROP INDEX 表名.索引名
```
比如下面的SQL语句用来删除刚才我们创建了两个索引：
```java  
DROP INDEX T_Person.idx_person_name;
DROP INDEX T_Person.idx_person_nameage;
```
Oracle和DB2中的DROP INDEX 语句不要求指定表名，只要指定索引名即可，语法如下：
```java  
DROP INDEX 索引名
```
比如下面的SQL语句用来删除刚才我们创建了两个索引：
```java  
DROP INDEX idx_person_name;
DROP INDEX idx_person_nameage;
```