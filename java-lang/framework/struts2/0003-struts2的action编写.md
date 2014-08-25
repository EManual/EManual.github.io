例 HelloWorld.jsp 
[code=java]
<% @ page contentType = "text/html; charset=UTF-8 " %> 
<% @ taglib prefix = "s" uri = "/struts-tags " %> 
<html> 
<head> 
    <title> Hello World! </title> 
</head> 
<body> 
    <h2><s:property value ="message"/></h2> 
</body> 
</html> 
[/code]
例 classes/tutorial/HelloWorld.java
[code=java]
import com.opensymphony.xwork2.ActionSupport;
public class HelloWorld extends ActionSupport  {
	private String message ;
	public String getMessage()  {
		return message;
	} 
	public void tring setMessage(String message)  {
		this.message=message;
	}
	@Override 
	public String execute ()  {
		message = " Hello World, Now is " + DateFormat.getInstance().format( new Date());
		return success;
	} 
} 
[/code]
例 classes/struts.xml中HelloWorld Action的配置
[code=java]
<package name ="ActionDemo" extends ="struts-default"> 
    <action name ="HelloWorld" class ="tutorial.HelloWorld"> 
        <result> /HelloWorld.jsp </result> 
    </action> 
</package> 
[/code]