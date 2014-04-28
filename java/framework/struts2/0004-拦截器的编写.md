编写权限控制器：
```java  
public class AuthorityInterceptor extends AbstractIntercepto r {   
    private static final long serialVersionUID = 1358600090729208361L;   
    //拦截Action处理的拦截方法   
    public String intercept(ActionInvocation invocation) throws Exception {   
        ActionContext ctx=invocation.getInvocationContext();   // 取得请求相关的ActionContext实例
        Map session=ctx.getSession();   
        String user=(String)session.get("user"); //取出名为user的session属性     
        //如果没有登陆，或者登陆所有的用户名不是aumy，都返回重新登陆   
        if(user!=null && user.equals("aumy")){   
            return invocation.invoke();    
        }   
        //没有登陆，将服务器提示设置成一个HttpServletRequest属性   
        ctx.put("tip","您还没有登录，请登陆系统");   
        return Action.LOGIN;           
    }   
}
```
Struts2.xml的配置文件：
```java  
<struts>    
    <include file="struts-default.xml"/>     
       
    <!--受权限控制的Action请求配置-->   
    <package name="authority" extends="struts-default">   
        <interceptors>   
            <!--定义一个名为authority的拦截器-->   
            <interceptor  class="com.aumy.struts.example.intercepter.AuthorityInterceptor"  name="authority"/>
            <!--定义一个包含权限检查的拦截器栈-->   
            <interceptor-stack name="mydefault">  
                <interceptor-ref name="defaultStack"/>   <!--配置内建默认拦截器--> 
                <interceptor-ref name="authority"/>  <!--配置自定义的拦截器-->   
            </interceptor-stack>   
        </interceptors>   
           
        <default-interceptor-ref name="mydefault" />    
        <!--定义全局Result-->   
        <global-results>   
            <result name="login">/login.jsp</result>   
        </global-results>   
           
        <action name="show" class="com.aumy.struts.example.LoginAction"  
            method="show">   
            <result name="success">/show.jsp</result>   
        </action>   
        <action name="add" class="com.aumy.struts.example.LoginAction"  method="add">
            <result name="success">/add.jsp</result>   
        </action>   
    </package>   
</struts>  
```
还要一种方法拦截器，可以对某个action的方法进行拦截 编码类似action拦截器：
```java  
public class MyInterceptor3 extends MethodFilterInterceptor {   
    @Override  
    protected String doIntercept(ActionInvocation invocation) throws Exception {   
        System.out.println("use MethodFilterInterceptor");   
        String result = invocation.invoke();   
        return result;   
    }  
}
```
只是在配置的时候和其他interceptor有些区别：
```java  
<interceptor name="myInterceptor3" class="com.langhua.interceptor.MyInterceptor3">  
                <param name="excludeMethods">execute，login</param>  <!-- execute，login两个方法不需要拦截 
               <!—addmessage 方法需要拦截 可以指名多个方法，只需要用逗号隔开
 <param name="includeMethods">addmessage</param>     
</interceptor> 
```