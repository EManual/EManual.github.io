方法属性：
[code=java]
open(string method, string url, boolean asynch, string username, string password)：
[/code]
post还是get，url地址，同步还是异步 后面三个参数是可选的
[code=java]
void send(content)：
string getAllResponseHeaders()
void setRequestHeader(string header, string value)：这个方法为HTTP请求中一个给定的首部设置值。它有两个参数，第一个串表示要设置的首部，第二个串表示要在首部中放置的值。需要说明，这个方法必须在调用open()之后才能调用。
string getResponseHeader(string header)：
onreadystatechange ：每个状态改变时都会触发这个事件处理器，通常会调用一个JavaScript函数、回调函数
readyState：请求的状态。有5个可取值：0 = 未初始化，1 = 正在加载，2 = 已加载，3 = 交互中，4 = 完成
responseText：服务器的响应，表示为一个串
responseXML：服务器的响应，表示为XML。这个对象可以解析为一个DOM对象
statusText：HTTP状态码的相应文本（OK或Not Found（未找到）等等）
[/code]