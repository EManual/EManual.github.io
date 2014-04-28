通过主键能够唯一定位一条数据记录，而且在进行外键关联的时候也需要被关联的数据表具有主键，所以为数据表定义主键是非常好的习惯。在CREATE TABLE 中定义主键是通过PRIMARY KEY 关键字来进行的，定义的位置是在所有字段定义之后。比如我们为公交车建立一张数据表，这张表中有公交车编号FNumber、驾驶员姓名FDriverName、投入使用年数FUsedYears等字段，其中公交车编号FNumber 字段要定义为主键，那么只要如下设计建表SQL：
```java  
MYSQL,MSSQLServer:
CREATE TABLE T_Bus (FNumber VARCHAR(20),FDriverName VARCHAR(20),
FUsedYears INT,PRIMARY KEY (FNumber))
Oracle:
CREATE TABLE T_Bus (FNumber VARCHAR2(20),FDriverName VARCHAR2(20),
FUsedYears NUMBER (10),PRIMARY KEY (FNumber))
DB2:
CREATE TABLE T_Bus (FNumber VARCHAR(20) NOT NULL,FDriverName
VARCHAR(20),
FUsedYears INT,PRIMARY KEY (FNumber))
```
可以看到，主键定义是在所有字段后的“约束定义段”中定义的，格式为PRIMARY KEY(主键字段名)，在有的数据库系统中主键字段名两侧的括号是可以省略的，也就是可以写成PRIMARY KEY FNumber，不过为了能够更好的跨数据库，建议不要采用这种不通用的写法。
需要注意的是，在上边列出的DB2数据库的CREATE TABLE 语句中，我们为FNumber字段设置了非空约束。因为在DB2 中，主键字段必须被添加非空约束，否则会报出类似“"FNUMBER"不能是一列主键或唯一键，因为它可包含空值。”的错误。
有的时候数据表中是不存在一个唯一的主键的，比如某个行业协会需要创建一个保存个人会员信息的表，表中记录了所属公司名称FCompanyName、公司内部工号FInternalNumber、姓名FName 等，由于存在同名的情况，所以不能够使用姓名做为主键，同样由于各个公司之间的内部工号也有可能重复，所以也不能使用公司内部工号做为主键。不过如果确定了公司名称，那么公司内部工号也就唯一了，也就是说通过公司名称FCompanyName 和公司内部工号FInternalNumber 两个字段一起就可以唯一确定一个个人会员了，我们可以让FCompanyName、FInternalNumber 两个字段联合起来做为主键，这样的主键被称为联合主键（或者称为复合主键）。可以有两个甚至多个字段来做为联合主键，这就可以解决一张表中没有唯一主键字段的问题了。定义联合主键的方式和唯一主键类似，只要在PRIMARY KEY后的括号中列出做为联合主键的各个字段就可以了。上面的例子的建表SQL如下：
```java  
MYSQL,MSSQLServer,DB2:
CREATE TABLE T_PersonalMember (FCompanyName VARCHAR(20),
FInternalNumber VARCHAR(20),FName VARCHAR(20),
PRIMARY KEY (FCompanyName,FInternalNumber))
Oracle:
CREATE TABLE T_PersonalMember (FCompanyName VARCHAR2(20),
FInternalNumber VARCHAR2(20),FName VARCHAR2(20),
PRIMARY KEY (FCompanyName,FInternalNumber))
DB2:
CREATE TABLE T_PersonalMember (FCompanyName VARCHAR(20) NOT NULL,
FInternalNumber VARCHAR(20) NOT NULL,FName VARCHAR(20),
PRIMARY KEY (FCompanyName,FInternalNumber))
```
同样需要注意的是，在DB2中组成联合主键的每一个字段也都必须被添加非空约束。采用联合主键可以解决表中没有唯一主键字段的问题，不过联合主键有如下的缺点：
1，效率低。在进行数据的添加、删除、查找以及更新的时候数据库系统必须处理两个字段，这样大大降低了数据处理的速度。
2，使得数据库结构设计变得糟糕。组成联合主键的字段通常都是有业务含义的字段，这与“使用逻辑主键而不是业务主键”的最佳实践相冲突，容易造成系统开发以及维护上的麻烦。
3，使得创建指向此表的外键关联关系变得非常麻烦甚至无法创建指向此表的外键关联关系。
4，加大开发难度。很多开发工具以及框架只对单主键有良好的支持，对于联合主键经常需要进行非常复杂的特殊处理。
考虑到这些缺点，我们应该只在兼容遗留系统等特殊场合才使用联合主键，而在其他场合则应该使用唯一主键。