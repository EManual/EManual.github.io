动态INCLUDE用jsp:include动作实现 
<jsp:include page=included.jsp flush=true />它总是会检查所含文件中的变化，适合用于包含动态页面，并且可以带参数 静态INCLUDE用include伪码实现,定不会检查所含文件的变化，适用于包含静态页面 <%@ include file=included.htm %> 