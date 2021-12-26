import requests
import re
from lxml import etree

content_re=re.compile('"excerptArea":{"text":"(.*?)"}')

url_re=re.compile('"link":{"url":"(.*?)"}')

#发包的请求头
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

def get_html():
    url='https://www.zhihu.com/billboard'
    html=requests.get(url,headers=headers)# 1s下载了这个页面  1s分成100部分

    soup=etree.HTML(html.text)  #xpath包装解析
    #xpath语法匹配内容
    #//代表全局匹配 a就是a标签  [@class="HotList-item"] /切换到里边的一级别 text()只要文本

    titles=soup.xpath('//a[@class="HotList-item"]/div/div[@class="HotList-itemTitle"]/text()')
    for t in  titles:
        print('标题：',t)
    imgs=soup.xpath('//div[@class="HotList-itemImgContainer"]/img/@src')
    for i in imgs:
        print('图片链接：',i)
    print('-'*20)
    #正则表达式语法匹配
    html_text=html.text
    contents=content_re.findall(html_text)
    for c in contents:
        print('内容：',c)

    #匹配URL
    urls=url_re.findall(html_text)
    for u in urls:
        print('URL:',u)


if __name__ == '__main__':
    get_html()
