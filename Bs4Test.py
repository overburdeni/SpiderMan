html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)

#节点选择器(只选择第一个)
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)

#提取信息
# print(soup.title.name)     #name属性获取节点名称
# print(soup.p.attrs)
# print(soup.p.attrs['name'])       #atters获取所有属性 也可不要attera直接[]
# print(soup.p.string)      #获取内容

#嵌套选择
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

#关联选择
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.contents)    #获取直接子节点contents属性
# print(soup.p.children)     #childern与contents效果一样
# for i,child in enumerate(soup.p.children):
#     print(i,child)
# print(soup.p.descendants)         #子孙节点
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)

#css选择器
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0]))
#嵌套选择
# for ul in soup.select('ul'):
#     print(ul.select('li'))

#获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

#获取文本
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)