主流的DBMS都提供了启动、提交以及回滚事务的机制，也提供了指定锁粒度、隔离级别的机制，不过这些机制一般是谁DBMS的不同而不同的，请参考具体DBMS的说明文档。比如在MSSQLServer中执行一个READ_UNCOMMITED级别事务的SQL语句如下：
```java  
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITED
BEGIN TRANSACTION
--具体的操作代码
COMMIT
```