1，浏览器发送请求，例如请求 /mypage.action     /report/myreport.pdf等。
2，核心控制器FilterDispatcher根据请求决定调用合适的Action。
3，WebWork的拦截器链自动对请求应用通用功能，例如 workflow，validation或文件下载和上传。
4，回调Action的execute方法(其实可以是任意方法)，该方法execute方法先获得用户的请求参数，然后执行某种数据操作，调用业务逻辑组组件来处理用户请求。
5，Action的execute方法处理结果信息将被输出发哦浏览器中，可以是html页面，pdf还有jsp，Velocity，FreeMarker等技术模板。