布局管理器，现在我们使用的布局管理器一般是使用默认的，或者屏蔽掉自己定义一个布局管理器。
1)容器里组件的位置和大小是由布局管理器来决定的。容器对布局管理器的特定实例保持一个引用。当容器需要定位一个组件时，它将调用布局管理器来完成。当决定一个组件的大小时，也是如此。
2)在AWT中，给我们提供了五种布局管理器[了解一下]：
```java  
BorderLayout
FlowLayout
GridLayout
CardLayout
GridBagLayout
```
3)容器中组件的布局通常由布局管理器控制。每个Container（比如一个Panel或一个Frame）都有一个与它相关的缺省布局管理器，它可以通过调用setLayout()来改变。
4)布局管理器负责决定布局方针以及其容器的每一个子组件的大小。
5)我们可以通过设置空布局管理器，来控制组件的大小和位置。调用setLayout(null)。
6)在设置空布局管理器后，必须对所有的组件调用setLocation()，setSize()或setBounds()，将它们定位在容器中。
  
* Border布局管理器
1)Border布局管理器为在一个Panel或Window中放置组件提供一个更复杂的方案。Border布局管理器包括五个明显的区域：东、南、西、北、中。
2)北占据面板的上方，东占据面板的右侧，等等。中间区域是在东、南、西、北都填满后剩下的区域。当窗口垂直延伸时，东、西、中区域也延伸；而当窗口水平延伸时，东、西、中区域也延伸。
3)当窗口缩放时，按钮相应的位置不变化，但其大小改变。
4)BorderLayout是Frame类的默认布局管理器。
5)BorderLayout将整个容器的布局划分成东、西、南、北、中五个区域，组件只能被添加到指定的区域。
6)如不指定组件的加入部位，则默认加入到Center区域。
7)每个区域只能加入一个组件，如加入多个，则先前加入的组件会被遗弃。
8)BorderLayout型布局容器尺寸缩放原则,如下图所示：
a)北、南两个区域只能在水平方向缩放(宽度可调整)。
b)东、西两个区域只能在垂直方向缩放(高度可调整)。
c)中部可在两个方向上缩放。
  
程序如下：
```java  
package com.ahuier.awt;
import java.awt.Button;  import java.awt.FlowLayout;  import java.awt.Frame;  
public class ExGui {
	private Frame frame;
	private Button button1;
	private Button button2;
	
	public void go(){
		frame = new Frame("gui example");
		frame.setLayout(new FlowLayout());
		
		button1 = new Button("Press me");
		button2 = new Button("Don't press me");		
		frame.add(button1);
		frame.add(button2);		
		frame.pack(); //这个方法表示这个容器刚刚能够包含到里面的组件的最小的大小
		frame.setVisible(true);
	}
	public static void main(String[] args) {
		ExGui window = new ExGui();
		window.go();
	}
}
```
* FlowLayout布局管理器
1) 与其它布局管理器不一样，Flow布局管理器不限制它所管理的组件的大小，而是允许它们有自己的最佳大小。
2) 默认是居中放置组件。
3) 如果想在组件之间创建一个更大的最小间隔，可以规定一个界限。
4) 当用户对由Flow布局管理的区域进行缩放时，布局就发生变化。[这与BorderLayout差别比较大]
5) FlowLayout的构造方法：
(1) new FlowLayout(FlowLayout.RIGHT,20,40);右对齐，组件之间水平间距20个像素，竖直间距40个像素；
(2) new FlowLayout(FlowLayout.LEFT);左对齐，水平和竖直间距为缺省值：5；
(3) new FlowLayout();使用缺省的居中对齐方式，水平和竖直间距为缺省值：5；
程序如下所示：
```java  
package com.ahueir.awt;
import java.awt.Button;  import java.awt.FlowLayout;   import java.awt.Frame;  
public class MyFlow {
	private Frame frame;
	private Button button1, button2, button3;
	public void go(){
		frame = new Frame("Flow Layout");
		//Frame的布局管理器默认是BorderLayout,要使用FlowLayout需要设置Layout为FlowLayout
		//使用FlowLayout替换掉默认的BorderLayout布局管理器
		frame.setLayout(new FlowLayout()); 
		
		button1 = new Button("hello");
		button2 = new Button("world");
		button3 = new Button("Welcome");		
		frame.add(button1);
		frame.add(button2);
		frame.add(button3);
		
		frame.setSize(100, 100);
		frame.setVisible(true);
	}
	public static void main(String[] args) {
		MyFlow flow = new MyFlow();
		flow.go();
	}
}
```
【说明】：你可以通过改变窗口大小，则里面的按钮会随着窗口的变化而变化。具体变化方式是按第一行排列，排列不下放在第二行。
如果将其上面程序的：frame.setLayout(new FlowLayout()); 这行代码屏蔽掉，则Frame默认使用BorderLayout，编译产生的结果是界面是只有一个Welcome按钮，其他两个按钮都被遮住了。
* 
1)Grid布局管理器为放置组件提供了灵活性。用许多行和栏来创建管理程序。然后组件就填充到由管理程序规定的单元中。
2)比如，由语句new GridLayout(3,2)创建的有三行两栏的Grid布局能产生六个单元
3)Grid布局管理器总是忽略组件的最佳大小。所有单元的宽度是相同的，是根据单元数对可用宽度进行平分而定的。同样地，所有单元的高度是相同的，是根据行数对可用高度进行平分而定的
4)将组件添加到网格中的命令决定它们占有的单元。单元的行数是从左到右填充，就象文本一样，而列是从上到下由行填充。
程序如下所示：
```java  
package com.ahueir.awt;
import java.awt.Button;  import java.awt.Frame;   import java.awt.GridLayout;   public class GridEx {
	private Frame frame;
	private Button b1, b2, b3, b4, b5, b6;
	
	public void go(){
		frame = new Frame("Grid Layout");
		frame.setLayout(new GridLayout(3, 2));		
		b1 = new Button("1");
		b2 = new Button("2");
		b3 = new Button("3");
		b4 = new Button("4");
		b5 = new Button("5");
		b6 = new Button("6");
		
		//这边直接增加进去，它是按顺序来的，第一放在第一行第一列，第二个方法第二行第二列......
		frame.add(b1);
		frame.add(b2);
		frame.add(b3);
		frame.add(b4);
		frame.add(b5);
		frame.add(b6);
		
		frame.pack();
		frame.setVisible(true);
	}
	public static void main(String[] args) {
		GridEx grid = new GridEx();
		grid.go();
	}
}
```
【说明】:我们电脑上计算器就是按GridLayout写的布局类似。
* 
Card布局管理器能将界面看作一系列的卡，其中的一个在任何时候都可见。用add()方法来将卡添加到Card布局中。Card布局管理器的show()方法应请求转换到一个新卡中。
* 
1)除了Flow、Border、Grid和Card布局管理器外，核心Java.awt也提供GridBag布局管理器。
2)GridBag布局管理器在网格的基础上提供复杂的布局，但它允许单个组件在一个单元中而不是填满整个单元那样地占用它们的最佳大小。网格包布局管理器也允许单个组件扩展成不止一个单元。
创建面板及复杂布局,程序如下所示：
```java  
package com.ahueir.awt;

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Frame;
import java.awt.Panel;

public class ExGui3 {
	private Frame frame;
	private Panel panel;
	private Button b1, b2, b3, b4;
	
	public void go(){
		frame = new Frame("complex layout");
		
		b1 = new Button("West");
		b2 = new Button("hello");		
		frame.add(b1, BorderLayout.WEST);
		frame.add(b2, BorderLayout.CENTER);
		
		panel = new Panel();
		
		b3 = new Button("world");
		b4 = new Button("welcome");
		
		//panel的布局管理器默认是FlowLayout
		panel.add(b3);
		panel.add(b4);
		frame.add(panel, BorderLayout.NORTH);
				frame.pack();
		frame.setVisible(true);
	}
	public static void main(String[] args) {
		ExGui3 gui = new ExGui3();
		gui.go();
	}
}
```
* 布局管理器总结:
1)Frame
a) Frame是一个顶级窗口。
b) Frame的缺省布局管理器为BorderLayout。
2)Panel
a) Panel无法单独显示，必须添加到某个容器中。
b) Panel的缺省布局管理器为FlowLayout。
c) 当把Panel作为一个组件添加到某个容器中后，该Panel仍然可以有自己的布局管理器。因此，可以利用Panel使得BorderLayout中某个区域显示多个组件。
3). 在程序中安排组件的位置和大小时，应注意：
a)容器中的布局管理器负责各个组件的大小和位置，因此用户无法在这种情况下设置组件的这些属性。如果试图使用Java语言提供的setLocation()，setSize()，setBounds()等方法，则都会被布局管理器覆盖。
b) 如果用户确实需要亲自设置组件大小或位置，则应取消该容器的布局管理器，方法为：setLayout(null)；