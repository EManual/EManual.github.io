子查询在DELETE 中唯一可以应用的位置就是WHERE 子句，使用子查询可以完成复杂的数据删除控制。其使用方式与SELECT 语句中的子查询基本相同，而且也可以使用相关子查询等高级的特性。下面的SQL语句用来将所有同类书本书超过3 本的图书删除：
```java  
DELETE FROM T_Book b1
WHERE
(
	SELECT COUNT(*) FROM T_Book b2
	WHERE b1. FCategoryId=b2. FCategoryId
)>3
```
上面的SQL 语句使用相关子查询来查询所有与待更新的书籍属于同类别的书籍的总数，如果总数大于3则将当前书籍删除。
执行完毕查看T_Book表中的内容：
```java  
FID FNAME FYEARPUBLISHED FCATEGORYID
1 About J2EE 2008 4
2 Learning Hibernate 2008 4
3 Two Cites 2008 1
4 Jane Eyre 2008 1
5 Oliver Twist 2008 1
14 How To Singing 2008 5
15 DaoDeJing 2008 6
16 Obedience toAuthority 2008 6
```