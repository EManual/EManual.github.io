1. kettasAjax.doGetText(url, textHandler, async):
用GET 方法发出请求到url, 返回的文本responseText 作为回调函数textHandler 的参数。
textHandler 的签名类似function(txt).
2. kettasAjax.doGetXml(url, xmlHandler, async):
用GET 方法发出请求到url, 返回的XML Document 也就是responseXML 作为回调函数
xmlHandler 的参数。xmlHandler 的签名类似function(doc).
3. kettasAjax.doPostText(url, textHandler, body, async):
用POST 方法将请求体body 发送到url, 返回的文本responseText 作为回调函数textHandler
的参数。textHandler 的签名类似function(txt).
4. kettasAjax.doPostXml(url, xmlHandler, body, async):
用POST 方法将请求体body 发送到url, 返回的XML Document 也就是responseXML 作为
回调函数xmlHandler 的参数。xmlHandler 的签名类似function(doc).