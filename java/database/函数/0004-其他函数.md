除了数学函数、字符串函数、日期函数之外，数据库中还有其他一些函数，比如进行类型转换的函数、进行非空逻辑判断的函数等，这些函数也是非常重要的，因此在本节中我们将对这些函数进行介绍。
* 类型转换
在使用SQL语句的时候，我们使用的数据的类型不一定符合函数或者运算符的需要，比如函数需要整数类型的数据而我们使用的则是一个字符串，在一些情况下数据库系统会替我们自动将字符串类型转换为整数类型，这种转换称为隐式转换。但是在有的情况下数据库系统不会进行隐式转换，这时就要使用类型转换函数了，这种转换称为显式转换。使用类型转换函数不仅可以保证类型转换的正确性，而且可以提高数据处理的速度，因此应该使用显式转换，尽量避免使用隐式转换。
在主流数据库系统中都提供了类型转换函数，下面分别进行介绍。
* MYSQL
MYSQL中提供了CAST()函数和CONVERT()函数用于进行类型转换，CAST()是符合ANSI SQL99的函数，CONVERT() 是符合ODBC标准的函数，这两个函数只是参数的调用方式略有差异，其功能几乎相同。这两个函数的参数格式如下：
```java  
CAST(expression AS type)
CONVERT(expression,type)
```
参数expression为待进行类型转换的表达式，而type为转换的目标类型，type可以是下面的任一个：
```java  
可选值缩写说明
BINARY BINARY字符串
CHAR 字符串类型
DATE 日期类型
DATETIME 时间日期类型
SIGNED INTEGER SIGNED 有符号整数
TIME 时间类型
UNSIGNED INTEGER UNSIGNED 无符号整数
```
下面的SQL语句分别演示以有符号整形、无符号整形、日期类型、时间类型为目标类型的数据转换：
```java  
SELECT CAST("-30" AS SIGNED) as sig,CONVERT ("36", UNSIGNED INTEGER) as usig,CAST("2008-08-08" AS DATE) as d,CONVERT ("08:09:10", TIME) as t
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
sig usig d t
-30 36 2008-08-08 08:09:10
```
* MSSQLServer
与MYSQL类似，MSSQLServer中同样提供了名称为CAST()和CONVERT()两个函数用于进行类型转换，CAST()是符合ANSI SQL99的函数，CONVERT() 是符合ODBC标准的函数。
与MYSQL中的CONVERT()函数不同的是MSSQLServer中的CONVERT()函数参数顺序正好与MYSQL中的CONVERT()函数参数顺序相反。这两个函数的参数格式如下：
```java  
CAST ( expression AS data_type)
CONVERT ( data_type, expression)
```
参数expression为待进行类型转换的表达式，而type为转换的目标类型，与MYSQL不同，MYSQLServer中的目标类型几乎可以是数据库系统支持的任何类型。
下面的SQL语句分别演示以整形、数值、日期时间类型为目标类型的数据转换：
```java  
SELECT CAST("-30" AS INTEGER) as i,CONVERT(DECIMAL,"3.1415726") as d,CONVERT(DATETIME,"2008-08-08 08:09:10") as dt
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
i d dt
-30 3 2008-08-08 08:09:10.0
```
下面的SQL语句用于将每个人的身份证后三位转换为整数类型并且进行相关的计算：
```java  
SELECT FIdNumber,RIGHT(FIdNumber,3) as 后三位,CAST(RIGHT(FIdNumber,3) AS INTEGER) as 后三位的整数形式,CAST(RIGHT(FIdNumber,3)
 AS INTEGER)+1 as 后三位加1,CONVERT(INTEGER,RIGHT(FIdNumber,3))/2 as 后三位除以2 FROM T_Person
```
* Oracle
Oracle中也有一个名称为CONVERT()的函数，不过这个函数是用来进行字符集转换的。Oracle中不支持用做数据类型转换的CAST()和CONVERT()两个函数，它提供了针对性更强的类型TO_CHAR()、TO_DATE()、TO_NUMBER()等函数，这些函数可以将数据显式的转换为字符串类型、日期时间类型或者数值类型。Oracle中还提供了HEXTORAW()、RAWTOHEX()、TO_MULTI_BYTE()、TO_SINGLE_BYTE()等函数用于存储格式的转换。
下面我们将对这些函数进行分别介绍。
1) TO_CHAR()
TO_CHAR()函数用来将时间日期类型或者数值类型的数据转换为字符串，其参数格式如下：
```java  
TO_CHAR(expression,format)
```
参数expression为待转换的表达式，参数format为转换后的字符串格式，参数format可以省略，如果省略参数format将会按照数据库系统内置的转换规则进行转换。参数format的可以采用的格式非常丰富，具体可以参考Oracle的联机文档。
下面的SQL语句将出生日期和身高按照不同的格式转换为字符串类型：
```java  
SELECT FBirthDay,TO_CHAR(FBirthDay,"YYYY-MM-DD") as c1,FWeight,TO_CHAR(FWeight,"L99D99MI") as c2,TO_CHAR(FWeight) as c3 FROM T_Person
```
2) TO_DATE()
TO_DATE()函数用来将字符串转换为时间类型，其参数格式如下：
```java  
TO_DATE (expression,format)
```
参数expression为待转换的表达式，参数format为转换格式，参数format可以省略，如果省略参数format将会按照数据库系统内置的转换规则进行转换。
下面的SQL语句用于将字符串形式的数据按照特定的格式解析为日期类型：
```java  
SELECT TO_DATE("2008-08-08 08:09:10", "YYYY-MM-DD HH24:MI:SS") as dt1,TO_DATE("20080808 080910", "YYYYMMDD HH24MISS") as dt2 FROM DUAL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
DT1 DT2
2008-08-08 08:09:10.0 2008-08-08 08:09:10.0
```
3) TO_NUMBER()
TO_NUMBER()函数用来将字符串转换为数值类型，其参数格式如下：
```java  
TO_NUMBER (expression,format)
```
参数expression为待转换的表达式，参数format为转换格式，参数format可以省略，如果省略参数format将会按照数据库系统内置的转换规则进行转换。参数format的可以采用的格式非常丰富，具体可以参考Oracle的联机文档。
下面的SQL语句用于将字符串形式的数据按照特定的格式解析为数值类型：
```java  
SELECT TO_NUMBER("33.33") as n1,TO_NUMBER("100.00", "9G999D99") as n2 FROM DUAL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
N1 N2
33.33 100.55
```
4) HEXTORAW()、RAWTOHEX()
HEXTORAW()用于将十六进制格式的数据转换为原始值，而RAWTOHEX()函数用来将原始值转换为十六进制格式的数据。例子如下：
```java  
SELECT HEXTORAW("7D"),RAWTOHEX ("a"),HEXTORAW(RAWTOHEX("w")) FROM DUAL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
HEXTORAW(7D) RAWTOHEX(A) HEXTORAW(RAWTOHEX(W))
} 61 w
```
5) TO_MULTI_BYTE()、TO_SINGLE_BYTE()
TO_MULTI_BYTE()函数用于将字符串中的半角字符转换为全角字符，而TO_SINGLE_BYTE()函数则用来将字符串中的全角字符转换为半角字符。例子如下：
```java  
SELECT TO_MULTI_BYTE("moring"),TO_SINGLE_BYTE("ｈｅｌｌｏ") FROM DUAL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
TO_MULTI_BYTE(MORING) TO_SINGLE_BYTE(ＨＥＬＬＯ)
ｍｏｒｉｎｇ hello
```
* DB2
DB2中没有提供专门进行显式类型转换的函数，取而代之的是借用了很多高级语言中的强制类型转换的概念，也就是使用目标类型名做为函数名来进行类型转换，比如要将expr转换为日期类型，那么使用DATE(expr)即可。这种实现机制非常方便，降低了学习难度。
下面的SQL语句展示了DB2中类型转换的方式：
```java  
SELECT CHAR(FRegDay),INT("33"),DOUBLE("-3.1415926") FROM T_Person
```
* 空值处理
在数据库中经常需要对空值（NULL）做处理，比如“如果名称为空值则返回别名”，甚至还有更复杂的需求，比如“如果名称为空值则返回别名，如果别名也为空则返回‘佚名’两个字”、“如果名称为与别名相等则返回空值，否则返回名称”。这些需求已经带有流程控制的色彩了，一般来说需要在宿主语言中使用流程控制语句来进行处理，可是如果是在报表程序等大数据量的程序中把这些任务交给宿主语言的话会大大降低运行速度，因此我们必须想办法在SQL这一层进行处理。
为了更好的演示本节中的例子，我们需要对T_Person表中的数据进行一下修改，也就是将Kerry的出生日期修改为空值，将Smith的出生日期和注册日期都修改为空值，执行下面的SQL语句：
```java  
UPDATE T_Person SET FBirthDay=nullWHERE FName="Kerry";
UPDATE T_Person SET FBirthDay=null AND FRegDay=nullWHERE FName="Smith";
```
* COALESCE()函数
主流数据库系统都支持COALESCE()函数，这个函数主要用来进行空值处理，其参数格式如下：
```java  
COALESCE ( expression,value1,value2……,valuen)
```
COALESCE()函数的第一个参数expression为待检测的表达式，而其后的参数个数不定。
COALESCE()函数将会返回包括expression在内的所有参数中的第一个非空表达式。如果expression不为空值则返回expression；否则判断value1是否是空值，如果value1不为空值则返回value1；否则判断value2是否是空值，如果value2不为空值则返回value3；……以此类推，如果所有的表达式都为空值，则返回NULL。
我们将使用COALESCE()函数完成下面的功能，返回人员的“重要日期”：如果出生日期不为空则将出生日期做为“重要日期”，如果出生日期为空则判断注册日期是否为空，如果注册日期不为空则将注册日期做为“重要日期”，如果注册日期也为空则将“2008年8月8
日”做为“重要日期”。实现此功能的SQL语句如下：
```java  
MYSQL、MSSQLServer、DB2:
SELECT FName,FBirthDay,FRegDay,COALESCE(FBirthDay,FRegDay,"2008-08-08") AS ImportDay FROM T_Person
Oracle:
SELECT FBirthDay,FRegDay,COALESCE(FBirthDay,FRegDay,TO_DATE("2008-08-08", "YYYY-MM-DD HH24:MI:SS")) AS ImportDay FROM T_Person
```
这里边最关键的就是Kerry和Smith这两行，可以看到这里的计算逻辑是完全符合我们的需求的。
* NULLIF()函数
主流数据库都支持NULLIF()函数，这个函数的参数格式如下：
```java  
NULLIF ( expression1 , expression2 )
```
如果两个表达式不等价，则NULLIF返回第一个expression1的值。如果两个表达式等价，则NULLIF返回第一个expression1类型的空值。也就是返回类型与第一个expression相同。
下面的SQL演示了NULLIF()函数的用法：
```java  
SELECT FBirthDay,FRegDay,NULLIF(FBirthDay,FRegDay) FROM T_Person
```
* CASE函数
COALESCE()函数只能用来进行空值的逻辑判断处理，如果要实现“如果年龄大于25则返回姓名，否则返回别名”这样的逻辑判断就比较麻烦了。在主流数据库系统中提供了CASE函数的支持，严格意义上来讲CASE函数已经是流程控制语句了，不是简单意义上的函数，不过为了方便，很多人都将CASE称作“流程控制函数”。
CASE函数有两种用法，下面分别介绍。
* 用法一
CASE函数的语法如下：
```java  
CASE expression
WHEN value1 THEN returnvalue1
WHEN value2 THEN returnvalue2
WHEN value3 THEN returnvalue3
……
ELSE defaultreturnvalue
END
```
CASE函数对表达式expression进行测试，如果expression等于value1则返回returnvalue1，如果expression等于value2则返回returnvalue2，expression等于value3则返回returnvalue3，…… 以此类推，如果不符合所有的WHEN条件，则返回默认值defaultreturnvalue。
可见CASE函数和普通编程语言中的SWITCH……CASE语句非常类似。使用CASE函数我们可以实现非常复杂的业务逻辑。下面的SQL用于判断谁是“好孩子”，我们比较偏爱Tom和Lily，所以我们将他们认为是好孩子，而我们比较不喜欢Sam和Kerry，所以认为他们是坏孩子，其他孩子则为普通孩子：
```java  
SELECT FName,(CASE FName
				WHEN "Tom" THEN "GoodBoy"
				WHEN "Lily" THEN "GoodGirl"
				WHEN "Sam" THEN "BadBoy"
				WHEN "Kerry" THEN "BadGirl"
				ELSE "Normal"
				END) as isgood
				FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FNAME ISGOOD
Tom GoodBoy
Jim Normal
Lily GoodGirl
Kelly Normal
Sam BadBoy
Kerry BadGirl
Smith Normal
BillGates Normal
```
CASE函数在制作报表的时候非常有用。比如表T_Customer中的FLevel字段是整数类型，它记录了客户的级别，如果为1则是VIP客户，如果为2则是高级客户，如果为3则是普通客户，在制作报表的时候显然不应该把1、2、3这样的数字显示到报表中，而应该显示相应的文字，这里就可以使用CASE函数进行处理，SQL语句如下：
```java  
SELECT FName,(CASE FLevel
		WHEN 1 THEN "VIP客户"
		WHEN 2 THEN "高级客户"
		WHEN 3 THEN "普通客户"
		ELSE "客户类型错误"
		END) as FLevelName
		FROM T_Customer
```
* 用法二
上边一节中介绍的CASE语句的用法只能用来实现简单的“等于”逻辑的判断，要实现“如果年龄小于18则返回‘未成年人’，否则返回‘成年人’”是无法完成的。值得庆幸的是，CASE函数还提供了第二种用法，其语法如下：
```java  
CASE
WHEN condition1 THEN returnvalue1
WHEN condition 2 THEN returnvalue2
WHEN condition 3 THEN returnvalue3
……
ELSE defaultreturnvalue
END
```
其中的condition1 、condition 2、condition 3……为条件表达式，CASE函数对各个表达式从前向后进行测试，如果条件condition1为真则返回returnvalue1，否则如果条件condition2为真则返回returnvalue2，否则如果条件condition3为真则返回returnvalue3，……以此类推，如果不符合所有的WHEN条件，则返回默认值defaultreturnvalue。
这种用法中没有限制只能对一个表达式进行判断，因此使用起来更加灵活。比如下面的SQL语句用来判断一个人的体重是否正常，如果体重小于40则认为太瘦，而如果体重大于50则认为太胖，介于40和50之间则认为是正常：
```java  
SELECT FName,FWeight,
		(CASE
		WHEN FWeight<40 THEN "thin"
		WHEN FWeight>50 THEN "fat"
		ELSE "ok"
		END) as isnormal
		FROM T_Person
```