除了数值类型的数据，字符串类型的数据也是数据库系统中经常用到的数据类型，比如用户的密码、电子邮箱地址、证件号码等都是以字符串类型保存在数据库中的。我们经常需要对这些数据进行一些处理，比如截取身份证号码前5位、将电子邮箱地址全部改为大写、去掉用户名中的空格，SQL 中提供了丰富的字符串函数用于完成这些功能，本节将对这些字符串函数进行详细讲解。
* 计算字符串长度
LENGTH()函数用来计算一个字符串的长度。该函数接受一个参数，此参数为待计算的字符串表达式，在MYSQLServer 中这个函数名称为LEN()。
执行下面的SQL语句：
```java  
MYSQL,Oracle,DB2:
SELECT FName, LENGTH(FName) FROM T_Person
MSSQLServer:
SELECT FName, LEN(FName) FROM T_Person
```
* 字符串转换为小写
LOWER()函数用来将一个字符串转换为小写。该函数接受一个参数，此参数为待转换的字符串表达式，在DB2 中这个函数名称为LCASE()。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,Oracle:
SELECT FName, LOWER(FName) FROM T_Person
DB2:
SELECT FName, LCASE(FName) FROM T_Person
```
* 字符串转换为大写
与LOWER()函数正好相反，UPPER()函数用来将一个字符串转换为大写。该函数接受一个参数，此参数为待转换的字符串表达式，在DB2中这个函数名称为UCASE ()。执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,Oracle:
SELECT FName, UPPER(FName) FROM T_Person
DB2:
SELECT FName, UCASE(FName) FROM T_Person
```
* 截去字符串左侧空格
LTRIM()函数用来将一个字符串左侧的空格去掉。该函数接受一个参数，此参数为待处理的字符串表达式。执行下面的SQL语句：
```java  
SELECT FName,LTRIM(FName),LTRIM("abc") FROM T_Person
```
* 截去字符串右侧空格
RTRIM ()函数用来将一个字符串左侧的空格去掉。该函数接受一个参数，此参数为待处理的字符串表达式。执行下面的SQL语句：
```java  
SELECT FName,RTRIM(FName),RTRIM("abc") FROM T_Person
```
* 截去字符串两侧的空格
TRIM ()函数用来将一个字符串两侧的空格去掉。该函数接受一个参数，此参数为待处理的字符串表达式。此函数只在MYSQL 和Oracle 中提供支持，不过在MSSQLServer和DB2中可以使用LTRIM()函数和RTRIM()函数复合来进行变通实现，也就是用LTRIM(RTRIM(string))来模拟实现TRIM (string)。执行下面的SQL语句：
```java  
MYSQL,Oracle:
SELECT FName,TRIM(FName),TRIM(" abc ") FROM T_Person
MSSQLServer,DB2:
SELECT FName,LTRIM(RTRIM(FName)),LTRIM(RTRIM(" abc ")) FROM T_Person
```
* 取子字符串
字符串是由多个字符组成的串，比如“HelloWorld”在内存是如下存储的：
```java  
1 2 3 4 5 6 7 8 9 10
H e l l o W o r l d
```
表格第一行的数字表示组成字符串的每个字符的位置，第二行则为各个位置上的字符。由这些字符中连续的多个字符还可以组成新的字符串，新的字符串则被称为“子字符串”。比如从第3 个字符到第5 个字符组成的“llo”就是一个子字符串，我们也可以称“llo”为从第3 个字符开始长度为3 的子字符串。
SQL中提供了用来计算子字符串的函数SUBSTRING()，其参数格式如下：
```java  
SUBSTRING(string,start_position,length)
```
其中参数string为主字符串，start_position为子字符串在主字符串中的起始位置，length为子字符串的最大长度。在MYSQL和MSSQLServer 中支持这个函数，而在Oracle和DB2中这个函数的名称则为SUBSTR()，仅仅是名称不同而已，在用法没有什么不同。
执行下面的SQL语句：
```java  
MYSQL、MSSQLServer:
SELECT SUBSTRING("abcdef111",2,3)
Oracle:
SELECT SUBSTR("abcdef111",2,3) FROM DUAL
DB2:
SELECT SUBSTR("abcdef111",2,3) FROM SYSIBM.SYSDUMMY1
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
SUBSTRING("abcdef111",2,3)
bcd
```
再执行下面的SQL语句：
```java  
MYSQL,MSSQLServer:
SELECT FName, SUBSTRING(FName,2,3) FROM T_Person
Oracle,DB2:
SELECT FName, SUBSTR(FName,2,3) FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName SUBSTRING(FName,2,3)
Tom om
Jim im
Lily ily
Kelly ell
Sam am
Kerry err
Smith mit
BillGates ill
```
* 计算子字符串的位置
SQL中提供了计算子字符串在主字符串中位置的函数，这个函数可以检测制定的子字符串是否存在于主字符串中，如果存在则还可以返回所在的位置。这个函数在MYSQL 和Oracle中名称为INSTR，其参数格式如下：
```java  
INSTR(string,substring)
```
其中参数string为主字符串，参数substring为待查询的子字符串。如果string中存在substring子字符串，则返回子字符串第一个字符在主字符串中出现的位置；如果string中不存在substring子字符串，则返回0。
在MSSQLServer中这个函数名为CHARINDEX，其参数格式以及返回值规则与MYSQL以及Oracle一致。
在DB2中这个函数名为LOCATE，其返回值规则与前述几种数据库系统一致，不过参数格式与它们正好相反，其参数格式如下：
```java  
LOCATE(substring,string)
```
其中参数substring为待查询的子字符串,参数string为主字符串，也就是两个参数的位置是与其它集中数据库系统相反的，这一点在使用的时候需要特别注意的。执行下面的SQL语句：
```java  
MYSQL,Oracle:
SELECT FName, INSTR(FName,"m") , INSTR(FName,"ly") FROM T_Person
MSSQLServer:
SELECT FName,CHARINDEX(FName,"m"), CHARINDEX(FName,"ly") FROM T_Person
DB2:
SELECT FName, LOCATE("m",FName) , LOCATE("ly",FName) FROM T_Person
```
* 从左侧开始取子字符串
使用SUBSTRING()函数我们可以从任意位置开始取任意长度的子字符串，不过有的时候我们只需要从左侧开始取子字符串，这样指定主字符串和要取的长度就可以了，不过如果使用SUBSTRING()函数的话仍然需要指定三个参数，其中第二个参数为常量1。MYSQL、MSSQLServer、DB2 中提供了LEFT()函数用于从左侧开始取任意长度的子字符串，其参数格式如下：
```java  
LEFT (string,length)
```
其中参数string为主字符串，length为子字符串的最大长度。
Oracle 中不支持LEFT()函数，只能使用SUBSTR()函数进行变通实现，也就是SUBSTR(string, 1, length)。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,DB2:
SELECT FName, LEFT(FName,3) , LEFT(FName,2) FROM T_Person
Oracle:
SELECT FName,SUBSTR(FName, 1,3),SUBSTR(FName, 1,2) FROM T_Person
```
* 从右侧开始取子字符串
使用SUBSTRING()函数我们可以从任意位置开始取任意长度的子字符串，不过有的时候我们只需要从右侧开始取子字符串，这样指定主字符串和要取的长度就可以了，不过如果使用SUBSTRING()函数的话仍然需要指定三个参数。MYSQL、MSSQLServer、DB2 中提供了RIGHT ()函数用于从左侧开始取任意长度的子字符串，其参数格式如下：
```java  
RIGHT (string,length)
```
其中参数string为主字符串，length为子字符串的最大长度。
Oracle中不支持RIGHT ()函数，只能使用SUBSTR()函数进行变通实现，其中起始位置用如下表达式计算出来：startposition= LENGTH(string)- length+1也就是SUBSTR(string, LENGTH(string)- length+1, length)等价于RIGHT (string,length)。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer,DB2:
SELECT FName, RIGHT(FName,3) , RIGHT(FName,2) FROM T_Person
Oracle:
SELECT FName,SUBSTR(FName, LENGTH(FName)-3 +1, 3),SUBSTR(FName, LENGTH(FName)-2 +1, 2) FROM T_Person
```
* 字符串替换
REPLACE()函数可以用来将字符串的指定的子字符串替换为其它的字符串，比如将“Hello World”中的“rl”替换为“ok”后得到“Hello Wookd”，而把“Just so so”中的“s”替换为“z”后得到“Juzt zo zo”。REPLACE()函数的参数格式如下：
```java  
REPLACE(string,string_tobe_replace,string_to_replace)
```
其中参数string为要进行替换操作的主字符串，参数string_tobe_replace为要被替换的字符串，而string_to_replace将替换string_tobe_replace中所有出现的地方。
执行下面的SQL语句：
```java  
select FName,REPLACE(FName,"i","e"),FIDNumber,REPLACE(FIDNumber,"2345","abcd") FROM T_Person
```
SQL中没有提供删除字符串中匹配的子字符串的方法，因为使用REPLACE()函数就可以达到删除子字符串的方法，那就是将第三个参数设定为空字符串，用空字符串来替换匹配的子字符串也就达到了删除指定子字符串的效果了。比如下面的SQL语句用来将FName中的m以及FIDNumber 中的123 删除：
```java  
SELECT FName, REPLACE(FName,"m","") ,FIDNumber,REPLACE(FIDNumber,"123","") FROM T_Person
```
LTRIM()、RTRIM()和TRIM()都只能删除两侧的字符串，无法删除字符串中间的空格，而使用REPLACE()函数也可以完成这个功能，也就是用空字符串替换中所有的空格。执行下面的SQL语句：
```java  
MYSQL、MSSQLServer：
SELECT REPLACE(" abc 123 wpf"," ",""),REPLACE(" ccw enet wcf f"," ","")
Oracle：
SELECT REPLACE(" abc 123 wpf"," ",""),REPLACE(" ccw enet wcf f"," ","") FROM DUAL
DB2：
SELECT REPLACE(" abc 123 wpf"," ",""),REPLACE(" ccw enet wcf f"," ","") FROM SYSIBM.SYSDUMMY1
```
* 得到字符的ASCII码
ASCII()函数用来得到一个字符的ASCII码，它有且只有一个参数，这个参数为待求ASCII码的字符，如果参数为一个字符串则函数返回第一个字符的ASCII码，比如执行下面的SQL语句：
```java  
MYSQL,MSSQLServer:
SELECT ASCII("a") , ASCII("abc")
Oracle:
SELECT ASCII("a") , ASCII("abc") FROM DUAL
DB2:
SELECT ASCII("a") , ASCII("abc") FROM SYSIBM.SYSDUMMY1
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
ASCII("a") ASCII("abc")
97 97
```
下面的SQL语句用来计算每个员工姓名的第一个字符的ASCII码：
```java  
MYSQL,MSSQLServer,DB2：
SELECT FName, LEFT(FName,1),ASCII(LEFT(FName,1)),ASCII(FName) FROM T_Person
Oracle：
SELECT FName,SUBSTR(FName,1,1),ASCII(SUBSTR(FName, 1,1)),ASCII(FName) FROM T_Person
```
* 得到一个ASCII码数字对应的字符
与 ASCII()函数正好相反，SQL 还提供了用来得到一个字符的ASCII 码的函数。在MYSQL、MSSQLServer 和DB2 中，这个函数的名字是CHAR()，而在Oracle中这个函数的名字则为CHR()。
执行下面的SQL语句：
```java  
MYSQL,MSSQLServer:
SELECT CHAR(56),CHAR(90),"a",CHAR(ASCII("a"))
Oracle:
SELECT CHR(56),CHR(90),"a",CHR(ASCII("a")) FROM DUAL
DB2:
SELECT CHR(56),CHR(90),"a",CHR( ASCII("a")) FROM SYSIBM.SYSDUMMY1
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
CHAR(56) CHAR(90) a CHAR( ASCII("a") )
8 Z a a
```
下面的SQL语句将FWeight转换为整数，然后得到它对应的字符：
```java  
MYSQL、MSSQLServer：
SELECT FWeight, CEILING(FWeight),CHAR( CEILING(FWeight) ) FROM T_Person
Oracle：
SELECT FWeight, CEIL(FWeight),CHAR( CEIL(FWeight) ) FROM T_Person
DB2：
SELECT FWeight, CEILING(FWeight),CHAR(int(CEILING(FWeight))) FROM T_Person
```
由于DB2 的类型检查机制非常严格，所以在DB2 中需要用int()函数将CEILING()函数的返回值显示的转换为整数类型。
* 发音匹配度
到目前为止所有关于字符串的匹配都是针对其拼写形式的，比如下面的SQL 语句用于检索年龄为“jack”的员工：
```java  
SELECT * from T_Person WHERE FName="jack"
```
有的时候我们并不知道一个人姓名的准确拼写，只知道它的发音，这是在公安、医疗、教育等系统中是经常需要的功能，比如“检索名字发音为和[jeck]类似的人员”，这时我们就要进行发音的匹配度测试了。
SQL中提供了SOUNDEX()函数用于计算一个字符串的发音特征值，这个特征值为一个四个字符的字符串，特征值的第一个字符总是初始字符串中的第一个字符，而其后则是一个三位数字的数值。下面的SQL语句用于查询几个名字的发音特征值：
```java  
MYSQL,MSSQLServer:
SELECT SOUNDEX("jack"),SOUNDEX("jeck"),SOUNDEX("joke"),SOUNDEX("juke"),SOUNDEX("look"),SOUNDEX("jobe")
Oracle:
SELECT SOUNDEX("jack"),SOUNDEX("jeck"),SOUNDEX("joke"),SOUNDEX("juke"),SOUNDEX("look"),SOUNDEX("jobe") FROM DUAL
DB2:
SELECT SOUNDEX("jack"),SOUNDEX("jeck"),SOUNDEX("joke"),SOUNDEX("juke"),SOUNDEX("look"),SOUNDEX("jobe") FROM SYSIBM.SYSDUMMY1
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
SOUNDEX("jack")
SOUNDEX("jeck")
SOUNDEX("joke")
SOUNDEX("juke")
SOUNDEX("look")
SOUNDEX("jobe")
J000 J000 J000 J000 L200 J100
```
可以看到jack、jeck、joke、juke 几个字符串的发音非常相似，而look、jobe 的发音则和它们差距比较大。
下面的SQL语句用于查询公司所有员工姓名的发音特征值：
```java  
SELECT FName, SOUNDEX(FName) FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName SOUNDEX(FName)
Tom T500
Jim J500
Lily L000
Kelly K400
Sam S500
Kerry K600
Smith S530
BillGates B4232
```
发音特征值的含义非常复杂，如果要根据两个发音特征值来分析两个字符串的发音相似度的话非常麻烦。不过在MSSQLServer和DB2中提供了DIFFERENCE()用来简化两个字符串的发音相似度比较，它可以计算两个字符串的发音特征值，并且比较它们，然后返回一个0至4之间的一个值来反映两个字符串的发音相似度，这个值越大则表示两个字符串发音思想度越大。
下面的SQL语句用来计算每个人的姓名发音与“Merry”的相似度：
```java  
SELECT DIFFERENCE(FName,"Merry") FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName
Tom Merry 2
Jim Merry 1
Lily Merry 2
Kelly Merry 3
Sam Merry 2
Kerry Merry 3
Smith Merry 0
BillGates Merry 1
```
可以看到Kerry、Kelly与Merry的发音相似度非常高。
在WHERE语句中使用DIFFERENCE()更有意义，比如下面的SQL语句用于查询和“Tim”发音相似度大于3 的员工：
```java  
SELECT * FROM T_Person WHERE DIFFERENCE(FName,"Tim")>=3
```