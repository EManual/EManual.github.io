在EJB3 中定义了四种Entity 的状态:
1. 新实体(new)。Entity 由应用产生，和EJB3 Persistence 运行环境没有联系，也没有唯一的标示符(Identity)。
2. 持久化实体(managed)。新实体和EJB3 Persistence 运行环境产生关联（通过persist(), merge()等方法)，在EJB3
Persistence 运行环境中存在和被管理，标志是在EJB3 Persistence 运行环境中有一个唯一的标示(Identity)。
3. 分离的实体(detached)。Entity 有唯一标示符，但它的标示符不被EJB3 Persistence 运行环境管理, 同样的该
Entity 也不被EJB3 Persistence 运行环境管理。
4. 删除的实体(removed)。Entity 被remove()方法删除，对应的纪录将会在当前事务提交的时候从数据库中删除。
持久化规范允许你在实体类中实现回调方法，当这些事件发生时将会通知你的实体对象。当然你也可以使用一个外部类去拦截这些事件，这个外部类称作实体监听者。通过@EntityListeners  注释绑定到实体Bean。
生命周期回调事件
如果需要在生命周期事件期间执行自定义逻辑，请使用以下生命周期事件注释关联生命周期事件与回调方法，EJB3.0允许你将任何方法指定为回调方法。这些方法将会被容器在实体生命周期的不同阶段调用。