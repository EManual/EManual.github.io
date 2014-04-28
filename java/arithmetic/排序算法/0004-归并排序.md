将两个或两个以上的有序表组合成一个新的有序表。归并排序要使用一个辅助数组，大小跟原数组相同，递归做法。每次将目标序列分解成两个序列，分别排序两个子序列之后，再将两个排序好的子序列merge到一起。
  
```java  
归并排序Java代码：
public class MergeSort { 
     private double[] bridge;//辅助数组
     public void sort(double[] obj){
         if (obj == null){
              throw new NullPointerException("The param can not be null!");
         }
         bridge = new double[obj.length]; // 初始化中间数组
         mergeSort(obj, 0, obj.length - 1); // 归并排序
         bridge = null;
     }
     private void mergeSort(double[] obj, int left, int right){
         if (left < right){
              int center = (left + right) / 2;
              mergeSort(obj, left, center);
              mergeSort(obj, center + 1, right);
              merge(obj, left, center, right);
         }
     }
     private void merge(double[] obj, int left,int center, int right){
         int mid = center + 1;
         int third = left;
         int tmp = left;
         while (left <= center && mid <= right){
			  // 从两个数组中取出小的放入中间数组
              if (obj[left]-obj[mid]<=10e-6){
                   bridge[third++] = obj[left++];
              } else{
                   bridge[third++] = obj[mid++];
              }
         }
 
         // 剩余部分依次置入中间数组
         while (mid <= right){
              bridge[third++] = obj[mid++];
         }
         while (left <= center){
              bridge[third++] = obj[left++];
         }
         // 将中间数组的内容拷贝回原数组
         copy(obj, tmp, right);
     }
     private void copy(double[] obj, int left, int right)
     {
         while (left <= right){
              obj[left] = bridge[left];
              left++;
         }
     }
     public static void main(String[] args) {
         Random random = new Random(6);
 
         int arraysize = 10;
         double[] sorted = new double[arraysize];
         System.out.print("Before Sort:");
         for (int j = 0; j < arraysize; j++) {
              sorted[j] = (int) (random.nextDouble() * 100);
              System.out.print((int) sorted[j] + " ");
         }
         System.out.println();
 
         MergeSort sorter = new MergeSort();
         sorter.sort(sorted);
        
         System.out.print("After Sort:");
         for (int j = 0; j < sorted.length; j++) {
              System.out.print((int) sorted[j] + " ");
         }
         System.out.println();
     }
}
```