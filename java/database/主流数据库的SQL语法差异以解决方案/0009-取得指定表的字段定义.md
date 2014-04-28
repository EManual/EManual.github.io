MYSQL中取得指定表的字段定义（假设表名为mytable）：
```java  
DESCRIBE mytable
```
MYSQLServer中取得指定表的字段定义（假设表名为mytable）：
```java  
SELECT syscols.name as COLUMN_NAME,st.name as DATA_TYPE,syscomm.text as DATA_DEFAULT,syscols.isnullable as NULLABLE
FROM syscolumns syscols
left join systypes st on syscols.xusertype=st.xusertype
left join syscomments syscomm on syscols.cdefault=syscomm.id
where syscols.id=OBJECT_ID(N"mytable")
order by syscols.id,syscols.colorder
```
Oracle中的all_tab_columns表是系统中所有表的字段定义，其中TABLE_NAME字段为表名，因此取得指定表的字段定义（假设表名为mytable）：
```java  
select COLUMN_NAME,DATA_TYPE,DATA_DEFAULT,NULLABLE from all_tab_columns where TABLE_NAME ="MYTABLE"
```
DB2中的syscat.columns表是系统中所有表的字段定义，其中TABNAME字段为表名，因此取得指定表的字段定义（假设表名为mytable）：
```java  
select COLNAME as COLUMN_NAME, TYPENAME as DATA_TYPE,DEFAULT as
DATA_DEFAULT,NULLS as NULLABLE
from syscat.columns where TABNAME="MYTABLE"
```