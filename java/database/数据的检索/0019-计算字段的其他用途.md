我们不仅能在SELECT语句中使用计算字段，我们同样可以在进行数据过滤、数据删除以及数据更新的时候使用计算字段，下面我们举几个例子。
计算处于合理工资范围内的员工我们规定一个合理工资范围：上限为年龄的1.8倍加上5000元，下限为年龄的1.5倍加上2000元，介于这两者之间的即为合理工资。我们需要查询所有处于合理工资范围内的员工信息。因此编写如下的SQL语句：
```java  
SELECT * FROM T_Employee WHERE Fsalary BETWEEN Fage*1.5+2000 AND Fage*1.8+5000
```
这里我们在BETWEEN……AND……语句中使用了计算表达式。执行完毕我们就能在输出结果中看到下面的执行结果：
  
查询“工资年龄指数”
我们定义“工资年龄指数”为“工资除以年龄”。我们需要查询“工资年龄指数”的最高值和最低值。因此编写如下的SQL语句：
```java  
SELECT MAX(FSalary/FAge) AS MAXVALUE,MIN(FSalary/FAge) AS MINVALUE FROM T_Employee
```
这里我们在MAX、MIN函数中使用了计算字段。执行完毕我们就能在输出结果中看到
下面的执行结果：
```java  
MAXVALUE 			MINVALUE
332.0000000000000 54.5454545454545
```
年龄全部加1
新的一年到来了，系统需要自动将员工的年龄全部加1。这个工作如果使用代码来完成的话会是这样：
```java  
result = executeQuery(“SELECT * FROM T_Employee”);
	for(i=0;i<result.count;i++)
	{
		age = result[i].get(“FAge”);
		number = result[i].get(“FNumber”);
		age=age+1;
		executeUpdate(“UPDATE T_Employee SET FAge=”+age+” WHERE
		FNumber=”+number);
	}
```
这种方式在数据量比较大的时候速度是非常慢的，而在UPDATE中使用计算字段则可以非常简单快速的完成任务，编写下面的SQL语句：
UPDATE T_Employee SET FAge=FAge+1
这里在SET子句中采用计算字段的方式为FAge字段设定了新值。
执行完毕后执行SELECT * FROM T_Employee来查看修改后的数据：
  