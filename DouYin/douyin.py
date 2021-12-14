import requests
import re
import json
import parsel
import pprint

ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) '
      'Gecko/20100101 Firefox/91.0')
#
# params = {
#     'source': 'search_history',
#     'aid': '9db5b4c1-ecbe-4d7c-a0a3-59552dddcc68',
#     'enter_from': 'recommend'
# }
headers = {
    'User-Agent': ua,
    # 'Referer': 'https://www.douyin.com/',
    'referer': 'https://www.douyin.com/search/%E7%94%B7%E7%94%9F%E8%88%9E%E8%B9%88?publish_time=0&sort_type=0&source=search_history&type=video',
    'origin': 'https://www.douyin.com',
    'referer': 'https://www.douyin.com/search/%E7%94%B7%E7%94%9F%E8%88%9E%E8%B9%88?publish_time=0&sort_type=0&source=search_history&type=video',
    'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'cookie': 'ttcid=f768c8618432425dad8f905cafe7719e17; ttwid=1%7CzKJUfQDRTQ-qDXymR7-2Lh_sl7pgYs2zNRYLuPR528s%7C1637115601%7C00babea4ec3d1088862bb59824e6bf730cba62f0e33daa442b9c515691f87da4; _tea_utm_cache_6383=undefined; MONITOR_WEB_ID=1afca3c1-338b-4f91-944b-b8b12cfadfda; passport_csrf_token_default=fec363cab4aaa6dd60b7c5c2cd0404a5; passport_csrf_token=fec363cab4aaa6dd60b7c5c2cd0404a5; _tea_utm_cache_1300=undefined; odin_tt=efc8102bad8306dd0d1e1ff2f31d86a4b6e1c793f7e45ce8cfa1586209ccc2e201def955913c484bce130a9de74d25f39017c4e1d547b1298f8f9b93555d6c55; __ac_nonce=0619b3efd00f2eb5cd33b; __ac_signature=_02B4Z6wo00f018Uq9xgAAIDCmmkYwfE6vJ.FDvOAAJDaINdlQ4SBOgyhK7ncZzXtVHNNOid2xZGKIbNsnVt0TYSn-c6ddRkh7ZFE.aPShHnAyNIvT7EaEZ0xzQfYjc.-yPZ9sCWkS0TkA49Ud4; douyin.com; s_v_web_id=verify_kwabf2vu_yA9hAeMy_8r2s_4CfN_96t1_Q5RiRWDDQ9XK; msToken=RkCEdDFoLLOtJVaWxhEI55fOaj5kG7SxDfob6UvAUoNeoI5o-eQOB97sUMWLByCmDvkjqfNJ9O-82pdPCPZv31yn-rG7IgGQS9fOcmmjxcI4rtX_0aFCf50=; msToken=nnSboW4eyFfIrpGL-y3CdU63eueMqa6NHvR6i4tj17dKIFE3t4pWoZGBIyAvT1nuqtTSPHQXEe0PJggjyQfyJgoAIliMRHKHdxfZP_YLxr8sD83Bt8IaAlU=; tt_scid=P7K5wAXYUgjLc5FGjigIUl3Zew7a-KfLrbjd4YNvohwUL88eR7wiEQSlvdM33Djz34e9',
}


# search = input('请输入要下载视频的网址：')
# number = re.findall('video/(.*?)\?', search)[0]
# key_word = input('请输入要搜素的关键字：
search_url = 'https://www.douyin.com/aweme/v1/web/search/item/'
boy_dance_url = 'https://www.douyin.com/search/%E7%94%B7%E7%94%9F%E8%88%9E%E8%B9%88?publish_time=0&sort_type=1&source=search_sug&type=video'
# base_url = f'https://www.douyin.com/search/{key_word}'
douyin = 'https://www.douyin.com/video/6707510811562085640'
douyin = 'https://www.douyin.com/video/6717062849803357453'
url = 'https://www.douyin.com/service/2/abtest_config/'
data = {
    'header': {
    'ab_sdk_version': '"3355428,3360995,90000985,3324619,90000906,3280611,3365690,3320527,3386593,3326759,3401217,3387389,3393491"',
    'ab_url': '"https://www.douyin.com/search/%E7%94%B7%E7%94%9F%E8%88%9E%E8%B9%88?publish_time=0&sort_type=0&source=search_history&type=video"',
    'ad_id': 'null',
    'aid': '6383',
    'app_id': '6383',
    'browser': '"Microsoft Edge"',
    'browser_version': '"95.0.1020.53"',
    'campaign_id': 'null',
    'creative_id': 'null',
    'custom': '{}',
    'device_model': '"Windows NT 10.0"',
    'height': '1080',
    'language': '"en-US"',
    'os_name': '"windows"',
    'os_version': '"10"',
    'platform': '"web"',
    'referrer': '"https://www.douyin.com/"',
    'referrer_host': '"www.douyin.com"',
    'resolution': '"1920x1080"',
    'screen_height': '1080',
    'screen_width': '1920',
    'sdk_lib': '"js"',
    'sdk_version': '"4.1.61"',
    'timezone': '8',
    'tz_offset': '-28800',
    'user_id': '"4231372894381868"',
    'user_is_auth': 'false',
    'user_is_login': 'false',
    'user_type': '12',
    'user_unique_id': '"7031357937041950208"',
    'web_id': '"7031357953580910113"',
    'width': '1920',}
}
params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'search_channel': 'aweme_video_web',
    'sort_type': '0',
    'publish_time': '0',
    'keyword': '男生舞蹈',
    'search_source': 'search_history',
    'query_correct_type': '1',
    'is_filter_search': '0',
    'offset': '0',
    'count': '30',
    'version_code': '170400',
    'version_name': '17.4.0',
    'cookie_enabled': 'true',
    'screen_width': '1920',
    'screen_height': '1080',
    'browser_language': 'en - US',
    'browser_platform': 'Win32',
    'browser_name': 'Mozilla',
    'browser_online': 'true',
    'msToken': 'U1TyzGUXhp6ObisNKMgSYk39IcLtU - 7rn3rADuV3demzXNcE4VyiNR3X_GzSg2G2850lPZ5Gn7L1czcN_UM03i5te9jRmqnmhLthwMcOxJ8I_vjf1zAqxH - R',
    'X - Bogus': 'DFSzswSO7C0ANSYCS7DniVT8gyTY',
    '_signature': '_02B4Z6wo00001PPC5fQAAIDBrIEKLJoPIqTzxuFAAF1xzXTej0NKJhcWm5I5pgmpRu3PlxIxIWPjnaGu5rczv8vOghXm4pZ-.Xo9dYzrV7jdj3t8D5J4XQOkzD5ZbK.e4uUDkJ92R3oHsSgne9',
}


# search_response = requests.get(url=search_url, headers=headers,params=params)
# print(search_response.text)
id_response = requests.post(url, headers=headers, data=data)
print(id_response.text)
# boy_dance_url_response = requests.get(url=boy_dance_url, headers=headers)
# print(boy_dance_url_response.text)


# web_url = f'https://www.douyin.com/video/{number}'

# response = requests.get(url=douyin, headers=headers, params=params).text
#
# response = requests.utils.unquote(response)

# print(douyin)
# print(response.text)
# data_response = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', response)[0]
# print(data_response)
# str3 = html.unescape(data_response)
# response_json = json.loads(data_response)
# pprint.pprint(response_json)
# play_url = response_json['C_20']['aweme']['detail']['video']['playAddr'][0]['src']
# result_url = 'https:' + play_url
# print(result_url)



# data_a = re.findall('\?a=(.*?)&', data_response)[0]
# data_br = re.findall('&br=(.*?)&', data_response)[0]
# data_ft = re.findall('&ft=(.*?)&', data_response)[0]
# data_l = re.findall('&l=(.*?)&', data_response)[0]
# data_rc = re.findall('&rc=(.*?)&', data_response)[0]
# data_ft = re.findall('&ft=(.*?)&', data_response)[0]
# print(data_a, data_br, data_ft, data_l, data_rc)

# params = {
#     'a': data_a,
#     'br': data_br,
#     'bt': data_br,
#     'cd': '0|0|0',
#     'ch': '26',
#     'cr': '3',
#     'cs': '0',
#     'cv': '1',
#     'dr': '0',
#     'ds': '6',
#     'er': '',
#     'ft': data_ft,
#     'l': data_l,
#     'lr': 'all',
#     'mime_type': 'video_mp4',
#     'net': '0',
#     'pl': '0',
#     'qs': '0',
#     'rc': data_rc,
#     'vl': '',
#     'vr': '',
# }
# base_html = parsel.Selector(response.text)
# lis = base_html.xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[2]/ul/li/div/a/@href').extract()
# print(lis)


# title = re.findall('<title data-react-helmet="true">(.*?)</title>', response.text)[0]
# title = re.sub(r'[/\\:*?"<>|]', '_', title)
# href = re.findall('src(.*?)vr%3D', response.text)[2]
# video_url = requests.utils.unquote(href).replace('":"', 'https:')
# video_content = requests.get(url=video_url).content
# with open('video\\' + title + '.mp4', mode='wb') as f:
#     f.write(video_content)
#     print(f'保存成功：{title}')
