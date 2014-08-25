a.page是代表与一个页面相关的对象和属性。一个页面由一个编译好的 Java servlet类（可以带有任何的include指令，但是没有include动作）表示。这既包括 servlet 又包括被编译成servlet的JSP页面
b.request是代表与 Web 客户机发出的一个请求相关的对象和属性。一个请求可能跨越多个页面，涉及多个 Web 组件（由于 forward 指令和 include 动作的关系）
c.session是代表与用于某个Web客户机的一个用户体验相关对象和属性。一个Web会话可以也经常会跨越多个客户机请求
d.application是代表与整个Web应用程序相关的对象和属性。这实质上是跨越整个Web应用程序，包括多个页面、请求和会话的一个全局作用域。