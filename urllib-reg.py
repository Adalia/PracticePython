#coding=utf-8
#http://python.jobbole.com/77825/
'''
下面说说Python3x中的urllib包、http包以及其他比较好使的第三方包
1、Python3 urllib、http
Python3不像2x中酷虎的和服务器模块结构散乱，Python3中把这些打包成为了2个包，就是http与urllib，详解如下：
http会处理所有客户端--服务器http请求的具体细节，其中：
（1）client会处理客户端的部分
（2）server会协助你编写Python web服务器程序
（3）cookies和cookiejar会处理cookie，cookie可以在请求中存储数据
使用cookiejar示例可以在前几篇博客中基于Python3的爬虫中找到示例，如下：
'''

# 示例
import http.cookiejar
import urllib.request
import urllib.parse

def getOpenner(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    openner = urllib.request.build_openner(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    openner.addheaders = header
    return openner

'''
urllib是基于http的高层库，它有以下三个主要功能：
（1）request处理客户端的请求
（2）response处理服务端的响应
（3）parse会解析url
'''

# 示例1-最简单
import urllib.request
response = urllib.request.urlopen('http://python.org')
html = response.read()

# 示例2-使用Request
import urllib.request
req = urllib.request.Request("http://www.baidu.com")
response = urllib.request.opener(req)
html = response.read()

# 示例3-发送数据
import urllib。parse
import urllib.request
url = ''
values = {
    'act':'login',
    'login[email]':'',
    'login[password]':''

}
data = urllib.request.urlencode(values)
req = urllib.request.Request(url, data)
req.add_header(('Referer','http://www.baidu.com'))
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page.decode("utf8"))

# 示例4-发送数据和header
import urllib.parse
import urllib.request
url = ''
user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5; Windows NT'
values = {
'act' : 'login',
'login[email]' : '',
'login[password]' : ''
}
headers = { 'User-Agent' : user_agent }
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page.decode("utf8"))


# 示例6-异常处理1
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
req = Request("http://www..net /")
try:
    response = urlopen(req)

    except HTTPError as e:
        print("The server couldn't fulfill the request.")
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
       print("good!")
       print(response.read().decode("utf8"))



# 示例8-HTTP 认证
import urllib.request
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = ""
password_mgr.add_password(None, top_level_url, 'rekfan', 'xxxxxx')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)
# use the opener to fetch a URL
a_url = ""
x = opener.open(a_url)
print(x.read())
# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)
a = urllib.request.urlopen(a_url).read().decode('utf8')
print(a)


# 示例9-使用代理
import urllib.request
proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
a = urllib.request.urlopen("").read().decode("utf8")
print(a)


#示例10-超时
import socket
import urllib.request
# timeout in seconds
timeout = 2
socket.setdefaulttimeout(timeout)
# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module
req = urllib.request.Request('')
a = urllib.request.urlopen(req).read()
print(a)


'''
请求消息格式如下所示：
请求行
通用信息头|请求头|实体头
CRLF(回车换行)
实体内容
其中“请求行”为：请求行 = 方法 [空格] 请求URI [空格] 版本号 [回车换行]
请求行实例：
GET /index.html HTTP/1.1
       Eg2：
POST http://192.168.2.217:8080/index.jsp HTTP/1.1
HTTP请求消息实例：
GET /hello.htm HTTP/1.1
Accept: */*
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate
If-Modified-Since: Wed, 17 Oct 2007 02:15:55 GMT
If-None-Match: W/"158-1192587355000"
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)
Host: 192.168.2.162:8080
Connection: Keep-Alive
'''