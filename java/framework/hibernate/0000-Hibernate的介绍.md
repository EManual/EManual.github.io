1.什么是Hibernate？
首先，Hibernate是数据持久层的一个轻量级框架。数据持久层的框架有很多比如：iBATIS,myBatis,Nhibernate,Siena等等。
并且Hibernate是一个开源的orm（object relations model）框架，提供了查询获取数据的方法，用面向对象的思想来操作数据库，节省了我们开发处理数据的时间。
2.那使用Hibernate的优点呢？
1)使用简介的hql语句（Hibernate query language）。可以不使用传统的insert，update等sql语句。比如insert一个对象，原来的做法是：insert into 表名称 alue（值1，值2，值3，……），而现在的做法是：save（对象）。
2)使用or映射。对象到关系数据库之间的映射。是从对象的角度操作数据库，再次体现了面向对象思想。原来的实体抽取方法：首先有了表，然后表映射实体对象。而现在Hibernate做法是：直接由对象映射到表。
3)没有侵入性，移植性比较好。什么是没有侵入性？就是Hibernate采用了pojo对象。所谓的pojo对象就是没有继承Hibernate类或实现Hibernate接口。这样的话，此类就是一个普通的java类，所以移植性比较好。  
4)支持透明持久化。透明是针对上层而言的。三层架构的理念是上层对下层的依赖，只是依赖接口不依赖具体实现。而Hibernate中的透明是指对业务逻辑层提供了一个接口session，而其他的都封装隐藏。持久化是指把内存中的数据存放到磁盘上的文件中。
3.当然一个事物，不可能十全十美，即使如此优秀的Hibernate也有自己的弱点。比如：若是大量数据批量操作。则不适合使用Hibernate。并且一个持久化对象不能映射到多张表中。
4.Hibernate中核心5个接口
1)Configuration接口：负责配置及启动Hibernate，用来创建sessionFactory
2)SessionFactory接口：一个SessionFactory对应一个数据源存储，也就是一个数据库对应一个SessionFactory。SessionFactory用来创建Session对象。并且SessionFactory是线程安全的，可以由多个线程访问SessionFactory共享。
3)Session接口：这个接口是Hibernate中常用的接口，主要用于对数据的操作（增删改查）。而这个Session对象不是线程安全的。不能共享。
4)Query接口：用于数据库的查询对象。
5)Transaction接口：Hibernate事务接口。它封装了底层的事务操作，比如JTA（java transcation architecture）所有的数据操作，比如增删改查都写在事务中。