import requests
import re
import os
import parsel

ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) '
      'Gecko/20100101 Firefox/91.0')
headers = {'User-Agent': ua}


def get_response(html_url):
    response = requests.get(url=html_url, headers=headers)
    return response


def save(music_url, name):
    filename = 'music_kugou\\'
    if not os.path.exists(filename):
        os.mkdir(filename)
    if music_url:
        name = re.sub(r'[/\\:*?"<>|]', '_', name)
        music_data = get_response(html_url=music_url).content
        with open(filename + name + '.mp3', mode='wb') as f:
            f.write(music_data)
            print('save successfully')


def get_music_id(html_url):
    # 获取hash and id
    html_data = get_response(html_url).text
    # 解析数据
    Hash_list = re.findall('"Hash":"(.*?)"', html_data)
    album_ids = re.findall('"album_id":(.*?),', html_data)
    zip_data = zip(Hash_list, album_ids)
    return zip_data


def get_music_info(Hash, album_id):
    index_url = 'https://wwwapi.kugou.com/yy/index.php'
    data = {
        'r': 'play/getdata',
        # 'callback': 'jQuery19107794429506209624_1634785491657',
        'hash': Hash,
        'dfid': '0jIgIH1HGyiA4IQzep0QDuiB',
        'appid': '1014',
        'mid': 'cea2eaa583d6273aeecef6a87475019b',
        'platid': '4',
        'album_id': album_id,
        '_': '1634785491658'
    }
    response = requests.get(url=index_url, params=data, headers=headers)
    # print(response.json())
    title = response.json()['data']['audio_name']
    play_url = response.json()['data']['play_url']
    save(music_url=play_url, name=title)
    print(title, play_url)


def get_list_url(html_url):
    html_data = get_response(html_url=html_url).text
    selector = parsel.Selector(html_data)
    list_name = selector.css('.pc_rank_sidebar li a::attr(title)').getall()
    list_url_each = selector.css('.pc_rank_sidebar li a::attr(href)').getall()
    # list_info = re.findall('<a title="(.*?)" hidefocus="true" href="(.*?)"', html_data)
    # print(html_data)
    list_data = zip(list_name, list_url_each)

    return list_data


def main(list_url):
    list_data = get_list_url(html_url=list_url)
    for list_name, list_url in list_data:
        print('正在爬取', list_name)
        get_music_id(html_url=list_url)
        zip_data = get_music_id(html_url=list_url)
        for hash, album_id in zip_data:
            get_music_info(Hash=hash, album_id=album_id)



if __name__ == '__main__':
    list_url = 'https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'
    main(list_url)