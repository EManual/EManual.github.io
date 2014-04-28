在使用INSERT语句的时候，一般都是使用它向数据库中一条条的插入数据，比如：
```java  
INSERT INTO MyTable(FId,FName,FAge)VALUES(1,"John",20)
```
但是有时我们可能需要将数据批量插入表中，比如创建一个和T_ReaderFavorite表结构完全相同的表T_ReaderFavorite2，然后将T_ReaderFavorite 中的输入复制插入到T_ReaderFavorite2表。
首先我们创建T_ReaderFavorite2 表：
```java  
MYSQL,MSSQLServer,DB2：
CREATE TABLE T_ReaderFavorite2 (FCategoryId INT,FReaderId INT)
Oracle：
CREATE TABLE T_ReaderFavorite2 (FCategoryId NUMBER (10),FReaderId NUMBER (10))
```
按照普通的实现思路，我们需要编写如下的宿主语言代码：
```java  
rs = ExecuteQuery("SELECT * from T_ReaderFavorite");
while(rs.next())
{
	int categoryId = rs.get("FCategoryId");
	int readerId = rs.get("FReaderId");
	Execute("INSERT INTo T_ReaderFavorite2(FCategoryId,FReaderId) VALUES(?,?)",
	categoryId, readerId);
}
```
在宿主语言中逐条读取T_ReaderFavorite表中的记录，然后将它们逐条插入T_ReaderFavorite2表中。这样的处理方式能够正确的完成要求的功能，而且由于目前T_ReaderFavorite 表中的数据量非常少，所以这样处理速度上也没有什么影响。但是如果T_ReaderFavorite 表中有大量的数据的话，由于每插入一条数据都要执行两次数据库操作，所以这种处理方式效率非常低，因此必须采用其他的处理方式。
除了INSERT……VALUES……这种用法外，INSERT语句还支持另外一种语法，那就是INSERT……SELECT……，采用这种使用方式可以将SELECT语句返回的结果集直接插入到目标表中，因为这一切都是都数据库内部完成的，所以效率非常高。下面看一下使用INSERT……SELECT……来实现将T_ReaderFavorite中的输入复制插入到T_ReaderFavorite2表，SQL语句如下：
```java  
INSERT INTO T_ReaderFavorite2(FCategoryId,FReaderId)
SELECT FCategoryId,FReaderId FROM T_ReaderFavorite
```
这里使用SELECT FCategoryId,FReaderId FROM T_ReaderFavorite将T_ReaderFavorite表中的数据读出，然后使用INSERT INTO T_ReaderFavorite2(FCategoryId,FReaderId)将检索结果插入到T_ReaderFavorite2 表中，注意上下的列顺序必须是一一对应的。
执行完毕我们后我们查看T_ReaderFavorite2 表中的内容：
```java  
FCategoryId FReaderId
1 1
5 2
2 3
3 4
5 5
1 6
1 7
4 8
6 9
5 10
2 11
2 12
1 12
3 1
1 3
4 4
```
可以看到T_ReaderFavorite表中的数据已经被正确的复制到T_ReaderFavorite2 表中了。
使用INSERT……SELECT……不仅能够实现简单的将一个表中的数据导出到另外一个表中的功能，还能在将输入插入目标表之前对数据进行处理，比如下面的SQL 语句用于将T_ReaderFavorite表中的数据复制到T_ReaderFavorite2 表中，但是如果T_ReaderFavorite表中的FReaderId 列的值大于10，则将FReaderId 的值减去FCategoryId 的值后再复制到T_ReaderFavorite2 表中。编写如下的SQL语句：
```java  
INSERT INTO T_ReaderFavorite2(FCategoryId,FReaderId)
SELECT FCategoryId,(CASE WHEN FReaderId<=10 THEN FReaderId ELSE FReaderId- FCategoryId END) FROM T_ReaderFavorite
```
这里在SELECT 语句中使用CASE 函数来实现对数据插入前的处理。执行完毕我们后我们查看T_ReaderFavorite2 表中的内容：
```java  
FCategoryId FReaderId
1 1
5 2
2 3
3 4
5 5
1 6
1 7
4 8
6 9
5 10
2 9
2 10
1 11
3 1
1 3
4 4
```
使用这种插入前的数据处理可以完成诸如“将数据从A表导出到B表，并且将B表的主键全部加上bak前缀”、“将A公司的所有员工插入到我们的会员表，自动导入所有的客户信息，并且为其自动生成会员编号”等复杂的任务。
因为可以在插入目标表前可以对数据进行处理，所以INSERT……SELECT……语句不局限于同结构表间的数据插入，也可以实现异构表见输入的插入。假设要将所有会员爱好的图书统一增加“小说”，也就是为T_Reader 表中的每个读者都在T_ReaderFavorite表中创建一条FCategoryId等于1 的记录，实现SQL语句如下：
```java  
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)
SELECT 1,FId FROM T_Reader
```
SELECT语句从T_Reader表中检索所有的读者信息，并且将第一列设定为固定值1，而将第二列设定为读者的主键，执行完毕查看T_ReaderFavorite表中的内容：
```java  
FCategoryId FReaderId
1 1
5 2
2 3
3 4
5 5
1 6
1 7
4 8
6 9
5 10
2 11
2 12
1 12
3 1
1 3
4 4
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
1 11
1 12
```
数据被正确的插入了，但是仔细查看T_ReaderFavorite表中的内容，不难发现其中有重复的数据，比如FCategoryId等于1、FReaderId等于1的记录出现了两次，这就出现了数据冗余，必须修改SQL语句防止这种情况的发生。也就是在将输入插入T_ReaderFavorite表之前要检查T_ReaderFavorite表中是否已经存在了同样的数据。
在继续进行之前请首先清空T_ReaderFavorite 表中的数据，然后执行开头的T_ReaderFavorite表数据的初始化代码。
首先需要在SELECT语句中添加WHERE子句，这个WHERE子句检查每个读者是否有Story的爱好，即是否存在图书分类主键为1的的爱好，只有没有的时候才返回记录：
```java  
SELECT 1,FId FROM T_Reader
WHERE NOT EXISTS
(
	SELECT * FROM T_ReaderFavorite
	WHERE T_ReaderFavorite. FCategoryId=1
	AND T_ReaderFavorite. FReaderId= T_Reader.FId
)
```
执行这个子查询片段，执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId
1 2
1 4
1 5
1 8
1 9
1 10
1 11
```
可以看到检索出的确实是还没有以Story做为爱好的读者，所以编写下面的SQL语句来执行数据的插入：
```java  
INSERT INTO T_ReaderFavorite(FCategoryId,FReaderId)
SELECT 1,FId FROM T_Reader
WHERE NOT EXISTS
(
	SELECT * FROM T_ReaderFavorite
	WHERE T_ReaderFavorite. FCategoryId=1
	AND T_ReaderFavorite. FReaderId= T_Reader.FId
)
```
执行完毕查看T_ReaderFavorite表中的内容：
```java  
FCategoryId FReaderId
1 1
5 2
2 3
3 4
5 5
1 6
1 7
4 8
6 9
5 10
2 11
2 12
1 12
3 1
1 3
4 4
1 2
1 4
1 5
1 8
1 9
1 10
1 11
```
可以看到表中的数据没有重复的了，即使重复执行这个SQL 语句也都不会添加新的记录，因为这个SQL语句已经对数据的重复做了检查。