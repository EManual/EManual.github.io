悲观锁：在查询时加
1. Student s=sess.get(Student.class,id,LockMode.UPGRADE);
五种模式：
LockMode.NONE：查询时先在cache（缓存）里找,如果没有，再到db里加载无锁机制。
LockMode.READ：不管cache有没有，都查询数据库，Hibernate在读取记录的时候会自动获取。
LockMode.UPGRADE：不管cache有没有，都查询数据库，并且 对查询的数据加锁,如果锁被其他事务拿走，当前事务会一直等到加上锁为止。 利用数据库的for update子句加锁。
LockMode.UPGRADE_NOWAIT：不管cache有没有,都查询数据库,并且对查询的数据加锁，如果锁被其他事务拿走，当前事务会立刻返回。	，hiberna Oracle的特定实现，利用Oracle的for update nowait子句实现加锁              
LockMode.WRITE：在做insert,update，delete会自动使用模式.内部使用
2. 以下情况用悲观锁：查询数据时，就给数据加锁
1)数据资源被多个事务并发访问的机会很大
2)修改数据所需时间非常短  
乐观锁，大多是基于数据版本 （Version）记录机制实现：
1，在javabean中加上version的属性提供set和get方法。
2，在数据库表上加上vershion列。
3，在映射文件的<id></id>后加上<version>
<version name=”version” column=”version”/>
实现原理：读取出数据时，将此版本号一同读出，之后更新时，对此版本号加一。此时，将提交数据的版本数据与数据库表对应记录的当前版本信息进行比对，如果提交的数据 版本号大于数据库表当前版本号，则予以更新，否则认为是过期数据。