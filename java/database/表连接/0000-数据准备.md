到目前为止，我们讲解的数据查询都是针对单张数据表的，但是在真实的业务系统中，各个表之间都存在这种联系，很少存在不与其他表存在关联关系的表，而在实现业务功能的时候也经常需要从多个表中进行数据的检索，而进行多表检索最常用的技术就是表连接。
为了更容易的运行本章中的例子，必须首先创建所需要的数据表，因此下面列出要用到数据表的创建SQL语句：
```java  
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_Customer (FId INT NOT NULL ,FName VARCHAR(20) NOT NULL ,FAge INT,PRIMARY KEY (FId))
Oracle：
CREATE TABLE T_Customer (FId NUMBER (10) NOT NULL ,FName VARCHAR2(20) NOT NULL ,FAge NUMBER (10),PRIMARY KEY (FId))
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_OrderType (FId INT NOT NULL ,FName VARCHAR(20) NOT NULL,PRIMARY KEY (FId))
Oracle：
CREATE TABLE T_OrderType (FId NUMBER (10) NOT NULL ,FName VARCHAR2(20) NOT NULL,PRIMARY KEY (FId))
MYSQL,DB2：
CREATE TABLE T_Order (FId INT NOT NULL ,FNumber VARCHAR(20) NOT NULL ,FPrice DECIMAL(10,2),FCustomerId INT,FTypeId INT,PRIMARY KEY (FId))
MSSQLServer：
CREATE TABLE T_Order (FId INT NOT NULL ,FNumber VARCHAR(20) NOT NULL ,FPrice NUMERIC(10,2),FCustomerId INT, FTypeId INT,PRIMARY KEY (FId))
Oracle：
CREATE TABLE T_Order (FId NUMBER (10) NOT NULL ,FNumber VARCHAR2(20) NOT NULL ,FPrice NUMERIC(10,2),FCustomerId NUMBER (10), FTypeId INT,PRIMARY KEY (FId))
```
请在不同的数据库系统中运行相应的SQL语句。其中表T_Customer保存的是客户信息，FId为主键、FName为客户姓名、FAge为客户年龄；表T_OrderType保存的是订单类型，FId为主键、FName为类型名；表T_Order为保存的是订单信息，FId为主键、FNumber为订单号、FPrice为价格、FCustomerId为客户的主键。
为了更加直观的验证本章中函数使用方法的正确性，我们需要在两张表中预置一些初始数据，请在数据库中执行下面的数据插入SQL语句：
```java  
INSERT INTO T_Customer(FId,FName,FAge)VALUES(1,"TOM",21);
INSERT INTO T_Customer(FId,FName,FAge)VALUES(2,"MIKE",24);
INSERT INTO T_Customer(FId,FName,FAge)VALUES(3,"JACK",30);
INSERT INTO T_Customer(FId,FName,FAge)VALUES(4,"TOM",25);
INSERT INTO T_Customer(FId,FName,FAge)VALUES(5,"LINDA",NULL);
INSERT INTO T_OrderType(FId,FName)VALUES(1,"MarketOrder");
INSERT INTO T_OrderType(FId,FName)VALUES(2,"LimitOrder");
INSERT INTO T_OrderType(FId,FName)VALUES(3,"Stop Order");
INSERT INTO T_OrderType(FId,FName)VALUES(4,"StopLimit Order");
INSERT INTO T_Order(FId,FNumber,FPrice,FCustomerId, FTypeId)VALUES(1,"K001",100,1,1);
INSERT INTO T_Order(FId,FNumber,FPrice,FCustomerId, FTypeId)VALUES(2,"K002",200,1,1);
INSERT INTO T_Order(FId,FNumber,FPrice,FCustomerId, FTypeId)VALUES(3,"T003",300,1,2);
INSERT INTO T_Order(FId,FNumber,FPrice,FCustomerId, FTypeId)VALUES(4,"N002",100,2,2);
INSERT INTO T_Order(FId,FNumber,FPrice,FCustomerId, FTypeId)VALUES(5,"N003",500,3,4);
INSERT INTO T_Order(FId,FNumber,FPrice,FCustomerId, FTypeId)VALUES(6,"T001",300,4,3);
INSERT INTO T_Order(FId,FNumber,FPrice,FCustomerId, FTypeId)VALUES(7,"T002",100,NULL,1);
```