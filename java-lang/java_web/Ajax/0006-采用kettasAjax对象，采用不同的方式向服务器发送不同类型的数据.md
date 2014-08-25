(1) html文件如下：
[code=java] 
<title>Send Request Parameters</title>
<script type="text/javascript" src="js/utils.js"></script>
<script type="text/javascript" src="js/kettasAjax.js"></script>
<script type="text/javascript">
	function handleForm(httpMethod){
		if(httpMethod == "GET"){
			// 采用GET方式向服务器发送表单数据
			kettasAjax.getText("echo.jsp?" + getQueryString(), display);
		}else{
			// 采用POST方式向服务器发送表单数据
			kettasAjax.postText("echo.jsp", getQueryString(), display);
		}}
	// 显示服务器返回的数据
	function display(txt){
		$("response").innerHTML = txt;
	}
	// 获得表单数据的字符串组织形式
	function getQueryString(){
		var name = escape(getEavById("name"));
		var age = escape(getEavById("age"));
		var password = escape(getEavById("password"));
		var queryStr = "name=" + name +"&age=" + age + "&password=" + password;
		return queryStr;
	}
	// 采用POST方式向服务器发送xml数据
	// 由于发送的是xml形式字符串 故服务端不能以getParameter的方式读取 要以readLine方式读取
	function handleXmlForm(){
		kettasAjax.postText("handleXml", getXmlFromForm(), display);
	}
	// 获得表单数据的xml字符串表现形式
	function getXmlFromForm(){
		var name = getEavById("name");
		var age = getEavById("age");
		var password = getEavById("password");
		var xmlStr = "<params>" 
		+ "<name>" + name + "</name>"
		+ "<age>" + age + "</age>"
		+ "<password>" + password + "</password>"
		+ "</params>"
		return xmlStr;
	}
</script>
</head>
<body>
	<form action="#">
	 Name: <input type="text" id="name"/><br/>
	 Age: <input type="text" id="age"/><br/>
	 Password: <input type="password" id="password"/><br/>
	</form>
	<button onclick="handleForm("GET")">Get</button>
	<button onclick="handleForm("POST")">Post</button>
	<button onclick="handleXmlForm()">Send Parameters as XML</button><br/>
	<div id="response"></div>
</body>
</html>
[/code]
(2) echo.jsp内容如下：
[code=java] 
Http method: ${pageContext.request.method}, and parameters
are name: ${param.name}, age: ${param.age}, password: ${param.password} 
[/code]
(3) Servlet文件HandleXmlServlet片段如下：
[code=java] 
protected void doPost(HttpServletRequest request,
		HttpServletResponse response) throws ServletException, IOException {
	response.setContentType("text/plain");
	StringBuilder sb = new StringBuilder();
	// 由于客户端发送的是xml形式的字符串 故要获得BufferedReader对象用于读取
	BufferedReader reader = request.getReader();
	PrintWriter out = response.getWriter();
	String line = null;
	// 可能客户端是采用多行发送的 故不能只读取一行了事
	while ((line = reader.readLine()) != null)
		sb.append(line);
	// 解析xml数据
	DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
	try {
		DocumentBuilder db = dbf.newDocumentBuilder();
		// 由于不存在.xml文件 故只能以内存字节流的方式初始化
		Document doc = db.parse(
			new ByteArrayInputStream(sb.toString().getBytes())
		);
		String name = getElementData(doc, "name");
		String age = getElementData(doc, "age");
		String password = getElementData(doc, "password");
		out.print("Parameters are name: " + name 
		 + " age: " + age
		 + " password: " + password
		);
	} catch (Exception e) {
		e.printStackTrace();
		out.print("error");
	}
	out.close();
}
[/code]