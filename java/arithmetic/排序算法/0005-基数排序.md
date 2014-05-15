使用10个辅助队列，假设最大数的数字位数为 x， 则一共做x次，从个位数开始往前，以第i位数字的大小为依据，将数据放进辅助队列，搞定之后回收。下次再以高一位开始的数字位为依据。
  
以Vector作辅助队列，基数排序的Java代码：
```java  
public class RadixSort {
     private int keyNum=-1;   
     private Vector<Vector<Double>> util;
    
     public void distribute(double [] sorted, int nth){       
         if(nth<=keyNum && nth>0){
              util=new Vector<Vector<Double>>();
              for(int j=0;j<10;j++){
                   Vector <Double> temp= new Vector <Double>();
                   util.add(temp);
              }            
              for(int j=0;j<sorted.length;j++){
                   int index= getNthDigit(sorted[j],nth);
                   util.get(index).add(sorted[j]);
              }
         }
     }   
     public int getNthDigit(double num,int nth){
         String nn= Integer.toString((int)num);
         int len= nn.length();
         if(len>=nth){
              return Character.getNumericValue(nn.charAt(len-nth)); 
         }else{
              return 0;
         }            
     }
     public void collect(double [] sorted){
         int k=0;
         for(int j=0;j<10;j++){
              int len= util.get(j).size();
              if(len>0){
                   for(int i=0;i<len;i++){
                       sorted[k++]= util.get(j).get(i);
                   }
              }
         }
         util=null;
     }
     public int getKeyNum(double [] sorted){    
         double max= Double.MIN_VALUE;
         for(int j=0;j<sorted.length;j++){
              if(sorted[j]>max){
                   max= sorted[j];
              }
         }       
         return Integer.toString((int)max).length();
     }
     public void radixSort(double [] sorted){
         if(keyNum==-1){            
              keyNum= getKeyNum(sorted);
         }
         for(int i=1;i<=keyNum;i++){
              distribute(sorted,i);
              collect(sorted);           
         }
     }
     public static void main(String[] args) {
         Random random = new Random(6);
 
         int arraysize = 21;
         double[] sorted = new double[arraysize];
         System.out.print("Before Sort:");
         for (int j = 0; j < arraysize; j++) {
              sorted[j] = (int) (random.nextDouble() * 100);
              System.out.print((int) sorted[j] + " ");
         }
         System.out.println();
 
         RadixSort sorter = new RadixSort();
         sorter.radixSort(sorted);
         System.out.print("After Sort:");
         for (int j = 0; j < sorted.length; j++) {
              System.out.print((int) sorted[j] + " ");
         }
         System.out.println();
     }
}
```