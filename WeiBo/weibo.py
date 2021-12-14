import re
import requests
import parsel
import pprint
import json
url = 'https://s.weibo.com/ajax/jsonp/gettopsug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38',
    'Host': 's.weibo.com',
    'Referer': 'https://d.weibo.com/',
    'Cookie': 'login_sid_t=b946ec25b93d682a26943456fa1b130f; cross_origin_proto=SSL; _s_tentry=www.google.com; UOR=www.google.com,weibo.com,www.google.com; Apache=4747427982569.656.1635676957788; SINAGLOBAL=4747427982569.656.1635676957788; ULV=1635676957793:1:1:1:4747427982569.656.1635676957788:; SUB=_2AkMWIvwPf8NxqwJRmfwRxG7ka4l-zArEieKgfg3UJRMxHRl-yT8XqlcStRB6PaLS4FpqA--TrTvpNwYlEwtakhgPviBe; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5UxYLeAbiXl0UOVGrpgdJ3',

}
params = {
    'uid': '3655689037',
    'ref': 'PC_topsug',
    'url': 'https://d.weibo.com/231650',
    'Mozilla': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38',
    '_cb': 'STK_163567707505412',
}
response = requests.get(url=url, headers=headers, params=params).text
ans = re.findall('window.STK_163567707505412&STK_163567707505412\((.*?)\)}catch\(e\){}', response)
print(response)
print(ans)
print(type(ans))
ans_json = json.loads(ans)
print(type(ans_json))
# pprint.pprint(ans_json)

# html_data = parsel.Selector(response)
# lis = html_data.xpath('//*[@id="Pl_Discover_Pt6Rank__3"]/div/div/div[1]/div/ul/li[1]/div/div[2]/div[1]/div[1]/a[1]').extract()
# # lis = re.findall('<a.*?>(.*?)</a>', html_data)
# print(lis)
