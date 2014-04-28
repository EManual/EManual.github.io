SQL中可供使用的函数是非常多的，这些函数的功能包括转换字符串大小写、求一个数的对数、计算两个日期之间的天数间隔等，数量的掌握这些函数将能够帮助我们更快的完成业务功能。本章将讲解这些函数的使用，并且对它们在不同数据库系统中的差异性进行比较。为了更容易的运行本章中的例子，必须首先创建所需要的数据表，因此下面列出用到数据表的创建SQL语句：
```java  
MYSQL:
CREATE TABLE T_Person (FIdNumber VARCHAR(20),FName VARCHAR(20),FBirthDay DATETIME,FRegDay DATETIME,FWeight DECIMAL(10,2))
MSSQLServer:
CREATE TABLE T_Person (FIdNumber VARCHAR(20),FName VARCHAR(20),FBirthDay DATETIME,FRegDay DATETIME,FWeight NUMERIC(10,2))
Oracle:
CREATE TABLE T_Person (FIdNumber VARCHAR2(20),FName VARCHAR2(20),FBirthDay DATE,FRegDay DATE,FWeight NUMERIC(10,2))
DB2:
CREATE TABLE T_Person (FIdNumber VARCHAR(20),FName VARCHAR(20),FBirthDay DATE,
```
请在不同的数据库系统中运行相应的SQL 语句。T_Person为记录人员信息的数据表，其中字段FIdNumber 为人员的身份证号码，FName 为人员姓名，FBirthDay 为出生日期，FRegDay为注册日期，FWeight为体重。
为了更加直观的验证本章中函数使用方法的正确性，我们需要在T_Person 表中预置一些初始数据，请在数据库中执行下面的数据插入SQL语句：
```java  
MYSQL、MSSQLServer、DB2：
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789120","Tom","1981-03-22","1998-05-01",56.67);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789121","Jim","1987-01-18","1999-08-21",36.17);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789122","Lily","1987-11-08","2001-09-18",40.33);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789123","Kelly","1982-07-12","2000-03-01",46.23);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789124","Sam","1983-02-16","1998-05-01",48.68);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789125","Kerry","1984-08-07","1999-03-01",66.67);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789126","Smith","1980-01-09","2002-09-23",51.28);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES("123456789127","BillGates","1972-07-18","1995-06-19",60.32);
Oracle：
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789120","Tom",TO_DATE("1981-03-22", "YYYY-MM-DD HH24:MI:SS"),TO_DATE("1998-05-01", "YYYY-MM-DD HH24:MI:SS"),56.67);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789121","Jim",TO_DATE("1987-01-18", "YYYY-MM-DD HH24:MI:SS"),TO_DATE("1999-08-21", "YYYY-MM-DD HH24:MI:SS"),36.17);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789122","Lily",TO_DATE("1987-11-08", "YYYY-MM-DD HH24:MI:SS"),TO_DATE("2001-09-18", "YYYY-MM-DD HH24:MI:SS"),40.33);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789123","Kelly",TO_DATE("1982-07-12", "YYYY-MM-DD HH24:MI:SS"),TO_DATE("2000-03-01", "YYYY-MM-DD HH24:MI:SS"),46.23);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789124","Sam",TO_DATE("1983-02-16", "YYYY-MM-DD HH24:MI:SS"),TO_DATE("1998-05-01", "YYYY-MM-DD HH24:MI:SS"),48.68);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789125","Kerry",TO_DATE("1984-08-07", "YYYY-MM-DD HH24:MI:SS"),TO_DATE("1999-03-01", "YYYY-MM-DD HH24:MI:SS"),66.67);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789126","Smith",TO_DATE("1980-01-09", "YYYY-MM-DD HH24:MI:SS"),TO_DATE("2002-09-23", "YYYY-MM-DD HH24:MI:SS"),51.28);
INSERT INTO T_Person(FIdNumber,FName,FBirthDay,FRegDay,FWeight) VALUES ("123456789127","BillGates",TO_DATE("1972-07-18", "YYYY-MM-DD HH24:MI:SS"),TO_DATE("1995-06-19", "YYYY-MM-DD HH24:MI:SS"),60.32);
```
初始数据预置完毕以后执行SELECT * FROM T_Person来查看表中的数据。