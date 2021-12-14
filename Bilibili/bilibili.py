import re
import requests
import subprocess
import pprint
# BV = input('请输入你要下载视频的BV号：')
BV = 'BV13E411P795'
url = f'https://www.bilibili.com/video/{BV}'
bvid = re.findall('video/(.*?)\?', url)
headers = {
    'referer': 'https://www.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38',
}
# params = {
# 'spm_id_from': '333.788.recommend_more_video.1'
# }
# url += '/?spm_id_from=333.788.recommend_more_video.1'
response = requests.get(url=url, headers=headers).text
# print(response)
# cid = re.findall('"cid":(\d+),', response)[0]
# session = re.findall('"session":"(.*?)"', response)[0]
# title = re.findall('<h1 title="(.*?)" class="video-title">', response)[0]
# video_info = [cid, session, title]
# video_name = title
#
# params = {
#     'cid': cid,
#     'qn': '80',
#     'type': '',
#     'otype': 'json',
#     'fourk': '1',
#     'bvid': bvid,
#     'fnver': '0',
#     'fnval': '976',
#     'session': session,
# }
# play_url = 'https://api.bilibili.com/x/player/playurl'
# print()
# html_data = requests.get(url=play_url, params=params, headers=headers).json()
# pprint.pprint(html_data)
# audio_url = html_data['data']['dash']['audio'][0]['baseUrl']
# video_url = html_data['data']['dash']['video'][0]['baseUrl']
#
# audio_data = requests.get(url=audio_url, headers=headers).content
# video_data = requests.get(url=video_url, headers=headers).content
#
# with open(title + '.mp3', mode='wb') as a:
#     a.write(audio_data)
# with open(title + '.mp4', mode='wb') as v:
#     v.write(video_data)
# cmd = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4'
# subprocess.run(cmd, shell=True)
# print('视频合成完成')
