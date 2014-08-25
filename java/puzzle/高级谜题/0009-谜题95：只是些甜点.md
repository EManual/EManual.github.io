本章的大多数谜题都是颇具挑战性的。但是这个不是。下面这个程序会打印出什么呢？如果你相信的话，前2个程序被报告为系统的缺陷[Bug 4157460 4763901]： 
```java  
public class ApplePie {
    public static void main(String[] args) {
        int count = 0;
        for(int i = 0; i < 100; i++); {
            count++;
        }
        System.out.println(count);
    }
}

import java.util.*;
public class BananaBread {
    public static void main(String[] args) {
        Integer[] array = { 3, 1, 4, 1, 5, 9 };
        Arrays.sort(array, new Comparator<Integer>() {
            public int compare(Integer i1, Integer i2) {
                return i1 < i2 ? -1 : (i2 > i1 ? 1 : 0);
            }
        });
       System.out.println(Arrays.toString(array));
  }
}

public class ChocolateCake {
    public static void main(String[] args) {
         System.out.println(true?false:true == true?false:true);
    }
}
```
如果你受够这些东西了，那么你不需要知道这些愚蠢谜题的详细解释，所以让我们把它们变得又短又甜： 
1，这个程序会打印出1。这是由多余的标号造成的。（分号的恶习？） 
2，这个程序在我们所知道的所有平台实现上都会打印出[3, 1, 4, 1, 5, 9]。从技术上说，程序的输出是未被定义的。它的比较器（comparator）承受着“是头我赢，是尾你输”的综合症。 
3，这个程序会打印出false。它书写的布局和它的操作符的优先级并不匹配。加一些括号可以解决问题。 
这个谜题的教训，也是整本书的教训，就是：不要像我的兄弟那样编码。 