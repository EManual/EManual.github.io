前面我们讲解了聚合函数的使用，比如要查看年龄为23岁员工的人数，只要执行下面的SQL就可以：
```java  
SELECT COUNT(*) FROM T_Employee WHERE FAge=23
```
可是如果我们想查看每个年龄段的员工的人数怎么办呢？一个办法是先得到所有员工的年龄段信息，然后分别查询每个年龄段的人数，显然这样是非常低效且烦琐的。这时候就是数组分组开始显现威力的时候了。
为了更好的演示本节中的例子，我们为T_Employee表增加两列，分别为表示其所属分公司的FSubCompany字段和表示其所属部门的FDepartment，在不同的数据库下执行相应的SQL语句：
MYSQL,MSSQLServer,DB2:
```java  
ALTER TABLE T_Employee ADD FSubCompany VARCHAR(20);
ALTER TABLE T_Employee ADD FDepartment VARCHAR(20);
```
Oracle:
```java  
ALTER TABLE T_Employee ADD FSubCompany VARCHAR2(20);
ALTER TABLE T_Employee ADD FDepartment VARCHAR2(20);
```
两个字段添加完毕后还需要将表中原有数据行的这两个字段值更新，执行下面的SQL语句：
```java  
UPDATE T_Employee SET FSubCompany="Beijing",FDepartment="Development" WHERE FNumber="DEV001";
UPDATE T_Employee SET FSubCompany="ShenZhen",FDepartment="Development" WHERE FNumber="DEV002";
UPDATE T_Employee SET FSubCompany="Beijing",FDepartment="HumanResource" WHERE FNumber="HR001";
UPDATE T_Employee SET FSubCompany="Beijing",FDepartment="HumanResource" WHERE FNumber="HR002";
UPDATE T_Employee SET FSubCompany="Beijing",FDepartment="InfoTech" WHERE FNumber="IT001";
UPDATE T_Employee SET FSubCompany="ShenZhen",FDepartment="InfoTech" WHERE FNumber="IT002";
UPDATE T_Employee SET FSubCompany="Beijing",FDepartment="Sales" WHERE FNumber="SALES001";
UPDATE T_Employee SET FSubCompany="Beijing",FDepartment="Sales" WHERE FNumber="SALES002";
UPDATE T_Employee SET FSubCompany="ShenZhen",FDepartment="Sales" WHERE FNumber="SALES003";
```