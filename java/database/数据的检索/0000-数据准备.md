到目前为止，我们已经学习了如何创建数据表、如何修改数据表以及如何删除数据表，我们还学习了如何将数据插入数据表、如何更新数据表中的数据以及如何数据删除。创建数据表是在创建存放数据的容器，修改和删除数据表是在维护数据模型的正确性，将数据插入数据表、更新数据表以及删除数据表中的数据则是在维护数据库中数据与真实业务数据之间的同步，这些操作都不是经常发生的，它们只占据数据库操作中很小的一部分，我们大部分时间都是在对数据库中的数据进行检索，并且基于检索结果进行响应的分析，可以说数据的检索是数据库中最重要的功能。
与数据表结构的管理以及数据表中数据的管理不同，数据检索所需要面对的问题是非常复杂的，不仅要求能够完成“检索出所有年龄小于12 岁的学生”、“检索出所有旷工时间超过3 天的职工”等简单的检索任务，而且还要完成“检索出本季度每种商品的出库入库详细情况”、“检索出所有学生家长的工作单位信息”等复杂的任务，甚至还需要完成其他更加复杂的检索任务。数据检索面对的场景是异常复杂的，因此数据检索的语法也是其他功能所不能比的，不仅语法规则非常复杂，而且使用方式也非常灵活。本书中大部分内容都是讲解数据检索相关知识的，为了降低学习的梯度，本章我们将讲解基本的数据检索语法，这些语法是数据检索功能中最基础也是最核心的部分，因此只有掌握我们才能继续学习更加复杂的应用。
本章中我们将使用一些数据表，为了更容易的运行本章中的例子，必须首先创建所需要的数据表，因此下面列出本章中要用到数据表的创建SQL语句：
MYSQL:
```java  
CREATE TABLE T_Employee (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT,FSalary DECIMAL(10,2),PRIMARY KEY (FNumber))
```
MSSQLServer:
```java  
CREATE TABLE T_Employee (FNumber VARCHAR(20),FName VARCHAR(20),FAge INT,FSalary NUMERIC(10,2),PRIMARY KEY (FNumber))
```
Oracle:
```java  
CREATE TABLE T_Employee (FNumber VARCHAR2(20),FName VARCHAR2(20),FAge NUMBER (10),FSalary NUMERIC(10,2),PRIMARY KEY (FNumber))
```
DB2:
```java  
CREATE TABLE T_Employee (FNumber VARCHAR(20) NOT NULL,FName VARCHAR(20),FAge INT,FSalary DECIMAL(10,2),PRIMARY KEY (FNumber))
```
请在不同的数据库系统中运行相应的SQL语句。T_Employee为记录员工信息的数据表，其中主键字段FNumber 为员工工号，FName 为人员姓名，FAge 为年龄，FSalary 为员工月工资。
为了更加直观的验证本章中检索语句的正确性，我们需要在T_Employee表中预置一些初始数据，请在数据库中执行下面的数据插入SQL语句：
```java  
INSERT INTO T_Employee(FNumber,FName,FAge,FSalary) VALUES("DEV001","Tom",25,8300);
INSERT INTO T_Employee(FNumber,FName,FAge,FSalary) VALUES("DEV002","Jerry",28,2300.80);
INSERT INTO T_Employee(FNumber,FName,FAge,FSalary) VALUES("SALES001","John",23,5000);
INSERT INTO T_Employee(FNumber,FName,FAge,FSalary) VALUES("SALES002","Kerry",28,6200);
INSERT INTO T_Employee(FNumber,FName,FAge,FSalary) VALUES("SALES003","Stone",22,1200);
INSERT INTO T_Employee(FNumber,FName,FAge,FSalary) VALUES("HR001","Jane",23,2200.88);
INSERT INTO T_Employee(FNumber,FName,FAge,FSalary) VALUES("HR002","Tina",25,5200.36);
INSERT INTO T_Employee(FNumber,FName,FAge,FSalary) VALUES("IT001","Smith",28,3900);
```