Servlet是位于Web服务器内部的服务器端的Java应用程序，与传统的从命令行启动的Java应用程序不同，Servlet由Web服务器进行加载，该Web服务器必须包含支持Servlet的Java虚拟机。
* 它们不是独立的应用程序，没有main()方法。
* 它们不是由用户或程序员调用，而是由另外一个应用程序(容器)调用。
* 它们都有一个生存周期，包含init()和destroy()方法。
要使用Servlet，必须导入包servlet-api.jar。这里使用的服务器是Tomcat，其主目录结构为：
|- bin：用于存放可执行命令( catalina.sh )。
|- conf：用于存放tomcat需要的配置文件。
|- lib：存放tomcat在运行时要用到的类文件(jsp-api.jar、servlet-api.jar、...)。
|- webapps：最重要的一个目录，其下放置各种Servlet文件、网页文件(JSP HTML ...)、
			配置文件以及资源文件.此目录的结构：
	|- 应用目录(比如是一个学生管理网站，就在webapps文件夹下建一个StudentManage目录)。
		|- WEB-INF目录。
			|- classes目录，放置所有的Servlet文件或其他类文件。
			|- lib目录，放置本应用所要用到的类文件(jar包)。
			|- web.xml 配置文件。
		|- 资源文件(比如图片), 网页文件(JSP HTML ...)。
						
|- logs：日志文件 .
|- work：内部临时文件.
|- temp：临时文件.
安装tomcat环境变量的配置，和配jdk差不多servlet-api.jar；jsp-api.jar。