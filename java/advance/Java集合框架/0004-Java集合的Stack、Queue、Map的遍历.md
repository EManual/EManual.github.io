在集合操作中，常常离不开对集合的遍历，对集合遍历一般来说一个foreach就搞定了，但是，对于Stack、Queue、Map类型的遍历，还是有一些讲究的。
最近看了一些代码，在便利Map时候，惨不忍睹，还有一些是遍历错误，忽略了队列、栈与普通Collection的差别导致的，这些代码就不作为反面教材了。
下面是常用的写法：
一、Map的遍历
```java  
import java.util.HashMap;    
import java.util.Iterator;   
import java.util.Map;     
/** 
* Map的遍历，这个遍历比较特殊，有技巧 
*/   
public class TestMap { 
        public static void main(String[] args) { 
                Map<String, String> map = new HashMap<String, String>(); 
                map.put("1", "a"); 
                map.put("2", "b"); 
                map.put("3", "c"); 

                //最简洁、最通用的遍历方式 
                for (Map.Entry<String, String> entry : map.entrySet()) { 
                        System.out.println(entry.getKey() + " = " + entry.getValue()); 
                } 
                //Java5之前的比较简洁的便利方式1 
                System.out.println("----1----"); 
                for (Iterator<Map.Entry<String, String>> it = map.entrySet().iterator(); it.hasNext();) { 
                        Map.Entry<String, String> entry = it.next(); 
                        System.out.println(entry.getKey() + " = " + entry.getValue()); 
                } 
                //Java5之前的比较简洁的便利方式2 
                System.out.println("----2----"); 
                for (Iterator<String> it = map.keySet().iterator(); it.hasNext();) { 
                        String key = it.next(); 
                        System.out.println(key + " = " + map.get(key)); 
                } 
        } 
}
 
3 = c 
2 = b 
1 = a 
----1---- 
3 = c 
2 = b 
1 = a 
----2---- 
3 = c 
2 = b 
1 = a 

Process finished with exit code 0
``` 
二、Queue的遍历
```java  
import java.util.Queue;    
import java.util.concurrent.LinkedBlockingQueue;   
/**     * 队列的遍历   */   
public class TestQueue { 
        public static void main(String[] args) { 
                Queue<Integer> q = new LinkedBlockingQueue<Integer>(); 
                //初始化队列 
                for (int i = 0; i < 5; i++) { 
                        q.offer(i); 
                } 
                System.out.println("-------1-----"); 
                //集合方式遍历，元素不会被移除 
                for (Integer x : q) { 
                        System.out.println(x); 
                } 
                System.out.println("-------2-----"); 
                //队列方式遍历，元素逐个被移除 
                while (q.peek() != null) { 
                        System.out.println(q.poll()); 
                } 
        } 
}
 
-------1----- 
0 
1 
2 
3 
4 
-------2----- 
0 
1 
2 
3 
4 

Process finished with exit code 0
```
三、Stack的遍历
```java  
import java.util.Stack;    /**      * 栈的遍历     */   
public class TestStack { 
        public static void main(String[] args) { 
                Stack<Integer> s = new Stack<Integer>(); 
                for (int i = 0; i < 10; i++) { 
                        s.push(i); 
                } 
                //集合遍历方式 
                for (Integer x : s) { 
                        System.out.println(x); 
                } 
                System.out.println("------1-----"); 
                //栈弹出遍历方式 
//                while (s.peek()!=null) {     //不健壮的判断方式，容易抛异常，正确写法是下面的 
                while (!s.empty()) { 
                        System.out.println(s.pop()); 
                } 
                System.out.println("------2-----"); 
                //错误的遍历方式 
//                for (Integer x : s) { 
//                        System.out.println(s.pop()); 
//                } 
        } 
}
 
0 
1 
2 
3 
4 
------1----- 
4 
3 
2 
1 
0 
------2----- 

Process finished with exit code 0
```
在遍历集合时候，优先考虑使用foreach语句来做，这样代码更简洁些。