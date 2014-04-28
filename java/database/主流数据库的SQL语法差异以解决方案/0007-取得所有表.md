MYSQL中取得当前数据库中所有表定义的SQL语句如下：
```java  
SHOWTABLES
```
MSSQLServer中的系统表sysobjects中记录了当前系统中定义的对象，其中xtype字段等于U的记录为表定义，因此取得当前数据库中所有表定义的SQL语句如下：
```java  
SELECT name FROM sysobjects where xtype="U"
```
Oracle中的系统表all_objects中记录了当前系统中定义的对象，其中Object_Type字段等于TABLE的记录为表定义，因此取得当前数据库中所有表定义的SQL语句如下：
```java  
select Object_Name from all_objects where Object_Type="TABLE"
```
DB2中的系统表all_syscat.tables中记录了当前系统中定义的表和视图，其中TYPE字段等于T的记录为表定义，因此取得当前数据库中所有表定义的SQL语句如下：
```java  
SELECT TABNAME FROM syscat.tables where TYPE="T"
```