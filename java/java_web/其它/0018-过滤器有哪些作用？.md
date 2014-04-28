可以验证客户是否来自可信的网络，可以对客户提交的数据进行重新编码，可以从系统里获得配置的信息，可以过滤掉客户的某些不应该
出现的词汇，可以验证用户是否登录，可以验证客户的浏览器是否支持当前的应用，可以记录系统的日志等等。
过滤器的用法？
首先要实现（implements）Filter接口，同时覆盖Filter接口的三个方法：
```java  
init(FilterConfig config) //用于获得FilterConfig对象；
doFilter(ServletRequest request, ServletResponse response, FilterChain chain) //进行过滤处理一些业务；
```