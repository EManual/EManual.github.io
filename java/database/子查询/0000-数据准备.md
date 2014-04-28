SQL语句允许将一个查询语句做为一个结果集供其他SQL语句使用，就像使用普通的表一样，被当作结果集的查询语句被称为子查询。所有可以使用表的地方几乎都可以使用子查询来代替，比如SELECT * FROM T 中就可以用子查询来代替表T，比如SELECT * FROM(SELECT * FROM T2 where FAge<30)，这里的“SELECT * FROM T2 where FAge<30”就是子查询，可以将子查询看成一张暂态的数据表，这张表在查询开始时被创造，在查询结束时被删除。子查询大大简化了复杂SQL语句的编写，不过使用不当也容易造成性能问题。
子查询的语法与普通的SELECT语句语法相同，所有可以在普通SELECT语句中使用的特性都可以在子查询中使用，比如WHERE子句过滤、UNION运算符、HAVING子句、GROUPBY子句、ORDER BY子句，甚至在子查询中还可以包含子查询。同时，不仅可以在SELECT语句中使用子查询，还可以在UPDATE、DELETE 等语句中使用子查询。
为了更容易的运行本章中的例子，必须首先创建所需要的数据表，因此下面列出本章中要用到数据表的创建SQL语句：
```java  
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_Reader (FId INT NOT NULL ,FName VARCHAR(50),FYearOfBirth INT,FCity VARCHAR(50),FProvince VARCHAR(50),FYearOfJoin INT)
Oracle：
CREATE TABLE T_Reader (FId NUMBER (10) NOT NULL ,FName VARCHAR2(50),FYearOfBirth NUMBER (10),FCity VARCHAR2(50),FProvince VARCHAR2(50), FYearOfJoin NUMBER (10))
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_Book (FId INT NOT NULL ,FName VARCHAR(50),FYearPublished INT,FCategoryId INT)
Oracle：
CREATE TABLE T_Book (FId NUMBER (10) NOT NULL ,FName VARCHAR2(50),FYearPublished NUMBER (10),FCategoryId NUMBER (10))
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_Category (FId INT NOT NULL ,FName VARCHAR(50))
Oracle：
CREATE TABLE T_Category (FId NUMBER (10) NOT NULL ,FName VARCHAR2(50))
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_ReaderFavorite (FCategoryId INT,FReaderId INT)
Oracle：
CREATE TABLE T_ReaderFavorite (FCategoryId NUMBER (10),FReaderId NUMBER (10))
```
请在不同的数据库系统中运行相应的SQL语句。其中表T_Reader保存的是读者信息，FId为主键、FName为读者姓名、FYearOfBirth为读者出生年份、FCity为读者所在城市、FProvince为读者所在省份、FYearOfJoin为读者入会年份；表T_Book保存的是书籍信息，FId为主键、FName为书名、FYearPublished为出版年份、FCategoryId为所属分类；表T_Category保存的是分类信息，FId为主键、FName为分类名；表T_ReaderFavorite保存的是读者和读者喜爱的类别之间的对应关系，FCategoryId为分类主键、FReaderId为读者主键。
为了更加直观的验证本章中函数使用方法的正确性，我们需要在这几张表中预置一些初始数据，请在数据库中执行下面的数据插入SQL语句：
```java  
INSERT INTO T_Category(FId,FName)VALUES(1,"Story");
INSERT INTO T_Category(FId,FName)VALUES(2,"History");
INSERT INTO T_Category(FId,FName)VALUES(3,"Theory");
INSERT INTO T_Category(FId,FName)VALUES(4,"Technology");
INSERT INTO T_Category(FId,FName)VALUES(5,"Art");
INSERT INTO T_Category(FId,FName)VALUES(6,"Philosophy");
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(1,"Tom",1979,"TangShan","Hebei",2003);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(2,"Sam",1981,"LangFang","Hebei",2001);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(3,"Jerry",1966,"DongGuan","GuangDong",1995);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(4,"Lily",1972,"JiaXing","ZheJiang",2005);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(5,"Marry",1985,"BeiJing","BeiJing",1999);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(6,"Kelly",1977,"ZhuZhou","HuNan",1995);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(7,"Tim",1982,"YongZhou","HuNan",2001);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(8,"King",1979,"JiNan","ShanDong",1997);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(9,"John",1979,"QingDao","ShanDong",2003);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(10,"Lucy",1978,"LuoYang","HeNan",1996);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(11,"July",1983,"ZhuMaDian","HeNan",1999);
INSERT INTO T_Reader(FId,FName,FYearOfBirth,FCity,FProvince,FYearOfJoin)VALUES(12,"Fige",1981,"JinCheng","ShanXi",2003);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(1,"About J2EE",2005,4);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(2,"Learning Hibernate",2003,4);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(3,"Two Cites",1999,1);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(4,"Jane Eyre",2001,1);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(5,"Oliver Twist",2002,1);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(6,"History of China",1982,2);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(7,"History of England",1860,2);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(8,"History of America",1700,2);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(9,"History of TheWorld",2008,2);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(10,"Atom",1930,3);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(11,"RELATIVITY",1945,3);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(12,"Computer",1970,3);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(13,"Astronomy",1971,3);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(14,"How To Singing",1771,5);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(15,"DaoDeJing",2001,6);
INSERT INTO T_Book(FId,FName,FYearPublished,FCategoryId)VALUES(16,"Obedience toAuthority",1995,6);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(1,1);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(5,2);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(2,3);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(3,4);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(5,5);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(1,6);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(1,7);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(4,8);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(6,9);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(5,10);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(2,11);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(2,12);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(1,12);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(3,1);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(1,3);
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)VALUES(4,4);
```
初始数据预置完毕以后执行SELECT * FROM T_Reader 查看T_Reader 表中的数据。