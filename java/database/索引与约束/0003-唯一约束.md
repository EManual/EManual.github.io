唯一约束又称为UNIQUE约束，它用于防止一个特定的列中两个记录具有一致的值，比如在员工信息表中希望防止两个或者多个人具有相同的身份证号码。唯一约束分为单字段唯一约束与复合唯一约束两种类型，下面分别介绍。
如果希望一个字段在表中的值是唯一的，那么就可以将唯一约束设置到这个字段上，设置方式就是在字段定义后增加UNIQUE，如果是DB2，那么还要同时将NOT NULL约束设置到这个字段上。下面的SQL语句创建了表T_Person，并且将唯一约束设置到FNumber字段上：
```java  
MYSQL、MSSQLServer：
CREATE TABLE T_Person (FNumber VARCHAR(20) UNIQUE,FName VARCHAR(20),FAge INT)
Oracle：
CREATE TABLE T_Person (FNumber VARCHAR2(20) UNIQUE,FName VARCHAR2(20),FAge NUMBER (10))
DB2：
CREATE TABLE T_Person (FNumber VARCHAR(20) NOT NULL UNIQUE,FName VARCHAR(20),FAge INT)
```
创建 T_Person表后我们执行下面的SQL语句向数据库中插入初始的一些测试数据：
```java  
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( "1" , "kingchou", 20);
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( "2" , "stef", 22);
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( "3" , "long", 26);
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( "4" , "yangzk", 27);
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( "5" , "beansoft", 26);
```
执行完毕后就能在表T_Person中的看到下面的数据：
```java  
FNUMBER FNAME FAGE
1 kingchou 20
2 stef 22
3 long 26
4 yangzk 27
5 beansoft 26
```
接着执行下面的SQL语句进行测试：
```java  
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( "2" , "kitty", 20)
```
在数据库中执行此SQL语句后数据库会报出下面错误信息：
* 违反了 UNIQUE KEY 约束 "UQ__T_Person__1A14E395"。不能在对象 "dbo.T_Person" 中插入重复键。
单字段唯一约束的相关知识就介绍到这里，请执行下面的SQL语句将T_Person表删除：
```java  
DROP TABLE T_Person
```
唯一约束可以添加到多个字段中，也就是一张表中的唯一约束可以有不止一个，但是这样的单字段唯一约束只能约束“字段A 的值在表中不重复”、“字段B的值在表中不重复”等，却不能约束“字段A的值在表中可以重复，字段B的值在表中也可以重复，但是不能存在字段A的值和字段B的值同时重复的记录”，这种约束也是有应用场景的：公司中每个部门单独进行工号编号，而且每个部门拥有唯一的部门编号，这样每个员工所属的部门编号是可以在表内重复的，而且每个员工的工号也是可以在表内重复的，但是不能存在所属的部门编号和每个员工的工号同时重复的员工。复合唯一约束是建立在多个字段上的约束，被约束的字段在不能同时重复。
定义复合唯一约束需要定义在所有字段列表之后，语法如下：
```java  
CONSTRAINT 约束名UNIQUE(字段1,字段2……字段n)
```
这里的“字段1,字段2……字段n”为组成约束的多个字段，如果只有一个字段则可以看做是单字段唯一约束定义的另外一种形式。通过这种形式定义的唯一约束由于有一个确定的名称，所以可以很容易的通过这个名字来删除这个约束。
下面的SQL语句创建了表T_Person，并且将在部门编号字段FDepartmentNumber 和工号字段FNumber 上设置复合唯一约束，并且命名为unic_dep_num：
```java  
MYSQL、MSSQLServer：
CREATE TABLE T_Person (FNumber VARCHAR(20),FDepartmentNumber VARCHAR(20),FName VARCHAR(20),FAge INT,CONSTRAINT unic_dep_num UNIQUE(FNumber,FDepartmentNumber))
Oracle：
CREATE TABLE T_Person (FNumber VARCHAR2(20),FDepartmentNumber VARCHAR(20),FName VARCHAR2(20),FAge NUMBER (10),CONSTRAINT unic_dep_num UNIQUE(FNumber,FDepartmentNumber))
DB2：
CREATE TABLE T_Person (FNumber VARCHAR(20) NOT NULL,FDepartmentNumber VARCHAR(20) NOT NULL,FName VARCHAR(20),FAge INT,CONSTRAINT unic_dep_num UNIQUE(FNumber,FDepartmentNumber))
```
创建T_Person表后我们执行下面的SQL语句向数据库中插入初始的一些测试数据：
```java  
INSERT INTO T_Person (FNumber, FDepartmentNumber,FName, FAge)VALUES ( "1" , "dev001","kingchou", 20);
INSERT INTO T_Person (FNumber, FDepartmentNumber,FName, FAge)VALUES ( "2" , "dev001", "stef", 22);
INSERT INTO T_Person (FNumber, FDepartmentNumber,FName, FAge)VALUES ( "1" , "sales001", "long", 26);
INSERT INTO T_Person (FNumber, FDepartmentNumber,FName, FAge)VALUES ( "2" , "sales001", "yangzk", 27);
INSERT INTO T_Person (FNumber, FDepartmentNumber,FName, FAge)VALUES ( "3" , "sales001", "beansoft", 26);
```
执行完毕后就能在表T_Person中的看到下面的数据：
```java  
FNumber FDepartmentNumber FName FAge
1 dev001 kingchou 20
2 dev001 stef 22
1 sales001 long 26
2 sales001 yangzk 27
3 sales001 beansoft 26
```
可以看到FNumber和FDepartmentNumber字段的值在表中都有重复的值，但是没有这两个字段同时重复的值，如果这两个字段同时重复的话执行就会失败，执行下面的SQL语句来验证一下：
```java  
INSERT INTO T_Person (FNumber, FDepartmentNumber,FName, FAge) VALUES ( "2" , "sales001", "daxia", 30);
```
因为FNumber等于"2"且FDepartmentNumber等于"sales001"的记录在表中已经存在了，所以在数据库中执行此SQL语句后数据库会报出下面错误信息：
* 违反了 UNIQUE KEY 约束 "unic_dep_num"。不能在对象 "dbo.T_Person" 中插入重复键。
为了运行后面的例子，请首先将表T_Person删除：DROP TABLE T_Person。
可以在一个表中添加多个复合唯一约束，只要为它们指定不同的名称即可。下面的SQL语句创建表T_Person，并且为字段FNumber和FDepartmentNumber创建一个复合唯一约束以及为FDepartmentNumber和FName创建一个复合唯一约束：
```java  
MYSQL、MSSQLServer：
CREATE TABLE T_Person (FNumber VARCHAR(20),FDepartmentNumber VARCHAR(20),FName VARCHAR(20),FAge INT,CONSTRAINT unic_1 UNIQUE(FNumber,FDepartmentNumber),CONSTRAINT unic_2 UNIQUE(FDepartmentNumber, FName))
Oracle：
CREATE TABLE T_Person (FNumber VARCHAR2(20),FDepartmentNumber VARCHAR(20),FName VARCHAR2(20),FAge NUMBER (10) ,CONSTRAINT unic_1 UNIQUE(FNumber,FDepartmentNumber),CONSTRAINT unic_2 UNIQUE(FDepartmentNumber, FName))
DB2：
CREATE TABLE T_Person (FNumber VARCHAR(20) NOT NULL,FDepartmentNumber VARCHAR(20) NOT NULL,FName VARCHAR(20) NOT NULL,FAge INT NOT NULL,CONSTRAINT unic_1 UNIQUE(FNumber,FDepartmentNumber) ,CONSTRAINT unic_2 UNIQUE(FDepartmentNumber, FName))
```
到目前为止，我们已经讲了如何在创建数据表的时候创建唯一约束了，可是有时我们需要在已经创建好的数据表上添加新的唯一约束，这时就需要使用ALTER TABLE 语句了，使用它我们可以为一张已经存在的数据表添加新的约束，语法如下：
```java  
ALTER TABLE 表名ADD CONSTRAINT 唯一约束名UNIQUE(字段1,字段2……字段n)
```
比如下面的SQL语句为T_Person表添加一个建立在字段FName和字段FAge上的新的唯一约束：
```java  
ALTER TABLE T_Person ADD CONSTRAINT unic_3 UNIQUE(FName, FAge)
```
同样ALTER TABLE语句我们也可以删除已经创建好的复合唯一约束，语法如下：
```java  
ALTER TABLE 表名DROP CONSTRAINT 唯一约束名
```
不过上边的语法不能在MYSQL中执行，MYSQL中删除约束的语法为：
```java  
ALTER TABLE 表名DROP INDEX 唯一约束名
```
比如下面的SQL语句将刚才创建的三个复合唯一约束删除：
```java  
MSQLServer、Oracle、DB2：
ALTER TABLE T_Person DROP CONSTRAINT unic_1;
ALTER TABLE T_Person DROP CONSTRAINT unic_2;
ALTER TABLE T_Person DROP CONSTRAINT unic_3;
MYSQL：
ALTER TABLE T_Person DROP INDEX unic_1;
ALTER TABLE T_Person DROP INDEX unic_2;
ALTER TABLE T_Person DROP INDEX unic_3;
```