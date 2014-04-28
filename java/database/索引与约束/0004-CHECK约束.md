CHECK约束会检查输入到记录中的值是否满足一个条件，如果不满足这个条件则对数据库做的修改不会成功。比如，一个人的年龄是不可能为负数的，一个人的入学日期不可能早于出生日期，出厂月份不可能大于12。可以在CHECK条件中使用任意有效的SQL表达式，CHECK约束对于插入、更新等任何对数据进行变化的操作都进行检查。
在字段定义后添加CHECK 表达式就可以为这个字段添加CHECK约束，几乎所有字段中都可以添加CHECK约束，也就是一张表中可以存在多个CHECK 约束。
下面的SQL语句创建了一张用于保存人员信息的表T_Person，其中字段FNumber 为人员编号，字段FName 为人员姓名，字段FAge为人员年龄，字段FWorkYear为人员工龄：
```java  
MYSQL,MSSQLServer,DB2:
CREATE TABLE T_Person (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT CHECK(FAge >0),FWorkYear INT CHECK(FWorkYear>0))
Oracle:
CREATE TABLE T_Person (FNumber VARCHAR2(20),FName VARCHAR2(20),FAge NUMBER (10) CHECK(FAge >0),FWorkYear NUMBER (10) CHECK(FWorkYear>0))
```
一个人的年龄和工龄显然不应该为负值的，所以为FAge和FWorkYear两个字段增加了CHECK约束“FAge>0”和“FWeight>0”。表创建完毕后执行下面的SQL语句进行测试：
```java  
INSERT INTO T_Person(FNumber, FName, FAge, FWorkYear) VALUES("001","John",25,-3)
```
因为这里将FWorkYear字段设置成了-3，这是违反“CHECK(FWorkYear>0)”这个CHECK约束，所以在数据库中执行此SQL语句后数据库会报出下面错误信息：
* INSERT 语句与CHECK 约束"CK__T_Person__FWorkY__24927208"冲突。该冲突发生于数据库"demo"，表"dbo.T_Person", column "FWorkYear"。
而执行下面的SQL语句则可以成功执行：
```java  
INSERT INTO T_Person(FNumber, FName, FAge, FWorkYear) VALUES("001","John",25,3)
```
除了可以在CHECK 约束中使用常量表达式之外，还可以在CHECK 约束中使用函数，比如人员编号长度要大于12，那么就需要如下编写建表语句：
```java  
MYSQL,DB2:
CREATE TABLE T_Person (FNumber VARCHAR(20) CHECK (LENGTH(FNumber)>12),FName VARCHAR(20),FAge INT CHECK(FAge >0),FWorkYear INT CHECK(FWorkYear>0))
MSSQLServer:
CREATE TABLE T_Person (FNumber VARCHAR(20) CHECK (LEN(FNumber)>12),FName VARCHAR(20),FAge INT CHECK(FAge >0),FWorkYear INT CHECK(FWorkYear>0))
Oracle:
CREATE TABLE T_Person (FNumber VARCHAR2(20) CHECK (LENGTH(FNumber)>12),FName VARCHAR2(20),FAge NUMBER (10) CHECK(FAge >0),FWorkYear NUMBER (10) CHECK(FWorkYear>12))
```
表创建完毕后执行下面的SQL语句进行测试：
```java  
INSERT INTO T_Person(FNumber, FName, FAge, FWorkYear) VALUES("001","John",25, 3)
```
因为这里将FNumber字段设置成了"001"，这是违反“CHECK(LENGTH(FNumber)>12)”这个CHECK约束的，所以在数据库中执行此SQL语句后数据库会报出下面错误信息：
* INSERT 语句与CHECK 约束"CK__T_Person__FNumbe__267ABA7A"冲突。该冲突发生于数据库"demo"，表"dbo.T_Person", column "FNumber"。
而执行下面的SQL语句则可以成功执行：
```java  
INSERT INTO T_Person(FNumber, FName, FAge, FWorkYear)VALUES("001001001001001","John",25,3)
```
这种直接在列定义中通过CHECK子句添加CHECK约束的方式的缺点是约束条件不能引用其他列。比如我们想约束“人员的工龄必须小于他的年龄”，那么我们执行下面的SQL语句：
```java  
MYSQL,DB2:
CREATE TABLE T_Person (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT,FWorkYear INT CHECK(FWorkYear< FAge))
MSSQLServer:
CREATE TABLE T_Person (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT,FWorkYear INT CHECK(FWorkYear< FAge))
Oracle:
CREATE TABLE T_Person (FNumber VARCHAR2(20),FName VARCHAR2(20),FAge NUMBER (10),FWorkYear NUMBER (10) CHECK(FWorkYear< FAge))
```
执行这个SQL语句以后，数据库会报出如下的错误信息：
表 "T_Person" 的列 "FWorkYear" 的列CHECK 约束引用了另一列。
出现这个错误的原因是因为在这种方式定义的CHECK子句中是不能引用其他列的，如果希望CHECK子句中的条件语句中使用其他列，则必须在CREATE TABLe 语句的末尾使用CONSTRAINT 关键字定义它。语法为：
```java  
CONSTRAINT 约束名 CHECK(约束条件)
```
重新编写上述的SQL语句，如下：
```java  
MYSQL,DB2:
CREATE TABLE T_Person (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT,FWorkYear INT,CONSTRAINT ck_1 CHECK(FWorkYear< FAge))
MSSQLServer:
CREATE TABLE T_Person (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT,FWorkYear INT,CONSTRAINT ck_1 CHECK(FWorkYear< FAge))
Oracle:
CREATE TABLE T_Person (FNumber VARCHAR2(20),FName VARCHAR2(20),FAge NUMBER (10),FWorkYear NUMBER (10),CONSTRAINT ck_1 CHECK(FWorkYear< FAge))
```
表创建完毕后执行下面的SQL语句进行测试：
```java  
INSERT INTO T_Person(FNumber, FName, FAge, FWorkYear) VALUES("001","John",25, 30)
```
因为这里将FWorkYear字段设置成了30，比如年龄25岁还大，这是违反“CHECK(FWorkYear<FAge)”这个CHECK约束的，所以在数据库中执行此SQL语句后数据库会报出下面错误信息：
* INSERT 语句与 CHECK 约束"ck_1"冲突。该冲突发生于数据库"demo"，表"dbo.T_Person"。
而执行下面的SQL语句则可以成功执行：
```java  
INSERT INTO T_Person(FNumber, FName, FAge, FWorkYear) VALUES("001001001001001","John",25,3)
```
可以看到，这种定义CHECK约束的方式几乎与定义一个复合唯一约束的方式一致。同样，可以通过ALTER TABLE的方式为已经存在的数据表添加CHECK 约束。下面的SQL语句在T_Person上添加新的约束：
```java  
ALTER TABLE T_Person ADD CONSTRAINT ck_2 CHECK(FAge>14)
```
上面的SQL语句中为约束指定了显式的名称，所以可以通过下面的SQL语句将CHECK约束ck_2删除（这个语句在MYSQL中无效）：
```java  
ALTER TABLE T_Person
DROP CONSTRAINT ck_2;
```