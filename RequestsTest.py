import requests
import logging
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
from requests import Request,Session
#抓取图标

# r = requests.get("https://github.com/favicon.ico")
#
# with open('favicon.ico','wb') as f:
#     f.write(r.content)

#高级用法 文件上传

# files = {'file':open('favicon.ico','rb')}
# r = requests.post("http://httpbin.org/post",files=files)
# print(r.text)

#cookies维持状态

# cookies = '_zap=cec27e3b-e82c-4d33-b2ee-b446e865712b; _xsrf=h65z2wduvqdsOWNdNU4Rlyys6N9N7Bdq; d_c0="AADtnhUvog-PTkPsGg0f32Qt2NXzVQi9tf0=|1561362016"; q_c1=97a09ff461724a60b64168319c8e85f7|1593078702000|1561362063000; __gads=ID=99194d956646b9be:T=1561362143:S=ALNI_Ma5V8Z3fhJz2eO6vYrWzx-w-9H5rg; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1595319936,1595401320,1595907652,1596370409; _ga=GA1.2.1472989419.1582683338; z_c0="2|1:0|10:1583468992|4:z_c0|92:Mi4xUHJSb0RBQUFBQUFBQU8yZUZTLWlEeVlBQUFCZ0FsVk53QjlQWHdER3VMMmFzY0M5Z1dIc01RdTZRTFRKb3ZlMTBB|bf8a8b1b1f72af218dc1251db573a68c4ea4fade26935a9f664ef1b5615de44e"; tst=r; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1596377237|1596376932; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1596377118; _gid=GA1.2.1811935220.1596370410; SESSIONID=VTznscRaCdfWoyg2qpKFgX5aY7nUFbXsdur90sEbSGI; JOID=UFkcAk3RwJeZytd8SNK3Q1KTp_hShJzl8L23JiGWp_nGoqoYcr1tvsXN3HxHjBg7huhHW5-8PDAMZHII-H3G3ps=; osd=W1kUCkzawJ-Ry9x8QNq2SFKbr_lZhJTt8ba3LimXrPnOqqsTcrVlv87N1HRGhxgzjulMW5e0PTsMbHoJ833O1po=; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1596370418; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1596377126; {0232aa83-6f15-4b2c-b8e2-596f662c6dba}=value'
#
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
# }
# for cookie in cookies.split(';'):
#     key,value = cookie.split('=',1)
#     jar.set(key,value)
#
# r = requests.get("http://www.zhihu.com",cookies=jar,headers=headers)
# print(r.text)

#会话维持

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/1678458207')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

#SSL证书验证 12306

# logging.captureWarnings(True)   #方法一直接logging直接忽略警告
# r = requests.get('https://12306.cn',cert=('/path/server.crt','/path/key'))     #方法二直接指定证书
# r = requests.get('https://12306.cn',verify=False)
# print(r.status_code)

#身份认证+超时设置

# r = requests.get('https://mail.qq.com/',auth=HTTPBasicAuth('1678458207','nmsl201911'),timeout=1)
# print(r.status_code)

#设置代理

# proxies = {
#     'http':'http://user:password@host:port',
#     'http':'socks5://user:password@host:port'
# }
# requests.get('https://www.taobao.com',proxies=proxies)

# prepared request

url = 'http://httpbin.org/post'
data = {
    'name':'yangborui'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)