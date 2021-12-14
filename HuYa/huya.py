import json
import requests  # 数据请求模块 第三方模块  pip install requests
import re  # 正则表达式模块 内置模块
from urllib.parse import quote
search = input('please input keywords: ')
search_url = quote(search, 'utf-8')
url = f'https://v.huya.com/search?w={search_url}&type=video&order=general&p=1'
headers = {
    'cookie': 'Hm_lvt_51700b6c722f5bb4cf39906a596ea41f=1637568838; Hm_lvt_9fb71726843792b1cba806176cecfe38=1637568894; udb_passdata=3; __yasmid=0.573359693711627; __yamid_tt1=0.573359693711627; __yamid_new=C99AF69FADD00001231D14EEA74B1E0E; _yasids=__rootsid%3DC99AF69FAE00000169BD12707827136B; hiido_ui=0.8102750609082412; amkit3-v-player-session-id=0.9647618175752399; amkit3-v-player-machine-id=0.5940354725937846; Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f=1637572123; Hm_lpvt_9fb71726843792b1cba806176cecfe38=1637572123; rep_cnt=321',
    'Referer': f'https://www.kuaishou.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
response = requests.get(url=url, headers=headers).text
if re.findall('<script> window.HNF_GLOBAL_INIT = (.*?) </script>', response) != '':
    response_text = re.findall('<script> window.HNF_GLOBAL_INIT = (.*?) </script>', response)[0]
    response_json = json.loads((response_text))
    response_data = response_json['searchResult']['videoInfoList']['value']
    list_data_all = []
    for i in response_data:
        title = i['videoTitle']
        vid = i['vid']
        list_data = [vid, title]
        list_data_all.append(list_data)
    for data in list_data_all:
        base_url = 'https://videotx-platform.cdn.huya.com/1048585/814817470/28502629/27a4bcf51ce57b7363dd3edd2d6bf96a.mp4'
        parmas = {
            'bitrate': '2069',
            'client': '106',
            'definition': '1300',
            'pid': '814817470',
            'scene': 'vod',
            'vid': data[0],
        }
        response = requests.get(url=base_url, headers=headers).content
        data[1] = re.sub(r'[/\:?"*<>|]', '', data[1])
        with open('video\\' + data[1] + '.mp4', mode='wb') as f:
            f.write(response)
        print(f'保存成功：{data[1]}')
else:
    print('got no data')
