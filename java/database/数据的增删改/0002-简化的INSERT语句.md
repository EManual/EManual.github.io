INSERT语句中也并不需要我们指定表中的所有列，比如在插入数据的时候某些字段没有值，我们可以忽略这些字段。下面我们插入一条没有备注信息的数据：
```java  
INSERT INTO T_Person(FAge,FName) VALUES(22,"LXF")
```
执行SELECT * FROM T_Person来查看表中的数据：
  
INSERT语句还有另一种用法，可以不用指定要插入的表列，这种情况下将按照定义表中字段顺序来进行插入，我们执行下面的SQL：
```java  
INSERT INTO T_Person VALUES("luren1",23,"China")
```
这里省略了VALUES前面的字段定义，VALUES后面的值列表中按照CREATE TABLE语句中的顺序排列。
这种省略字段列表的方法可以简化输入，不过我们推荐这种用法，因为省略字段列表之后就无法很容易的弄清楚值列表中各个值到底对应哪个字段了，非常容易导致程序出现BUG 并且给程序的调试带来非常大的麻烦。