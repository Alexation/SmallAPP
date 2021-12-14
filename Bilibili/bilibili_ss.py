import pprint
import re
import requests
import subprocess
from tqdm import tqdm

from ffmpy import FFmpeg

url = 'https://www.bilibili.com/bangumi/play/ss39462?spm_id_from=333.1007.partition_rank.content.click'

headers = {
    'referer': 'https://www.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38',
    'cookie': "b_ut=-1; i-wanna-go-back=-1; _uuid=DFF6B592-2291-5AAD-73E8-88A0A587EF4576747infoc; buvid3=9A6924D9-B6BC-4A80-8FFC-22C4734818FF167643infoc; b_nut=1633101277; fingerprint=c53c7f2cc3b1434ac40a9b61b17213e1; buvid_fp=9A6924D9-B6BC-4A80-8FFC-22C4734818FF167643infoc; buvid_fp_plain=9A6924D9-B6BC-4A80-8FFC-22C4734818FF167643infoc; DedeUserID=32804780; DedeUserID__ckMd5=8d301a718889e45a; SESSDATA=e939d92b%2C1648653300%2C8596d*a1; bili_jct=943f4ef4031fbe19a00cacfb564d51f4; blackside_state=1; rpdid=|(u)~RuJJRuY0J'uYJJkYuk)|; CURRENT_QUALITY=80; video_page_version=v_new_home_13; bp_video_offset_32804780=586840283804194559; sid=aejg6end; LIVE_BUVID=AUTO8716357639447773; innersign=0; CURRENT_BLACKGAP=1; CURRENT_FNVAL=80; bsource=search_google; PVID=1",
}
response = requests.get(url=url, headers=headers).text


cid = re.findall('"cid":(\d+),', response)[0]
episodes = re.findall('"episodes":(.*?)"cover"', response)
avid = re.findall('"aid":(\d+),', response)[0]
bvid = re.findall('"bvid":(.*?),', response)[0]
session = re.findall('"session":"(.*?)"', response)
title = re.findall('<title>(.*?)</title>', response)[0]
video_name = title
video_info = [avid, bvid, cid, session, title]
print(video_info)
params = {
    'avid': avid,
    'bvid': bvid,
    'cid': cid,
    'qn': '80',
    'fnver': '0',
    'fnval': '80',
    'fourk': '1',
    'ep_id': '424605',
    'session': ''
}
play_url = 'https://api.bilibili.com/pgc/player/web/playurl'

html_data = requests.get(url=play_url, params=params, headers=headers).json()
# print(html_data)
# pprint.pprint(html_data)
# audio_url = html_data['data']['dash']['audio'][0]['baseUrl']
# video_url = html_data['data']['dash']['video'][0]['baseUrl']

audio_url = html_data['result']['dash']['audio'][0]['baseUrl']
video_url = html_data['result']['dash']['video'][0]['baseUrl']

audio_data = requests.get(url=audio_url, headers=headers).content
video_data = requests.get(url=video_url, headers=headers).content
with open(title + '.mp3', mode='wb') as a:
    a.write(audio_data)
with open(title + '.mp4', mode='wb') as v:
    v.write(video_data)
cmd = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4'
tqdm(subprocess.run(cmd, shell=True))
print('视频合成完成')
