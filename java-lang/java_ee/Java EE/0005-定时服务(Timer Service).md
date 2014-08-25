定时服务用作在一段特定的时间后执行某段程序，估计各位在不同的场合中已经使用过。下面就直接介绍EJB3.0定时服务的开发过程。定时服务的开发过程与会话Bean 的开发过程大致相同，但比会话Bean 多了几个操作，那就是使用容器对象SessionContext 创建定时器，并使用@Timeout 注释声明定时器方法。
[code=java]
@Stateless
@Remote (TimerService.class)
public class TimerServiceBean implements TimerService {
	private int count = 1;
	private @Resource SessionContext ctx;
	public void scheduleTimer(long milliseconds){
		count = 1;
		ctx.getTimerService().createTimer(new Date(new Date().getTime() + milliseconds),milliseconds,"大家好，这是我的第一个定时器");
	}
	@Timeout
	public void timeoutHandler(Timer timer) {
		System.out.println("---------------------");
		System.out.println("定时器事件发生,传进的参数为: " + timer.getInfo());
		System.out.println("---------------------");
		if (count>=5){
			timer.cancel();//如果定时器触发5次，便终止定时器
		}
		count++;
	}
}
[/code]
下面是TimerServiceBean 的Remote 业务接口
[code=java]
TimerService.java
package com.foshanshop.ejb3;
public interface TimerService {
	public void scheduleTimer(long milliseconds);
}
[/code]
通过依赖注入@Resource SessionContext ctx，我们获得SessionContext 对象，调用ctx.getTimerService().createTimer
(Date arg0, long arg1, Serializable arg2)方法创建定时器，三个参数的含义如下：
Date arg0：定时器启动时间，如果传入时间小于现在时间，定时器会立刻启动。
long arg1：间隔多长时间后再次触发定时事件。单位：毫秒
Serializable arg2：你需要传给定时器的参数，该参数必须实现Serializable 接口。
当定时器创建完成后，我们还需声明定时器方法。定时器方法的声明很简单，只需在方法上面加入@Timeout 注
释，另外定时器方法必须遵守如下格式：
[code=java]
void XXX(Timer timer)
[/code]
在定时事件发生时，此方法将被执行。