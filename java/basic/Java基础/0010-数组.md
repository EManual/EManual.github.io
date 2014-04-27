数组是有序数据的集合，数组中的每个元素具有相同的数组名和下标来唯一地确定数组中的元素。
* 声明数组：   
数组能以下列形式声明：
类型[] array;
类型 array[];  
注：
JAVA中推荐用：类型[] array;
一个数组是一个对象
声明一个数组没有创建一个对象
声明时不用指定长度
* 创建数组：
创建基本数据类型数组：int[] i = new int[2]; 
创建引用数据类型数组：Student[] s = new Student[100]; 
数组创建后其中的元素有初始值
```java  
类型          	 	黙认值 
byte                  0 
short                 0 
int                   0 
long                  0l 
float                 0.0f 
double                0.0d 
char                  \u0000
boolean               false 
reference types    	  null
```
注：
创建时一定要指定长度
```java  
int[] i2=new int[];           	//error
```
* 初始化数组： 
声明、创建、初始化分开：
```java   
int[] i;   //定义数组
i = new int[2]; 	//分配空间
i[0] = 0;   	//初始化
i[1] = 1; 
```
声明、创建、初始化在同一时间：
```java  
int[] i = {0,1};  	//显示初始化  {}中有几个值,则数组长度为几
Student[] s = {new Student(),new Student()}; 
```
注：
```java  	
int[] i=new int[]{1,2,3};     	//后面[]中不可以写数值
int[] i1=new int[3]{1,2,3};   	//error
```			 
* 二维数组：(其实是一个一维数组，它的每一个元素又是一个一维数组)
```java  
int[][] i1 = new int[2][3]; 
int[][] i4 = {{1,1,1},{2,2,2},{3,3,3}};
int[][] i3 = new int[][3];		//不允许高维没分配空间而先给低维分配空间
int[][] i2 = new int[2][]; 
i2[0] = new int[2];
i2[1] = new int[3];     
```
数组长度：
数组的属性length
数组长度一旦确定,不可改变   
```java    
int[] i = new int[5]; 则i.length= 5
```
* 数组拷贝：
系统类System提供的：
```java  
static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length) 
src： 源数组		
srcPos： 从源数组哪个位置开始拷贝(位置指的是元素的下标)
dest： 目标数组
destPos： 拷贝的元素放到目标数组的起始位置
length： 拷贝多少个
```		
* 数组排序：
自己实现一个排序方法来进行排序。
或者调用java.util.Arrays.sort(Object o)。