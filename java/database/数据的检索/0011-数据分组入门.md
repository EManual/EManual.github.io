数据分组用来将数据分为多个逻辑组，从而可以对每个组进行聚合运算。SQL语句中使用GROUP BY子句进行分组，使用方式为“GROUP BY 分组字段”。分组语句必须和聚合函数一起使用，GROUP BY子句负责将数据分成逻辑组，而聚合函数则对每一个组进行统计计算。
虽然GROUP BY子句常常和聚合函数一起使用，不过GROUP BY子句并不是不能离开聚合函数而单独使用的，虽然不使用聚合函数的GROUP BY子句看起来用处不大，不过它能够帮助我们更好的理解数据分组的原理，所以本小节我们将演示GROUP BY子句的分组能力。
我们首先来看一下如果通过SQL语句实现“查看公司员工有哪些年龄段的”，因为这里只需要列出员工的年龄段，所以使用GROUP BY子句就完全可以实现：
```java  
SELECT FAge FROM T_Employee GROUP BY FAge
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FAge
22
23
25
27
28
```
这个SQL语句处理表中的所有记录，并且将FAge相同的数据行放到一组，分组后的数据可以看作一个临时的结果集，而SELECT FAge语句则取出每组的FAge字段的值，这样我们就得到上表的员工年龄段表了。
GROUP BY子句将检索结果划分为多个组，每个组是所有记录的一个子集。上面的SQL例子在执行的时候数据库系统将数据分成了下面的分组：
  
需要注意的是GROUP BY子句的位置，GROUP BY子句必须放到SELECT语句的之后，如果SELECT语句有WHERE子句，则GROUP BY子句必须放到WHERE语句的之后。比如下面的SQL语句是错误的：
```java  
SELECT FAge FROM T_Employee GROUP BY FAge WHERE FSubCompany = "Beijing"
```
而下面的SQL语句则是正确的：
```java  
SELECT FAge FROM T_Employee WHERE FSubCompany = "Beijing" GROUP BY FAge
```
需要分组的所有列都必须位于GROUP BY子句的列名列表中，也就是没有出现在GROUP BY子句中的列（聚合函数除外）是不能放到SELECT语句后的列名列表中的。比如下面的SQL语句是错误的：
```java  
SELECT FAge,FSalary FROM T_Employee GROUP BY FAge
```
道理非常简单，因为采用分组以后的查询结果集是以分组形式提供的，由于每组中人员的
员工工资都不一样，所以就不存在能够统一代表本组工资水平的FSalary字段了，所以上面的SQL语句是错误的。不过每组中员工的平均工资却是能够代表本组统一工资水平的，所以可以对FSalary使用聚合函数，下面的SQL语句是正确的：
```java  
SELECT FAge,AVG(FSalary) FROM T_Employee GROUP BY FAge
```
GROUP BY子句中可以指定多个列，只需要将多个列的列名用逗号隔开即可。指定多个分组规则以后，数据库系统将按照定义的分组顺序来对数据进行逐层分组，首先按照第一个分组列进行分组，然后在每个小组内按照第二个分组列进行再次分组……逐层分组，从而实现“组中组”的效果，而查询的结果集是以最末一级分组来进行输出的。比如下面的SQL语句将会列出所有分公司的所有部门情况：
```java  
SELECT FSubCompany,FDepartment FROM T_Employee GROUP BY FSubCompany,FDepartment
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
上面的SQL例子在执行的时候数据库系统将数据分成了下面的分组：
  