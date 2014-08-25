Javascript的数据类型
JavaScript中的数据类型相对于其他的开发语言来说要简洁很多，分为简单数据类型和复杂数据类型。简单数据类型只有undefined，null，boolean，number和string这五种；而复杂数据类型只有一种，即object。
JavaScript的代码都是由function组成，即函数。
注意：JavaScript语言是区分大小写的，以上数据类型的单词都是小写的，不要和Number，String，Object，Function等JavaScript的内置函数混淆了。
关于object
JavaScript中没有“类”的概念，只有对象。
对象的声明方式
第一种，调用Object函数创建对象：
[code=java]
var person = new Object();
[/code]
对于一个已经声明的对象，可以给该对象设置任意属性。比如我们为person对象设置一个名称的属性：
[code=java]
person.name = ‘zhangsan’;
alert(person.name);
[/code]
这样就给person对象设置了一个叫做name的属性，alert中会弹出name的属性值’zhangsan’。
第二种，采用JSON形式创建对象：
[code=java]
var person = {name:’zhangsan’};
alert(person.name);
[/code]
这种声明方式与第一种方式是等价的，alert中同样会弹出name的属性值’zhangsan’。
第三种，自定义函数形式创建对象：
[code=java]
function Person(){};//定义一个空函数
var person = new Person();//使用new关键字创建一个对象。
[/code]
对象的属性
对象的属性通常有两种访问方式，即“对象式”和“数组式”。
对象式：
[code=java]
person.name = ‘zhangsan’;
alert(person.name);//将name作为对象person的一个属性
[/code]
数组式：
[code=java]
person[‘name’] = ‘zhangsan’;
alert(person[name]);//将对象作为一个数组以属性名作为下标来访问。
[/code]
遍历对象的所有属性和方法：
[code=java]
for(var s in person){

	alert(person[s]);

}
[/code]
对象的属性可以是简单数据类型，也可以是复杂数据类型，也可以是一个函数。比如：
[code=java]
person.say = function(){

	alert(‘hello!’);

}

person.say();//将name作为对象person的一个属性

person[‘say’]();// 将对象作为一个数组以属性名作为下标来访问
[/code]