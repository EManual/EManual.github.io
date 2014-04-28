到目前为止我们使用的聚合函数都是对普通结果集进行统计的，我们同样可以使用聚合函数来对分组后的数据进行统计，也就是统计每一个分组的数据。我们甚至可以认为在没有使用GROUP BY语句中使用聚合函数不过是在一个整个结果集是一个组的分组数据中进行数据统计分析罢了。
让我们来看一下“查看每个年龄段的员工的人数”如何用数据分组来实现，下面是实现此功能的SQL语句：
```java  
SELECT FAge,COUNT(*) AS CountOfThisAge FROM T_Employee GROUP BY FAge
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
GROUP BY子句将检索结果按照年龄划分为多个组，每个组是所有记录的一个子集。上面的SQL例子在执行的时候数据库系统将数据分成了下面的分组：
  
可以看到年龄相同的员工被分到了一组，接着使用“COUNT(*)”来统计每一组中的条数，这样就得到了每个年龄段的员工的个数了。
可以使用多个分组来实现更精细的数据统计，比如下面的SQL语句就可以统计每个分公司的年龄段的人数：
```java  
SELECT FSubCompany,FAge,COUNT(*) AS CountOfThisSubCompAge FROM T_Employee GROUP BY FSubCompany,FAge
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
上面的执行结果是按照数据库系统默认的年龄进行排序的，为了更容易的按照每个分公司进行查看，我们可以指定按照FSubCompany字段进行排序，带ORDER BY的SQL语句如下：
```java  
SELECT FSubCompany,FAge,COUNT(*) AS CountOfThisSubCompAge FROM T_Employee GROUP BY FSubCompany,FAge ORDER BY FSubCompany
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
上面的SQL语句中，GROUP BY子句将检索结果首先按照FSubCompany进行分组，然后在每一个分组内又按照FAge进行分组，数据库系统将数据分成了下面的分组：
  
“COUNT(*)”对每一个分组统计总数，这样就可以统计出每个公司每个年龄段的员工的人数了。
SUM、AVG、MIN、MAX也可以在分组中使用。比如下面的SQL可以统计每个公司中的工资的总值：
```java  
SELECT FSubCompany,SUM(FSalary) AS FSalarySUM FROM T_Employee GROUP BY FSubCompany
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
下面的SQL可以统计每个垂直部门中的工资的平均值：
```java  
SELECT FDepartment,SUM(FSalary) AS FSalarySUM FROM T_Employee GROUP BY FDepartment
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
下面的SQL可以统计每个垂直部门中员工年龄的最大值和最小值：
```java  
SELECT FDepartment,MIN(FAge) AS FAgeMIN,MAX(FAge) AS FAgeMAX FROM T_Employee GROUP BY FDepartment
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  