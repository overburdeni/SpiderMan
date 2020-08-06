from lxml import etree

#etree会自动修正html文本
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

#文本导入读取

# html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

#匹配所有节点
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
# print(result)

#匹配指定节点
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li')
# print(result)
# print(result[0])

#匹配子节点(/)子孙节点（//） /用于选取直接子节点 //获取所有子孙节点
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li//a')
# print(result)

#匹配父节点
# html = etree.parse('./test.html', etree.HTMLParser())
# # result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)

#属性匹配
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)

#文本属性
# html = etree.parse('./test.html',etree.HTMLParser())
# #先选取a节点再获取文本
# # result = html.xpath('//li[@class="item-0"]/a/text()')
# #用//
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)

#属性获取
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)

#属性多值匹配
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)

#多属性匹配
text = '''  
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

