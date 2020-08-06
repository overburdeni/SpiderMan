import re


#math()匹配方法 从字符串的开头匹配内容（适合用来检测某个字符串是否符合某个正则表达式的规则）

# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
# print(result)
# print(result.group())
# print(result.span())

#匹配目标

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld',content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

#通用匹配

# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())

#贪婪匹配 非贪婪匹配（中间匹配适用）

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*?Demo$',content)     #非贪婪匹配
# result = re.match('^He.*(\d+).*Demo$',content)           #贪婪匹配
# print(result)
# print(result.group(1))

#贪婪匹配（结尾匹配适用）

# content = 'http://weibo.com/comment/kEraCN'
# result1 = re.match('http.*?comment/(.*?)', content)
# result2 = re.match('http.*?comment/(.*)', content)
# print('result1', result1.group(1))
# print('result2', result2.group(1))

#修饰符re.S re.I

# content = '''Hello 1234567 World_This
#           is a Regex Demo'''
# result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
# print(result.group(1))

#转义匹配

# content = '(百度)www.baidu.com'
# result = re.match('\(百度\)www\.baidu\.com',content  )
# print(result)

#search()方法 扫描整个字符串 匹配时扫描整个字符串 返回第一个内容

# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)

html = '''<div id="songs-list">
<h2 class="title"> 经典老歌 </h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2"> 一路上有你 </li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐"> 沧海一声笑 </a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦"> 往事随风 </a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond"> 光辉岁月 </a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳"> 记事本 </a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君"> 但愿人长久 </a>
</li>
</ul>
</div>'''

# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#     print(result.group(1),result.group(2))

#findall() 搜索整个字符串 获取正则表达的所有内容

# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0],result[1],result[2])

#sub()方法 修改文本  第一个参数传入需求匹配 第二个参数为替换成的字符串（去除该参数则设置为空）

# content = '5sf7das6d5s5cvf2g1ge3'
# content = re.sub('\d+','',content)
# print(content)

#值提取歌名
# html = re.sub('<a.*?>|</a>','',html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>',html,re.S)
# for result in results:
#     print(result.strip())

#compile（）方法 将正则字符串编译成正则表达式对象

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)

