关于prototype
prototype即原型。JavaScript中所有的函数都有一个prototype属性。这个prototype属性本身又是一个object类型的对象。因此我们可以对这个prototype对象添加任意属性和方法。prototype的特点是：在prototype上定义的属性和方法，可以通过其构造出来的实例对象直接访问和调用。也就是说，prototype提供了一组同类对象共享属性和方法的机制。下面给出两个例子进行对比说明prototype的作用。
例子1：
[code=java]
function Person(name){

	this.name = name;

}

Person.say = function(){

	alert("hello,"+this.name);

}

Person.say();//输出“hello,undefined”

var zhangsan = new Person("zhangsan");

var lisi = new Person("lisi");

zhangsan.say();//此处会抛出“对象不支持此属性和方法”的错误

lisi.say();//此处会抛出“对象不支持此属性和方法”的错误
[/code]
通过例子1可以看出，虽然我们为Person函数定义了名称为say方法，但是只有Person函数自己可以调用该方法，通过Person函数构造出来的zhangsan和lisi两个对象都不能调用该方法，也就是说Person构造出来的对象是不能共享Person函数的属性和方法的。
例子2：
[code=java]
function Person(name){

	this.name = name;

}

Person.prototype.say = function(){

	alert("hello,"+this.name);

}

Person.say();//此处会抛出“对象不支持此属性和方法”的错误

Person. prototype .say();//输出“hello,undefined”

var zhangsan = new Person("zhangsan");

var lisi = new Person("lisi");

zhangsan.say();//输出“hello,zhangsan”

lisi.say();//输出“hello,lisi”
[/code]
通过例子2可以看出，我们在Person函数的prototype属性上定义的say方法，通过Person函数构造出来的zhangsan和lisi两个对象都可以调用该方法，也就是说Person构造出来的对象是可以共享Person函数在prototype属性上定义的属性和方法的。但是，Person函数自身却不能直接调用该方法，因此在调用Person.say()时会报错，只能通过Person. prototype .say()进行调用。