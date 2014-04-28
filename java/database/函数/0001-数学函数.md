SQL标准中只规定了4个数学函数，不过很多主流的数据库系统都提供了大量常用的数学函数，而且几乎所有的数据库系统都对它们提供了支持，因此这里我们有必要对这些函数进行详细的介绍。
* 求绝对值
ABS()函数用来返回一个数值的绝对值。该函数接受一个参数，这个参数为待求绝对值的表达式。执行下面的SQL语句：
```java  
SELECT FWeight - 50,ABS(FWeight - 50) , ABS(-5.38) FROM T_Person
```
* 求指数
POWER()函数是用来计算指数的函数。该函数接受两个参数，第一个参数为待求幂的表达式，第二个参数为幂。执行下面的SQL语句：
```java  
SELECT FWeight,POWER(FWeight,-0.5),POWER(FWeight,2),POWER(FWeight,3),POWER(FWeight,4) FROM T_Person
```
* 求平方根
SQRT()函数是用来计算平方根的函数。该函数接受一个参数，这个参数为待计算平方根的表达式。执行下面的SQL语句：
```java  
SELECT FWeight,SQRT(FWeight) FROM T_Person
```
* 求随机数
在生成随机密码、随机问题等的时候需要使用随机算法生成随机数。不同的数据库提供的生成随机数的方法不同。
* MYSQL
在MYSQL中提供了RAND()函数用来生成随机算法，执行下面的SQL语句：
```java  
SELECT RAND()
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
0.4614449609115853
```
因为RAND()函数的返回值是随机的，所以这里看到的执行结果很可能与您的执行结果不同。
* MSSQLServer
在MSSQLServer中也提供了RAND()函数用来生成随机算法，其使用方法和MYSQL中的类似。除此之外RAND()函数还支持一个参数，这个参数为随机数种子，执行下面的SQL语句：
```java  
SELECT RAND(9527)
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
0.8910896774185367
* Oracle
```
Oracle中没有内置的生成随机数的函数，不过Oracle 提供了包dbms_random用来生成随机数，使用方法如下：
```java  
SELECT dbms_random.value FROM dual
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
VALUE
0.14190212623840265315906642197785380122
```
除了上面这种使用方式，dbms_random包中还提供了其他几种方法用来完成其他的随机处理。
dbms_random.value (low, high)用来返回一个大于或等于low，小于high的随机数，执行下面的SQL语句：
```java  
SELECT dbms_random.value(60,100) FROM dual
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
DBMS_RANDOM.VALUE(60,100)
89.1205784709389820708190169252633962636
```
dbms_random. normal 用来返回服从正态分布的一组数。此正态分布标准偏差为1，期望值为0。这个函数返回的数值中有68%是介于-1 与+1 之间，95%介于-2 与+2 之间，99%介于-3与+3之间。执行下面的SQL语句：
```java  
SELECT dbms_random.normal FROM dual
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
NORMAL
-0.8376085098260252406127477817042282552217
```
dbms_random.string(opt, len)用来返回一个随机字符串，opt为选项参数，len表示返回的字符串长度，最大值为60。参数opt 可选值如下：
```java  
"U"：返回全是大写的字符串。
"L"：返回全是小写的字符串。
"A"：返回大小写结合的字符串。
"X"：返回全是大写和数字的字符串。
"P"：返回键盘上出现字符的随机组合。
```
可以使用dbms_random.string 来产生随机的用户密码或者验证码。执行下面的SQL 语句：
```java  
SELECT dbms_random.string("U",8) as UP,
dbms_random.string("L",5) as LP,
dbms_random.string("A",6) as AP,
dbms_random.string("X",6) as XP,
dbms_random.string("P",8) as PP FROM dual
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
UP LP AP XP PP
RXSINVJD swokb blsYor M63XKZ 4H{lUKMs
```
* DB2
和Oracle一样，DB2同样没有内置的生成随机数的函数，不过DB2的SYSFUN包提供了rand函数用来生成随机数，在使用之前要确保已经被正确安装了，其使用方法非常简单，执行下面的SQL语句：
```java  
select SYSFUN.rand() from SYSIBM.SYSDUMMY1
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
1
0.1216772972808008
```
舍入到最大整数
在MYSQL、MSSQLServer和DB2中提供了名称为CEILING()函数，Oracle也提供了类似的函数CEIL()。这个函数用来舍掉一个数的小数点后的部分，并且向上舍入到邻近的最大的整数。比如3.33将被舍入为4、2.89 将被舍入为3、-3.61将被舍入为-3。如果感觉-3.61将被舍入为-3 而不是-4 感到奇怪，那么请记住这个函数是用来向上舍入到最大的整数，在英语中CEILING可以理解为“天花板”，舍入到“高高在上的天花板”当然也就是尽可能大的舍入了。
这个函数有一个参数，参数为待舍入的数值，执行下面的SQL语句：
```java  
MYSQL、MSSQLServer、DB2：
SELECT FName,FWeight, CEILING(FWeight), CEILING(FWeight*-1) FROM T_Person
Oracle：
SELECT FName,FWeight, CEIL(FWeight) , CEIL (FWeight*-1) FROM T_Person
```
舍入到最小整数
SQL中提供了FLOOR()函数，和CEILING()函数正好相反，FLOOR()函数用来舍掉一个数的小数点后的部分，并且向下舍入到邻近的最小的整数。比如3.33将被舍入为3、2.89将被舍入为2、-3.61将被舍入为-4。如果感觉-3.61将被舍入为-4而不是-3感到奇怪，那么请记住这个函数是用来向下舍入到最小的整数，在英语中FLOOR 可以理解为“地板”，舍入到“低低在下的地板”当然也就是尽可能小的舍入了。
这个函数有一个参数，参数为待舍入的数值，执行下面的SQL语句：
```java  
SELECT FName,FWeight,FLOOR(FWeight),FLOOR(FWeight*-1) FROM T_Person
```
* 四舍五入
ROUND()函数也是用来进行数值四舍五入的，不过不像CEILING()函数那样总是向最大值舍入或者像FLOOR()函数那样总是向最小值舍入，ROUND()函数将数值向最近的数值舍入。在英语中ROUND可以理解为“半径”，舍入到“离我半径最近的数”当然也就是四舍五入了。
ROUND()函数有两个参数和单一参数两种用法，下面分别进行介绍。
* 两个参数
两个参数的ROUND()函数用法为：ROUND(m,d)，其中m为待进行四舍五入的数值，而d则为计算精度，也就是进行四舍五入时保留的小数位数。比如3.663 进行精度为2 的四舍五入得到3.66、-2.337 进行精度为2 的四舍五入得到-2.34、3.32122进行精度为3的四舍五入得到3.321。当d为0 的时候则表示不保留小数位进行四舍五入，比如3.663进行精度为0的四舍五入得到4、-2.337进行精度为0的四舍五入得到-2、3.32122进行精度为
0的四舍五入得到3。
特别值得一提的是，d还可以取负值，这时表示在整数部分进行四舍五入。比如36.63进行精度为-1 的四舍五入得到40、233.7 进行精度为-2 的四舍五入得到200、3321.22 进行精度为-2的四舍五入得到3300。
执行下面的SQL语句：
```java  
SELECT FName,FWeight, ROUND(FWeight,1),ROUND(FWeight*-1,0) , ROUND(FWeight,-1) FROM T_Person;
```
* 单一参数
单一参数的ROUND()函数用法为：ROUND(m)，其中m为待进行四舍五入的数值，它可以看做精度为0 的四舍五入运算，也就是ROUND(m,0)。比如3.663进行四舍五入得到4、-2.337进行四舍五入得到-2、3.32122进行四舍五入得到3。
执行下面的SQL语句：
```java  
SELECT FName,FWeight, ROUND(FWeight), ROUND(FWeight*-1) FROM T_Person
```
注意这种单一函数的用法在MSSQLServer 上以及DB2 上不被支持，必须显示的指明精度为0。
* 求正弦值
用来计算一个数值的正弦值的函数为SIN()，它接受一个参数，这个参数为待计算正弦值的表达式。执行下面的SQL语句：
```java  
SELECT FName,FWeight,SIN(FWeight) FROM T_Person
```
* 求余弦值
用来计算一个数值的余弦值的函数为COS ()，它接受一个参数，这个参数为待计算余弦值的表达式。执行下面的SQL语句：
```java  
SELECT FName,FWeight, COS(FWeight) FROM T_Person
```
* 求反正弦值
用来计算一个数值的反正弦值的函数为ASIN()，它接受一个参数，这个参数为待计算反正弦值的表达式。执行下面的SQL语句：
```java  
SELECT FName,FWeight, ASIN(1/FWeight) FROM T_Person
```
* 求反余弦值
用来计算一个数值的反余弦值的函数为ACOS()，它接受一个参数，这个参数为待计算反余弦值的表达式。执行下面的SQL语句：
```java  
SELECT FName,FWeight, ACOS(1/FWeight) FROM T_Person
```
* 求正切值
用来计算一个数值的正切值的函数为TAN()，它接受一个参数，这个参数为待计算正切值的表达式。执行下面的SQL语句：
```java  
SELECT FName,FWeight, TAN(FWeight) FROM T_Person
```
* 求反正切值
用来计算一个数值的反正切值的函数为ATAN()，它接受一个参数，这个参数为待计算反正切值的表达式。执行下面的SQL语句：
```java  
SELECT FName,FWeight, ATAN(FWeight) FROM T_Person
```
* 求2个变量的反正切
ATAN2函数（在MYSQLServer 中这个函数名称为ATN2）用来计算2 个变量的反正切，其使用格式为：ATAN2(X,Y)，函数返回2 个变量X 和Y 的反正切。它类似于计算Y/X 的反正切，除了两个参数的符号被用来决定结果的象限。
执行下面的SQL语句：
```java  
MYSQL,Oracle,DB2:
SELECT FName,FWeight, ATAN2(FWeight,2) FROM T_Person
MSSQLServer:
SELECT FName,FWeight, ATN2(FWeight,2) FROM T_Person
```
* 求余切
用来计算一个数值的反正切值的函数为COT()，它接受一个参数，这个参数为待计算余切值的表达式。在Oracle中不支持这个函数，不过根据余切是正切的倒数这一个特性，可以使用TAN()函数来变通实现。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,DB2:
SELECT FName,FWeight, COT(FWeight) FROM T_Person
Oracle:
SELECT FName,FWeight,1/tan(FWeight) FROM T_Person
```
* 求圆周率π值
圆周率π值是一个恒定值，所以在使用它的时候可以使用3.1415926……来引用它，不过手工输入π值非常容易出错，在MYSQL 和MSSQLServer 中提供了PI()函数用来取得圆周率π值，这个函数不需要使用参数，在Oracle和DB2中不支持PI()函数，不过根据-1的反余弦值等于π值的这一特性，我们可以用ACOS(-1)来变通实现。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer:
SELECT FName,FWeight,FWeight *PI() FROM T_Person
Oracle,DB2:
SELECT FName,FWeight,FWeight * acos(-1) FROM T_Person
```
* 弧度制转换为角度制
用来将一个数值从弧度制转换为角度制的函数为DEGREES ()，它接受一个参数，这个参数为待转换的表达式。在Oracle和DB2 中不支持这个函数，不过根据：角度制=弧度制*180/π这一个特性，可以用变通方式来实现。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer:
SELECT FName,FWeight, DEGREES(FWeight) FROM T_Person
Oracle,DB2:
SELECT FName,FWeight,(FWeight*180)/acos(-1) FROM T_Person
```
* 角度制转换为弧度制
用来将一个数值从角度制转换为弧度制的函数为RADIANS ()，它接受一个参数，这个参数为待转换的表达式。在Oracle和DB2 中不支持这个函数，不过根据：弧度制=角度制*π/180这一个特性，可以用变通方式来实现。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer:
SELECT FName,FWeight, RADIANS(FWeight) FROM T_Person
Oracle,DB2:
SELECT FName,FWeight,(FWeight*acos(-1)/180) FROM T_Person
```
* 求符号
SIGN()函数用来返回一个数值的符号，如果数值大于0 则返回1，如果数值等于0 则返回0，如果数值小于0 则返回-1。该函数接受一个参数，这个参数为待求绝对值的表达式。执行下面的SQL语句：
```java  
SELECT FName,FWeight-48.68,SIGN(FWeight-48.68) FROM T_Person
```
* 求符号
SIGN()函数用来返回一个数值的符号，如果数值大于0 则返回1，如果数值等于0 则返回0，如果数值小于0 则返回-1。该函数接受一个参数，这个参数为待求绝对值的表达式。执行下面的SQL语句：
```java  
SELECT FName,FWeight-48.68,SIGN(FWeight-48.68) FROM T_Person
```
* 求整除余数
MOD()函数用来计算两个数整除后的余数。该函数接受两个参数，第一个参数为除数，而第二个参数则是被除数。在MYSQL 和Oracle 中提供了对MOD()函数的直接支持；在MSSQLServer中不支持MOD()，不过MSSQLServer中直接提供了操作符“%”用来计算两个数的整除余数；DB2中不支持求整除余数操作。
执行下面的SQL语句：
```java  
MYSQL,Oracle:
SELECT FName,FWeight,MOD(FWeight , 5) FROM T_Person
MSSQLServer:
SELECT FName,FWeight,FWeight % 5 FROM T_Person
```
* 求自然对数
LOG()函数用来计算一个数的自然对数值。该函数接受一个参数，此参数为待计算自然对数的表达式，在Oracle中这个函数的名称为LN()。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,DB2:
SELECT FName,FWeight, LOG(FWeight) FROM T_Person
Oracle:
SELECT FName,FWeight, LN(FWeight) FROM T_Person
```
* 求自然对数
LOG()函数用来计算一个数的自然对数值。该函数接受一个参数，此参数为待计算自然对数的表达式，在Oracle中这个函数的名称为LN()。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,DB2:
SELECT FName,FWeight, LOG(FWeight) FROM T_Person
Oracle:
SELECT FName,FWeight, LN(FWeight) FROM T_Person
```
* 求以10为底的对数
LOG10()函数用来计算一个数的以10 为底的对数值。该函数接受一个参数，此参数为待计算对数的表达式，在Oracle中不支持这个函数，不过Oracle中有一个可以计算任意数为底的对数的函数LOG(m,n)，它用来计算以m为底n的对数，我们将m设为常量10 就可以了。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,DB2:
SELECT FName,FWeight, LOG10(FWeight) FROM T_Person
Oracle:
SELECT FName,FWeight,LOG(10,FWeight) FROM T_Person
```
* 求幂
POWER(X,Y)函数用来计算X的Y次幂。
执行下面的SQL语句：
```java  
SELECT FName,FWeight, POWER(1.18,FWeight) FROM T_Person
```