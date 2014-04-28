去掉一个Vector集合中重复的元素
```java  
Vector newVector = new Vector();
For (int i=0;i<vector.size();i++){
	Object obj = vector.get(i);
	if(!newVector.contains(obj);
		newVector.add(obj);
}
```
还有一种简单的方式，HashSet set = new HashSet(vector); 