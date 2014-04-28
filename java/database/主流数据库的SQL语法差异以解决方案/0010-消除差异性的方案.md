由于不同数据库系统的语法有差异，所以如果想要开发的系统能够运行于多数据库系统下就必须通过一定的方法来消除这些差异性。消除差异性的主要方法有：
为每种数据库编写不同的SQL语句；使用语法交集；使用抽象SQL；使用ORM工具；使用SQL翻译器。
下面对这几种方案进行分析。
* 为每种数据库编写不同的SQL语句
采用这种方案时，对于有语法差异的SQL语句则为为每种数据库编写不同的SQL，然后在运行时根据当前数据库类型来执行不同的SQL语句，比如：
```java  
if(currentdatabase="MYSQL")
{
	executeQuery(" SELECT * FROM T_Person LIMIT 0, 10");
}
else if(currentdatabase="MSSQLServer")
{
	executeQuery(" SELECT TOP 10 * FROM T_Person");
} else if(currentdatabase="Oracle")
{
	executeQuery(" SELECT * FROM T_Person WHERE ROWNUM <= 10");
}
else if(currentdatabase="DB2")
{
	executeQuery(" SELECT * FROM T_Person FETCH FIRST 10 ROWS ONLY");
}
```
采用这种方案的时候能够比较好的解决多数据库的问题，但是要求开发人员对每种数据库的语法差异性非常精通，而且这增加了开发的工作量。
* 使用语法交集
为了避免多数据库的问题，在开发的时候避免使用各个数据库系统语法的差异部分，只使用所有数据库系统都支持的SQL语句。采用这种方案的时候能够比较好的解决多数据库的问题，但是由于不能使用一些高级的语法，因此有的功能无法实现或者必须在宿主语言中通过代码来实现，这不仅限制了系统功能的实现而且降低了运行效率，最重要的问题是：我既然花大价钱买了Oracle数据，为什么不用Oracle提供的一些耗用的特性呢？
* 使用SQL实体对象
该方案下，开发人员访问数据库方法并不是直接执行SQL语句，而是以SQL实体对象的方式描述出对应SQL语句的语意；然后调用SQL实体执行器对SQL实体描述对象处理，生成对应的数据类型的SQL语句，并执行。在SQL执行器中，为每种数据库实现一个适配翻译器，该适配翻译器接收传入的SQL实体对象，并能根据SQL实体对象描述的语意，生成符合对应数据库语法的SQL语句。SQL实体执行器在运行期间才与具体适配翻译器关联，不必事先知道由何种适配翻译器处理SQL实体对象；当需要增加对新数据库的支持时，不必修改任何原有软件，只需要实现一个新的适配翻译器即可。
采用这种方案，开发人员不能直接编写SQL语句，只能编写抽象的语法结构，比如下面的代码来实现取得表T_Person中前10行数据的功能：
```java  
Query query = new Query();
query.SetColumn("*");
query.SetTableName("T_Person");
query.SetLimit(0,10);
ExecuteQuery(query);
```
系统框架会将Query翻译成对应数据库系统支持的SQL语句，比如：
```java  
MYSQL：
SELECT * FROM T_Person LIMIT 0, 10
MSSQLServer：
SELECT TOP 10 * FROM T_Person
Oracle：
SELECT * FROM T_Person WHERE ROWNUM <= 10
DB2：
SELECT * FROM T_Person FETCH FIRST 10 ROWS ONLY
```
采用这种方式能最大程度的利用目标数据库的高级特性，而且开发人员甚至不需要对SQL语法有任何了解，其缺点是编写的代码量增加了，同时如果要实现子查询、连接等复杂功能就编写非常冗长且难懂的代码，使用普通SQL语句三五行就能完成的功能如果采用这种方式可能就需要几十行代码。
* 使用ORM工具
Java中的Hibernate、EJB以及.Net中的Linq、NHibernate等都是非常优秀的ORM工具，这些ORM工具提供了以面向对象的方式使用数据库，开发人员只要操作实体对象就可以，从而避免了直接编写SQL语句，比如下面的代码用来向人员表中加入一条记录：
```java  
Person person = new Person();
person.Name="Tom";
person.Age=22;
ormTool.Save(person);
```
ORM工具会将其翻译成如下的SQL语句：
```java  
INSERT INTO T_Person(FName,FAge)VALUES("Tom",22);
```
下面的代码用来取得人员表中排名前十的人员：
```java  
Query query = new Query();
query.SetLimit(0,10);
query.SetEntityName("Person");
ormTool.ExecuteQuery(query);
```
系统框架会将Query翻译成对应数据库系统支持的SQL语句，比如：
```java  
MYSQL：
SELECT * FROM T_Person LIMIT 0, 10
MSSQLServer：
SELECT TOP 10 * FROM T_Person
Oracle：
SELECT * FROM T_Person WHERE ROWNUM <= 10
DB2：
SELECT * FROM T_Person FETCH FIRST 10 ROWS ONLY
```
ORM工具将对实体对象的操作翻译成SQL语句，这本质上也是一种“使用SQL实体对象”的解决方案。
除了支持以操作实体对象的方式使用ORM工具，很多ORM工具都提供了以一种类似于SQL语句的语法工具，比如EJB中的EJB-SQL以及Hibernate中的HSQL，我们可以统称为ORMSQL，在实现复杂功能的时候使用ORMSQL可以避免编写过长的对象操作代码，ORM工具会将ORMSQL语句翻译成目标数据库平台支持的语法。ORMSQL简化了开发，但是目前的ORMSQL支持的语法主要集中在数据查询上，对DELETE、INSERT、UPDATE以及DDL语句的支持非常有限，而且对常用函数的支持也明显不足。
* 使用SQL翻译器
SQL翻译器是这样一种翻译器，它接受开发人员编写的SQL，然后会将SQL翻译成目标数据库系统支持的SQL语句。比如开发人员编写下面的SQL语句来取得人员表中排名前十的人员：
```java  
SELECT TOP 10 * FROM T_Person
```
SQL翻译器会将其翻译成目标数据库系统支持的SQL语句：
```java  
MYSQL：
SELECT * FROM T_Person LIMIT 0, 10
MSSQLServer：
SELECT TOP 10 * FROM T_Person
Oracle：
SELECT * FROM T_Person WHERE ROWNUM <= 10
DB2：
SELECT * FROM T_Person FETCH FIRST 10 ROWS ONLY
```
SQL翻译器支持完整的SELECT、INSERT、UPDATE、DELETE以及DDL语句语法，而且支持任意复杂度的SQL语句，而且开发人员只要熟悉一种SQL语法就可以了，无需对SQL语句在不同数据库系统中的实现差异性有了解。
目前SQL翻译器产品有三个，分别是SwisSQL、LDBC和CowNewSQL，SwisSQL是一个非开源的商业公司的公开产品，LDBC和CowNewSQL是开源项目。