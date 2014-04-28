这里的关系是指对象之间的关系，不是数据库之间的关系。
简化问题：
a)怎么写Annotation
b)增删改查CRUD怎么写。
三种关系（一对一，一对多，多对多）如果在程序里就有（单向，多向）七种。
常用的主键关联的单向的外建关联。
一对一的单向外建关联：
a)如果在类里面new另一个对象，则是类的单向引用 。多对多，一对一都是多对多的特殊例子；下面一段代码在annotation：
```java  
@OneToOne
@JoinColumn(name = "wifeId")
public Wife getWife() {
	return wife;
}
```
需要关联的字段get方法上@OneToOne
在xml文件里怎么配置：
<many-to-one name=”student” column = “studentId” unique=”true”></many-to-one>//不能按照字面理解。Uinque=”true”就变成了一对一的单向关联，column关联字段。
注意在建立关联的时候，每个表格的配置都正确，不然会出错，不提示
一对一的双向外建关联：
a)两个关联；
b)在@OneToOne(mappedBy=”wife”)相当于告诉hibernate它跟该对象是一个一对一的关联，告诉它在Wife已经在husband类的一个属性wife上做了映射了。
c)在xml里面参考文档；（hibernate文档）
i.<one-to-onename="stuIdCard"property-ref="student"></one-to-one> property-ref设置由谁设置。
ii.<many-to-one name=”student” column = “studentId” unique =”true”></many-to-one>
一对一的单向主键关联（不重要）
a)@OneToOne	@PrimaryKeyJoinColumn，但是有bug，无法统一
b)Xml: <one-to-one name="student" constrained=”true” "student"  ></one-to-one>，可以设置主键约束：加上：constrained=”true”主键也要改成：<id name="id" column="id"><generator class="foregin"><paramname="property">student</param></generator></id>
双向的主键关联（不重要）
联合主键：
在设置主键关联的类的主键字段需要单独建立一个类，字段就是实体类需要主键关联的主键，wifePK.java。这个类不是实体类。不做任何操作
@IdClass(WifePK.class)//设置联合的类；包含联合的字段
WifePK需要实现serializable和重写equals和hashcode方法。
在每一个联合的属性上加@Id就可以了。（默认就可以了）
如果要更改字段名字，在联合主键里用JoinColumns
```java  
@JoinColumns(
(
@JoinColumn(name = “wifeId”,referencedColumnName=”id”)
//后者参考id字段。
@JoinColumn(name=”wifeName”,referencedColumnName=”name”)
//后者参考name字段。
)
```
只要有双向关联mappedBy必设（不应该在两边都插数据）。
当用powerDesigner连接mysql数据库的时候，必须把jdbc连接的jar包设置到系统的classpath里面。
组键映射
a)当安全是一对一的关系时候，可以放到一个表里面。
b)如果把Wife当Husband 一部分：
i.不需要@Entity,@Id也不需要了。在Husband的wifer的getWife上面加上@Embedded，将对象wife嵌入。
ii.运行时候就合并成了一张表格。
iii.两个类的属性不能冲突，当冲突的时候
1.	 
a)组建重写。
b)改属性名字；
c)在映射的时候，改成其它名字@Column()
iv.可以通过两个对象访问。
v.在xml里设置：用<component>标签把另一个类当成一部分嵌入表中。
多对一与一对多单向(重点)
a)多对一单向关联，
i.项目名称；
ii.多个User可以是一个Group
iii.在多那一方加外键。 Onetomany加在对应的get方法上……
1.	 
iv.多对一的映射关联用在映射类的get方法上@ManyToOne，如果类名与表名不一样，用@Table(name=”tableName”)
v.Xml:<many-to-onename=”student”column=“studentId”></many-to-one>
一对多单向
a)一个Group可以有多个User
b)用Set<User> user = new HashSet<User>();再在get方法上@OneToMany，这样会当成多对多特殊情况来处理（不合适）。在@OneToMany下面需要@JoinColumn(name=”hb”)
c)Group.hbm.xml：<set name=”user”>
<key column=”groupId”></key>//指定关联的字段名；
			<one-to-many class=”bjxst.User”></one-to-many>
多对一与一对多双向
a)一对多双向与多对一双向关联一回事。
b)maooedBy=”group”
c)xml里：<many-to-one name=”group” column=”columnId”></many-to-one>//两个地方 的columnId必须一样。
多对多的单向关联（重点）
a)单向关联。
b)中间表
c)Student与Teacher之间就是多对多的关联。
d)两个类,做为Teahcer知道自己教多个Student，但做为Student不知道自己被多个Teacher教。所以Teacher里需要一个Set<Student>集合，在get方法上@ManyToMany，@JoinTable(name=”t_s”,//修改默认名字。也可以指定JoinColumns=@JoinColumn(name=”teacher_id”),
inverseJoinColumns=@JoinColumn(name=”student_id”)//逆转对方的那个表的id
)
在xml里配：在<set name=”name” table=”t_s></set>table指定中间表名。再<many-to-manyclass=”bjsxt.Student”column=”student_Id”></many-to-many>
多对多的双向关联（相当少用，相对是重点）
a)	两个类,做为Teahcer知道自己教多个Student，但做为Student也知道自己被多个Teacher教。
b)	两边都需要Set集合。上面@ManyToMany(mappedBy=”students”)
当有中间表的时候hibernate不会自己删除，要手动删
在测试时候，sf=new Configuration().configure().buildSessionFactory();不要随便加，会不报错异常。