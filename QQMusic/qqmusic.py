import requests
import re
import json
from urllib import parse
ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) '
      'Gecko/20100101 Firefox/91.0')
headers = {
    'User-Agent': ua,
    #':authority': 'u.y.qq.com',
    #':method': 'POST',
    #':path': '/cgi-bin/musics.fcg?_=1635230999712&sign=zzb8ae07570pizak160lzi86bcykg2dw291a8e26',
    #':scheme': 'https',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-length': '409',
    'content-type': 'application/x-www-form-urlencoded',
    # 'content-type': 'application/json',
    'cookie': 'RK = gY78exn7Nl;ptcz = 96078adfb9898130a799367e33b8e7635eb6f197593d2c88510a2914413ba331;pgv_pvid = 3285517400;fqm_pvqid = 7edb9faf - d1fc - 427a - a1d5 - e060c0827304;ts_uid = 6735119628;luin = o0820214971;tvfe_boss_uuid = c3cb5c40d39b978b;o_cookie = 820214971;lskey = 0001000073f3ccd5b202a3a4aaba50e203a0c43f03dad298b21719b7df2f17e39ba6cbfcff733494731df7e5;ts_refer = www.google.com /;psrf_musickey_createtime = 1635085331;qm_keyst = Q_H_L_2C1Rr560eeDKcyJufGBuPCBr34GwzMBN1fbI - 9GRYmmRdm61LMp9bWtXZHpRMrA;euin = Ne - zow6PNKS5;psrf_qqaccess_token = 26333410645BD8DC49732B0792DFC61F;qqmusic_key = Q_H_L_2C1Rr560eeDKcyJufGBuPCBr34GwzMBN1fbI - 9GRYmmRdm61LMp9bWtXZHpRMrA;wxopenid =;psrf_qqrefresh_token = CBBAAE759BE861C309068357BC5C3208;qm_keyst = Q_H_L_2C1Rr560eeDKcyJufGBuPCBr34GwzMBN1fbI - 9GRYmmRdm61LMp9bWtXZHpRMrA;wxrefresh_token =;wxunionid =;tmeLoginType = 2;psrf_qqopenid = 7BCE888D3015FF103876B84A8CFD2093;psrf_qqunionid = F25D7995F081C8E74F63306EAFA2C906;psrf_access_token_expiresAt = 1642861331;uin = 820214971;fqm_sessionid = 626ecf0c - 0c3c - 4a2b - 9e71 - adda48afd87c;pgv_info = ssid = s6197913710;ts_last = y.qq.com / n / ryqq / search',
    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site'
}

# web_url = 'https://u.y.qq.com/cgi-bin/musics.fcg?_=1635230999712&sign=zzb8ae07570pizak160lzi86bcykg2dw291a8e26'
web_url = 'https://u.y.qq.com/cgi-bin/musics.fcg'
params = {
    '_': '1635230999712',
    'sign': 'zzb8ae07570pizak160lzi86bcykg2dw291a8e26'
}

# data = {
#     "comm": {
#         "cv": '4747474',
#         "ct": '24',
#         "format": "json",
#         "inCharset": "utf-8",
#         "outCharset": "utf-8",
#         "notice": '0',
#         "platform": "yqq.json",
#         "needNewCode": '1',
#         "uin": '0',
#         "g_tk_new_20200303": '5381',
#         "g_tk": '5381',
#         "req_1": {
#             "method": "DoSearchForQQMusicDesktop",
#             "module": "music.search.SearchCgiService",
#             "param": {
#                 "remoteplace": "txt.yqq.center",
#                 "searchid": "55654620066664603",
#                 "search_type": '0',
#                 "query": "李荣浩",
#                 "page_num": '1',
#                 "num_per_page": '10'}
#         }
#     }
# }

data = {
    "cv": '4747474',
    "ct": '24',
    "format": "json",
    "inCharset": "utf-8",
    "outCharset": "utf-8",
    "notice": '0',
    "platform": "yqq.json",
    "needNewCode": '1',
    "uin": '0',
    "g_tk_new_20200303": '5381',
    "g_tk": '5381',
    "req_1": {
        "method": "DoSearchForQQMusicDesktop",
        "module": "music.search.SearchCgiService",
        "param": {
            "remoteplace": "txt.yqq.center",
            "searchid": "55654620066664603",
            "search_type": '0',
            "query": "李荣浩",
            "page_num": '1',
            "num_per_page": '10'}
    }
}
data = json.dumps(data)
# data = parse.urlencode(data)
response = requests.post(url=web_url, headers=headers, params=params, data=data)
# response = json.loads(response)
print(response.text)
