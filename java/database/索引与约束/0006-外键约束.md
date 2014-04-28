当一些信息在表中重复出现的时候，我们就要考虑要将它们提取到另外一张表中了，然后在源表中引用新创建的中的数据。比如很多作者都著有不止一本著作，所以在保存书籍信息的时候，应该把作者信息放到单独的表中，创建表的SQL语句如下：
```java  
MYSQL、MSSQLServer：
CREATE TABLE T_AUTHOR(FId VARCHAR(20) PRIMARY KEY,FName VARCHAR(100),FAge INT,FEmail VARCHAR(20));
CREATE TABLE T_Book(FName VARCHAR(100),FPageCount INT,);
Oracle：
CREATE TABLE T_AUTHOR(FId VARCHAR2(20) PRIMARY KEY,FName VARCHAR2(100),FEmail VARCHAR2(20));
CREATE TABLE T_Book(FName VARCHAR2(100),FPageCount NUMBER (10),FAuthorId VARCHAR2(20));
DB2：
CREATE TABLE T_AUTHOR(FId VARCHAR(20) NOT NULL PRIMARY KEY,FName VARCHAR(100),FAge INT,FEmail VARCHAR(20));
CREATE TABLE T_Book(FId VARCHAR(20) NOT NULL PRIMARY KEY,FName VARCHAR(100),FPageCount INT,FAuthorId VARCHAR(20));
```
表T_AUTHOR是作者信息表，FId字段为主键，FName字段为作者姓名，FAge字段为作者年龄，FEmail字段为作者Email地址；表T_Book是书籍信息表，FId字段为主键，FName字段为书名，FPageCount 字段为页数，FAuthorId 字段储存的对应的T_AUTHOR 表中主键字段FId的值。
这里最重要的就是T_Book表的FAuthorId字段，它的值来自于T_AUTHOR表的FId字段。为了更清楚的表述这两个表的关系，我们插入一些演示数据，执行下面的SQL语句：
```java  
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail) VALUES("1","lily",20,"lily@cownew.com");
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail) VALUES("2","kingchou",23,"kingchou@cownew.com");
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail) VALUES("3","stef",28,"stef@cownew.com");
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail) VALUES("4","long",26,"long@cownew.com");
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail) VALUES("5","badboy",31,"badboy@cownew.com");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId) VALUES("1","About Java",300,"1");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId) VALUES("2","Inside Ruby",330,"2");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId) VALUES("3","Inside Curses",200,"5");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId) VALUES("4","Python InAction",450,"4");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId) VALUES("5","WPF Anywhere",250,"1");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId) VALUES("6","C# KickStart",280,"3");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId) VALUES("7","Compling",800,"1");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId) VALUES("8","Faster VB.Net",300,"5");
```
表T_Book 的FAuthorId字段存储的是代表每个作者的主键值，如果要查询一本书的作者信息，那么只要按照FAuthorId字段的值到T_AUTHOR 表中查询就可了。不过这样的表结构仍然存在问题，那就是不能约束表T_Book的FAuthorId字段中存储在表T_AUTHOR中不存在的值，比如执行下面的SQL语句向T_Book表中插入新数据：
```java  
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("9","AboutWinCE",320,"9");
```
表T_Book中最后一条数据的FAuthorId字段值为9，但是在T_AUTHOR表中却没有主键值为9 的记录，也就是这条记录引用了不存在的作者。
同样，这种结果也不能约束删除T_AUTHOR中已经被T_Book表引用的记录，比如我们执行下面的SQL语句删除T_AUTHOR表中的部分记录：
```java  
DELETE FROM T_AUTHOR WHERE FAge>30
```
虽然表T_Book中《Inside Curses》这本书还引用着badboy这个作者，但是这个作者仍然被删除了，这样同样造成了T_Book表中引用了T_AUTHOR表中不存在的记录。
如何防止数据表之间的关系被破坏呢？SQL提供的外键约束机制可以解决这个问题，它允许指定一个表中的一个列的值是另外一个表的外间，即一个表中的一个列是引用另外一个表中的记录。例如，可以设定T_Book 表中的FAuthorId 字段是一个依赖于T_AUTHOR表的FId列中存在的主键值。
我们可以在创建表的时候就添加外键约束，其定义方式和复合主键类似，语法如下：
```java  
FOREIGN KEY 外键字段REFERENCES 外键表名(外键表的主键字段)
```
比如下面的SQL语句就是添加了外键约束的T_AUTHOR表和T_Book表的创建语句：
```java  
MYSQL、MSSQLServer：
CREATE TABLE T_AUTHOR(FId VARCHAR(20) PRIMARY KEY,FName VARCHAR(100),FAge INT,FEmail VARCHAR(20));
CREATE TABLE T_Book(FId VARCHAR(20) PRIMARY KEY,FName VARCHAR(100),FPageCount INT,FAuthorId VARCHAR(20) ,FOREIGN KEY (FAuthorId) REFERENCES T_AUTHOR(FId));
Oracle：
CREATE TABLE T_AUTHOR(FId VARCHAR2(20) PRIMARY KEY,FName VARCHAR2(100),FAge NUMBER (10),FEmail VARCHAR2(20));
CREATE TABLE T_Book(FId VARCHAR2(20) PRIMARY KEY,FName VARCHAR2(100),FPageCount NUMBER (10),FAuthorId VARCHAR2(20) ,FOREIGN KEY (FAuthorId) REFERENCES T_AUTHOR(FId));
DB2：
CREATE TABLE T_AUTHOR(FId VARCHAR(20) NOT NULL PRIMARY KEY,FName VARCHAR(100),FAge INT,FEmail VARCHAR(20));
CREATE TABLE T_Book(FId VARCHAR(20) NOT NULL PRIMARY KEY,FName VARCHAR(100),FPageCount INT,FAuthorId VARCHAR(20) ,FOREIGN KEY (FAuthorId) REFERENCES T_AUTHOR(FId));
```
我们插入一些演示数据，执行下面的SQL语句：
```java  
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail)VALUES("1","lily",20,"lily@cownew.com");
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail)VALUES("2","kingchou",23,"kingchou@cownew.com");
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail)VALUES("3","stef",28,"stef@cownew.com");
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail)VALUES("4","long",26,"long@cownew.com");
INSERT INTO T_AUTHOR(FId,FName,FAge,FEmail)VALUES("5","badboy",31,"badboy@cownew.com");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("1","About Java",300,"1");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("2","Inside Ruby",330,"2");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("3","Inside Curses",200,"5");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("4","Python InAction",450,"4");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("5","WPF Anywhere",250,"1");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("6","C# KickStart",280,"3");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("7","Compling",800,"1");
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("8","Faster VB.Net",300,"5");
```
尝试向表中插入违反外键约束的数据，不如：
```java  
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("9","AboutWinCE",320,"9");
```
因为表T_AUTHOR 中没有主键值等于9 的记录，所以上面的SQL 语句执行后数据库系统会报出如下的错误信息：
* INSERT 语句与 FOREIGN KEY 约束"FK__T_Book__FAuthorI__38996AB5"冲突。该冲突发生于数据库"demo"，表"dbo.T_AUTHOR", column "FId"。
我们修改上面的SQL语句，使其FAuthorId字段的值为在表T_AUTHOR中存在的主键值：
```java  
INSERT INTO T_Book(FId,FName,FPageCount,FAuthorId)VALUES("9","AboutWinCE",320,"3");
```
同样，我们不能删除被T_Book表引用的T_AUTHOR表中的数据，比如我们想执行下面的SQL语句将作者long从T_AUTHOR表中删除：
```java  
DELETE FROM T_AUTHOR
WHERE FName=" badboy"
```
因为《Inside Curses》、《Faster VB.Net》这两本书的作者为主键值等于5的作者badboy，所以上面的SQL语句执行后数据库系统会报出如下的错误信息：
* DELETE 语句与REFERENCE 约束"FK__T_Book__FAuthorI__38996AB5"冲突。该冲突发生于数据库"demo"，表"dbo.T_Book", column "FAuthorId"。
在删除一个表中的数据的时候，如果有其他的表中存在指向这些数据的外键关系，那么这个删除操作会是失败的，除非将所有的相关的数据。比如我们可以首先执行下面的SQL 语句将作者long 的所有著作删除：
```java  
DELETE FROM T_Book
WHERE FAuthorId =5;
```
然后就可以执行下面的SQL语句将作者long从T_AUTHOR表中删除了：
```java  
DELETE FROM T_AUTHOR
WHERE FName="badboy"
```
如果在创建表的时候没有添加外键约束，也可以使用ALTER TABLE语句添加外键约束，其语法与添加UNIQUE约束类似，比如下面的SQL语句就是以ALTER TABLE 语句的方式添加外键约束：
```java  
ALTER TABLE T_Book
ADD CONSTRAINT fk_book_author
FOREIGN KEY (FAuthorId) REFERENCES T_AUTHOR(FId)
```
现在可以删除T_AUTHOR表和T_Book表了：
```java  
DROP TABLE T_Book;
DROP TABLE T_AUTHOR;
```
注意这里的删除顺序是首先删除T_Book，再删除T_AUTHOR，否则会因为违反外键约束而执行失败。