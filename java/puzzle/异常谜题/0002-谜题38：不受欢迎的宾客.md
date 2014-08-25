本谜题中的程序所建模的系统，将尝试着从其环境中读取一个用户ID，如果这种尝试失败了，则缺省地认为它是一个来宾用户。该程序的作者将面对有一个静态域的初始化表达式可能会抛出异常的情况。因为Java不允许静态初始化操作抛出被检查异常，所以初始化必须包装在try-finally语句块中。那么，下面的程序会打印出什么呢？ 
```java  
public class UnwelcomeGuest {
    public static final long GUEST_USER_ID = -1;
    private static final long USER_ID;
    static {
        try {
            USER_ID = getUserIdFromEnvironment();
        } catch (IdUnavailableException e) {
            USER_ID = GUEST_USER_ID;
            System.out.println("Logging in as guest");
        }
    }

    private static long getUserIdFromEnvironment() 
            throws IdUnavailableException { 
        throw new IdUnavailableException(); 
    }

    public static void main(String[] args) {
        System.out.println("User ID: " + USER_ID);
    }
}

class IdUnavailableException extends Exception { 
}
```
该程序看起来很直观。对getUserIdFromEnvironment的调用将抛出一个异常，从而使程序将GUEST_USER_ID(-1L)赋值给USER_ID，并打印Loggin in as guest。然后main方法执行，使程序打印User ID: -1。表象再次欺骗了我们，该程序并不能编译。如果你尝试着去编译它，你将看到和下面内容类似的一条错误信息： 
```java  
UnwelcomeGuest.java:10: 
variable USER_ID might already have been assigned
            USER_ID = GUEST_USER_ID;
            ^
```
问题出在哪里了？USER_ID域是一个空final（blank final），它是一个在声明中没有进行初始化操作的final域[JLS 4.12.4]。很明显，只有在对USER_ID赋值失败时，才会在try语句块中抛出异常，因此，在catch语句块中赋值是相当安全的。不管怎样执行静态初始化操作语句块，只会对USER_ID赋值一次，这正是空final所要求的。为什么编译器不知道这些呢？ 
要确定一个程序是否可以不止一次地对一个空final进行赋值是一个很困难的问题。事实上，这是不可能的。这等价于经典的停机问题，它通常被认为是不可能解决的[Turing 36]。为了能够编写出一个编译器，语言规范在这一点上采用了保守的方式。在程序中，一个空final域只有在它是明确未赋过值的地方才可以被赋值。规范长篇大论，对此术语提供了一个准确的但保守的定义[JLS 16]。因为它是保守的，所以编译器必须拒绝某些可以证明是安全的程序。这个谜题就展示了这样的一个程序。 
幸运的是，你不必为了编写Java程序而去学习那些骇人的用于明确赋值的细节。通常明确赋值规则不会有任何妨碍。如果碰巧你编写了一个真的可能会对一个空final赋值超过一次的程序，编译器会帮你指出的。只有在极少的情况下，就像本谜题一样，你才会编写出一个安全的程序，但是它并不满足规范的形式化要求。编译器的抱怨就好像是你编写了一个不安全的程序一样，而且你必须修改你的程序以满足它。 
解决这类问题的最好方式就是将这个烦人的域从空final类型改变为普通的final类型，用一个静态域的初始化操作替换掉静态的初始化语句块。实现这一点的最佳方式是重构静态语句块中的代码为一个助手方法： 
```java  
public class UnwelcomeGuest {
    public static final long GUEST_USER_ID = -1;
    private static final long USER_ID = getUserIdOrGuest;
    private static long getUserIdOrGuest {
        try {
            return getUserIdFromEnvironment();
        } catch (IdUnavailableException e) {
            System.out.println("Logging in as guest");
            return GUEST_USER_ID;
        }
    }
    ...// The rest of the program is unchanged
}
```
程序的这个版本很显然是正确的，而且比最初的版本根据可读性，因为它为了域值的计算而增加了一个描述性的名字，而最初的版本只有一个匿名的静态初始化操作语句块。将这样的修改作用于程序，它就可以如我们的期望来运行了。 
总之，大多数程序员都不需要学习明确赋值规则的细节。该规则的作为通常都是正确的。如果你必须重构一个程序，以消除由明确赋值规则所引发的错误，那么你应该考虑添加一个新方法。这样做除了可以解决明确赋值问题，还可以使程序的可读性提高。