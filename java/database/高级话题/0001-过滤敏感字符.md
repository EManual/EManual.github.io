过滤敏感字符的思路非常简单，由于恶意攻击者一般需要在输入框中输入的文本一般含有or、and、select、delete之类的字符串片段，所以在拼接SQL之前检查用户提交的文本中是否含有这些敏感字符串，如果含有则终止操作。示例代码如下：
```java  
string user=txtUser.getText();
string password = txtPassword.getText();
//校验是否含有敏感字符
if(user.contains("or","and","select","delete"))
{
	ShowMessage("可能存在注入漏洞攻击！");
	return;
}
if(password.contains("or","and","select","delete"))
{
	ShowMessage("可能存在注入漏洞攻击！");
	return;
}
rs = ExuecuteQuery("SELECT (FPassword=‘"+password+"’) AS PwdCorrect FROM T_User WHERE FUser=‘"+password+"’");
if(rs.getBool("PwdCorrect ")==true)
{
	ShowMessage("密码正确");
}
else
{
	ShowMessage("密码错误");
}
```
这种方式能够过滤大部分注入漏洞攻击，但是有如下两个缺陷：
1，给正常用户的正常操作造成了麻烦。比如一个正常的用户的密码是“more”、“select”甚至就是“1” or “1”=“1”，它们是没有恶意的，但是在点击【提交】按钮后，系统却弹出了一个报错信息，用户必须将密码修改为一个不包含这些敏感字符串的密码，无疑这造成系统给用户的友好性非常差。国内著名的CMS产品“动易CMS”采用的就是这种方式来防止注入漏洞攻击的，这带来的麻烦就是如果用户要发表一个SQL 语句相关的文章，因为文章中有大量敏感字符，这造成这篇文章几乎无法发表。
2，逻辑难以严谨。尽管过滤了大部分的敏感字符串，但是攻击者是非常聪明的，他们也许能构造一个能够骗过敏感字符串过滤的字符串从而绕过这道“防火墙”。谈到安全性的时候人们都会说：所有用户输入都是不可信的！