删除数据的SQL 语句非常简单，我们只要指定要删除的表就可以了，比如我们要将T_Debt和T_Person表中的数据删除，那么执行下面的SQL语句即可：
```java  
DELETE FROM T_Debt;
DELETE FROM T_Person;
```
由于T_Debt 表中FPerson 字段是指向表T_Person 的FName 字段的外键，所以必须首先删除T_Debt表中的数据后才能删除T_Person中的数据。
执行SELECT * FROM T_Debt查看T_Debt表中的数据变化。
执行完此SQL语句后执行SELECT * FROM T_Person来查看T_Person表中的数据变化。
可以见表中所有的数据行都被删除了，T_Debt和T_Person中没有任何数据。
初学者往往容易把DROP TABLE 语句和DELETE 混淆，虽然二者名字中都有“删除”两个字，不过DELETE 语句仅仅是删除表中的数据行，而表的结构还存在，而DROP TABLE语句则不仅将表中的数据行全部删除，而且还将表的结构也删除。可以形象的比喻成DELETE 语句仅仅是“吃光碗里的饭”，而DROP TABLE 语句则是“吃光碗里的饭还将碗砸碎”。如果我们执行“DROP TABLE T_Person”的话，那么再次执行“SELECT * FROMT_Person”的时候数据库系统就会报告“数据表T_Person不存在”。
上边介绍的DELETE 语句将表中的所有数据都删除了，如果我们只想删除我们指定的数据行怎么办呢？和UPDATE 语句类似，DELETE 语句也提供了WHERE 语句进行数据的过滤，这样只有符合过滤条件的数据行才会被删除。