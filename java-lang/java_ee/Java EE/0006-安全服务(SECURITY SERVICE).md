使用Java验证和授权服务（JAAS）可以很好地解决在应用程序变得越来越复杂时，安全需求也会变得很复杂的问题，你可以用它来管理应用程序的安全性。JAAS具有两个特性：验证（Authentication）和授权（authorization），认证是完成用户名和密码的匹配校验；授权是决定用户可以访问哪些资源，授权是基于角色的
1）开发的第一步是定义安全域，安全域的定义有两种方法
第一种方法：通过Jboss 发布文件(jboss.xml )进行定义
[code=java]
<?xml version="1.0" encoding="UTF-8"?>
<jboss>
<!-- Bug in EJB3 of JBoss 4.0.4 GA
<security-domain>java:/jaas/other</security-domain>
-->
<security-domain>other</security-domain>
<unauthenticated-principal>AnonymousUser</unauthenticated-principal>
</jboss>
[/code]
第二种方法：通过@SecurityDomain 注释进行定义 ，注释代码片断如下：
[code=java]
@Stateless
@Remote ({SecurityAccess.class})
@SecurityDomain("other")
public class SecurityAccessBean implements SecurityAccess{}
[/code]
2）定义好安全域之后，因为我们使用Jboss 默认的安全域”other”，所以必须使用users.propertes 和roles.properties 存
储用户名/密码及用户角色。现在开发的第二步就是定义用户名，密码及用户的角色。用户名和密码定义在users.propertes 文件，用户所属角色定义在roles.properties 文件。以下是这两个文件的具体配置：
[code=java]
users.propertes（定义了本例使用的三个用户）
lihuoming=123456
zhangfeng=111111
wuxiao=123
roles.properties（定义了三个用户所具有的角色，其中用户lihuoming 具有三种角色）
lihuoming=AdminUser,DepartmentUser,CooperateUser
zhangfeng=DepartmentUser
wuxiao=CooperateUser
[/code]
以上两个文件必须存放于类路径下。在进行用户验证时，Jboss 容器会自动寻找这两个文件。
3）开发的第三步就是为业务方法定义访问角色。本例定义了三个方法：AdminUserMethod(),
DepartmentUserMethod(),AnonymousUserMethod()，第一个方法只允许具有AdminUser角色的用户访问，第二个方法只允许具有DepartmentUser 角色的用户访问，第三个方法允许所有角色的用户访问。下面是Session Bean 代码。
[code=java]
@Stateless
@Remote (SecurityAccess.class)
public class SecurityAccessBean implements SecurityAccess{
	@RolesAllowed ({"AdminUser"})
	public String AdminUserMethod() {
		return "具有管理员角色的用户才可以访问AdminUserMethod()方法";
	}
	@RolesAllowed({"DepartmentUser"})
	public String DepartmentUserMethod() {
		return "具有事业部门角色的用户才可以访问DepartmentUserMethod()方法";
	}
	@PermitAll 
	public String AnonymousUserMethod() {
		return "任何角色的用户都可以访问AnonymousUserMethod()方法, 注：用户必须存在
	users.properties文件哦";
	}
}
[/code]
自定义安全域
把用户名/密码及角色存放在users.propertes 和roles.properties 文件，不便于日后的管理。大多数情况下我们都希望把用户名/密码及角色存放在数据库中。为此，我们需要自定义安全域。他采用数据库存储用户名及角色（两个表）下面的例子定义了一个名为foshanshop的安全域，安全域在[jboss 安装目录]/server/default/conf/login-config.xml 文件中定义，本例配置片断如下：
[code=java]
<!-- ....................... foshanshop login configuration ....................-->
<application-policy name="foshanshop">
<authentication>
<login-module code="org.jboss.security.auth.spi.DatabaseServerLoginModule"
flag="required">
<module-option name="dsJndiName">java:/DefaultMySqlDS</module-option>
<module-option name="principalsQuery">
select password from sys_user where name=?
</module-option>
<module-option name="rolesQuery">
select rolename,‘Roles’ from sys_userrole where username=?
</module-option>
<module-option name = "unauthenticatedIdentity">AnonymousUser</module-option>
</login-module>
</authentication>
</application-policy>
[/code]
上面使用了Jboss 数据库登录模块(org.jboss.security.auth.spi.DatabaseServerLoginModule)，他的dsJndiName 属性（数据源JNDI 名）使用DefaultMySqlDS 数据源(本教程自定义的数据源，关于数据源的配置请参考前面章节：JBoss数据源的配置), principalsQuery 属性定义Jboss 通过给定的用户名如何获得密码, rolesQuery 属性定义Jboss通过给定的用户名如何获得角色列表，注意:SQL 中的‘Roles’常量字段不能去掉。unauthenticatedIdentity 属性允许匿名用户(不提供用户名及密码)访问。“foshanshop”安全域使用的sys_user 和sys_userrole 表是自定义表，实际项目开发中你可以使用别的表名。sys_user 表必须含有用户名及密码两个字段，字段类型为字符型，至于字符长度视你的应用而定。sys_userrole 表必须含有用户名及角色两个字段，字段类型为字符型，字符长度也视你的应用而定。