答：首先要了解中文字符有多种编码及各种编码的特征。
假设n为要截取的字节数。
[code=java]
public static void main(String[] args) throws Exception{
	String str = "我a爱中华abc我爱中国def";
	String str = "我ABC汉";
	int num = trimGBK(str.getBytes("GBK"),5);
	System.out.println(str.substring(0,num) );
}

public static int  trimGBK(byte[] buf,int n){
	int num = 0;
	boolean bChineseFirstHalf = false;
	for(int i=0;i<n;i++){
		if(buf[i]<0 && !bChineseFirstHalf){
			bChineseFirstHalf = true;
		}else{
			num++;
			bChineseFirstHalf = false;				
		}
	}
	return num;
}
[/code]