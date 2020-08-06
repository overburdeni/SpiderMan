#TXT文本存储
# import requests
# from pyquery import PyQuery as pq
#
# url = 'https://www.zhihu.com/explore'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# html = requests.get(url, headers=headers).text
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()
# for item in items:
#     question = item.find('h2').text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
#     # file = open('explore.txt', 'a', encoding='utf-8')
#     # file.write('\n'.join([question, author, answer]))  # 返回通过指定字符连接序列中元素后生成的新字符串
#     # file.write('\n' + '=' * 50 + '\n')
#     # file.close()
#     with open("explore.txt", 'a', encoding='utf-8') as f:  # 保存
#         f.write('\n'.join([question, author, answer]))
#         f.write('\n' + '=' * 50 + '\n')
#
#
#JSON文件存储
import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
# print(type(str))
# #loads 方法将字符串转为 JSON 对象。由于最外层是中括号，所以最终的类型是列表类型。
# data = json.loads(str)
# print(data)
# print(type(data))
# # 直接索引  通过中括号加 0 索引，可以得到第一个字典元素，然后再调用其键名即可得到相应的键值。
# data[0]['name']
# data[0].get('name')
# #推荐使用 get 方法，这样如果键名不存在，则不会报错，会返回 None。另外，get 方法还可以传入第二个参数
# data[0].get('age')
# data[0].get('age', 25)

# with open('data.json','r')as file:
#     str = file.read()
#     data = json.loads(str)
#     print(data)

# data = [{
#     'name': 'luying',
#     'gender': 'female',
#     'birthday': '1996-1-23'
# }]
# with open('data.json','w')as file:
#     file.write(json.dumps(data,indent=2))

# data = [{
#     'name': '芦颖',
#     'gender': '女',
#     'birthday': '1996-1-23'
# }]
# with open('data.json','w',encoding='utf-8')as file:
#     file.write(json.dumps(data,indent=2,ensure_ascii=False))

#CSV文件存储
import csv
# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 21])

#修改列与列之间的分隔符，可以传入 delimiter 参数
# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 21])

#调用 writerows 方法同时写入多行，此时参数就需要为二维列表
# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])

# #调用 writerows 方法同时写入多行，此时参数就需要为二维列表
# with open('data.csv', 'w') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
# #追加内容
# with open('data.csv', 'a') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})
# #字符编码问题
# with open('data.csv','a',encoding='utf-8') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '10005', 'name': '芦颖', 'age': 23})

#读取
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
import pandas as pd
df = pd.read_csv('data.csv')
print(df)