在UPDATE语句中可以在更新列表中以及WHERE语句使用子查询。下面演示一个将图书的出版日期全部更新为所有图书中的最新出版日期，SQL语句如下：
```java  
UPDATE T_Book SET FYearPublished=(SELECT MAX(FYearPublished) FROM T_Book)
```
注意，在MYSQL 中是不支持使用子查询来更新一个列的，所以这个UPDATE 语句无法在MYSQL中执行。
执行完毕查看T_Book表中的内容：
```java  
FID FNAME FYEARPUBLISHED FCATEGORYID
1 About J2EE 2008 4
2 Learning Hibernate 2008 4
3 Two Cites 2008 1
4 Jane Eyre 2008 1
5 Oliver Twist 2008 1
6 History of China 2008 2
7 History of England 2008 2
8 History of America 2008 2
9 History of TheWorld 2008 2
10 Atom 2008 3
11 RELATIVITY 2008 3
12 Computer 2008 3
13 Astronomy 2008 3
14 How To Singing 2008 5
15 DaoDeJing 2008 6
16 Obedience toAuthority 2008 6
```
如果UPDATE语句拥有WHERE子句，那么还可以在WHERE子句中使用子查询，其使用方式与SELECT语句中的子查询基本相同，而且也可以使用相关子查询等高级的特性。
下面的SQL语句用来将所有同类书本书超过3 本的图书的出版日期更新为2005：
```java  
UPDATE T_Book b1 SET b1.FYearPublished=2005
WHERE
(
	SELECT COUNT(*) FROM T_Book b2
	WHERE b1. FCategoryId=b2. FCategoryId
)>3
```
上面的SQL 语句使用相关子查询来查询所有与待更新的书籍属于同类别的书籍的总数，如果总数大于3则将当前书籍的出版日期更新为2005。
执行完毕查看T_Book表中的内容：
```java  
FID FNAME FYEARPUBLISHED FCATEGORYID
1 About J2EE 2008 4
2 Learning Hibernate 2008 4
3 Two Cites 2008 1
4 Jane Eyre 2008 1
5 Oliver Twist 2008 1
6 History of China 2005 2
7 History of England 2005 2
8 History of America 2005 2
9 History of TheWorld 2005 2
10 Atom 2005 3
11 RELATIVITY 2005 3
12 Computer 2005 3
13 Astronomy 2005 3
14 How To Singing 2008 5
15 DaoDeJing 2008 6
16 Obedience toAuthority 2008 6
```