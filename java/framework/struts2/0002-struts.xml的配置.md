struts.xml的配置：
```java  
<struts>
 <!-- include节点是struts2中组件化的方式 可以将每个功能模块独立到一个xml配置文件中 然后用include节点引用 -->
    <include file="struts-default.xml"></include>
    <!-- package提供了将多个Action组织为一个模块的方式
        package的名字必须是唯一的 package可以扩展 当一个package扩展自
        另一个package时该package会在本身配置的基础上加入扩展的package
        的配置 父package必须在子package前配置 
        name：package名称 extends:继承的父package名称
        abstract:设置package的属性为抽象的 抽象的package不能定义action 值true:false
        namespace:定义package命名空间 该命名空间影响到url的地址，例如此命名空间为/test那么访问是的地址为                     
http://localhost:8080/struts2/test/XX.action    -->
    <package name="com.kay.struts2" extends="struts-default" namespace="/test">
        <interceptors>
            <!-- 定义拦截器 name:拦截器名称  class:拦截器类路径  -->
            <interceptor name="timer" class="com.kay.timer"></interceptor>
            <interceptor name="logger" class="com.kay.logger"></interceptor>
            <!-- 定义拦截器栈 -->
            <interceptor-stack name="mystack ">
                <interceptor-ref name="timer"></interceptor-ref>
                <interceptor-ref name="logger"></interceptor-ref>
            </interceptor-stack>
        </interceptors>
        <!-- 定义默认的拦截器 每个Action都会自动引用 如果Action中引用了其它的拦截器 默认的拦截器将无效 -->
        <default-interceptor-ref name="mystack"></default-interceptor-ref>
        <!-- 全局results配置 -->
        <global-results><result name="input">/error.jsp</result> </global-results>
        <!-- Action配置 一个Action可以被多次映射(只要action配置中的name不同)
             name：action名称 class: 对应的类的路径  method: 调用Action中的方法名 -->
        <action name="hello " class="com.kay.struts2.Action.LoginAction">
            <!-- 引用拦截器 name:拦截器名称或拦截器栈名称  -->
            <interceptor-ref name="timer"></interceptor-ref>
            <!-- 节点配置 name : result名称 和Action中返回的值相同
                type : result类型 不写则选用superpackage的type struts-default.xml中的默认为dispatcher
             -->
         <result name="success" type="dispatcher">/talk.jsp</result>
<result name="error" type="dispatcher">/error.jsp</result>
<result name="input" type="dispatcher">/login.jsp</result>
<!-- 配置Action返回cancel时重定向到Welcome的Action-->
         <result name="cancel" type="redirect-action">Welcome</result>
          <!—异常处理  result表示出现异常时返回的name为success的结果处理—》
<exception-mapping exception=”java.lang.Exception” result=”success”/>
         <!-- 参数设置 name：对应Action中的get/set方法 -->
         <param name="url">http://www.sina.com</param>
        </action>
    </package>
          <!—引用国际化文件的base名-->
<constant name=”struts2.custom.i18n.resources”value=”messageResource”
</struts>
```