摘要：作者Veera Sundar在清理代码工作时发现一些常见的违规编码，因此，Veera Sundar把针对常见的一些违规编码总结成一份列表，以便帮助Java爱好者提高代码的质量和可维护性。
最近，我给Java项目做了一次代码清理工作。经过清理后，我发现一组常见的违规代码（指不规范的代码并不表示代码错误）重复出现在代码中。因此，我把常见的这些违规编码总结成一份列表，分享给大家以帮助Java爱好者提高代码的质量和可维护性。
这份列表没有依据任何规则或顺序，所有的这些都是通过代码质量工具包括CheckStyle，FindBugs和PMD检查出。一起来看下：
一、Eclipse编译器提供源代码格式输入
Eclipse提供自动源码格式选项，并且组织输入（删除未使用的代码）。你可以使用下面的这些快捷键进行操作。
Ctrl + Shift + F——源代码格式
Ctrl + Shift + O——组织输入并删除未使用的代码
代替手动调用这两个函数，只需根据Eclipse自动格式和自动组织选项，可以随时保存文件。
操作步骤，在Eclipse中进入Window -> Preferences -> Java -> Editor -> Save Actions，然后以选定的方式保存，最后检查Format source code + Organize imports。
二、避免多个返回（退出点）
依照你的方法，确保只有一个退出点。不要在同一个地方或多个地方使用返回。比如，下面的代码，NOT RECOMMENDED（不建议），这是因为有多个退出点（返回语句）。
```java  
private boolean isEligible(int age){  
  if(age > 18){  
    return true;  
  }else{  
    return false;  
  }  
} 
```
下面的代码有所提升，这是更高版本的。
```java  
private boolean isEligible(int age){  
  boolean result;  
  if(age > 18){  
    result = true;  
  }else{  
    result = false;  
  }  
  return result;  
} 
```
三、简化if-else
我写了几个实用的方法作为参考，检查语句条件并且基于该条件返回值。比如，考虑到isEligible方法，正如你之前所看到的：
```java  
private boolean isEligible(int age){  
  boolean result;  
  if(age > 18){  
    result = true;  
  }else{  
    result = false;  
  }  
  return result;  
} 
```
整个方法以一个单一的return语句重新编写：
```java  
private boolean isEligible(int age){  
 
	return age > 18;  
 
} 
```
四、不要给Boolean, Integer或者String创建新的实例
避免给Boolean，Integer，String创建新的实例。比如，使用new Boolean(true)，Boolean，valueOf(true)。修改后的语句与之前的效果基本相同，除了在性能上有所提升。
五、使用大括号模块语句
永远别忘了使用大括号模块语句比如if、for、while。这样做的好处是当你在修改模块级语句时减少了模糊代码并且避免引进bug的机会。
不建议：
```java  
if(age > 18)  
  result = true;  
else  
  result = false; 
```
建议：
```java  
if(age > 18){  
  result = true;  
}else{  
  result = false;  
} 
```
六、以final类型标记方法参数，任何时候都适用
请记住，以final类型标记方法参数，任何时候都适用。这样做的好处在于当你不小心修改参数值时，编译器会给你警告，同时它还能以更好的方式优化编译器代码字节。
建议：
```java  
private boolean isEligible(final int age){ ... } 
```
七、在UPPERCASE中命名public static final字段
在UPPERCASE中命名public static final字段（通常也被称之为常量）。这个可以让你轻松区分常量字段和局部变量之间的不同。
不建议：
```java  
public static final String testAccountNo = "12345678";
``` 
建议：
```java  
public static final String TEST_ACCOUNT_NO = "12345678";
```
八、组合成单一的if语句
在尽可能多的情况下，把多个if语句组合成单一的if语句，比如下面的代码：
```java  
if(age > 18){  
  if( voted == false){  
    // eligible to vote.  
  }  
} 
```
合并成单一的if语句：
```java  
if(age > 18 && !voted){  
  // eligible to vote  
} 
```
九、Switch应该有default
始终给Switch语句添加default。
十、使用常量来避免重复定义相同的字符串值
如果你在多个地方必须使用字符串，那么使用常量来避免重复定义拥有相同值的字符串。
比如，看下面的代码：
```java  
private void someMethod(){  
  logger.log("My Application" + e);  
  ....  
  ....  
  logger.log("My Application" + f);  
} 
string literal“我的应用”可以作为常量并且能在代码中使用。

public static final String MY_APP = "My Application";  
 
private void someMethod(){  
  logger.log(MY_APP + e);  
  ....  
  ....  
  logger.log(MY_APP + f);  
} 
```