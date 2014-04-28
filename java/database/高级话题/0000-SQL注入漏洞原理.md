系统中安全性是非常重要的，为了保证安全性很多解决方案被应用到系统中，比如架设防火墙防止数据库服务器直接暴露给外部访问者、使用数据库的授权机制防止未授权的用户访问数据库，这些解决方案可以很大程度上避免了系统受攻击，但是如果开发人员不注意SQL的安全性造成了SQL注入漏洞，那么所有的这些解决方案都形同虚设了，因为通过SQL注入漏洞，恶意访问者可以堂而皇之的对数据库进行任意操作，因为恶意访问者破坏数据库时所使用的一切操作都看起来是合法。我们来看一下什么是SQL注入漏洞。
到目前为止，本书演示的SQL语句都是静态的SQL语句，比如下面的SQL用于校验用户名为“admin”的用户的密码是否是“123456”，如果密码正确则PwdCorrect的值为true，否则为false：
```java  
SELECT (FPassword="123456") AS PwdCorrect FROM T_User WHERE FUser="admin"
在实际开发过程中一般是开发人员提供一个界面，允许用户输入用户名和密码，然后程序读取用户输入用户名和密码来构造SQL 语句来校验用户名和密码是否正确。实现的代码如下：
string user=txtUser.getText();
string password = txtPassword.getText();
rs = ExuecuteQuery("SELECT (FPassword=""+password+"") AS PwdCorrect FROM T_User WHERE FUser=""+password+""");
if(rs.getBool("PwdCorrect ")==true)
{
	ShowMessage("密码正确");
}
else
{
	ShowMessage("密码错误");
}
```
这里采用拼接字符串的方式根据用户录入的用户名和密码来构建SQL语句，如果用户名为“guest”，密码为“123456”，那么拼接出来的SQL语句如下：
```java  
SELECT (FPassword="123456") AS PwdCorrect FROM T_User WHERE FUser="guest"
```
这看起来是没有任何问题的，但是试想如果恶意攻击者在用户名输入框中随意输入一个“abc”，而在密码数据框中输入“1" or "1"="1”，那么拼接出来的SQL语句如下：
```java  
SELECT (FPassword="1" or "1"="1") AS PwdCorrect FROM T_User WHERE FUser="abc"
```
由于“"1"="1"”这个表达式永远返回true，而true与任何布尔值的or 运算的结果都是true，那么无论正确密码是什么“FPassword="1" or "1"="1"”的计算值永远是true，这样恶意攻击者就可以使用任何帐户登录系统了。十分惊讶吧！这样的漏洞就被称作“SQL注入漏洞（SQL
Injection）”。
对付SQL注入漏洞有两种方式：过滤敏感字符和使用参数化SQL。