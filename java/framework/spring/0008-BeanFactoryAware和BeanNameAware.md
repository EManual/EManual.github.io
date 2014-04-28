实现 BeanFactoryAware 接口的 bean 可以直接访问 Spring 容器，被容器创建以后，它会拥有一个指向 Spring 容器的引用。 
BeanFactoryAware 接口只有一个方法void setBeanFactory(BeanFactorybeanFactory)。配置和一般的bean一样。
如果某个 bean 需要访问配置文件中本身的 id 属性，则可以使用 BeanNameAware 接口，该接口提供了回调本身的能力。实现
该接口的 bean，能访问到本身的 id 属性。该接口提供一个方法:void setBeanName(String name)。