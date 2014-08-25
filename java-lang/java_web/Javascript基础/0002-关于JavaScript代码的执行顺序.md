关于JavaScript的执行顺序
JavaScript执行引擎并非一行一行地分析和执行程序，而是一段一段地分析执行的。而且在分析执行同一段代码中，定义式的函数语句会被提取出来优先执行。函数定义执行完后，才会按顺序执行其他代码。
先看看两个例子：
例子1：
[code=java]
var hello = function(){

	alert("hello,zhangsan");

}

hello();//第一次调用，输出“hello,zhangsan”

var hello = function(){

	alert("hello,lisi");

}

hello();//第二次调用，输出“hello,lisi”
[/code]
例子2：
[code=java]
function hello(){

	alert(‘hello,zhangsan’);

}

hello();//第一次调用，猜猜输出什么内容？

function hello(){

alert(‘hello,lisi’);

}

hello();//第二次调用，猜猜输出什么内容？
[/code]
在例子2中，两次调用都会输出相同的内容“hello,lisi”。同样是声明两个相同名称的函数，为什么调用的结果却不一样呢？
这就是JavaScript执行顺序导致的。JavaScript执行引擎并非一行一行地分析和执行程序，而是一段一段地分析执行的。而且在分析执行同一段代码中，定义式的函数语句会被提取出来优先执行。函数定义执行完后，才会按顺序执行其他代码。也就是说，在第一次调用hello函数之前，第一个函数语句定义的代码已经被第二个函数定义语句的代码覆盖了，这就是为什么在例子2中第一次调用hallo时，也会输出后面定义的函数内容的原因了。
下面我们再给一个例子证明JavaScript执行引擎是一段一段地分析执行的。我们将实例2中的代码分成两段。将他们放到同一个html中，但是用不同的
这时，两次调用的输出才是按照各自的顺序进行的。