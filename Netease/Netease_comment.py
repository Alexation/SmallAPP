import requests
import parsel
import pprint
import json
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

headers = {
    'Referer': 'https://music.163.com/',
    'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
}
data = {
    'params': 'kfu/9ly4rmloqiHbxh9bUMEda4AY/2rNzENQDqS9uyErXhIUp74pCWaSfBCsqwKG89l8K4XcDCQpFZq37ZpbBg69NQh0Gk6EMVpZvGJOcROOiOQB2tsWoN2+72b2DiOwERW6fCC8M5DObzDqrpkM766d8y1LHJBY3QqVnIygB/JBTa883DMRWksjOMhJxT6WSShSp1BbA+wH0Dz/Pw4QEKvQ/Gr0pll+B7NOnNWIEaf6bT20s0ArPwxzz/gPmB4zfRl7zdOOif+dbqpTh2g5SkpAlNOD1y1Jcjy+1yD0DeM=',
    'encSecKey': '3008dcd3f038e57e0b0f7e35c1a0e2d6352a717380994c02ab72fac3119e26c9040afc6862424847ae7ede9e48140eadd5185a24bbcc008737fa3b99e37da7c330197805f9339f049ee75c43bcb3ba325f444f7c8106dce948a9502165275ed03d1b4689aaddeb9e6c9152e6ea7e593e5fce9cec21cd0581997553c4178f2bd9',
}
html = requests.post(url=url, data=data, headers=headers).text
# print(type(html))
response_json = json.loads(html)
# pprint.pprint(response_json)
comment = response_json['data']['hotComments']
for i in comment:
    comment_content = i['content']
    print(comment_content)