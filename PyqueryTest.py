# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
#字符串初始化
from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))
#URL初始化
# doc = pq(url='http://cuiqingcai.com')
# print(doc('title'))
#相同效果
# import requests
# doc = pq(requests.get('http://cuiqingcai.com').text)
# print(doc('title'))

#文件初始化
# doc = pq(filename='test.html')
# print(doc('li'))


#基本CSS选择器
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

#查找节点   子节点
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')     # find 的查找范围是节点的所有子孙节点
# lis = items.children()     #只想查找子节点，那可以用 children 方法
# lis = items.children('.active')       #筛选出子节点中 class 为 active 的节点，可以向 children() 方法传入 CSS 选择器.active
# print(type(lis))
# print(lis)

#父节点
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
# items = doc('.list')
# container = items.parent()    #直接父节点
# print(type(container))
# print(container)
# parents = items.parents()        #祖先节点
# parents = items.parents('.wrap')   #筛选某个祖先节点的话，可以向 parents 方法传入 CSS 选择器，这样就会返回祖先节点中符合 CSS 选择器的节点
# print(type(parents))
# print(parents)

#兄弟节点  siblings() 方法
li = doc('.list .item-0.active')
# print(li.siblings())
#筛选某个兄弟节点，我们依然可以向 siblings 方法传入 CSS 选择器，这样就会从所有兄弟节点中挑选出符合条件的节点
print(li.siblings('.active'))