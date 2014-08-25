Enum作为Sun全新引进的一个关键字，看起来很象是特殊的class,它也可以有自己的变量，可以定义自己的方法，可以实现一个或者多个接口。 当我们在声明一个enum类型时，我们应该注意到enum类型有如下的一些特征。 
1．它不能有public的构造函数，这样做可以保证客户代码没有办法新建一个enum的实例。 
2．所有枚举值都是public,static,final的。注意这一点只是针对于枚举值，我们可以和在普通类里面定义变量一样定义其它任何类型的非枚举变量，这些变量可以用任何你想用的修饰符。 
3．Enum默认实现了java.lang.Comparable接口。 
4．Enum覆载了toString方法，因此我们如果调用Color.Blue.toString()默认返回字符串”Blue”. 
5．Enum提供了一个valueOf方法，这个方法和toString方法是相对应的。调用valueOf(“Blue”)将返回Color.Blue.因此我们在自己重写toString方法的时候就要注意到这一点，一把来说应该相对应地重写valueOf方法。 
6．Enum还提供了values方法，这个方法使你能够方便的遍历所有的枚举值。 
7．Enum还有一个oridinal的方法，这个方法返回枚举值在枚举类种的顺序，这个顺序根据枚举值声明的顺序而定，这里Color.Red.ordinal()返回0。 
了解了这些基本特性，我们来看看如何使用它们。 
1．遍历所有有枚举值. 知道了有values方法，我们可以轻车熟路地用ForEach循环来遍历了枚举值了。 
[code=java]
for (Color c: Color.values()) 
　　System.out.println(“find value:” + c); 
[/code]
2．在enum中定义方法和变量，比如我们可以为Color增加一个方法随机返回一个颜色。 
[code=java]
public enum Color { 
　　Red, 
　　Green, 
　　Blue; 

　　/* 
　　 *定义一个变量表示枚举值的数目。 
　　 *(我有点奇怪为什么sun没有给enum直接提供一个size方法). 
　　 */ 
　　private static int number = Color.values().length ; 

　　/** 
　　* 随机返回一个枚举值 
　　	@return a random enum value. 
　　*/ 
　　public static Color getRandomColor(){ 
	　　long random = System.currentTimeMillis() % number; 
	　　switch ((int) random){ 
	　　　case 0: 
	　　　　return Color.Red; 
	　　　case 1: 
	　　　　return Color.Green; 
	　　　case 2: 
	　　　　return Color.Blue; 
	　　　default : return Color.Red; 
	　　} 
　　} 
} 
[/code]
可以看出这在枚举类型里定义变量和方法和在普通类里面定义方法和变量没有什么区别。唯一要注意的只是变量和方法定义必须放在所有枚举值定义的后面，否则编译器会给出一个错误。 
3．覆载(Override)toString, valueOf方法 
前面我们已经知道enum提供了toString,valueOf等方法，很多时候我们都需要覆载默认的toString方法，那么对于enum我们怎么做呢。其实这和覆载一个普通class的toString方法没有什么区别。 
[code=java]
…. 
public String toString(){ 
    switch (this){ 
    case Red: 
        return "Color.Red"; 
    case Green: 
        return "Color.Green"; 
    case Blue: 
        return "Color.Blue"; 
    default: 
        return "Unknow Color"; 
    } 
} 
…. 
[/code]
这时我们可以看到，此时再用前面的遍历代码打印出来的是 
[code=java]
Color.Red 
Color.Green 
Color.Blue 
[/code]
而不是 
[code=java]
Red 
Green 
Blue 
[/code]
可以看到toString确实是被覆载了。一般来说在覆载toString的时候我们同时也应该覆载valueOf方法，以保持它们相互的一致性。 
4．使用构造函数 
虽然enum不可以有public的构造函数，但是我们还是可以定义private的构造函数，在enum内部使用。还是用Color这个例子。 
[code=java]
public enum Color { 
    Red("This is Red"), 
    Green("This is Green"), 
    Blue("This is Blue"); 
        
    private String desc; 
        
       Color(String desc){ 
        　this.desc = desc; 
       } 
        
       public String getDesc(){ 
        　return this.desc; 
       } 
} 
[/code]
这里我们为每一个颜色提供了一个说明信息, 然后定义了一个构造函数接受这个说明信息。 
要注意这里构造函数不能为public或者protected,从而保证构造函数只能在内部使用，客户代码不能new一个枚举值的实例出来。这也是完全符合情理的，因为我们知道枚举值是public static final的常量而已。 
5．实现特定的接口 
我们已经知道enum可以定义变量和方法，它要实现一个接口也和普通class实现一个接口一样，这里就不作示例了。 
6．定义枚举值自己的方法。 
前面我们看到可以为enum定义一些方法，其实我们甚至可以为每一个枚举值定义方法。这样，我们前面覆载 toString的例子可以被改写成这样。 
[code=java]
public enum Color { 
    Red { 
        public String toString(){ 
            return "Color.Red"; 
        } 
    }, 
    Green { 
        public String toString(){ 
            return "Color.Green"; 
        } 
    }, 
    Blue{ 
        public String toString(){ 
            return "Color.Blue"; 
        } 
    }; 
} 
[/code]
从逻辑上来说这样比原先提供一个“全局“的toString方法要清晰一些。 
总的来说，enum作为一个全新定义的类型，是希望能够帮助程序员写出的代码更加简单易懂，个人觉得一般也不需要过多的使用enum的一些高级特性，否则就和简单易懂的初衷想违背了。