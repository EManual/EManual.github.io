第一范式要求每张表都要有主键，因此主键约束是非常重要的，而且主键约束是外键关联的基础条件。主键约束为表之间的关联提供了链接点。
主键必须能够唯一标识一条记录，也就是主键字段中的值必须是唯一的，而且不能包含NULL 值。从这种意义上来说，主键约束是UNIQUE 约束和非空约束的组合。虽然一张表中可以有多个UNIQUE 约束和非空约束，但是每个表中却只能有一个主键约束。在CREATE TABLE语句中定义主键约束非常简单，和UNIQUE 约束和非空约束非常类似，只要在字段定义后添加PRIMARY KEY关键字即可。不过在DB2中，主键列也必须显式的定义为NOT NULL。下面的代码创建了员工信息表，并且将字段FNumber 设置为主键字段：
```java  
MYSQL、MSSQLServer:
CREATE TABLE T_Person (FNumber VARCHAR(20) PRIMARY KEY,FName VARCHAR(20),FAge INT)
Oracle:
CREATE TABLE T_Person (FNumber VARCHAR2(20) PRIMARY KEY,FName VARCHAR2(20),FAge NUMBER (10))
DB2：
CREATE TABLE T_Person (FNumber VARCHAR(20) NOT NULL PRIMARY KEY,FName VARCHAR(20),FAge INT)
```
创建完T_Person表后，请执行下面的SQL语句预置一些初始数据到T_Person表中：
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
INSERT INTO T_Person (FNumber, FName, FAge) VALUES ( "3" , "sunny", 22);
```
由于表T_Person 中已经存在FNumber 等于3 的值了，所以执行上边的SQL 语句后数
据库系统会报出如下的错误信息：
* 违反了 PRIMARY KEY 约束"PK__T_Person__2E1BDC42"。不能在对象 "dbo.T_Person" 中插入重复键。
现在可以删除T_Person表了：
```java  
DROP TABLE T_Person;
```
除了这种由单一字段组成的主键之外，还可以由多个字段来组成主键，这样的主键被称为复合主键或者联合主键。复合主键的定义和复合唯一约束的定义类似，下面的SQL 语句用来创建员工信息表，并且将字段FNumber 和FName设置为复合主键：
```java  
MYSQL、MSSQLServer:
CREATE TABLE T_Person (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT,CONSTRAINT pk_1 PRIMARY KEY(FNumber,FName))
Oracle:
CREATE TABLE T_Person (FNumber VARCHAR2(20)FName VARCHAR2(20),FAge NUMBER (10) ,CONSTRAINT pk_1 PRIMARY KEY(FNumber,FName))
DB2：
CREATE TABLE T_Person (FNumber VARCHAR(20) NOT NULL,FName VARCHAR(20) NOT NULL,FAge INT,CONSTRAINT pk_1 PRIMARY KEY(FNumber,FName))
```
尽管在创建表的时候就定义主键是一个好的习惯，但是如果表创建了时候没有定义主键，那么也可以在以后添加主键，其添加方式与添加UNIQUE 约束类似，也就是使用ALTER TABLe语句。不过通过这种方式添加主键的时候有一个附加条件，那就是组成主键的字段必须包含NOT NULL约束。如果在没有添加非空约束的字段上创建主键，系统将会爆出错误信息。
首先创建一个没有主键的T_Person 表，注意其中的字段FNumber 和FName 添加了非空约束：
```java  
MYSQL、MSSQLServer:
CREATE TABLE T_Person (FNumber VARCHAR(20) NOT NULL,FName VARCHAR(20) NOT NULL,FAge INT)
Oracle:
CREATE TABLE T_Person (FNumber VARCHAR2(20) NOT NULL,FName VARCHAR2(20) NOT NULL,FAge NUMBER (10))
DB2：
CREATE TABLE T_Person (FNumber VARCHAR(20) NOT NULL,FName VARCHAR(20) NOT NULL,FAge INT)
```
可以执行下面的SQL语句为T_Person创建主键约束：
```java  
ALTER TABLE T_Person ADD CONSTRAINT pk_1 PRIMARY KEY(FNumber,FName)
```
最后删除主键约束的方式与删除UNIQUE 约束以及CHECK 约束的方式相同，只要使
用带有DROP子句的ALTER TABLE 语句即可：
```java  
ALTER TABLE T_Person
DROP CONSTRAINT pk_1;
```
这个语句在MYSQL中无效，在MYSQL中要执行下面的SQL语句才能删除主键：
```java  
ALTER TABLE T_Person
DROP PRIMARY KEY;
```