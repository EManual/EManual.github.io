Hibernate中的实体对象可以分为三种状态：Transient（临时）、Persistent（持久）、Detached（游离）
* Transient 
用new创建出对象，这些对象还没有与数据库发生任何的关系，不对应于数据库中的任一笔数据；Persistent 对象通过调用delete()方法，也成为Transient 的，例：
```java  
Session session = sessions.openSession();
Transaction tx = session.beginTransaction();
int userID = 1234;
User user = (User) session.get(User.class, new Long(userID));
session.delete(user);
tx.commit();
session.close();
```
这种方法实际执行了delete sql语句。把Detached （脱管）对象转换成Transient（瞬时）的，例：
```java  
Session session = sessions.openSession();
Transaction tx = session.beginTransaction();
session.delete(user);
tx.commit();
session.close();
```
将对象同Session 关联然后删除。
* Persistent
当对象与数据库中的数据有对应关系，并且与Session实例有关联，并且Session实例尚未关闭，则它是在Persistent状态。例：Transient状态的对象使用Session的save()方法保存到数据库后，对象成为persistent状态，例：
```java  
DomesticCat fritz = new DomesticCat();
fritz.setColor(Color.GINGER);
fritz.setSex(‘M’);
fritz.setName("Fritz");
Long generatedId = (Long) session.save(fritz);
//使用Hibernate从数据库得到数据并封装为对象（例如使用get()、load()），则该对象为Persistent状态
//get()
User user = (User) session.get(User.class, new Long(userID)); 
//load()
User user = (User) session.load(User.class, new Long(userID));
//get()和load()的区别在于：当要查找的对象数据不存在时，load()方法就是直接抛出异常，而get()方法则返回null值 
//Detached 状态对象重新和session关联后（通过update或lock方法）变成Persistent 状态，例：
/update() 
//user是session1关闭后留下的脱管对象
user.setPassword("secret");
Session session2 = sessionFactory.openSession();
Transaction tx = session2.beginTransaction();
session2.update(user);
user.setUsername("jonny");
tx.commit();
session2.close();
//这种方式，关联前后做修改都不打紧，关联前后做的修改都会被更新到数据库；
//比如关联前你修改了password，关联后修改了username，事务提交时执行的update语句会把password、username都更新
//lock()
Session session2 = sessions.openSession();
Transaction tx = session2 .beginTransaction();
session2 .lock(user, LockMode.NONE);
user.setPassword("secret");
user.setLoginName("jonny");
tx.commit();
session2 .close();
```
这种方式，关联前后是否做修改很重要，关联前做的修改不会被更新到数据库，比如关联前你修改了password，关联后修改了loginname，事务提交时执行的update语句只会把loginname更新到数据库，所以，确信分离对象没有做过更改才能使用lock()。如果将Session实例关闭，则Persistent状态的对象会成为Detached状态。
* Detached
Detached状态的对象，与数据库中的具体数据对应，但脱离Session实例的管理，例如：在使用load()、get()方法查询到数据并封装为对象之后，将Session实例关闭，则对象由Persistent状态变为Detached状态。
Detached状态的对象之任何属性变动，不会对数据库中的数据造成任何的影响。这种状态的对象相当于cache数据，因为他不和session关联，谁都可以用，任何session都可以用它，用完后再放到cache中。从上面看，hibernate对数据的处理确实比较聪明，一个session用完一个持久对象后，可以不删除这个对象，而是把它和session分离开，放到应用的cache中，其他session可以到cache中找需要的数据，但这导致了新的问题，和新的解决办法。
三种状态的转换图如下：
  