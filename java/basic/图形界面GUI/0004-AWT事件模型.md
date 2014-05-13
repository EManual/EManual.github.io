* 1、什么是事件
1)事件------描述发生了什么的对象 [事件与异常类似，是由一个个类构成的，当一个事件产生的时候，实际上是由对应的那个事件的类来生成了一个对象，这个对象封装了与这个事件相关的信息，我们可以通过这个对象获取到事件相关的信息]。
2)事件源------事件的产生器 [比如说是一个按钮]。
3)事件处理器------接收事件、解释事件并处理用户交互的方法[注意是一个方法]。
如果用户在用户界面层执行了一个动作(鼠标点击和按键)，这将导致一个事件的发生。事件是描述发生了什么的对象。存在各种不同类型的事件类用来描述各种类型的用户交互。
* 2、事件源
事件源是一个事件的产生者。例如，在Button组件上点击鼠标会产生以这个Button为源的一个ActionEvent[可以理解为JDK给我们提供的鼠标点击按钮产生的事件，这个事件是ActionEvent这个类的对象]. 这个ActionEvent实例是一个对象，它包含关于刚才所发生的那个事件的信息的对象，这些信息包括：
1)getActionCommand － 返回与动作相关联的命令名称
2)getWhen — 返回事件发生的时间
查看JDK Doc文档中的ActionEvent类：
```java  
java.awt.event
Class ActionEvent
java.lang.Object
  java.util.EventObject
      java.awt.AWTEvent
          java.awt.event.ActionEvent
public class ActionEventextends AWTEvent
    A semantic event which indicates that a component-defined action occurred. 
```
[Java中的事件一般都位于 java.awt.event包下面
这个类表示一个语义上的事件，它表明了一个组件定义的动作发生了]比如点击Button，这个事件就发生了.它竟然是一个类，我们就可以通过它的对象来访问它一下的一些方法，如 etActionCommand() 和 getWhen()。
* 3、事件处理器
事件处理器就是一个接收事件、解释事件并处理用户交互的方法。[归根结底就是一个方法，用来处理点击的动作，当点击事件发生的时候，事件处理器就会自动得到调用。]
* JDK1.1的事件模型：委托模型
事件监听器：实现了监听器接口的类。一个监听器对象是一个实现了专门的监听器接口的类的实例。
  
Demo如下所示：
```java  
package com.ahueir.awt;import java.awt.BorderLayout;  import java.awt.Button;  import java.awt.Frame;     import java.awt.event.ActionEvent;   import java.awt.event.ActionListener;    
public class TestButton {
	public static void main(String[] args) {
		Frame frame = new Frame("Test Button");
		Button button = new Button("Press Me!");		
		//增加事件处理器		button.addActionListener(new ButtonHandler());				frame.add(button, BorderLayout.CENTER);
		frame.pack();
		frame.setVisible(true);
	}
}

class ButtonHandler implements ActionListener{	
	/*	 * 这边为什么要给actionPerformed()传递一个ActionEvent的参数 e 呢？为什么不传递一个字符串呢？	 * 原因是当我们点击了按钮，就会产生一个事件对象，这个事件对象封装了产生对象的时候所有对象的信息，	 * 包括按钮上面的标签，点击产生事件发生的时间等	 * 这个ActionEvent产生的对象是由底层系统帮助我们生成的类似前面所讲的异常。	 * 这个对象传递给与这个事件关联的事件处理器，事件处理器得到调用，可以通过这个对象获得封装的一些信息。	 */
	@Override
	public void actionPerformed(ActionEvent e) {
		System.out.println("Button is Pressed!");
		String str = e.getActionCommand();
		System.out.println(str);
	}
}
```
编译执行结果产生一个按钮，点击这个按钮输出以下内容(这边就不截图了)：
Button is Pressed!
Press Me!
【说明1】：
1)在Button对象上用鼠标进行点击时，将发送一个ActionEvent事件。这个ActionEvent事件会被使用addActionListener()方法进行注册的所有ActionListener的actionPerformed()方法接收。
2)ActionEvent类的getActionCommand()方法返回与动作相关联的命令名称。
3)以按钮的点击动作为例，将返回Button的标签。
【说明2】：
查看JDK Doc文档中的Button这个类，查看里面的方法 addActionListener()
```java  
addActionListener
   public void addActionListener(ActionListener l)
Adds the specified action listener to receive action events from this button. 
```
[添加一个特定的动作当监听到从这个按钮接受到的事件后]。
* 委托模型优点
1)事件不会被意外地处理。
2)有可能创建并使用适配器(adapter)类对事件动作进行分类。
3)委托模型有利于把工作分布到各个类中。[比如说有Frame、Panel、Button三个组件，我们可以写三个事件处理器，可以针对这三个组件进行处理，点击某一个组件就对应某一个事件管理器进行处理，对应关系比较明确的]。