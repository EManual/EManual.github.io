我们在定义字段的时候为字段设置一个默认值，当向表中插入数据的时候如果没有为这个字段赋值则这个字段的值会取值为这个默认值。比如我们希望设置教师信息表中的是否班主任字段FISMaster的默认值为“NO”，那么只要如下设计建表SQL：
```java  
MYSQL、MSSQLServer、DB2：
CREATE TABLE T_Teacher (FNumber VARCHAR(20),FName VARCHAR(20),FAge
INT,FISMaster VARCHAR(5) DEFAULT "NO")
Oracle：
CREATE TABLE T_Teacher (FNumber VARCHAR2(20),FName VARCHAR2(20),FAge
NUMBER (10),FISMaster VARCHAR2(5) DEFAULT "NO")
```
可以看到，与普通字段定义不同的地方是，非空字段的定义在类型定义后增加了“DEFAULT默认值表达式”，其他定义方式与普通字段相同。