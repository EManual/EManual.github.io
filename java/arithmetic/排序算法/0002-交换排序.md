包括冒泡排序，快速排序。
* 冒泡排序法：
该算法是专门针对已部分排序的数据进行排序的一种排序算法。如果在你的数据清单中只有一两个数据是乱序的话，用这种算法就是最快的排序算法。如果你的数据清单中的数据是随机排列的，那么这种方法就成了最慢的算法了。因此在使用这种算法之前一定要慎重。这种算法的核心思想是扫描数据清单，寻找出现乱序的两个相邻的项目。当找到这两个项目后，交换项目的位置然后继续扫描。重复上面的操作直到所有的项目都按顺序排好。
  
* 快速排序：
通过一趟排序，将待排序记录分割成独立的两个部分，其中一部分记录的关键字均比另一部分记录的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。具体做法是：使用两个指针low,high, 初值分别设置为序列的头，和序列的尾，设置pivotkey为第一个记录，首先从high开始向前搜索第一个小于pivotkey的记录和pivotkey所在位置进行交换，然后从low开始向后搜索第一个大于pivotkey的记录和此时pivotkey所在位置进行交换，重复知道low=high了为止。
  
冒泡排序Java代码：
```java  
public class bubbleSort {  
	public  bubbleSort(){  
		int a[]={49,38,65,97,76,13,27,49,78,34,12,64,5,4,62,99,98,54,56,17,18,23,34,15,35,25,53,51};  
		int temp=0;  
		for(int i=0;i<a.length-1;i++){  
			for(int j=0;j<a.length-1-i;j++){  
				if(a[j]>a[j+1]){  
					temp=a[j];  
					a[j]=a[j+1];  
					a[j+1]=temp;  
				}  
			}  
		}  
		for(int i=0;i<a.length;i++)  
			System.out.println(a[i]);     
	}  
} 
```
快速排序Java代码：
```java  
public class quickSort {  
	int a[]={49,38,65,97,76,13,27,49,78,34,12,64,5,4,62,99,98,54,56,17,18,23,34,15,35,25,53,51};  
	public  quickSort(){  
		quick(a);  
		for(int i=0;i<a.length;i++)  
			System.out.println(a[i]);  
	}  
	public int getMiddle(int[] list, int low, int high) {     
		int tmp = list[low];    //数组的第一个作为中轴     
		while (low < high) {     
			while (low < high && list[high] >= tmp) {     
				high--;     
			}     
			list[low] = list[high];   //比中轴小的记录移到低端     
			while (low < high && list[low] <= tmp) {     
				low++;     
			}     
			list[high] = list[low];   //比中轴大的记录移到高端     
		}     
		list[low] = tmp;              //中轴记录到尾     
		return low;                   //返回中轴的位置     
		}    
	public void _quickSort(int[] list, int low, int high) {     
		if (low < high) {     
		   int middle = getMiddle(list, low, high);  //将list数组进行一分为二     
			_quickSort(list, low, middle - 1);        //对低字表进行递归排序     
		   _quickSort(list, middle + 1, high);       //对高字表进行递归排序     
		}     
	}   
	public void quick(int[] a2) {     
		if (a2.length > 0) {    //查看数组是否为空     
			_quickSort(a2, 0, a2.length - 1);     
		}     
   }   
}  
```