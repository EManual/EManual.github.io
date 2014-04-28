前边我们讲解了一些常用的函数，这些函数不是在各个主流数据库系统中有着相同的名称和用法，就是在各个主流数据库系统中有等价的实现，这些函数可以基本满足我们大部分需求。不过在各个主流数据库系统还提供了一些自身独有的函数，这些函数在其他的数据库系统中一般都没有等价的实现，使用这些函数以后会给系统的跨数据库移植带来一定的麻烦，不过如果系统对跨数据库移植没有要求的话，那么使用这些函数不仅能提高开发速度，而且能够更好发挥数据库系统的性能，所以了解它们还是非常有必要的，因此这里我们专门安排一节来介绍这些函数。
* MYSQL中的独有函数
* IF()函数
使用CASE函数可以实现非常复杂的逻辑判断，可是若只是实现“如果符合条件则返回A，否则返回B”这样简单的判断逻辑的话，使用CASE函数就过于繁琐，如下：
```java  
CASE WHEN condition THENA ELSE B END
```
MYSQL提供了IF()函数用于简化这种逻辑判断，其语法格式如下：
```java  
IF(expr1,expr2,expr3)
```
如果expr1 为真(expr1 <> 0 以及expr1<>NULL)，那么IF()返回expr2，否则返回expr3。IF()返回一个数字或字符串，这取决于它被使用的语境。
这里使用IF()函数来判断一个人的体重是否太胖，而如果体重大于50则认为太胖，否则认为正常：
```java  
SELECT FName,FWeight,IF(FWeight>50,"太胖","正常") AS ISTooFat FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName FWeight ISTooFat
Tom 56.67 太胖
Jim 36.17 正常
Lily 40.33 正常
Kelly 46.23 正常
Sam 48.68 正常
Kerry 66.67 太胖
Smith 51.28 太胖
BillGates 60.32 太胖
```
* CONV()函数
CONV()函数用于对数字进行进制转换，比如将十进制的26转换为2进制显示，其参数格式如下：
```java  
CONV(N,from_base,to_base)
```
将数字N从from_base进制转换到to_base进制，并以字符串表示形式返回。from_base和to_base的最小值为2，最大值为36。如果to_base是一个负值，N 将被看作为是一个有符号数字。否则，N 被视为是无符号的。
下面的SQL语句用于将十进制的26转换为2进制显示、将十六进制的7D转换为八进制显示：
```java  
SELECT CONV("26",10,2), CONV(26,10,2),CONV("7D",16,8)
```
可以看到数字N既可以为字符串也可以为整数，如果为整数则它被解释为十进制数字。
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
CONV("26",10,2) CONV(26,10,2) CONV("7D",16,8)
11010 11010 175
```
下面的SQL语句用来将每个人的体重四舍五入为整数，然后以二进制的形式显示它们：
```java  
SELECT FWeight,Round(FWeight),CONV(Round(FWeight),10,2) FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FWeight Round(FWeight) CONV(Round(FWeight),10,2)
56.67 57 111001
36.17 36 100100
40.33 40 101000
46.23 46 101110
48.68 49 110001
66.67 67 1000011
51.28 51 110011
60.32 60 111100
```
在日常系统开发过程中，我们最常进行的进制转换是将十进制的整数转换为十六进制显示，如果使用CONV()函数来进行转换的话比较麻烦，为此MYSQL提供了简化调用的函数BIN(N)、OCT(N)、HEX(N)它们分别用于返回N的字符串表示的二进制、八进制值和十六进制形式。下面的SQL语句将每个人的体重四舍五入为整数，然后以二进制、八进制值和十六进制的形式显示它们：
```java  
SELECT FWeight,Round(FWeight),BIN(Round(FWeight)) as b,OCT(Round(FWeight)) as o,HEX(Round(FWeight)) as h FROM T_Person
。在MYSQL中提供了LPAD()、RPAD()函数用于对字符串进行左填充和右填充，其参数格式如下：
```java  
LPAD(str,len,padstr)
RPAD(str,len,padstr)
```
用字符串padstr 对str 进行左（右）边填补直至它的长度达到len个字符长度，然后返回str。如果str的长度长于len"，那么它将被截除到len 个字符。
下面的SQL语句分别将每个人的姓名用星号左填充和右填充到5个字符：
```java  
SELECT FName,LPAD(FName,5,"*"),RPAD(FName,5,"*") FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName LPAD(FName,5,"*") RPAD(FName,5,"*")
Tom **Tom Tom**
Jim **Jim Jim**
Lily *Lily Lily*
Kelly Kelly Kelly
Sam **Sam Sam**
Kerry Kerry Kerry
Smith Smith Smith
BillGates BillG BillG
```
* REPEAT()函数
REPEAT()函数用来得到一个子字符串重复了若干次所组成的字符串，其参数格式如下：
```java  
REPEAT(str,count)
参数str为子字符串，而count为重复次数。
下面的SQL语句用于得到一个由5个星号以及一个由3个“OK”组成的字符串：
```java  
SELECT REPEAT("*",5), REPEAT("OK",3)
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
REPEAT("*",5) REPEAT("OK",3)
```
***** OKOKOK
MYSQL中提供了一个简化REPEAT()的函数SPACE(N)，它用来得到一个有N 空格字符组成的字符串，可以看做是REPEAT(" ",N)的等价形式。
* 字符串颠倒
REVERSE()函数用来将一个字符串的顺序颠倒，下面的SQL语句将所有人员的姓名进行了颠倒：
```java  
SELECT FName, REVERSE(FName) FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName REVERSE(FName)
Tom moT
Jim miJ
Lily yliL
Kelly ylleK
Sam maS
Kerry yrreK
Smith htimS
BillGates setaGlliB
```
* 字符串的集合操作
使用CASE函数可以完成“将1翻译成VIP客户，将2翻译成高级客户，将3翻译成普通客户”这样的任务，但是使用起来比较麻烦，MYSQL中提供了几个字符串集合操作函数，分别是ELT()、FIELD()和FIND_IN_SET()，它们将“VIP客户”、“高级客户”、“普通客户”这样的匹配目标字符串当作集合处理，而将“1、2、3”这样的数字当成待匹配项。
首先来看ELT()函数，它的参数格式如下：
```java  
ELT(N,str1,str2,str3,...)
```
如果N = 1，返回str1，如果N = 2，返回str2，等等。如果N 小于1 或大于参数的数量，返回NULL。下面的SQL演示了ELT()函数的使用：
```java  
SELECT ELT(2, "ej", "Heja", "hej", "foo"),ELT(4, "ej", "Heja", "hej", "foo")
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
ELT(2, "ej", "Heja", "hej", "foo") ELT(4, "ej", "Heja", "hej", "foo")
Heja foo
```
ELT()函数在制作报表的时候非常有用。比如表T_Customer中的FLevel字段是整数类型，它记录了客户的级别，如果为1则是VIP客户，如果为2则是高级客户，如果为3则是普通客户，在制作报表的时候显然不应该把1、2、3这样的数字显示到报表中，而应该显示相应的文字，这里就可以使用ELT()函数进行处理，SQL语句如下：
```java  
SELECT FName,ELT(FLevel, "VIP客户", "高级客户", "普通客户") FROM T_Customer
```
与ELT()函数正好相反，FIELD()函数用于计算字符串在一个字符串集合中的位置，它可以看做是ELT()的反函数。FIELD()函数的参数格式如下：
```java  
FIELD(str,str1,str2,str3,...)
```
返回str在列表str1, str2, str3, ... 中的索引。如果没有发现匹配项，则返回0。下面的SQL演示了FIELD ()函数的使用：
```java  
SELECT FIELD("vip","normal","member","vip") as f1,FIELD("ej", "Hej", "ej", "Heja", "hej", "foo") as f2
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
f1 f2
3 2
```
在数据库中有时存储的是字符串，有的情况下需要将字符串转换成整数，方便后续系统的处理，这时就可以使用CASE()函数，但是如果是在MYSQL中，则使用FIELD()函数更方便。假设客户信息表T_Customer中的FCustomerTypeName保存的是“VIP”、“会员”、“普通客户”这样的文本信息，我们可以使用下面的SQL语句将这些文本信息转换为整数来表示：
```java  
SELECT FName,FIELD(FCustomerTypeName, "VIP", "会员", "普通客户") FROM T_Customer
```
FIELD()函数将中的参数个数是不确定的，但是在使用的时候参数的个数又是确定，是不能在运行时动态改变的。有时待匹配的字符串集合也是不确定的，这时就无法使用FIELD()函数函数了，MYSQL中提供了FIND_IN_SET()函数，它用一个分隔符分割的字符串做为待匹配字符串集合，它的参数格式如下：
```java  
FIND_IN_SET(str,strlist)
```
如果字符串str 在由N 个子串组成的列表strlist 中，返回它在strlist中的索引次序（从1开始计数）。一个字符串列表是由通过字符“,” 分隔的多个子串组成。如果str 在不strlist 中或者如果strlist 是一个空串，返回值为 0。如果任何一个参数为NULL，返回值也是NULL。如果第一个参数包含一个“,”，这个函数将抛出错误信息。下面的SQL演示了FIELD ()函数的使用：
```java  
SELECT FIND_IN_SET("b","a,b,c,d") as f1,FIND_IN_SET("d","a,b,c,d") as f2,FIND_IN_SET("w","a,b,c,d") as f3
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
f1 f2 f3
2 4 0
```
* 计算集合中的最大最小值
MYSQL中的GREATEST()函数和LEAST()函数用于计算一个集合中的最大和最小值，它们的参数个数都是不定的，也就是它们可以对多个值进行比较。使用演示如下：
```java  
SELECT GREATEST(2,7,1,8,30,4,3,99,2,222,12),LEAST(2,7,1,8,30,4,3,99,2,222,12)
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
GREATEST(2,7,1,8,30,4,3,99,2,222,12) LEAST(2,7,1,8,30,4,3,99,2,222,12)
222 1
```
* 辅助功能函数
DATABASE()函数返回当前数据库名；VERSION()函数以一个字符串形式返回MySQL服务器的版本；USER()函数（这个函数还有SYSTEM_USER、SESSION_USER两个别名）返回当前MySQL 用户名。下面的SQL语句演示了这几个函数的使用：
```java  
SELECT DATABASE(),VERSION(),USER()
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
DATABASE() VERSION() USER()
demo 5.0.27-community-nt yzk@192.168.88.2
```
ENCODE(str,pass_str)函数使用pass_str 做为密钥加密str，函数的返回结果是一个与string 一样长的二进制字符。如果希望将它保存到一个列中，需要使用BLOB列类型。
与ENCODE()函数相反，DECODE()函数使用pass_str 作为密钥解密经ENCODE加密后的字符串crypt_str。
下面的SQL语句演示了这两个函数的使用：
```java  
SELECT FName,Length(ENCODE(FName,"aha")),DECODE(ENCODE(FName,"aha"),"aha") FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName Length(ENCODE(FName,"aha")) DECODE(ENCODE(FName,"aha"),"aha")
Tom 3 Tom
Jim 3 Jim
Lily 4 Lily
Kelly 5 Kelly
Sam 3 Sam
Kerry 5 Kerry
Smith 5 Smith
BillGates 9 BillGates
```
除了加解密函数，MYSQL中还提供了对摘要算法的支持，MD5(string)、SHA1(string)两个函数就是分别用来使用MD5算法和SHA1算法来进行字符串的摘要计算的函数，下面的SQL语句用来计算每个人的姓名的MD5摘要和SHA1摘要：
```java  
SELECT FName,MD5(FName),SHA1(FName) FROM T_Person
```
使用UUID算法来生成一个唯一的字符串序列被越来越多的开发者所使用，MYSQL中也提供了对UUID算法的支持，UUID()函数就是用来生成一个UUID字符串的，使用方法如下：
```java  
SELECT UUID(),UUID()
```
执行完毕我们就能在输出结果中看到下面的执行结果（由于UUID算法生成的字符串是全局唯一的，所以你的运行结果会与这里显示的不同）：
```java  
UUID() UUID()
d7495ecd-1863-102b-9b74-218a53021251 d7495ef7-1863-102b-9b74-218a53021251
```
* MSSQLServer中的独有函数
* PATINDEX()函数
MSSQLServer的CHARINDEX()函数用来计算字符串中指定表达式的开始位置，它是一种确定值的匹配，有时我们需要按照一定模式进行匹配，比如“计算字符串中第一个长度为2并且第二个字符为m的子字符串的位置”，这时使用CHARINDEX()函数就不凑效了。
MSSQLServer中PATINDEX()函数就是用来进行这种模式字串匹配的，其参数格式如下：
```java  
PATINDEX ( "%pattern%" , expression )
```
它返回指定表达式中模式"%pattern%"第一次出现的起始位置；如果在全部有效的文本和字符数据类型中没有找到该模式，则返回零。在模式中可以使用通配符。
下面的SQL语句用来查找每个人的姓名中第一个长度为2并且第二个字符为m的子字符串的位置：
```java  
SELECT FName,PATINDEX("%_m%",FName) FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName
Tom 2
Jim 2
Lily 0
Kelly 0
Sam 2
Kerry 0
Smith 1
BillGates 0
```
* REPLICATE ()函数
REPLICATE()函数用来得到一个子字符串重复了若干次所组成的字符串，它和MYSQL中的REPEAT()函数是一样的，其参数格式如下：
```java  
REPLICATE (str,count)
```
参数str为子字符串，而count为重复次数。
下面的SQL语句用于将每个人的姓名重复n次，n等于体重与20的整除结果：
```java  
SELECT FName,FWeight,CAST(FWeight/20 AS INT),REPLICATE(FName, CAST(FWeight/20 AS INT)) FROM T_Person
```
和MYSQL一样，MYSQL中同样提供了一个简化REPLICATE()调用的函数SPACE(N)，它用来得到一个有N空格字符组成的字符串，可以看做是REPLICATE (" ",N)的等价形式。
* 字符串颠倒
REVERSE()函数用来将一个字符串的顺序颠倒，下面的SQL语句将所有人员的姓名进行了颠倒：
```java  
SELECT FName, REVERSE(FName) FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FName
Tom moT
Jim miJ
Lily yliL
Kelly ylleK
Sam maS
Kerry yrreK
Smith htimS
BillGates setaGlliB
```
* ISDATE()函数
ISDATE()函数用来确定输入表达式是否为有效日期。如果输入表达式是有效日期，那么ISDATE 返回 1；否则，返回 0。其参数格式如下：
```java  
ISDATE ( expression )
```
expression参数为要验证其是否为日期的表达式。expression可以是text、ntext表达式和image表达式以外的任意表达式，可以隐式转换为nvarchar。
下面的SQL语句演示了这个函数的使用：
```java  
SELECT ISDATE(NULL) as d1,
ISDATE("13/43/3425") as d2,
ISDATE("1995-10-1a") as d3,
ISDATE(19920808) as d4,
ISDATE("1/23/95") as d5,
ISDATE("1995-10-1") as d6,
ISDATE("19920808") as d7,
ISDATE(" Abc") as d8
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
d1 d2 d3 d4 d5 d6 d7 d8
0 0 0 1 0 1 1 0
```
* ISNUMERIC()函数
ISNUMERIC ()函数用来确定表达式是否为有效的数值类型。如果输入表达式的计算值为有效的整数、浮点数、money 或decimal 类型时，ISNUMERIC 返回 1；否则返回 0。
其参数格式如下：
```java  
ISNUMERIC ( expression )
```
expression参数为要计算的表达式。下面的SQL语句演示了这个函数的使用：
SELECT
ISNUMERIC(NULL) as d1,
ISNUMERIC("13/43/3425") as d2,
ISNUMERIC("30a.8") as d3,
ISNUMERIC(19920808) as d4,
ISNUMERIC("1/23/95") as d5,
ISNUMERIC("3E-3") as d6,
ISNUMERIC("19920808") as d7,
ISNUMERIC("-30.3") as d8
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
d1 d2 d3 d4 d5 d6 d7 d8
0 0 0 1 0 1 1 1
```
* 辅助功能函数
APP_NAME()函数返回当前会话的应用程序名称；CURRENT_USER函数（注意这个函数不能带括号调用）返回当前登陆用户名；HOST_NAME()函数返回工作站名。下面的SQL语句演示了这几个函数的使用：
```java  
SELECT APP_NAME() as appname,CURRENT_USER as cu,HOST_NAME() as hostname
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
appname cu hostname
jTDS dbo YANGZK
```
与MYSQL类似，MSSQLServer 中同样提供了生成全局唯一字符串的函数NEWID()，下面生成三个UUID 字符串：
SELECT NEWID() AS id1,NEWID() AS id2
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
id1 id2
705FAA88-12B9-4C52-9B77-589DD20256C3 A110A5E5-92C7-461F-91F8-BF35129FE7B4
```
* Oracle中的独有函数
* 填充函数
与MYSQL类似，Oracle中也提供了用于进行字符串填充的函数LPAD()、RPAD()，其参数格式如下：
```java  
LPAD(char1,n [,char2])
RPAD(char1, n [,char2])
```
与MYSQL中不同的是，Oracle中LPAD()和RPAD()函数的第三个参数是可以省略的，如果省略第三个参数，则使用单个空格进行填充。
下面的SQL语句分别将每个人的姓名用星号左填充和井号右填充到5个字符：
```java  
SELECT FName,LPAD(FName,5,"*"),RPAD(FName,5,"#") FROM T_Person
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
FNAME LPAD(FNAME,5,*) RPAD(FNAME,5,#)
Tom **Tom Tom##
Jim **Jim Jim##
Lily *Lily Lily#
Kelly Kelly Kelly
Sam **Sam Sam##
Kerry Kerry Kerry
Smith Smith Smith
BillGates BillG BillG
```
* 返回当月最后一天
Oracle中的LAST_DAY()函数可以用来计算指定日期所在月份的最后一天的日期。下面的SQL语句用于计算每个人出生时当月的最后一天的日期：
```java  
SELECT FName,FBirthDay,LAST_DAY(FBirthDay) FROM T_Person WHERE FBirthDay IS NOT NULL
```
* 计算最大最小值
和MYSQL类似，Oracle中提供了用来计算一个集合中的最大和最小值的GREATEST()函数和LEAST()函数。其使用方法和MYSQL一致：
```java  
SELECT GREATEST(2,7,1,8,30,4,5566,99,2,222,12),LEAST(2,7,1,8,30,4,3,99,-2,222,12) FROM DUAL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
GREATEST(2,7,1,8,30,4,5566,99,2,222,12) LEAST(2,7,1,8,30,4,3,99,-2,222,12)
5566 -2
```
* 辅助功能函数
USER函数用来取得当前登录用户名，注意使用这个函数的时候不能使用括号形式的空参数列表，也就是USER()这种使用方式是不对的。正确使用方式如下：
```java  
SELECT USER FROM DUAL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
USER
SYS
```
USERENV()函数用来取得当前登录用户相关的环境信息，这个函数的返回值为字符串类型，需要根据情况将返回值转换为合适的类型。它的参数格式如下：
```java  
USERENV(option)
```
option参数为要取得的环境信息的名称，可取值如下：
```java  
可取值说明
"ISDBA" 如果当前登录用户有DBA的角色则返回TRUE，否则返回FALSE
"LANGUAGE" 返回当前登录用户使用的语言和字符集，返回格式为“语言.字符集”
"TERMINAL" 返回当前登录用户的操作系统标识
"SESSIONID" 返回当前登录用户的会话标识
"ENTRYID" 返回当前登录用户的认证标识
"LANG" 返回当前用户使用的语言，它比"LANGUAGE"的返回值短
"INSTANCE" 返回当前实例的标识
```
下面的SQL语句用来取得当前登录用户的语言信息和权限信息：
```java  
SELECT USERENV("ISDBA") AS ISDBA,USERENV("LANGUAGE") AS LANGUAGE,USERENV("LANG") AS LANG FROM DUAL
```
执行完毕我们就能在输出结果中看到下面的执行结果：
```java  
ISDBA LANGUAGE LANG
TRUE SIMPLIFIED
CHINESE_CHINA.AL32UTF8
ZHS
```