Json 是一种线上协议，轻量级的xml 一种文体格式
Json的功能，简单的说，就是实现字符串和对象之间的转换。要使用其功能，在客户端，要引入
json.js文件，在服务器端，则要引入json.jar这个包。
Json对象和数组  {}大括号代表一个对象，，【】代表数组
(1) Json在客户端的应用实例：
[code=java]
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>JSON test</title>
<script type="text/javascript" src="js/json.js"></script>
<script type="text/javascript" src="js/utils.js"></script>
<script type="text/javascript">
	// 创建一个对象，注意格式  {}
	var product = {
		id: 1,  name: "core java",	price: 100		};
	// 创建一个对象字符串，注意格式
	var s = "{"id": 1, "name": "George", "age":30}";
	// 实现对象和字符串之间的互换 只须stringify和parse这两个方法即可
	function display(){
		// 将对象转换为字符串，发送给服务器处理
		byId("json").innerHTML = JSON.stringify(product);
		// 将字符串转换为对象，把服务端的字符串组装成对象
		var student = JSON.parse(s);
		alert(student.id + "\t" + student.name + "\t" + student.age); }
</script>
</head>
<body onload="display()"><h2>
	<div id="json"></div>
	</h2>
</body>
</html>
[/code]
(2) Json在客户端和服务器端同时应用：
1 客户端html文件：
[code=java]
<html><head>
<title>Query Price</title>
<script type="text/javascript" src="js/json.js"></script>
<script type="text/javascript" src="js/kettasAjax.js"></script>
<script type="text/javascript" src="js/utils.js"></script>
<script type="text/javascript">
	function query(){
		// obj4form是一个工具函数 根据表单id 将用户输入表单的数据封装为一个对象
		var car = obj4form("carInfo");
		// 直接向服务器发送对象字符串 
//"queryPrice"是访问servlet地址，JSON.stringify(car)发送对象字符串，display为服务器返回内容
		kettasAjax.postText("queryPrice", JSON.stringify(car), display);
	}
	function display(txt){
		// 将从服务器返回的对象字符串转换为对象
		var ret = JSON.parse(txt);
		var model = ret.model;
		var price = ret.price;
		$("result").innerHTML = model + " " + price
	}
</script>
</head>
<body>
	<h2>Please enter car information</h2>
	<!-- 利用输入的汽车id和生产厂商信息 得以查询汽车的价格 -->
	<form action=#" id="carInfo">
		Id: <input type="text" id="id"/><br/>
		Make: <input type="text" id="make"/><br/>
	</form>
	<button onclick="query()">Query Price</button>
	<div id="result"></div>
</body>
</html>
[/code]
2 Servlet文件QueryPriceServlet的片段：
[code=java] 
	protected void doPost(HttpServletRequest request, HttpServletResponse response) 
	throws ServletException, IOException {
	response.setContentType("text/plain");
	BufferedReader reader = request.getReader();//得到客户端的字符串
	PrintWriter out = response.getWriter();
	StringBuilder sb = new StringBuilder();
	String str = null;
	while((str = reader.readLine()) != null)
		sb.append(str);
	try {	// 将客户端发送的对象字符串转化为JSONObject对象
		JSONObject jsonObj = new JSONObject(sb.toString());
		// 获得对象中的数据 注意格式
		int id = jsonObj.getInt("id");
		String make = jsonObj.getString("make");
		// 不用make.equals("Audi") 避免了make == null的情况下抛异常 小技巧
		if(id == 1 && "Audi".equals(make)){
			// 给客户端回应一个对象字符串 注意格式// 首先创建一个新的JSONObject对象
			jsonObj = new JSONObject();
			// 向这个对象中填充数据
			jsonObj.put("model", "A8");
			jsonObj.put("price", 860000);
			// 将对象转化为对象字符串 回发给客户端
			// 这个对象字符串的格式为： "{"model"： "A8" , "price"： 860000}"
			out.print(jsonObj.toString());
		}
	} catch (Exception e) {
		e.printStackTrace();	throw new ServletException(e);
	}finally{	out.close();
	}}  
[/code]	
(3) 在服务器端将java中的实体bean、collections、array以及map对象转换为对象字符串：
要实现这个功能，可以借助内部工具类JsonUtil.java，其中的几个方法是很有用的，如：
[code=java] 
	public static JSONObject bean2Json(Object bean)，
	public static JSONObject map2Json(Map map)，
	public static JSONArray array2Jarr(Object value)，
	public static JSONArray collection2Json(Object value)
[/code]
测试类片段如下： 
[code=java] 			
public class TestJsonUtil {			
	public static void main(String[] args) {
		SuperStore ss = new SuperStore();
		// ss.getProducts()方法返回一个商品对象的集合
		JSONArray jarr = JsonUtil.collection2Json(ss.getProducts());
		System.out.println(jarr.toString());
	}			
}	
[/code]