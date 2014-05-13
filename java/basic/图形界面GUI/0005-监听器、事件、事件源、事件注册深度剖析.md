* AWT事件处理
事件处理机制，几类具有典型代表意义的事件：
  
* 用户图形界面的行为
1、事件类型
(1)事件类的层次结构图如下所示。许多事件类在java.awt.event包中，也有一些事件类在API的其他地方。
(2)对于每类事件，都有一个接口，这个接口必须由想接收这个事件的类的对象实现。这个接口还要求定义一个或多个方法。当发生特定的事件时，就会调用这些方法。
2、事件类的结构图：不需要记，用的时候学会查看JDK文档即可。
  
3、方法类型和接口
  
demo程序如下：
```java  
package com.ahueir.awt;  
import java.awt.Button;   import java.awt.Frame;   import java.awt.event.ActionEvent;   import java.awt.event.ActionListener;   import java.awt.event.WindowEvent;   import java.awt.event.WindowListener;  import java.util.Date;  
public class MyFrame2 {
	public static void main(String[] args) {
		Frame frame =  new Frame("My Frame2");
		/*		 * 在JDk 中查找frame类里面的addXxxListener类似的方法，找不到再从其父类中寻找		 */
		frame.addWindowListener(new MyWindowListener());		
		Button button = new Button("Click Me");
		button.addActionListener(new MyListener());	
		frame.add(button);
		frame.setSize(200, 200);
		frame.setVisible(true);
	}
}

class MyListener implements ActionListener{
	@Override	@SuppressWarnings("deprecation")	public void actionPerformed(ActionEvent e) {
		/*
		 * 时间就是按格林威治时间：January 1, 1970, 00:00:00 GMT.到当前所经历的毫秒数。		 * 将这个毫秒数转化为时间		 */
		long milliSeconds = e.getWhen();
		/*		 * 查看JDK Doc文档中的Date类的 public Date(long date)		 */
		Date date = new Date(milliSeconds);
		
		System.out.println(date.toLocaleString());
	}
}

class MyWindowListener implements WindowListener{

	@Override	public void windowOpened(WindowEvent e) {
		// TODO Auto-generated method stub	}

	@Override	public void windowClosing(WindowEvent e) {
		System.out.println("关闭窗口");
		System.exit(0); //推出Java虚拟机
	}

	@Override	public void windowClosed(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void windowIconified(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override	public void windowDeiconified(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override	public void windowActivated(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override	public void windowDeactivated(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	
}
```
编译执行结果产生一个窗口，这里不截图出来了，输出以下内容：
2013-1-13 21:25:39
关闭窗口
下面我们联系以下两个监听器的使用方法：
Demo程序如下所示：
```java  
package com.ahueir.awt;
import java.awt.BorderLayout;  import java.awt.Frame;  import java.awt.Label;  import java.awt.TextField;   import java.awt.event.MouseEvent;   import java.awt.event.MouseListener;   import java.awt.event.MouseMotionListener;   
public class TwoListen implements MouseListener, MouseMotionListener{
	private Frame frame;
	private TextField textField; //文本框	
	@Override	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
	}

	@Override	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub	}

	@Override	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub	}

	@Override	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub		
	}

	//当鼠标退出Frame后，在命令行中打印出信息	@Override	public void mouseExited(MouseEvent e) {
		String str = "The mouse has left the Frame";
		this.textField.setText(str);	}


	//鼠标拖动的时候，注意是点击拖动	@Override	public void mouseDragged(MouseEvent e) {
		/*		 * 对于图形界面来说，窗口的坐上角是起点		 */
		String str = "x: " + e.getX() + ", y:" + e.getY();  
		this.textField.setText(str); //将鼠标拖动获得的信息加到文本框中	}

	@Override	public void mouseMoved(MouseEvent e) {
		// TODO Auto-generated method stub		
	}

	public void go(){
		frame = new Frame("Two Listener Example");		
		frame.add(new Label("click"), BorderLayout.NORTH); //添加一个 Label:标签
		textField = new TextField(30); //表示文本框的长度为30		
		frame.add(textField, BorderLayout.SOUTH);
		frame.addMouseMotionListener(this); //使用this表示直接使用本类中当前的对象
		frame.addMouseListener(this);
		frame.addMouseListener(new MyMouseListener());
		frame.setSize(300, 200);
		frame.setVisible(true);
	}
	public static void main(String[] args) {
		TwoListen two = new TwoListen();
		two.go();
	}
}


class MyMouseListener implements MouseListener{
	@Override	public void mouseClicked(MouseEvent e) {		// TODO Auto-generated method stub
	}

	@Override	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
	}

	@Override	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub	}

	@Override	public void mouseEntered(MouseEvent e) {
		String str = "The mouse has entered the Frame";
		System.out.println(str);
	}

	@Override	public void mouseExited(MouseEvent e) {
		String str = "The mouse has exited the Frame";
		System.out.println(str);
	}
}
```
【说明】：对于同一个事件源，注册两个同种类型的监听器是没有问题的，而且他们同时的都会发生作用。如下图所示：
  