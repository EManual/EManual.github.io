利用事务模板TransactionTemplate来手动添加事务
```java  
public void addRant(Rant rant) {
	transactionTemplate.execute(-?transactionTemplate是注入transactionManager得到的
	new TransactionCallback() {-? TransactionCallback()只有一个方法实现doInTransaction，用一个匿名内部类实现
		public Object doInTransaction(TransactionStatus ts) {  ------?在事务内执行
			try {
				rantDao.saveRant(rant);
			} catch (Exception e) {
				ts.setRollbackOnly();------------------?出现异常就回滚
			}
			return null;
		}
	}
}
```
配置文件
```java  
<bean id="rantService"
class="com.roadrantz.service.RantServiceImpl">
…
<property name="transactionTemplate  ">
<bean class="org.springframework.transaction.support.
? TransactionTemplate">
<property name="transactionManager"
ref="transactionManager" />
</bean>
</property>
</bean>
```