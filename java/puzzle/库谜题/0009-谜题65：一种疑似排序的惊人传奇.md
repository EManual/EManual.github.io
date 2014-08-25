下面的程序使用定制的比较器，对一个由随机挑选的Integer实例组成的数组进行排序，然后打印了一个描述了数组顺序的单词。回忆一下，Comparator接口只有一个方法，即compare，它在第一个参数小于第二个参数时返回一个负数，在两个参数相等时返回0，在第一个参数大于第二个参数时返回一个整数。这个程序是展示5.0版特性的一个样例程序。它使用了自动包装和解包、泛型和枚举类型。那么，它会打印出什么呢？ 
```java  
import java.util.*;
public class SuspiciousSort {
    public static void main(String[ ] args) {
        Random rnd = new Random();
        Integer[ ] arr = new Integer[100];
        for (int i = 0; i < arr.length; i++)
            arr[i] = rnd.nextInt();
        Comparator<Integer> cmp = new Comparator<Integer>() {
            public int compare(Integer i1, Integer i2) {
                return i2 - i1;
            }
        };
        Arrays.sort(arr, cmp);
        System.out.println(order(arr));
    }

    enum Order { ASCENDING, DESCENDING, CONSTANT, UNORDERED }; 

    static Order order(Integer[ ] a) {
        boolean ascending  = false;
        boolean descending = false;
        for (int i = 1; i < a.length; i++) {
            ascending  |= a[i] > a[i-1];
            descending |= a[i] < a[i-1];
        }
        if (ascending  && !descending)
            return Order.ASCENDING;
        if (descending && !ascending)
            return Order.DESCENDING;
        if (!ascending)
            return Order.CONSTANT;   // All elements equal 
        return Order.UNORDERED;      // Array is not sorted 
    } 
}
```
该程序的main方法创建了一个Integer实例的数组，并用随机数对其进行了初始化，然后用比较器cmp对该数组进行排序。这个比较器的compare方法将返回它的第二个参数减去第一个参数的值，如果第二个参数表示的是比第一个参数大的数值，其返回值就是正的；如果这两个参数相等，其返回值为0；如果第二个参数表示的是比第一个参数小的数值，其返回值就是负的。这种行为正好与compare方法通常的做法相反，因此，该比较器应该施加的是降序排列。 
在对数组排序之后，main方法将该数组传递给了静态方法order，然后打印由这个方法返回的结果。该方法在数组中所有的元素都表示相同的数值时，返回CONSTANT；在数组中每一对毗邻的元素中第二个元素都大于等于第一个元素时，返回ASCENDING；在数组中每一对毗邻的元素中第二个元素都小于等于第一个元素时，返回DESCENDING；在这些条件都不满足时，返回UNORDERED。尽管理论上说，数组中的100个随机数有可能彼此都相等，但是这种奇特现象发生的非常小：232×99分之一，即大约5×10953分之一。因此，该程序看起来应该打印DESCENDING。如果你运行该程序，几乎可以肯定你将看到它打印的是UNORDERED。为什么它会产生如此的行为呢？ 
order方法很直观，它并不会说谎。Arrays.sort方法已经存在许多年了，它工作得非常好。现在只有一个地方能够发现bug了：比较器。乍一看，这个比较器似乎不可能出错。毕竟，它使用的是标准的惯用法：如果你有两个数字，你想得到一个数值，其符号表示它们的顺序，那么你可以计算它们的差。这个惯用法至少从1970年代早期就一直存在了，它在早期的UNIX里面被广泛地应用。遗憾的是，这种惯用法从来都没有正确地工作过。本谜题也许应该称为“白痴一般的惯用法的案例”。这种惯用法的问题在于定长的整数没有大到可以保存任意两个同等长度的整数之差的程度。当你在做两个int或long数值的减法时，其结果可能会溢出，在这种情况下我们就会得到错误的符号。 
例如，请考虑下面的程序： 
```java  
public class Overflow {
    public static void main(String[] args){
        int x = -2000000000;
        int z = 2000000000;
        System.out.println(x - z);
    }
}
```
很明显，x比z小，但是程序打印的是294967296，它是一个正数。既然这种比较的惯用法是有问题的，那么为什么它会被如此广泛地应用呢？因为它在大多数时间里可以正常工作的。它只在用来来进行比较的两个数字的差大于Integer.MAX_VALUE的时候才会出问题。这意味着对于许多应用而言，在实际使用中是不会看到这种错误的。更糟的是，它们被观察到的次数少之又少，以至于这个bug永远都不会被发现和订正。 
那么这对于我们的程序的行为意味着什么呢？如果你查阅一下Comparator的文档，你就会看到它所实现的排序关系必须是可传递的（transitive），换句话说，(compare(x,y) > 0)&&(compare(y,z) > 0)蕴含着compare(x,z) > 0。如果我们取Overflow例子中的x和z，并取y为0，那么我们的比较器在这些数值上就违反了可传递性。事实上，在所有随机选取的int数值对中，有四分之一该比较器都会返回错误的值。用这样的比较器来执行一个搜索或排序，或者用它去排序一个有序的集合，都会产生不确定的行为，就像我们在运行本谜题的程序时所看到的那样。出于数学上的倾向性，Comparator.compare方法的一般约定要求比较器要产生一个全序（total order），但是这个比较器在数个计算上都未能做到这一点。 
我们可以通过替换遵守上述一般约定的Comparator实现来订正我们的程序。因为我们只是想要反转自然排序的顺序，所以我们甚至可以不必编写我们自己的比较器。Collection类提供了一个可以产生这种顺序的比较器。如果你用Arrays.sort(arr,Collections.reverseOrder())来替代最初的Arrays.sort调用，该程序就可以打印出我们所期望的DESCENDING。 
或者，你可以编写你自己的比较器。下面的代码并不“聪明”，但是它可以工作，从而使该程序可以打印出我们所期望的DESCENDING： 
```java  
public int compare(Integer i1, Integer i2) {
    return (i2 < i1 ? -1 : (i2 == i1 ? 0 :1));
}
```
本谜题有数个教训，最具体的是：不要使用基于减法的比较器，除非你能够确保要比较的数值之间的差永远不会大于Integer.MAX_VALUE [EJ Item 11]。更一般地讲，要意识到int的溢出，就像谜题3、26和33所讨论的那样。另一个教训是你应该避免“聪明”的代码。应该努力去编写清晰正确的代码，不要对它作任何优化，除非该优化被证明是必需的[EJ Item 37]。 
对语言设计者来说，得到的教训与谜题3、26和33相同：也许真的值得去考虑支持某种形式整数算数运算，它不会在溢出时不抛出异常。还有就是可能应该在语言中提供一个三值的比较器操作符，就像Perl所作的那样（<=>操作符）。