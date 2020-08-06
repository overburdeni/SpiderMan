import os
from hashlib import md5
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json
import re
from selenium import webdriver

import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_index(offset, keyword):
    para = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': '1593665684775',
        '_signature': '7' +
                      'yD7.AAgEBApd0Jxcjcfwe8huuAALHovmaBcff719uWpg6PhnCCgTgbuUckg1kLI3dQFdQZ1b3VwbtvV9P3ZaGHpjzTDdgJm.hxt6TELcPiJAsAOBYizC - 15.PpPHKolFtN'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'cookie': 'tt_webid=6844895200352765453; ttcid=147baf1d0de44bcfaa3aaccb43de319231; csrftoken=e72569f7c754e03b930bbb54f34b7759; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6845096485504583176; s_v_web_id=verify_kc5ojvq4_iZKfsEzB_AubR_44PZ_AgkE_hvFA5OJnJ4nc; SLARDAR_WEB_ID=ba4439ab-f467-42a9-9dcd-8be836757cc3; __tasessionId=mbg1eigaz1593748245904; tt_webid=6845096485504583176; __ac_nonce=05efeab2d00f5555e228f; __ac_signature=_02B4Z6wo00f01JctsQwAAIBDjnNXOcxFq8yXKbWAAHs9kTU3N2TXnkkV75OXvSXoT5pfhWopyS8N2zbrE1VOQlMWB8pFBr0ZvUmL9qtI0GvgW6d9cv9TeAEXgf1HZ3bDCooMMUBc9Rq-r53241; tt_scid=8TNWiPBmsnVRkGGZJ5frIVGKsH4gMngyY0s4KQWdyckfgNuI45yMdiqvIa1sudDF15e8'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(para)  # urlencode可以吧字典类型转化为url中的请求参数
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('索引页请求成功')
            response.encoding = 'UTF-8'
            return response.text
        return None
    except RequestException:
        print('索引页请求失败')
        return None

def parse_index_json(html):
    data = json.loads(html)  # 解析为json对象
    if data and 'data' in data.keys():
        for item in data.get('data'):  # 遍历data这个json数据
            if item and 'abstract' in item.keys():
                yield (item.get('article_url'), item.get('display').get('title').get('text'))

def get_detail(url):
    driver = webdriver.Chrome()  # 声明浏览器驱动对象
    try:
        driver.get(url)
        html = driver.page_source
        driver.close()
        return html
    except RequestException:
        print('详情页请求失败')
        return None

def parse_detail(html):
    result = re.findall('JSON.parse\("(.*?)"\),', html, re.S)
    if result:
        data = result[0].encode('utf-8').decode('unicode-escape')  # 去掉\\\u002F，先用utf-8编码再用unicode-escape解码
        data = json.loads(data)
        if data and 'sub_images' in data.keys():  # 过滤掉不能爬的
            sub_images = data.get('sub_images')
            image_url = [item.get('url') for item in sub_images]
            return image_url

def save_to_mongo(result):
    if db[MONGO_TABLE].insert_one(result):
        print('存储到MongoDB成功', result)
        return True
    else:
        return False

def download_image(img_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Connection': 'keep - alive',
    }
    try:
        response = requests.get(img_url, headers=headers)
        if response.status_code == 200:
            save_image(response.content)  # 返回二进制内容，返回图片一般返回二进制内容
        return None
    except RequestException:
        print('图片请求失败')
        return None

def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd() + '\\toutiaojiepai', md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

def main():
    index_html = get_index(0, '美女')
    # print(index_html)  #index_html是一个字符串，json格式
    for url, title in parse_index_json(index_html):
        if url and title:
            detail_html = get_detail(url)
            img_url = parse_detail(detail_html)
            result = {
                'url': url,
                'title': title,
                'image_url': img_url
            }
            save_to_mongo(result)
            if img_url:
                for j in img_url:
                    download_image(j)

if __name__ == '__main__':
    main()