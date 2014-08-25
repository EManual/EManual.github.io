在保存的前面必须先建立好关联。但是默认情况下还是不会自动保存，如果保存会出错。
Cascade all所有关联的所有持久化都是级联到另一个对象。保存这个对象的时候关联的对象自动保存。
Cascade只是给我们编程的关联关系方便。
双向关联必须要设置双向关系，双向mappedBy在读取的时候，如果读取的是一的一方，那么不会自动拿出多的一方。拿出group的时候不会拿出user，当拿出user的时候会自动拿出group关联读取的时候是用另一个参数fetch设置的，与cascade分工不同。Cascade管CURD而fetch管load和get和其它的读取。很少用fetch，其值为eager的时候，多发一条select语句，理解。只要一边设置eager就行了，不然你取了我，我又取了你，两次。
在xml里面set参数加上inverst=”true”，关联读取。
先取user，接下来才会把user和group取出来。
Fetch：
a)双向不要两边设置eager（）
b)具体应用，一般用lazy不用eager。
删除的时候s.setGroup(null)打破关联关系，就可以了。删User就不会把关联的Group和与group关联的User全部删除；如果不删除记录，寻么记录就成为垃圾记录。直接用hql也可以(delete from User u where u.id=1).executeUpdate();
当删除Group但没有删User的时候那么User里group_id必须允许为空。
数据查询语言：
a)HQL
b)EJBOL(JPOL)（是HQL的一个子集）