Object类的方法有：
* hashCode()：
返回该对象的哈希码值
hashCode 的常规协定是： 
在 Java 应用程序执行期间，在同一对象上多次调用 hashCode 方法时，必须一致地返回相同的整数，前提是对象上 equals 比较中所用的信息没有被修改。
如果根据 equals(Object) 方法，两个对象是相等的，那么在两个对象中的每个对象上调用 hashCode 方法都必须生成相同的整数结果。 
* toString()：
返回该对象的字符串表示。
通常，toString 方法会返回一个“以文本方式表示”此对象的字符串。结果应是一个简明但易于读懂。建议所有子类都重写此方法。
* equals()：
指示某个其他对象是否与此对象“相等”。 
equals 方法在非空对象引用上实现相等关系： 
自反性：对于任何非空引用值 x，x.equals(x) 都应返回 true。 
对称性：对于任何非空引用值 x 和 y，当且仅当 y.equals(x) 返回 true 时，x.equals(y) 才应返回 true。 
传递性：对于任何非空引用值 x、y 和 z，如果 x.equals(y) 返回 true，并且 y.equals(z) 返回 true，那么 x.equals(z) 应返回 true。 
一致性：对于任何非空引用值 x 和 y，多次调用 x.equals(y)始终返回 true 或始终返回 false，前提是对象上 equals 比较中所用的信息没有被修改。对于任何非空引用值 x，x.equals(null) 都应返回 false。 
* 注意：
当此方法被重写时，通常有必要重写 hashCode 方法，以维护 hashCode 方法的常规协定，该协定声明相等对象必须具有相等的哈希码。