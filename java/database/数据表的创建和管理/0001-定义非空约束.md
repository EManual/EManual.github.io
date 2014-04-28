我们在注册一些网站的会员的时候都需要填写一些表格，这些表格中有一些属于必填内容，如果不填写的话会无法完成注册。同样我们在设计数据表的时候也希望某些字段为必填值，比如学生信息表中的学号、姓名、年龄字段是必填的，而个人爱好、家庭电话号码等字段则选填，所以我们如下设计建表SQL：
```java  
MYSQL、MSSQLServer、DB2：
CREATE TABLE T_Student (FNumber VARCHAR(20) NOT NULL ,FName VARCHAR(20)
						NOT NULL ,FAge INT NOT NULL ,FFavorite VARCHAR(20),FPhoneNumber VARCHAR(20))
Oracle：
CREATE TABLE T_Student (FNumber VARCHAR2(20) NOT NULL ,FName
						VARCHAR2(20) NOT NULL ,FAge NUMBER (10) NOT NULL ,FFavorite
						VARCHAR2(20),FPhoneNumber VARCHAR2(20))
```
可以看到，与普通字段定义不同的地方是，非空字段的定义在类型定义后增加了“NOT NULL”，其他定义方式与普通字段相同。