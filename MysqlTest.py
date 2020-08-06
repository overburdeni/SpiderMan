import pymysql

#连接数据库 创建spider数据库
# db = pymysql.connect(host='localhost',user='root', password='ybr080414', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

#创建student表
# db = pymysql.connect(host='localhost', user='root', password='ybr080414', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

#插入数据
# id = '1804310330'
# user = 'luying'
# age = 20
# db = pymysql.connect(host='localhost', user='root', password='ybr080414', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id, name, age) values(% s, % s, % s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()


#动态插入方法  字典动态构造，元组也动态构造
# data = {
#     'id': '1804310317',
#     'name': 'yangborui',
#     'age': 23
# }
# db = pymysql.connect(host='localhost', user='root', password='ybr080414', port=3306, db='spiders')
# cursor = db.cursor()
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['% s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
#    if cursor.execute(sql, tuple(data.values())):
#        print('Successful')
#        db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#更新数据
# db = pymysql.connect(host='localhost', user='root', password='ybr080414', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'UPDATE students SET age = % s WHERE name = % s'
# try:
#    cursor.execute(sql, (25, 'luying'))
#    db.commit()
# except:
#    db.rollback()
# db.close()

#更新数据 重复的覆盖 没有加入
# data = {
#     'id': '20120001',
#     'name': 'Bob',
#     'age': 21
# }
# db = pymysql.connect(host='localhost', user='root', password='ybr080414', port=3306, db='spiders')
# cursor = db.cursor()
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['% s'] * len(data))
#
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
# update = ','.join(["{key} = % s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()
#查询
sql = 'SELECT * FROM students WHERE age >= 20'
db = pymysql.connect(host='localhost', user='root', password='ybr080414', port=3306, db='spiders')
cursor = db.cursor()
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')