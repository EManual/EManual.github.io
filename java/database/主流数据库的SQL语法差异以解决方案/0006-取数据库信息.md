MYSQL中可以通过函数来取得数据库的信息，包括当前数据库名、版本、当前登录用户等信息：DATABASE()函数返回当前数据库名；VERSION()函数以一个字符串形式返回MySQL 服务器的版本；USER()函数（这个函数还有SYSTEM_USER、SESSION_USER两个别名）返回当前MySQL 用户名。
MSSQLServer中也可以通过函数来取得数据库的信息：APP_NAME()函数返回当前会话的应用程序名称；CURRENT_USER函数（注意这个函数不能带括号调用）返回当前登陆用户名；HOST_NAME()函数返回工作站名。
不过，在MSSQLServer中如果要查询当前数据库名，则必须到系统表sysprocesses中查询，SQL语句如下：
```java  
select dbname = case when dbid = 0 then null when dbid <> 0 then db_name(dbid) end
from master..sysprocesses where spid=@@SPID
```
系统表“master..sysprocesses”中存储了当前数据库系统中的进程信息，而“@@SPID”则表示当前进程号。
Oracle中使用USER函数用来取得当前登录用户名，注意使用这个函数的时候不能使用括号形式的空参数列表，也就是USER()这种使用方式是不对的。正确使用方式如下：
```java  
SELECT USER FROM DUAL
```
Oracle中使用USERENV()函数用来取得当前登录用户相关的环境信息，USERENV()函数有一个参数，参数的可选值如下：ISDBA、LANGUAGE、TERMINAL、SESSIONID、ENTRYID、LANG和INSTANCE。
DB2中可以通过CURRENT_USER来取得当前登陆用户名，而CURRENT_SERVER用来取得当前服务名，比如：
```java  
SELECT CURRENT_USER,CURRENT_SERVER FROM sysibm.sysdummy1
```
DB2中取得当前数据库的版本的SQL语句如下：
```java  
SELECT * FROM sysibm.sysversions
```