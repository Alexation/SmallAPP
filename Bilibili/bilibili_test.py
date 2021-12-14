import requests
import re
import subprocess
import os
headers = {
    'referer': 'https://www.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',

}


def get_response(html_url):
    """发送请求"""
    response = requests.get(url=html_url, headers=headers)
    return response


def get_video_info(html_url):
    """获取 cid session 视频标题"""
    response = get_response(html_url)
    cid = re.findall('"cid":(\d+),', response.text)[0]
    session = re.findall('"session":"(.*?)"', response.text)[0]
    title = re.findall('<h1 title="(.*?)" class="video-title">', response.text)[0].replace(' ', '')
    video_info = [cid, session, title]
    return video_info


def get_video_content(cid, session, bvid):
    """获取音频内容以及视频内容"""
    index_url = 'https://api.bilibili.com/x/player/playurl'
    data = {
        'cid': cid,
        'qn': '80',
        'type': '',
        'otype': 'json',
        'fourk': '1',
        'bvid': bvid,
        'fnver': '0',
        'fnval': '976',
        'session': session,
    }
    json_data = requests.get(url=index_url, params=data, headers=headers).json()
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    video_content = [audio_url, video_url]
    return video_content


def save(name, audio_url, video_url):
    """保存数据"""
    audio_content = get_response(audio_url).content
    video_content = get_response(video_url).content
    with open(name + '.mp3', mode='wb') as a:
        a.write(audio_content)
    with open(name + '.mp4', mode='wb') as v:
        v.write(video_content)
    print(name, '保存成功')


def merge_data(video_name):
    """数据的合并"""
    print('视频合成开始:', video_name)
    cmd = f"ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 " \
          f"-c:v copy -c:a aac -strict experimental {video_name}output.mp4 -loglevel quiet"
    # print(cmd)
    subprocess.run(cmd, shell=True)
    os.remove(f'{video_name}.mp4')
    os.remove(f'{video_name}.mp3')
    print('视频合成结束:', video_name)


def main(bv_id):
    """主函数"""
    url = f'https://www.bilibili.com/video/{bv_id}'
    video_info = get_video_info(url)
    video_content = get_video_content(video_info[0], video_info[1], bv_id)
    save(video_info[2], video_content[0], video_content[1])
    merge_data(video_info[2])


key_world = input('请输入你的下载的视频BV号: ')
main(key_world)