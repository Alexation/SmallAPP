import requests
import re
import os
print('------------关闭此窗口以停止程序-------------')
headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) '
      'Gecko/20100101 Firefox/91.0')}
fold_name = '表情包'
if not os.path.exists(fold_name):
    os.mkdir(fold_name)
for page in range(1, 201):
    print(f'------------正在爬取第{page}页-------------')
    url = f'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'
    response = requests.get(url=url, headers=headers).text
    images = re.findall('<img class="ui image lazy" data-original="(.*?)"', response)
    titles = re.findall('<a href=".*?" title="(.*?)">', response)
    for img_url, title in zip(images, titles):
        title = re.sub(r'[/\\:*?"<>|]', '_', title)
        if len(title) > 50:
            title = title[:50]
        suffix = img_url.split('.')[-1]
        img_data = requests.get(url=img_url, headers=headers).content
        with open(f'{fold_name}/{title}.{suffix}', mode='wb') as f:
            f.write(img_data)
        print(f'正在保存：{title}')
