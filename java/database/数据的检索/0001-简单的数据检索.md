“取出一张表中所有的数据”是最简单的数据检索任务，完成这个最简单任务的SQL语句也是最简单的，我们只要执行“SELECT * FROM 表名”即可。比如我们执行下面的SQL语句：
```java  
SELECT * FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
执行结果中列出了表中的所有行，而且包含了表中每一列的数据。
上面的SQL 语句执行的结果中包含了表中每一列的数据，有的时候并不需要所有列的数据。比如我们只需要检索所有员工的工号，如果我们采用“SELECT* FROM T_Employee”进行检索的话，数据库系统会将所有列的数据从数据库中取出来，然后通过网络发送给我们，这不仅会占用不必要的CPU 资源和内存资源，而且会占用一定的网络带宽，这在我们这种测试模式下不会有影响，但是如果是在真实的生产环境中的话就会大大降低系统的吞吐量，因此最好在检索的之后只检索需要的列。那么如何只检索出需要的列呢？
检索出所有的列的SQL 语句为“SELECT * FROM T_Employee”，其中的星号“*”就意味着“所有列”，那么我们只要将星号“*”替换成我们要检索的列名就可以了。比如我
们执行下面的SQL语句：
```java  
SELECT FNumber FROM T_Employee
```
这就表示我们要检索出表T_Employee 中的所有数据，并且只取出FNumber 列。执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FNumber
DEV001
DEV002
HR001
HR002
IT001
SALES001
SALES002
SALES003
```
可以看到只有FNumber 列中的数据被检索出来了。
上面的SQL 语句列出了FNumber 列中的数据，那么如果想列出不止一个列中的数据呢？非常简单，只要在SELECT 语句后列出各个列的列名就可以了，需要注意的就是各个列之间要用半角的逗号“,”分隔开。比如我们执行下面的SQL语句：
```java  
SELECT FName,FAge FROM T_Employee
```
这就表示我们要检索出表T_Employee 中的所有数据，并且只取出FName和FAge两列的内容。执行完毕我们就能在输出结果中看到下面的执行结果。
可以看到，执行结果中列出了所有员工的姓名和他们的年龄。
如果要用这种显式指定数据列的方式取出所有列，我们就可以编写下面的SQL：
SELECT FNumber,FName,FAge,FSalary FROM T_Employee
执行完毕我们就能在输出结果中看到下面的执行结果。
这和“SELECT * FROM T_Employee”的执行结果是一致的，也就是说“SELECT FNumber,FName,FAge,FSalary FROM T_Employee”和“SELECT* FROM T_Employee”是等价的。
* 列别名
由于编码命名规范、编程框架要求等的限制，数据表的列名有的时候意思并不是非常易读，比如T_Employee中的姓名字段名称为FName，而如果我们能用Name甚至“姓名”来代表这个字段就更清晰易懂了，可是字段名已经不能更改了，那么难道就不能用别的名字来使用已有字段了吗？
当然不是！就像可以为每个人取一个外号一样，我们可以为字段取一个别名，这样就可以使用这个别名来引用这个列了。别名的定义格式为“列名AS 别名”，比如我们要为FNumber字段取别名为Number16，FName字段取别名为Name、FAge 字段取别名为Age、为FSalary
字段取别名为Salary，那么编写下面的SQL即可：
```java  
SELECT FNumber AS Number1,FName AS Name,FAge AS Age,FSalary AS Salary FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  
这里的执行结果和“SELECT FNumber,FName,FAge,FSalary FROM T_Employee”
执行结果一样，唯一不同的地方就是表头中的列名，这里的表头的列名就是我们为各列设定的别名。
定义别名的时候“AS”不是必须的，是可以省略的，比如下面的SQL也是正确的：
```java  
SELECT FNumber Number1,FName Name,FAge Age,FSalary Salary FROM T_Employee
```
如果数据库系统支持中文列名，那么还可以用中文来为列设定别名，这样可读性就更好了，比如在MSSQLServer中文版上执行下面的SQL：
```java  
SELECT FNumber 工号,FName 姓名,FAge 年龄,FSalary 工资FROM T_Employee
```
执行完毕我们就能在输出结果中看到下面的执行结果：
  