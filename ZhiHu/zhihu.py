import parsel
import requests
import re

url = 'https://www.zhihu.com/billboard'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38',
    'cookie': '_zap=d2ddd806-bdd5-41b3-9d7f-7c2d959497ff; d_c0="AJDeajEFzxOPTrfCyTBet0BOJDBoW4ob7EA=|1633090410"; tst=r; _xsrf=d7b822c4-f1cc-4322-9fdd-64d1597ef614; NOT_UNREGISTER_WAITING=1; SESSIONID=aWqgImKCsmbiDkA3oaHk1W5Vejhd4pgZtzlpS4HO4kc; JOID=WlgdAEm9_aDFCN0mc7b_PTM70-tg1KLao0u4ZTvEmMqnTbxvSPB51K8K3SV5jLMdybbepR2VBG0gtySZ9GHv_a8=; osd=VF0TA0qz-K7GC9MjfbX8MzY10Ohu0azZoEW9azjHls-pTr9hTf5616EP0yZ6grYTyrXQoBOWB2MluSea-mTh_qw=; gdxidpyhxdE=VC%2FRnGce6kRJx9KqVkAPcvrLfXrt8qKqsN%2Bx8WCEz5y9pS01Cz2Ry%2F5SvsQ1vK3n9tVHIsUktt%5C14%5COzdzGQU1WHPQgThyej%5CTAsdVyzpGp5KQhi3e%2B2sK0uhDNaTS1Hm%2FCBLnTsU55g%2FHaGbLoRW0ouVNvemq2v2WMeGdqT3mrKKW0a%3A1635683512912; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=jEwIYABWvE%2Bp0eqwmCtVJ2rNG5i7ySBgX5Y0yY%2Bj9ge1vrVSkBpPTwiau1mU%2FGovapMXeRS%2FPlMornRsgY74QDEZUxIl9f3BZwPf1kDz3T66c2zil1lEiX8FslYuXRvAQUc%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea6f37490b485b9f75b8bb08fa7d15a879b9ebaf17c9086bc85d721b2b39d9af42af0fea7c3b92aaa9bb9aadc4b8289baa6aa7cf4bbbf98f049b88a86d3f14685eba7d8fc5982b998d6dc3cbb87e58bbc6da7efba93d559a99ec0b1d77dabbfbbd2f05fed99a197e47c8f88abb3d22594b48390f16692ada9bab640939c8bbbd8748bb4f787b24a9aa9a087b46188a6fdb5b53ea1eeb68aef3bb09ba7b9bb4eb1b49796db5ab69f9fb6e237e2a3; YD00517437729195%3AWM_TID=GqLEIJ8J2ulEFRBRVFY%2FpOdocHqq3Xy%2F; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1635682671|1635682124; captcha_session_v2="2|1:0|10:1635682671|18:captcha_session_v2|88:Z1FRRkQ3VjYraTZnODBZcGU4azlMaER3ZmRGZkJiSnV3aUQ3UGdxMCtwVG93Q0Fhblc1R0owUGZTY0ZBeXRWNQ==|514b9ac689748a18874de4f21387b110bf4cc6217d17c894db6df205b57ffd8a"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1635682125,1635682142,1635682617,1635682672; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1635682672',

    'referer': 'https://www.google.com/',
}
response = requests.get(url=url, headers=headers).text
print(response)
html_data = parsel.Selector(response)
html_content = html_data.xpath('//*[@id="root"]/div/main/div/a/div[2]/div[1]').extract()
html_content2 = html_data.xpath('//*[@id="root"]/div/main/div/a[1]/div[2]/div[2]/text()').extract()
content = re.findall('<div class="HotList-itemTitle">(.*?)</div>', response)
content2 = re.findall('<div class="HotList-itemExcerpt">(.*?)</div>', response)
print(html_content2)
print(content2)