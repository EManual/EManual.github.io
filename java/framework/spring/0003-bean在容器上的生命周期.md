初始化两种方法：
1，使用init-method属性指定那个方法在bean依赖关系设置好后自动执行。
2，实现initializingBean接口 实现该接口必须实现void afterPropertiesSet（）throws Exception那么就不用设置init-method方法了，注意：最好使用init-method方法，减少代码的侵入性，如果两种方法都实现则先实现接口再init方法（一般写入日志文件）。
销毁两种方法和初始化一样也有两种方法：destroy-method和实现DisposableBean接口。
  