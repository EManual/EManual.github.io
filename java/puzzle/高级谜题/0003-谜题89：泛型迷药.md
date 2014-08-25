和前一个谜题一样，本谜题也大量使用了泛型。我们从前面的错误中吸取教训，这次不再使用原生类型了。这个程序实现了一个简单的链表数据结构。main程序构建了一个包含2个元素的list，然后输出它的内容。那么，这个程序会打印出什么呢？ 
```java   
public class LinkedList<E> {
    private Node<E> head = null;

    private class Node<E> {
        E value;
        Node<E> next;

        // Node constructor links the node as a new head
        Node(E value) {
            this.value = value;
            this.next = head;
            head = this;
        }
    }

    public void add(E e) {
        new Node<E>(e);
        // Link node as new head
    }

    public void dump() {
        for (Node<E> n = head; n != null; n = n.next)
            System.out.println(n.value + " ");
    }

    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<String>();
        list.add("world");
        list.add("Hello");
        list.dump();
    }
}
```
又是一个看上去相当简单的程序。新元素被添加到链表的表头，而dump方法也是从表头开始打印list。因此，元素的打印顺序正好和它们被添加到链表中的顺序相反。在本例中，程序先添加了“world”然后添加了“Hello”，所以总体来看它似乎就是一个复杂化的Hello World程序。遗憾的是，如果你尝试着编译它，就会发现它不能通过编译。编译器的错误消息是令人完全无法理解的： 
```java   
LinkedList.java:11: incompatible types
found : LinkedList<E>.Node<E>
required: LinkedList<E>.Node<E>
              this.next = head;
                            ^
LinkedList.java:12: incompatible types
found : LinkedList<E>.Node<E>
required: LinkedList<E>.Node<E>
              head = this;
                      ^
```
编译器试图告诉我们，这个程序太过复杂了。一个泛型类的内部类可以访问到它的外围类的类型参数。而编程者的意图很明显，即一个Node的类型参数应该和它外围的LinkedList类的类型参数一样，所以Node完全不需要有自己的类型参数。要订正这个程序，只需要去掉内部类的类型参数即可： 
// 修复后的代码，可以继续修改得更好
```java   
public class LinkedList<E> {
    private Node head = null;

    private class Node {
        E value;
        Node next;

        //Node的构造器，将node链接到链表上作为新的表头
        Node(E value) {
            this.value = value;
            this.next = head;
            head = this;
        }
    }

    public void add(E e) {
        new Node(e);
        //将node链接到链表上作为新的表头
    }

    public void dump() {
        for (Node n = head; n != null; n = n.next)
            System.out.print(n.value + " ");
    }
}
```
以上是解决问题的最简单的修改方案，但不是最优的。最初的程序所使用的内部类并不是必需的。正如谜题80中提到的，你应该优先使用静态成员类而不是非静态成员类[EJ Item 18]。LinkedList.Node的一个实例不仅含有value和next域，还有一个隐藏的域，它包含了对外围的LinkedList实例的引用。虽然外部类的实例在构造阶段会被用来读取和修改head，但是一旦构造完成，它就变成了一个甩不掉的包袱。更糟的是，这样使得构造器中被置入了修改head的负作用，从而使程序变得难以读懂。应该只在一个类自己的方法中修改该类的实例域。 
因此，一个更好的修改方案是将最初的那个程序中对head的操作移到LinkedList.add方法中，这将会使Node成为一个静态嵌套类而不是真正的内部类。静态嵌套类不能访问它的外围类的类型参数，所以现在Node就必须有自己的类型参数了。修改后的程序既简单清楚又正确无误：
```java    
class LinkedList<E> {
    private Node<E> head = null;
    private static class Node<T> {
        T value; Node<T> next;
        Node(T value, Node<T> next) {
            this.value = value;
            this.next = next;
        }
    }
    public void add(E e) {
        head = new Node<E>(e, head);
    }
    public void dump() {
        for (Node<E> n = head; n != null; n = n.next)
            System.out.print(n.value + " ");
    }
} 
```
总之，泛型类的内部类可以访问到其外围类的类型参数，这可能会使得程序模糊难懂。本谜题所阐述的误解对于初学泛型的程序员来说是普遍存在的。在一个泛型类中设置一个内部类并不是必错的，但是很少用到这种情况，而且你应该考虑重构你的代码来避免这种情况。当你在一个泛型类中嵌套另一个泛型类时，最好为它们的类型参数设置不同的名字，即使那个嵌套类是静态的也应如此。对于语言设计者来说，或许应该考虑禁止类型参数的遮蔽机制，同样的，局部变量的遮蔽机制也应该被禁止。这样的规则就可以捕获到本谜题中的错误了。