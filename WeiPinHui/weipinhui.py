import requests
import csv
search = input('请输入要查找的关键字：')

url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/search/product/rank'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'
    'WebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
    'referer': 'https://category.vip.com/',
}
data = {
    # 'callback': 'getMerchandiseIds',
    'app_name': 'shop_pc',
    'app_version': '4.0',
    'warehouse': 'VIP_NH',
    'fdc_area_id': '104104101',
    'client': 'pc',
    'mobile_platform': '1',
    'province_id': '104104',
    'api_key': '70f71280d5d547b2a7bb370a529aeea1',
    'user_id': '',
    'mars_cid': '1635209143189_efd586d905629bb970641912bb5a11f2',
    'wap_consumer': 'a',
    'standby_id': 'nature',
    'keyword': search,
    'lv3CatIds': '',
    'lv2CatIds': '',
    'lv1CatIds': '',
    'brandStoreSns': '',
    'props': '',
    'priceMin': '',
    'priceMax': '',
    'vipService': '',
    'sort': '0',
    'pageOffset': '0',
    'channelId': '1',
    'gPlatform': 'PC',
    'batchSize': '120',
    '_': '1635209201065',
}

def get_shop_info(shop_id):
    shop_info_url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2'
    params = {
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_NH',
        'fdc_area_id': '104104101',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '104104',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '',
        'mars_cid': '1635209143189_efd586d905629bb970641912bb5a11f2',
        'wap_consumer': 'a',
        'productIds': shop_id,
        'scene': 'search',
        'standby_id': 'nature',
        'extParams': '{"stdSizeVids": "", "preheatTipsVer": "3", "couponVer": "v2", "exclusivePrice": "1", "iconSpec": "2x","ic2label": 1}',
        'context': '',
        '_': '1635209201068',
    }
    response = requests.get(url=shop_info_url, params=params, headers=headers)
    shop_info_list = response.json()['data']['products']
    for index in shop_info_list:
        attrs = '        '.join([j['name'] + ':' + j['value'] for j in index['attrs']])
        href = f'https://detail.vip.com/detail-{index["brandId"]}-{index["productId"]}.html'
        dit = {
            '标题': index['title'],
            '商品名称': index['brandShowName'],
            '商品属性': attrs,
            '原价': index['price']['marketPrice'],
            '折扣': index['price']['saleDiscount'],
            '售价': index['price']['salePrice'],
            '详情页': href,
        }
        csv_writer.writerow(dit)


f = open(f'{search}数据_唯品会.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '商品名称',
    '商品属性',
    '原价',
    '折扣',
    '售价',
    '详情页',
])
csv_writer.writeheader()  # 写入表头

response = requests.get(url=url, params=data, headers=headers)

products = response.json()['data']['products']

pid_list = [i['pid'] for i in products]

string_1 = ','.join(pid_list[0:50])
string_2 = ','.join(pid_list[50:100])
string_3 = ','.join(pid_list[100:])

get_shop_info(string_1)
get_shop_info(string_2)
get_shop_info(string_3)
print('保存成功')
