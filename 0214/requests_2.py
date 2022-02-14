# -*- coding: UTF-8 -*-
import requests
res = requests.get('https://www.baidu.com/img/PC_880906d2a4ad95f5fafb2e540c5cdad7.png')
if res.status_code == 200:
    with open('baidu.png', 'wb') as f:
        f.write(res.content)
