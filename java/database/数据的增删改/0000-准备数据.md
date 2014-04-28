介绍了创建和管理数据表的方法，数据表只是数据的容器，没有任何数据的表是没有任何意义的。主流的数据库系统都提供了管理数据库的工具，使用这些工具可以查看表中的数据，还可以添加、修改和删除表中的数据，但是使用工具进行数据的增删改通常只限于测试数据库时使用，更常见的方式时通过程序或者Web 页面来向数据库发出SQL语句指令来进行这些操作，因此本章将介绍通过SQL语句增删改表中数据的方法。
本章中我们将使用一些数据表，为了更容易的运行本章中的例子，必须首先创建所需要的数据表，因此下面列出本章中要用到数据表的创建SQL语句：
MYSQL：
```java  
CREATE TABLE T_Person (FName VARCHAR(20),FAge INT,FRemark VARCHAR(20),PRIMARY KEY (FName));
CREATE TABLE T_Debt (FNumber VARCHAR(20),FAmount DECIMAL(10,2) NOT NULL,FPerson VARCHAR(20),PRIMARY KEY (FNumber),FOREIGN KEY (FPerson) REFERENCES T_Person(FName));
```
MSSQLServer：
```java  
CREATE TABLE T_Person (FName VARCHAR(20),FAge INT,FRemark VARCHAR(20),PRIMARY KEY (FName));
CREATE TABLE T_Debt (FNumber VARCHAR(20),FAmount NUMERIC(10,2) NOT NULL,FPerson VARCHAR(20),PRIMARY KEY (FNumber),FOREIGN KEY (FPerson) REFERENCES T_Person(FName));
```
Oracle：
```java  
CREATE TABLE T_Person (FName VARCHAR2(20),FAge NUMBER (10),FRemark VARCHAR2(20),PRIMARY KEY (FName)) ;
CREATE TABLE T_Debt (FNumber VARCHAR2(20),FAmount NUMERIC(10,2) NOTNULL,FPerson VARCHAR2(20),PRIMARY KEY (FNumber),FOREIGN KEY (FPerson) REFERENCES T_Person(FName));
```
DB2：
```java  
CREATE TABLE T_Person (FName VARCHAR(20) NOT NULL,FAge INT,FRemark VARCHAR(20),PRIMARY KEY (FName));
CREATE TABLE T_Debt (FNumber VARCHAR(20) NOT NULL,FAmount DECIMAL(10,2) NOT NULL,FPerson VARCHAR(20),PRIMARY KEY (FNumber),FOREIGN KEY (FPerson) REFERENCES T_Person(FName));
```
请在不同的数据库系统中运行相应的SQL 语句。T_Person为记录人员信息的数据表，其中主键字段FName 为人员姓名，FAge 为年龄，而FRemark则为备注信息；T_Debt 记录了债务信息，其中主键字段FNumber 为债务编号，FAmount为欠债金额，FPerson字段为欠债人姓名，FPerson字段与T_Person中的FName 字段建立了外键关联关系。