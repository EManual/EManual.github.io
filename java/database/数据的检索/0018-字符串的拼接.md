SQL允许两个或者多个字段之间进行计算，字符串类型的字段也不例外。比如我们需要以“工号+姓名”的方式在报表中显示一个员工的信息，那么就需要把工号和姓名两个字符串类型的字段拼接计算；再如我们需要在报表中在每个员工的工号前增加“Old”这个文本。
这时候就需要我们对字符串类型的字段（包括字符串类型的常量字段）进行拼接。在不同的数据库系统下的字符串拼接是有很大差异的，因此这里我们将讲解主流数据库下的字符串拼接的差异。
需要注意的是，在Java、C#等编程语言中字符串是用半角的双引号来包围的，但是在有的数据库系统的SQL语法中双引号有其他的含义（比如列的别名），而所有的数据库系统都支持用单引号包围的形式定义的字符串，所以建议读者使用以单引号包围的形式定义的字符串，而且本书也将使用这种方式。
* MYSQL
在Java、C#等编程语言中字符串的拼接可以通过加号“+”来实现，比如："1"+"3"、"a"+"b"。在MYSQL中也可以使用加号“+”来连接两个字符串，比如下面的SQL：
```java  
SELECT "12"+"33",FAge+"1" FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
"12"+"33" FAge+"1"
45			26
45 			29
45 			24
45 			26
45 			29
45 			28
45 			24
45 			29
45 			23
```
仔细观察第一列，惊讶吗？这个列的显示结果并不是我们希望的“1233”，而是把“12”和“33”两个字符串当成数字来求两个数的和了；同样将一个数字与一个字符串用加号“+”连接也是同样的效果，比如这里的第二列。
在MYSQL中，当用加号“+”连接两个字段（或者多个字段）的时候，MYSQL会尝试将字段值转换为数字类型（如果转换失败则认为字段值为0），然后进行字段的加法运算。因此，当计算的"12"+"33"的时候，MYSQL会将“12”和“33”两个字符串尝试转换为数字类型的12和33，然后计算12+33的值，这就是为什么我们会得到45的结果了。同样道理，在计算FAge+"1"的时候，由于FAge为数字类型，所以不需要进行转换，而"1"为字符串类型，所以MYSQL将"1"尝试转换为数字1，然后计算FAge+1做为计算列的值。
MYSQL会尝试将加号两端的字段值尝试转换为数字类型，如果转换失败则认为字段值为0，比如我们执行下面的SQL语句：
```java  
SELECT "abc"+"123",FAge+"a" FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
"abc"+"123" FAge+"a"
	123		 25
	123 	 28
	123 	 23
	123 	 25
	123 	 28
	123 	 27
	123 	 23
	123 	 28
	123 	 22
```
在MYSQL中进行字符串的拼接要使用CONCAT函数，CONCAT函数支持一个或者多个参数，参数类型可以为字符串类型也可以是非字符串类型，对于非字符串类型的参数MYSQL将尝试将其转化为字符串类型，CONCAT函数会将所有参数按照参数的顺序拼接成一个字符串做为返回值。比如下面的SQL语句用于将用户的多个字段信息以一个计算字段的形式查询出来：
```java  
SELECT CONCAT("工号为:",FNumber,"的员工的幸福指数:",FSalary/(FAge-21)) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
CONCAT("工号为:",FNumber,"的员工的幸福指数:",FSalary/(FAge-21))
工号为:DEV001 的员工的幸福指数:2075.000000
工号为:DEV002 的员工的幸福指数:328.685714
工号为:HR001的员工的幸福指数:1100.440000
工号为:HR002的员工的幸福指数:1300.090000
工号为:IT001 的员工的幸福指数:557.142857
工号为:IT002 的员工的幸福指数:466.666667
工号为:SALES001 的员工的幸福指数:2500.000000
工号为:SALES002 的员工的幸福指数:885.714286
工号为:SALES003 的员工的幸福指数:1200.000000
```
CONCAT支持只有一个参数的用法，这时的CONCAT可以看作是一个将这个参数值尝试转化为字符串类型值的函数。MYSQL中还提供了另外一个进行字符串拼接的函数CONCAT_WS，CONCAT_WS可以在待拼接的字符串之间加入指定的分隔符，它的第一个参数值为采用的分隔符，而剩下的参数则为待拼接的字符串值，比如执行下面的SQL：
```java  
SELECT CONCAT_WS(",",FNumber,FAge,FDepartment,FSalary) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
CONCAT_WS(",",FNumber,FAge,FDepartment,FSalary)
DEV001,25,Development,8300.00
DEV002,28,Development,2300.80
HR001,23,HumanResource,2200.88
HR002,25,HumanResource,5200.36
IT001,28,InfoTech,3900.00
IT002,27,InfoTech,2800.00
SALES001,23,Sales,5000.00
SALES002,28,Sales,6200.00
SALES003,22,Sales,1200.00
```
MSSQLServer
与MYSQL不同，MSSQLServer中可以直接使用加号“+”来拼接字符串。比如执行下面的SQL语句：
```java  
SELECT "工号为"+FNumber+"的员工姓名为"+Fname FROM T_Employee WHERE FName IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
工号为 DEV001 的员工姓名为Tom
工号为DEV002 的员工姓名为Jerry
工号为HR001的员工姓名为Jane
工号为HR002的员工姓名为Tina
工号为IT001 的员工姓名为Smith
工号为SALES001 的员工姓名为John
工号为SALES002 的员工姓名为Kerry
工号为SALES003 的员工姓名为Stone
```
Oracle
Oracle中使用“||”进行字符串拼接，其使用方式和MSSQLServer中的加号“+”一样。
比如执行下面的SQL语句：
```java  
SELECT "工号为"||FNumber||"的员工姓名为"||FName FROM T_Employee WHERE FName IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
工号为||FNUMBER||的员工姓名为||FNAME
工号为DEV001 的员工姓名为Tom
工号为DEV002 的员工姓名为Jerry
工号为SALES001 的员工姓名为John
工号为SALES002 的员工姓名为Kerry
工号为SALES003 的员工姓名为Stone
工号为HR001的员工姓名为Jane
工号为HR002的员工姓名为Tina
工号为IT001 的员工姓名为Smith
```
除了“||”，Oracle还支持使用CONCAT()函数进行字符串拼接，比如执行下面的SQL语句：
```java  
SELECT CONCAT("工号:",FNumber) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
CONCAT(工号:,FNUMBER)
工号:DEV001
工号:DEV002
工号:HR001
工号:HR002
工号:IT001
工号:IT002
工号:SALES001
工号:SALES002
工号:SALES003
```
如果CONCAT中连接的值不是字符串，Oracle会尝试将其转换为字符串，比如执行下面的SQL语句：
```java  
SELECT CONCAT("年龄:",FAge) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
CONCAT(年龄:,FAGE)
年龄:25
年龄:28
年龄:23
年龄:28
年龄:22
年龄:23
年龄:25
年龄:28
年龄:27
```
与MYSQL的CONCAT()函数不同，Oracle的CONCAT()函数只支持两个参数，不支持两个以上字符串的拼接，比如下面的SQL语句在Oracle中是错误的：
```java  
SELECT CONCAT("工号为",FNumber,"的员工姓名为",FName) FROM T_Employee WHERE FName IS NOT NULL
```
运行以后Oracle会报出下面的错误信息：
参数个数无效
如果要进行多个字符串的拼接的话，可以使用多个CONCAT()函数嵌套使用，上面的SQL可以如下改写：
```java  
SELECT CONCAT(CONCAT(CONCAT("工号为",FNumber),"的员工姓名为"),FName) FROM T_Employee WHERE FName IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
CONCAT(CONCAT(CONCAT(工号为,FNUMBER),的员工姓名为),FNAME)
工号为DEV001 的员工姓名为Tom
工号为DEV002 的员工姓名为Jerry
工号为SALES001 的员工姓名为John
工号为SALES002 的员工姓名为Kerry
工号为SALES003 的员工姓名为Stone
工号为HR001的员工姓名为Jane
工号为HR002的员工姓名为Tina
工号为IT001 的员工姓名为Smith
```
DB2
DB2中使用“||”进行字符串拼接，其使用方式和MSSQLServer中的加号“+”一样。比如执行下面的SQL语句：
```java  
SELECT "工号为"||FNumber||"的员工姓名为"||FName FROM T_Employee WHERE FName IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1
工号为DEV001 的员工姓名为Tom
工号为DEV002 的员工姓名为Jerry
工号为SALES001 的员工姓名为John
工号为SALES002 的员工姓名为Kerry
工号为SALES003 的员工姓名为Stone
工号为HR001的员工姓名为Jane
工号为HR002的员工姓名为Tina
工号为IT001 的员工姓名为Smith
```
除了“||”，DB2还支持使用CONCAT()函数进行字符串拼接，比如执行下面的SQL语句：
```java  
SELECT CONCAT("工号:",FNumber) FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1
工号:DEV001
工号:DEV002
工号:HR001
工号:HR002
工号:IT001
工号:IT002
工号:SALES001
工号:SALES002
工号:SALES003
```
与Oracle不同，如果CONCAT中连接的值不是字符串，则DB2不会尝试进行类型转换而是报出错误信息，比如执行下面的SQL语句是错误的：
```java  
SELECT CONCAT("年龄:",FAge) FROM T_Employee
```
运行以后DB2会报出下面的错误信息：
未找到类型为"FUNCTION" 命名为 "CONCAT" 且具有兼容自变量的已授权例程与MYSQL的CONCAT()函数不同，DB2的CONCAT()函数只支持两个参数，不支持两个以上字符串的拼接，比如下面的SQL语句在Oracle中是错误的：
```java  
SELECT CONCAT("工号为",FNumber,"的员工姓名为",FName) FROM T_Employee WHERE FName IS NOT NULL
```
运行以后Oracle会报出下面的错误信息：
未找到类型为"FUNCTION" 命名为 "CONCAT" 且具有兼容自变量的已授权例程
如果要进行多个字符串的拼接的话，可以使用多个CONCAT()函数嵌套使用，上面的SQL可以如下改写：
```java  
SELECT CONCAT(CONCAT(CONCAT("工号为",FNumber),"的员工姓名为"),FName) FROM T_Employee WHERE FName IS NOT NULL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1
工号为DEV001 的员工姓名为Tom
工号为DEV002 的员工姓名为Jerry
工号为SALES001 的员工姓名为John
工号为SALES002 的员工姓名为Kerry
工号为SALES003 的员工姓名为Stone
工号为HR001的员工姓名为Jane
工号为HR002的员工姓名为Tina
工号为IT001 的员工姓名为Smith
```