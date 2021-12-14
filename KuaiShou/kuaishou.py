import requests
import re
import json
from urllib.parse import quote
search = '男生舞蹈'
search_url = quote(search, 'utf-8')
ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) '
      'Gecko/20100101 Firefox/91.0')
headers_base = {'User-Agent': ua,}
url_base = f'https://www.kuaishou.com/search/video?searchKey={search_url}'
cookie_base = 'clientid=3; did=web_06c97de230d6ab7ff9835159a7b06824; kpf=PC_WEB; kpn=KUAISHOU_VISION'
def getcookie():
      cookie_base = ''
      cookie = requests.get(url=url_base, headers=headers_base)
      for key, value in cookie.cookies.items():
            cookie_temp = f'{key}={value}; '
            cookie_base += cookie_temp
      cookie_base = cookie_base[:-2]
      return cookie_base
headers = {
      'User-Agent': ua,
      'accept': '*/*',
      'content-type': 'application/json',
      'Cookie': cookie_base,
      'Host': 'www.kuaishou.com',
      'Origin': 'https://www.kuaishou.com',
      'Referer': f'https://www.kuaishou.com/search/video?searchKey={search_url}'
}
data = {
      'operationName': 'visionSearchPhoto',
      'query': 'query visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        photoUrl\n        liked\n        timestamp\n        expTag\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n',
      'variables': {'keyword': search, 'pcursor': "", 'page': "search"}
}
web_url = 'https://www.kuaishou.com/graphql'
data = json.dumps(data)
response = requests.post(url=web_url, headers=headers, data=data)
def main():
      if response.json()['data']['visionSearchPhoto'] != None:
            video_list = response.json()['data']['visionSearchPhoto']['feeds']
            for feed in video_list:
                  video_name = feed['author']['name']
                  video_name = re.sub(r'[/\\:*?"<>|]', '_', video_name)
                  video_content = requests.get(url=feed['photo']['photoUrl']).content
                  with open('video\\' + video_name + '.mp4', mode='wb') as f:
                        f.write(video_content)
                        print(f'保存成功：{video_name}')
      else:
            cookie_base = getcookie()
            main()

main()