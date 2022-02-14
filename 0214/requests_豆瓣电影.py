# -*- coding: UTF-8 -*-
import random
import re
import time

import requests

for page  in range(1,11):
# 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出不是浏览器而阻止我们的请求。
# 通过get函数的headers参数设置User-Agent的值，具体的值可以在浏览器的开发者工具查看到。
# 用爬虫访问大部分网站时，将爬虫伪装成来自浏览器的请求都是非常重要的一步。
    res = requests.get(url=f'https://movie.douban.com/top250?start={(page-1)*25}',
                       headers={
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
                       }
                       )
    # 通过正则表达式获取class属性为title且标签体不以&开头的span标签并用捕获组提取标签内容
    pa1 = re.compile(r'<span class="title">([^&]*?)</span>')
    title = pa1.findall(res.text)
    # 通过正则表达式获取class属性为rating_num的span标签并用捕获组提取标签内容
    pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    ranks = pattern2.findall(res.text)
    for title, pf in zip(title, ranks):
        print(title, '===>',pf)
    time.sleep(random.random()*4+1)
    # print(res.text)