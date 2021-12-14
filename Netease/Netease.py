import requests
import re

url = 'https://music.163.com/discover/toplist'
outer = 'https://music.163.com/song/media/outer/url?id='
ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) '
      'Gecko/20100101 Firefox/91.0')
headers = {'User-Agent': ua}
response = requests.get(url=url, headers=headers).text

zip_data = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>', response)
for music_id, title in zip_data:
    url_1 = outer + music_id
    music_data = requests.get(url=url_1, headers=headers).content
    title = re.sub(r'[/\\:*?"<>|]', '_', title)
    with open('music_netease\\' + title + '.mp3', mode='wb') as f:
        f.write(music_data)
    print(f'正在保存：{title}')
