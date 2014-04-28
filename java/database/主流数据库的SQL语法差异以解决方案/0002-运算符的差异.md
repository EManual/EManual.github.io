在不同的数据库系统中字符串拼接的方式是不同的，下面的主流数据库系统对字符串拼接的支持：
MYSQL：在MYSQL 中进行字符串的拼接要使用CONCAT 函数，CONCAT 函数支持一个或者多个参数，比如CONCAT("Hello",1,"World")；MYSQL 中还提供了另外一个进行字符串拼接的函数CONCAT_WS，CONCAT_WS 可以在待拼接的字符串之间加入指定的分隔符，比如CONCAT_WS ("Hello",1,"World")。
MSSQLServer：MSSQLServer 中可以直接使用加号“+”来拼接字符串，比如"Hello"+"World"。
Oracle：Oracle中使用“||”进行字符串拼接，比如"Hello"||"World"；除了“||”，Oracle还支持使用CONCAT()函数进行字符串拼接，不过与MYSQL 的CONCAT()函数不同，Oracle 的CONCAT()函数只支持两个参数，不支持两个以上字符串的拼接。
DB2：DB2 中使用“||”进行字符串拼接，比如"Hello"||"World"。