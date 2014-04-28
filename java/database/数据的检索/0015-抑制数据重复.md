如果要检索公司里有哪些垂直部门，那么可以执行下面的SQL语句：
```java  
SELECT FDepartment FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FDepartment
Development
Development
HumanResource
HumanResource
InfoTech
InfoTech
Sales
Sales
Sales
```
这里列出了公司所有的垂直部门，不过很多部门名称是重复的，我们必须去掉这些重复的部门名称，每个重复部门只保留一个名称。DISTINCT关键字是用来进行重复数据抑制的最简单的功能，而且所有的数据库系统都支持DISTINCT，DISTINCT的使用也非常简单，只要在SELECT之后增加DISTINCT即可。比如下面的SQL语句用于检索公司里有哪些垂直部门，并且抑制了重复数据的产生：
```java  
SELECT DISTINCT FDepartment FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FDepartment
Development
HumanResource
InfoTech
Sales
```
DISTINCT是对整个结果集进行数据重复抑制的，而不是针对每一个列，执行下面的SQL语句：
```java  
SELECT DISTINCT FDepartment,FSubCompany FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FDepartment FSubCompany
Development Beijing
Development ShenZhen
HumanResource Beijing
InfoTech Beijing
InfoTech ShenZhen
Sales Beijing
Sales ShenZhen
```
检索结果中不存在FDepartment和FSubCompany列都重复的数据行，但是却存在FDepartment列重复的数据行，这就验证了“DISTINCT是对整个结果集进行数据重复抑制的”这句话。