在设计数据库的时候，有时需要表的某个字段是自动增长的，最常使用自动增长字段的就是表的主键，使用自动增长字段可以简化主键的生成。不同的DBMS 中自动增长字段的实现机制也有不同，下面分别介绍。
* MYSQL中的自动增长字段
MYSQL中设定一个字段为自动增长字段非常简单，只要在表定义中指定字段为AUTO_INCREMENT即可。比如下面的SQL语句创建T_Person表，其中主键FId为自动增长字段：
```java  
CREATE TABLE T_Person(FId INT PRIMARY KEYAUTO_INCREMENT,FName VARCHAR(20),FAge INT);
```
执行上面的SQL 语句后就创建成功了T_Person 表，然后执行下面的SQL 语句向T_Person表中插入一些数据：
```java  
INSERT INTO T_Person(FName,FAge)VALUES(‘Tom’,18);
INSERT INTO T_Person(FName,FAge)VALUES(‘Jim’,81);
INSERT INTO T_Person(FName,FAge)VALUES(‘Kerry’,33);
```
注意这里的INSERT语句没有为FId字段设定任何值，因为DBMS会自动为FId字段设定值。执行完毕后查看T_Person表中的内容：
```java  
FId FName FAge
1 Tom 18
2 Jim 81
3 Kerry 33
```
可以看到FId中确实是自动增长的。
* MSSQLServer 中的自动增长字段
MSSQLServer中设定一个字段为自动增长字段非只要在表定义中指定字段为IDENTITY即可，格式为IDENTITY(startvalue,step)，其中的startvalue参数值为起始数字，step参数值为步长，即每次自动增长时增加的值。
比如下面的SQL语句创建T_Person表，其中主键FId为自动增长字段，并且设定100 为起始数字，步长为3：
```java  
CREATE TABLE T_Person(FId INT PRIMARY KEY IDENTITY(100,3),FName VARCHAR(20),FAge INT);
```
执行上面的SQL 语句后就创建成功了T_Person 表，然后执行下面的SQL 语句向T_Person表中插入一些数据：
```java  
INSERT INTO T_Person(FName,FAge)VALUES(‘Tom’,18);
INSERT INTO T_Person(FName,FAge)VALUES(‘Jim’,81);
INSERT INTO T_Person(FName,FAge)VALUES(‘Kerry’,33);
```
注意这里的INSERT语句没有为FId字段设定任何值，因为DBMS会自动为FId字段设定值。执行完毕后查看T_Person表中的内容：
```java  
FId FName FAge
100 Tom 18
103 Jim 81
106 Kerry 33
```
可以看到FId中确实是100 为起始数字、步长为3自动增长的。
* Oracle中的自动增长字段
Oracle 中不像MYSQL 和MSSQLServer 中那样指定一个列为自动增长列的方式，不过在Oracle中可以通过SEQUENCE序列来实现自动增长字段。
在Oracle中SEQUENCE 被称为序列，每次取的时候它会自动增加，一般用在需要按序列号排序的地方。
在使用SEQUENCE前需要首先定义一个SEQUENCE，定义SEQUENCE的语法如下：
```java  
CREATE SEQUENCE sequence_name INCREMENT BY step STARTWITH startvalue;
```
其中sequence_name为序列的名字，每个序列都必须有唯一的名字；startvalue参数值为起始数字，step参数值为步长，即每次自动增长时增加的值。一旦定义了SEQUENCE，你就可以用CURRVAL来取得SEQUENCE的当前值，也可以通过NEXTVAL来增加SEQUENCE，然后返回新的SEQUENCE值。比如：
```java  
sequence_name.CURRVAL
sequence_name.NEXTVAL
```
如果SEQUENCE 不需要的话就可以将其删除：
```java  
DROP SEQUENCE sequence_name;
```
下面举一个使用SEQUENCE 序列实现自动增长的例子。
首先创建一个名称为seq_PersonId 的 SEQUENCE：
```java  
CREATE SEQUENCE seq_PersonId INCREMENT BY 1 START WITH 1;
```
然后创建T_Person表：
```java  
CREATE TABLE T_Person(FId NUMBER (10) PRIMARY KEY,FName VARCHAR2(20),FAge NUMBER (10));
```
执行上面的SQL 语句后就创建成功了T_Person 表，然后执行下面的SQL 语句向T_Person表中插入一些数据：
```java  
INSERT INTO T_Person(FId,FName,FAge)VALUES(seq_PersonId.NEXTVAL,‘Tom’,18);
INSERT INTO T_Person(FId,FName,FAge)VALUES(seq_PersonId.NEXTVAL,‘Jim’,81);
INSERT INTO T_Person(FId,FName,FAge)VALUES(seq_PersonId.NEXTVAL,‘Kerry’,33);
```
注意这里的INSERT语句没有为FId字段设定任何值，因为DBMS会自动为FId字段设定值。执行完毕后查看T_Person表中的内容：
```java  
FID FNAME FAGE
1 Tom 18
2 Jim 81
3 Kerry 33
```
使用SEQUENCE实现自动增长字段的缺点是每次向表中插入记录的时候都要显式的到SEQUENCE中取得新的字段值，如果忘记了就会造成错误。为了解决这个问题，我们可以使用触发器来解决，创建一个T_Person表上的触发器：
```java  
CREATE OR REPLACE TRIGGER trigger_personIdAutoInc
BEFORE INSERT ON T_Person
FOR EACH ROW
DECLARE
BEGIN
SELECT seq_PersonId.NEXTVAL INTO:NEW.FID FROM DUAL;
END trigger_personIdAutoInc;
```
这个触发器在T_Person 中插入新记录之前触发，当触发器被触发后则从seq_PersonId中取道新的序列号然后设置给FID字段。
执行下面的SQL语句向T_Person表中插入一些数据：
```java  
INSERT INTO T_Person(FAge)VALUES(‘Wow’,22);
INSERT INTO T_Person(FName,FAge)VALUES(‘Herry’,28);
INSERT INTO T_Person(FName,FAge)VALUES(‘Gavin’,36);
```
注意在这个SQL 语句中无需再为FId 字段赋值。执行完毕后查看T_Person 表中的内容：
```java  
FID FNAME FAGE
1 Tom 18
2 Jim 81
3 Kerry 33
4 Wow 22
5 Herry 28
7 Gavin 36
```
这个例子讲解完了，请删除T_Person表以及SEQUENCE：
```java  
DROP TABLE T_Person;
DROP SEQUENCE seq_PersonId;
```
* DB2 中的自动增长字段
DB2中实现自动增长字段有两种方式：定义带有IDENTITY 属性的列；使用SEQUENCE 对象。
* 定义带有IDENTITY 属性的列
首先创建T_Person表，SQL语句如下：
```java  
CREATE TABLE T_Person(FId INT PRIMARY KEY NOT NULLGENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1),FName VARCHAR(20),
FAge INT);
```
执行上面的SQL 语句后就创建成功了T_Person 表，然后执行下面的SQL 语句向T_Person表中插入一些数据：
```java  
INSERT INTO T_Person(FName,FAge)VALUES(‘Tom’,18);
INSERT INTO T_Person(FName,FAge)VALUES(‘Jim’,81);
INSERT INTO T_Person(FName,FAge)VALUES(‘Kerry’,33);
```
注意这里的INSERT语句没有为FId字段设定任何值，因为DBMS会自动为FId字段设定值。执行完毕后查看T_Person表中的内容：
```java  
FId FName FAge
100 Tom 18
103 Jim 81
106 Kerry 33
```
* 使用SEQUENCE 对象
DB2中的SEQUENCE 和Oracle中的SEQUENCE 相同，只是定义方式和使用方式略有不同。
下面创建了一个SEQUENCE：
```java  
CREATE SEQUENCE seq_PersonId AS INT INCREMENT BY 1 START WITH 1;
```
使用SEQUENCE的方式如下：
```java  
NEXT VALUE FOR sequence_name
```
这样就可以通过下面的SQL语句来使用SEQUENCE：
```java  
INSERT INTO T_Person(FId,FName,FAge)VALUES(NEXT VALUE FOR seq_PersonId,‘Kerry’,33);
```
如果想在向表中插入记录的时候自动设定FId 字段的值则同样要使用触发器，具体请参考相关资料，这里不再赘述。