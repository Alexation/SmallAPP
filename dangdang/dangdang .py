import requests
import parsel
import re
import csv

f = open('当当图书畅销榜.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['名称', '评论', '作者', '出版社', '价格', '折扣', '详情链接'])
csv_writer.writeheader()

for page in range(1):
    url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-{page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40',
    }
    response = requests.get(url=url, headers=headers)
    html_data = parsel.Selector(response.text)
    base = '//ul[@class="bang_list clearfix bang_list_mode"]/li'
    lis = html_data.xpath(base)
    for li in lis:
        name = li.xpath('//div[@class="name"]/a/@title').extract()
        comment = li.xpath('//div[@class="star"]/span/a/text()').extract()
        publisher = li.xpath('//div[@class="publisher_info"][1]/a/@title').extract()
        shop = li.xpath('//div[@class="publisher_info"][2]/a/text()').extract()
        price = li.xpath('//div[@class="price"]/p/span[1]/text()').extract()
        discount = li.xpath('//div[@class="name"]/p/span[3]').extract()
        url = li.xpath('//div[@class="name"]/a/@href').extract()
        dit = {
            '名称': name,
            '评论': comment,
            '作者': publisher,
            '出版社': shop,
            '价格': price,
            '折扣': discount,
            '详情链接': url
        }
        csv_writer.writerow(dit)
print('保存完成')
