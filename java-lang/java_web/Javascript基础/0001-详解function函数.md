关于function
JavaScript的所有代码都是由function组成，function即函数的类型。JavaScript的函数有两种写法：“定义式”和“变量式”。
定义式：
[code=java]
function test1(){

	alert(‘hello,world’);

}
[/code]
变量式：
[code=java]
var test2 = function(){

	alert(‘hello,world’);

}
[/code]
我们可以用typeof(test1)和typeof(test2)查看test1和test2的类型都为function，两种声明方式除了写法不同外，其内部实现和作用都是相同的。其实从第二种写法就可以看出，函数也只是一个命了名的变量而已。
JavaScript中的函数也是一个对象，对象有的属性和功能，函数同样也有。比如对函数也可以动态的增加属性。
[code=java]
function test(){

	alert(‘hello,world’);

}

test.name = ‘zhangsan’;

alert(test.name);//输出“zhangsan”
[/code]
函数的实例化
函数的实例化也有两种方式，常见的方式是直接在函数名后加上“()”即可，也可以使用关键字“new”进行实例化。比如
[code=java]
function test(){

	alert(‘hello,world’);

}

test();//输出“hello,world”

new test();//同样输出“hello,world”
[/code]