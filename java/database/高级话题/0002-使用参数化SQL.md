Java、C#等语言提供了参数化SQL机制，使用参数化SQL开发人员为在运行时才能确定的参数值设置占位符，在执行的时候再指定这些占位符所代表的值。示例代码如下：
```java  
string user=txtUser.getText();
string password = txtPassword.getText();
query = CreateQuery("SELECT (FPassword=:password) AS PwdCorrect FROM T_User WHERE FUser=:user");
query.SetParameter(":password ",password);
query.SetParameter(":user", user);
if(rs.getBool("PwdCorrect ")==true)
{
	ShowMessage("密码正确");
}
else
{
	ShowMessage("密码错误");
}
```
在上面的例子中，为运行时才能确定的用户名和密码设置了占位符，然后在运行时再设定占位符的值，在执行时Java、C#会直接将参数化SQL以及对应的参数值传递给DBMS，在DBMS中会将参数值当成一个普通的值来处理而不是将它们拼接到参数化SQL中，因此从根本上避免了SQL注入漏洞攻击。建议开发人员使用参数化SQL来代替字符串拼接，不过如果开发的时候采用的ASP、PHP等语言，那么由于这些语言没有提供参数化SQL机制，因此只能采用其它方式来避免了SQL注入漏洞攻击。