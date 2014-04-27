ClassLoader一个经常出现又让很多人望而却步的词，本文将试图以最浅显易懂的方式来讲解 ClassLoader，希望能对不了解该机制的朋友起到一点点作用。 
要深入了解ClassLoader，首先就要知道ClassLoader是用来干什么的，顾名思义，它就是用来加载Class文件到JVM，以供程序使用的。我们知道，java程序可以动态加载类定义，而这个动态加载的机制就是通过ClassLoader来实现的，所以可想而知ClassLoader的重要性如何。 
看到这里，可能有的朋友会想到一个问题，那就是既然ClassLoader是用来加载类到JVM中的，那么ClassLoader又是如何被加载呢？难道它不是java的类？ 
没有错，在这里确实有一个ClassLoader不是用java语言所编写的，而是JVM实现的一部分，这个ClassLoader就是bootstrap classloader（启动类加载器），这个ClassLoader在JVM运行的时候加载java核心的API以满足java程序最基本的需求，其中就包括用户定义的ClassLoader，这里所谓的用户定义是指通过java程序实现的ClassLoader，一个是ExtClassLoader，这个ClassLoader是用来加载java的扩展API的，也就是/lib/ext中的类，一个是AppClassLoader，这个ClassLoader是用来加载用户机器上CLASSPATH设置目录中的Class的，通常在没有指定ClassLoader的情况下，程序员自定义的类就由该ClassLoader进行加载。 
当运行一个程序的时候，JVM启动，运行bootstrap classloader，该ClassLoader加载java核心API（ExtClassLoader和AppClassLoader也在此时被加载），然后调用ExtClassLoader加载扩展API，最后AppClassLoader加载CLASSPATH目录下定义的Class，这就是一个程序最基本的加载流程。 
上面大概讲解了一下ClassLoader的作用以及一个最基本的加载流程，接下来将讲解一下ClassLoader加载的方式，这里就不得不讲一下ClassLoader在这里使用了双亲委托模式进行类加载。 
每一个自定义ClassLoader都必须继承ClassLoader这个抽象类，而每个ClassLoader都会有一个parent ClassLoader，我们可以看一下ClassLoader这个抽象类中有一个getParent()方法，这个方法用来返回当前ClassLoader的parent，注意，这个parent不是指的被继承的类，而是在实例化该ClassLoader时指定的一个ClassLoader，如果这个parent为null，那么就默认该ClassLoader的parent是bootstrap classloader，这个parent有什么用呢？ 
我们可以考虑这样一种情况，假设我们自定义了一个ClientDefClassLoader，我们使用这个自定义的ClassLoader加载java.lang.String，那么这里String是否会被这个ClassLoader加载呢？事实上java.lang.String这个类并不是被这个ClientDefClassLoader加载，而是由bootstrap classloader进行加载，为什么会这样？实际上这就是双亲委托模式的原因，因为在任何一个自定义ClassLoader加载一个类之前，它都会先委托它的父亲ClassLoader进行加载，只有当父亲ClassLoader无法加载成功后，才会由自己加载，在上面这个例子里，因为java.lang.String是属于java核心API的一个类，所以当使用ClientDefClassLoader加载它的时候，该ClassLoader会先委托它的父亲ClassLoader进行加载，上面讲过，当ClassLoader的parent为null时，ClassLoader的parent就是bootstrap classloader，所以在ClassLoader的最顶层就是bootstrap classloader，因此最终委托到bootstrap classloader的时候，bootstrap classloader就会返回String的Class。 
我们来看一下ClassLoader中的一段源代码：
```java   
protected synchronized Class loadClass(String name, boolean resolve) throws ClassNotFoundException
{
	// 首先检查该name指定的class是否有被加载
	Class c = findLoadedClass(name);
	if (c == null) {
		try {
			if (parent != null) {
				//如果parent不为null，则调用parent的loadClass进行加载
				c = parent.loadClass(name, false);
			} else {
				//parent为null，则调用BootstrapClassLoader进行加载
				c = findBootstrapClass0(name);
			}
		} catch (ClassNotFoundException e) {
			//如果仍然无法加载成功，则调用自身的findClass进行加载			
			c = findClass(name);
		}
	}
	if (resolve) {
		resolveClass(c);
	}
	return c;
}
```
从上面一段代码中，我们可以看出一个类加载的大概过程与之前我所举的例子是一样的，而我们要实现一个自定义类的时候，只需要实现findClass方法即可。 
为什么要使用这种双亲委托模式呢？ 
第一个原因就是因为这样可以避免重复加载，当父亲已经加载了该类的时候，就没有必要子ClassLoader再加载一次。 
第二个原因就是考虑到安全因素，我们试想一下，如果不使用这种委托模式，那我们就可以随时使用自定义的String来动态替代java核心api中定义类型，这样会存在非常大的安全隐患，而双亲委托的方式，就可以避免这种情况，因为String已经在启动时被加载，所以用户自定义类是无法加载一个自定义的ClassLoader。 
上面对ClassLoader的加载机制进行了大概的介绍，接下来不得不在此讲解一下另外一个和ClassLoader相关的类，那就是Class类，每个被ClassLoader加载的class文件，最终都会以Class类的实例被程序员引用，我们可以把Class类当作是普通类的一个模板，JVM根据这个模板生成对应的实例，最终被程序员所使用。 
我们看到在Class类中有个静态方法forName，这个方法和ClassLoader中的loadClass方法的目的一样，都是用来加载class的，但是两者在作用上却有所区别。 
```java  
Class<?> loadClass(String name) 
Class<?> loadClass(String name, boolean resolve) 
```
我们看到上面两个方法声明，第二个方法的第二个参数是用于设置加载类的时候是否连接该类，true就连接，否则就不连接。 
说到连接，不得不在此做一下解释，在JVM加载类的时候，需要经过三个步骤，装载、连接、初始化。装载就是找到相应的class文件，读入JVM，初始化就不用说了，最主要就说说连接。 
连接分三步，第一步是验证class是否符合规格，第二步是准备，就是为类变量分配内存同时设置默认初始值，第三步就是解释，而这步就是可选的，根据上面loadClass方法的第二个参数来判定是否需要解释，所谓的解释根据《深入JVM》这本书的定义就是根据类中的符号引用查找相应的实体，再把符号引用替换成一个直接引用的过程。有点深奥吧，呵呵，在此就不多做解释了，想具体了解就翻翻《深入JVM吧》，呵呵，再这样一步步解释下去，那就不知道什么时候才能解释得完了。 
我们再来看看那个两个参数的loadClass方法，在JAVA API 文档中，该方法的定义是protected，那也就是说该方法是被保护的，而用户真正应该使用的方法是一个参数的那个，一个参数的loadclass方法实际上就是调用了两个参数的方法，而第二个参数默认为false，因此在这里可以看出通过loadClass加载类实际上就是加载的时候并不对该类进行解释，因此也不会初始化该类。而Class类的forName方法则是相反，使用forName加载的时候就会将Class进行解释和初始化，forName也有另外一个版本的方法，可以设置是否初始化以及设置ClassLoader，在此就不多讲了。 
不知道上面对这两种加载方式的解释是否足够清楚，就在此举个例子吧，例如JDBC DRIVER的加载，我们在加载JDBC驱动的时候都是使用的forName而非是ClassLoader的loadClass方法呢？我们知道，JDBC驱动是通过DriverManager，必须在DriverManager中注册，如果驱动类没有被初始化，则不能注册到DriverManager中，因此必须使用forName而不能用loadClass。 
通过ClassLoader我们可以自定义类加载器，定制自己所需要的加载方式，例如从网络加载，从其他格式的文件加载等等都可以，其实ClassLoader还有很多地方没有讲到，例如ClassLoader内部的一些实现等等，希望能够给一些有需要的朋友一点帮助吧。