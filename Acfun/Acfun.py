import requests
import re
import os
from tqdm import tqdm
url = 'https://www.acfun.cn/v/ac31525983'

ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) '
      'Gecko/20100101 Firefox/91.0')
headers = {
    'User-Agent': ua,
}
response = requests.get(url, headers=headers)
#print(response.text)
title = re.findall('<title >(.*?)</title>', response.text)[0]
m3u8_url = re.findall('backupUrl(.*?)\"]', response.text)[0].replace('\"', '').split('\\')[2]
m3u8_data = requests.get(url=m3u8_url, headers=headers).text

print(m3u8_url)

m3u8_data = requests.get(url=m3u8_url, headers=headers).text
m3u8_data = re.sub('#EXTM3U', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-VERSION:\d', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-TARGETDURATION:\d', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-MEDIA-SEQUENCE:\d', '', m3u8_data)
m3u8_data = re.sub('#EXTINF:\d.\d+,', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-ENDLIST', '', m3u8_data).split()

# print(m3u8_data)
# m3u8_data = re.sub('#EXTM3U', '', m3u8_data)
for index in tqdm(m3u8_data):
    ts_url = 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/' + index
    # print(ts_url)
    ts_name = index.split('.')[1]
    ts_content = requests.get(url=url, headers=headers).content
    with open('video_Acfun\\' + ts_name + '.ts', mode='wb') as f:
        f.write(ts_content)
#     # with open('video_Acfun\\' + title + '.mp4', mode='ab') as f:
#     #     f.write(ts_content)
# # print(title, '保存完成')
#
