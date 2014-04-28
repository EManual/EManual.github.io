外键是非常重要的概念，也是体现关系数据库中“关系”二字的体现，通过使用外键，我们才能把互相独立的表关联起来，从而表达丰富的业务语义。
外键是定义在源表中的，定义位置同样为所有字段定义的后面，使用FOREIGN KEY关键字来定义外键字段，并且使用REFERENCES关键字来定义目标表名以及目标表中被关联的字段，格式为：
```java  
FOREIGN KEY 外键字段名称REFERENCES 目标表名(被关联的字段名称)
```
比如我们创建一张部门信息表，表中记录了部门主键FId、部门名称FName、部门级别FLevel等字段，建表SQL如下：
```java  
MYSQL,MSSQLServer:
CREATE TABLE T_Department (FId VARCHAR(20),FName VARCHAR(20),
FLevel INT,PRIMARY KEY (FId))
Oracle:
CREATE TABLE T_Department (FId VARCHAR2(20),FName VARCHAR2(20),
FLevel NUMBER (10) ,PRIMARY KEY (FId))
DB2:
CREATE TABLE T_Department (FId VARCHAR(20) NOT NULL,FName VARCHAR(20),
FLevel INT,PRIMARY KEY (FId))
```
接着创建员工信息表，表中记录工号、姓名以及所属部门等信息，为了能够建立同部门信息表之间的关联关系，我们在员工信息表中保存部门信息表中的主键，保存这个主键的字段就被称为员工信息表中指向部门信息表的外键。
建表SQL如下：
```java  
MYSQL,MSSQLServer,DB2:
CREATE TABLE T_Employee (FNumber VARCHAR(20),FName VARCHAR(20),
FDepartmentId VARCHAR(20),
FOREIGN KEY (FDepartmentId) REFERENCES T_Department(FId))
Oracle:
CREATE TABLE T_Employee (FNumber VARCHAR2(20),FName VARCHAR2(20),
FDepartmentId VARCHAR2(20),
FOREIGN KEY (FDepartmentId) REFERENCES T_Department(FId))
```