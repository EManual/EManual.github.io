下面的程序循环遍历了一个int类型的数组序列，并且记录了满足某个特定属性的数组个数。那么，该程序会打印出什么呢？ 
```java  
public class Loop {
    public static void main(String[] args) {
        int[][] tests = { { 6, 5, 4, 3, 2, 1 }, { 1, 2 },
                      { 1, 2, 3 }, { 1, 2, 3, 4 }, { 1 } };
        int successCount = 0;
        try {
            int i = 0;
            while (true) {
                if (thirdElementIsThree(tests[i++]))
                    successCount ++;
            }
        } catch(ArrayIndexOutOfBoundsException e) {
            // No more tests to process
        }
        System.out.println(successCount);
    }    

    private static boolean thirdElementIsThree(int[] a) {
        return a.length >= 3 & a[2] == 3;
    }
}
```
该程序用thirdElementIsThree方法测试了tests数组中的每一个元素。遍历这个数组的循环显然是非传统的循环：它不是在循环变量等于数组长度的时候终止，而是在它试图访问一个并不在数组中的元素时终止。尽管它是非传统的，但是这个循环应该可以工作。如果传递给thirdElementIsThree的参数具有3个或更多的元素，并且其第三个元素等于3，那么该方法将返回true。对于tests中的5个元素来说，有2个将返回true，因此看起来该程序应该打印2。如果你运行它，就会发现它打印的时0。肯定是哪里出了问题，你能确定吗？ 
事实上，这个程序犯了两个错误。第一个错误是该程序使用了一种可怕的循环惯用法，该惯用法依赖的是对数组的访问会抛出异常。这种惯用法不仅难以阅读，而且运行速度还非常地慢。不要使用异常来进行循环控制；应该只为异常条件而使用异常[EJ Item 39]。为了纠正这个错误，可以将整个try-finally语句块替换为循环遍历数组的标准惯用法：
```java   
for (int i = 0; i < test.length; i++)
	if (thirdElementIsThree(tests[i]))
		successCount++;
```
如果你使用的是5.0或者是更新的版本，那么你可以用for循环结构来代替： 
```java  
for (int[] test : tests)
	if(thirdElementIsThree(test))
		successCount++;
```
就第一个错误的糟糕情况来说，只有它自己还不足以产生我们所观察到的行为。然而，订正该错误可以帮助我们找到真正的bug，它更加深奥： 
```java   
Exception in thread "main" 
java.lang.ArrayIndexOutOfBoundsException: 2
        at Loop1.thirdElementIsThree(Loop1.java:19)
        at Loop1.main(Loop1.java:13)
```
很明显，在thirdElementIsThree方法中有一个bug：它抛出了一个ArrayIndexOutOfBoundsException异常。这个异常先前伪装成了那个可怕的基于异常的循环的终止条件。 
如果传递给thirdElementIsThree的参数具有3个或更多的元素，并且其第三个元素等于3，那么该方法将返回true。问题是在这些条件不满足时它会做些什么呢。如果你仔细观察其值将会被返回的那个布尔表达式，你就会发现它与大多数布尔AND操作有一点不一样。这个表达式是a.length >= 3 & a[2] == 3。通常，你在这种情况下看到的是 && 操作符，而这个表达式使用的是 & 操作符。那是一个位AND操作符吗？ 
事实证明 & 操作符有其他的含义。除了常见的被当作整型操作数的位AND操作符之外，当被用于布尔操作数时，它的功能被重载为逻辑AND操作符[JLS 15.22.2]。这个操作符与更经常被使用的条件AND操作符有所不同，& 操作符总是要计算它的两个操作数，而 && 操作符在其左边的操作数被计算为false时，就不再计算右边的操作数了[JLS 15.23]。因此，thirdElementIsThree方法总是要试图访问其数组参数的第三个元素，即使该数组参数的元素不足3个也是如此。订正这个方法只需将 & 操作符替换为 && 操作符即可。通过这样的修改，这个程序就可以打印出我们所期望的2了： 
```java   
private static boolean thirdElementIsThree(int[] a) {
	return a.length >= 3 && a[2] == 3;
}
```
正像有一个逻辑AND操作符伴随着更经常被使用的条件AND操作符一样，还有一个逻辑OR操作符(|)也伴随着条件OR操作符(||)[JLS 15.22.2，15.24]。| 操作符总是要计算它的两个操作数，而 || 操作符在其左边的操作数被计算为true时，就不再计算右边的操作数了。我们一不注意，就很容易使用了逻辑操作符而不是条件操作符。遗憾的是，编译器并不能帮助你发现这种错误。有意识地使用逻辑操作符的情形非常少见，少到了我们对所有这样使用的程序都应该持怀疑态度的地步。如果你真的想使用这样的操作符，为了是你的意图清楚起见，请加上注释。 
总之，不要去用那些可怕的使用异常而不是使用显式的终止测试的循环惯用法，因为这种惯用法非常不清晰，而且会掩盖bug。要意识到逻辑AND和OR操作符的存在，并且不要因无意识的误用而受害。对语言设计者来说，这又是一个操作符重载会导致混乱的明证。对于在条件AND和OR操作符之外还要提供逻辑AND和OR操作符这一点，并没有很明显的理由。如果这些操作符确实要得到支持的话，它们应该与其相对应的条件操作符存在着视觉上的明显差异。