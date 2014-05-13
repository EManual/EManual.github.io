abstract表示抽象的，是最重要的一个修饰符，可以修饰类和方法。分别叫做抽象方法和抽象类。人们在认识事物的时候，会把具有相同特征和行为的事物归为一个抽象类。比如动物就是一个很抽象的概念。当得到动物的实例时，总是某个具体物种的实例。所以说，在需要某个抽象类的实例时，只能够用某个具体类的实例来代替。抽象类不能实例化，不能生成抽象类的对象，但能定义一个引用。
* abstract修饰类：
会使这个类成为一个抽象类，这个类将不能生成对象实例，但可以做为对象变量声明的类型，也就是编译时类型。
抽象类就相当于一个类的半成品，需要子类继承并覆盖其中的抽象方法，这时子类才又创建实例的能力，如果子类没有实现父类的抽象方法，那么子类也要为抽象类。
* abstract修饰方法：
会使这个方法变成抽象方法，也就是只有声明而没有实现，实现部分以“;”代替，需要子类继承实现。
抽象方法代表了某种标准，定义标准，定义功能，在子类中去实现功能（子类继承了父类并需要给出从父类继承的抽象方法的实现）。
方法一时间想不到怎么被实现，或有意要子类去实现而定义某种标准，这个方法可以被定义为抽象。
* 注意：
有抽象方法的类一定是抽象类。但是抽象类中不一定都是抽象方法，也可以全是具体方法。
当一个非抽象类继承自某个抽象类时，必须实现所继承抽象类的所有抽象方法，即抽象类的第一个非抽象子类必须要实现其父类所有的抽象方法。其中也包括了父类继承的抽象方法。
一个类中只要包含有抽象方法，那么这个类就必须被定义成抽象类，反之，即使一个类不包含任何抽象方法，这个类仍然可以被定义成抽象类。
abstract和final不能同时使用，这两个关键字有着相反的含义。abstract修饰方法和类，就是想让别人重写或者是继承的，而final是组织重写和继承的。private和abstract也不能同时修饰方法。因为private组织继承，也就阻止了重写实现，与abstract的意义相违背。
```java  
/**   * @param args   * 这个类中有多个类，注意他们之间的关系    * 这个程序测试抽象方法和抽象类   * 抽象类之间的集成和非抽象类继承抽象类，实现抽象方法   */  
public class AbstractTest {
	 public static void main(String[] args) {
		// TODO Auto-generated method stub
		Shepherd shepherd=new Shepherd();
		shepherd.eat();
		shepherd.run();
		Chihuahua chihuahua=new Chihuahua();
		chihuahua.eat();
		chihuahua.run();
	 }
}

abstract class Animal {//抽象类Animal
	public abstract void eat();
} 

//抽象类Dog，继承自Animal，有抽象方法run，继承了父类的抽象方法eat  abstract class Dog extends Animal {
	public abstract void run();
	@Override
	public void eat() {
	// TODO Auto-generated method stub
	
	}
}

//Chihuahua继承了抽象类Dog，实现了Dog的方法run和其继承的抽象类的eat方法  class Chihuahua extends Dog {

	@Override
	public void run() {
		System.out.println("吉娃娃活泼的很，向前跑");
	}
	@Override
	public void eat(){
		System.out.println("吉娃娃池的好少");
	}
}

//Shepherd继承了Dog，实现了Dog的方法run和其继承的抽象类的eat方法    class Shepherd extends Dog {
	@Override
	public void run() {
		System.out.println("牧羊犬跑得好快去接飞盘");
	}
	@Override
	public void eat(){
		System.out.println("牧羊犬齿东西狼吞虎咽的");
	}
}
```