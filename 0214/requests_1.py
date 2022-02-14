# -*- coding: UTF-8 -*-
import requests
import re

pattern = re.compile(r'<a.*?href="(.*?)".?title="(.*?)".*?>')
res = requests.get('https://www.sohu.com')
if res.status_code == 200:
    print(res.text)
    print("#######"*100)
    all_match = pattern.findall(res.text)
    for href, title in all_match:
        print(title, "  ===> ", href)