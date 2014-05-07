## Java简介
Java是由Sun Microsystems公司于1995年5月推出的Java程序设计语言和Java平台的总称。（注：Sun公司已于2009年04月20日被Oracle公司收购）
目前，Java 分为三个版本：
Java SE：Java Standard Edition 适用于桌面系统的Java 2平台标准版。
Java ME: Java Micro Edition 适用于小型设备和智能卡的Java 2平台Micro版。
Java EE：Java Enterprise Edition 适用于创建服务器应用程序和服务的Java 2平台企业版。
## JDK与JRE的区别
JDK：Java Development Kit （Java开发必备），简单的说JDK是面向开发人员使用的SDK，它提供了Java的开发环境和运行环境。
JRE：Java Runtime Environment （Java执行环境），JRE是指Java的运行环境，是面向Java程序的使用者，而不是开发者。
注：JDK包含了JRE。
以下是各版本的名称及发布日期：
  
## Java开发环境配置
* 第一步：下载并安装JDK。
现在可以去oracle的官方网站下载，或者google搜索“JDK下载”。
* 第二步：配置环境变量。
#### windows系统：
右击我的电脑-->属性-->高级-->环境变量，在这里设置java的开发环境变量。
JAVA_HOME：配置JDK的目录。
CLASSPATH：指定到哪里去找运行时需要用到的类代码（字节码）。
PATH：指定可执行程序的位置。
#### Linux系统：
在" .bash_profile "下的环境变量设置。
```java  
JAVA_HOME=/opt/jdk1.5.0_06
CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
PATH=$PATH:$JAVA_HOME/bin:.
export JAVA_HOME CLASSPATH PATH (将指定的环境变量声明为全局的)
```