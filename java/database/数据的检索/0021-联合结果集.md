有的时候我们需要组合两个完全不同的查询结果集，而这两个查询结果之间没有必然的联系，只是我们需要将他们显示在一个结果集中而已。在SQL中可以使用UNION运算符来将两个或者多个查询结果集联合为一个结果集中。
为了更好的讲解本节的内容，需要首先创建一张用来存储临时工信息的新表，在数据库系统下执行下面的SQL语句：
MYSQL:
```java  
CREATE TABLE T_TempEmployee (FIdCardNumber VARCHAR(20),FName VARCHAR(20),FAge INT ,PRIMARY KEY (FIdCardNumber))
```
MSSQLServer:
```java  
CREATE TABLE T_TempEmployee (FIdCardNumber VARCHAR(20),FName VARCHAR(20),FAge INT, PRIMARY KEY (FIdCardNumber))
```
Oracle:
```java  
CREATE TABLE T_TempEmployee (FIdCardNumber VARCHAR2(20),FName VARCHAR2(20),FAge NUMBER (10), PRIMARY KEY (FIdCardNumber))
```
DB2：
```java  
CREATE TABLE T_TempEmployee (FIdCardNumber VARCHAR(20) Not NULL,FName VARCHAR(20),FAge INT, PRIMARY KEY (FIdCardNumber))
```
由于临时工没有分配工号，所以使用身份证号码FIdCardNumber来标识一个临时工，同时由于临时工不是实行月薪制，所以这里也没有记录月薪信息。我们还需要一些初始数据，执行下面的SQL语句以插入初始数据：
```java  
INSERT INTO T_TempEmployee(FIdCardNumber,FName,FAge) VALUES("1234567890121","Sarani",33);
INSERT INTO T_TempEmployee(FIdCardNumber,FName,FAge) VALUES("1234567890122","Tom",26);
INSERT INTO T_TempEmployee(FIdCardNumber,FName,FAge) VALUES("1234567890123","Yalaha",38);
INSERT INTO T_TempEmployee(FIdCardNumber,FName,FAge) VALUES("1234567890124","Tina",26);
INSERT INTO T_TempEmployee(FIdCardNumber,FName,FAge) VALUES("1234567890125","Konkaya",29);
INSERT INTO T_TempEmployee(FIdCardNumber,FName,FAge) VALUES("1234567890126","Fotifa",46);
```