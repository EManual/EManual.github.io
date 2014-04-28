我们讲到可以将标量子查询当成SELECT列表中的一个列，唯一的约束就是子查询的返回值必须只有一行记录，而且只能有一个列。看完上章的例子有的读者可能认为标量子查询只能返回唯一的值，其实标量子查询完全可以返回随当前查询记录而变化的值。比如下面的SQL语句可以清楚的说明这一点：
```java  
SELECT FId,FName,(SELECTMAX(FYearPublished) FROM T_Book WHERE T_Book. FCategoryId= T_Category.FId) FROM T_Category
```
这个SELECT语句首先检索FId、FName两个字段，而第三个字段不是一个列二是一个子查询。这个子查询位于主查询的内部，它返回一类图书的最新出版年份。因为聚合函数仅返回一行记录，所以这满足标量子查询的条件。通过WHERE语句，这个子查询也被连接到外部的SELECT查询语句中，因为这个连接，MAX(FYearPublished)将返回每类图书的最新出版年份。
需要注意的是这里的子查询与前边讲的有所不同，前面用到的子查询没有依赖于外部查询中的字段，也就是可以直接单独执行，而这里的子查询是依赖于外部查询中的T_Category.FId字段的，这个子查询是无法单独执行的，尝试在数据库系统中执行下面的SQL语句：
```java  
SELECTMAX(FYearPublished) FROM T_Book WHERE T_Book. FCategoryId= T_Category.FId
```
执行后数据库系统会报出如下的错误信息：
* 无法绑定由多个部分组成的标识符"T_Category.FId"。
因为这个子查询中引用了外部查询中的字段。这种引用了外部查询中字段的子查询被称为相关子查询。
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FId FName
1 Story 2002
2 History 2008
3 Theory 1971
4 Technology 2005
5 Art 1771
6 Philosophy 2001
```
下面结合执行结果来仔细分析一下这句SQL语句。首先看执行结果中的第一行，它的FId是1.子查询通过T_Book表中的FCategoryId字段和T_Category表中的FId连接到外部查询。对于第一行，FId是1，因此子查询在T_Book表中检索FCategoryId字段等于1的所有图书的FYearPublished字段的最大值；接着查看外部查询的第二行，FId是2，这次子查询检索T_Book表中FCategoryId字段等于2的所有图书的FYearPublished字段的最大值；然后查看外部查询的第三行……以此类推。
如果没有子查询中的WHERE子句将子查询连接到外部查询，则结果将只是子查询返回的所有记录的最大值。比如修改上面的SQL语句，将子查询中的WHERE 子句删除，将得到下面的SQL语句：
```java  
SELECT FId,FName,(SELECTMAX(FYearPublished) FROM T_Book) FROM T_Category
```
执行这个SQL语句则会得到下面的执行结果：
```java  
FId FName
1 Story 2008
2 History 2008
3 Theory 2008
4 Technology 2008
5 Art 2008
6 Philosophy 2008
```
MAX(FYearPublished)现在是T_Book 表中所有记录的最大出版年份，它不与任何书籍分类相关。