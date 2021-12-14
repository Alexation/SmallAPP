import time
from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options
search = input('请输入你要搜索的关键字：')

f = open(f'{search}数据_京东.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '价格', '店铺', '评论', '链接'])
csv_writer.writeheader()

def drop_down():
    for x in range(1, 12, 2):  # 1 3 5 7 9 在不断下拉的过程中，页面高度也会变化
        time.sleep(1)
        j = x / 9  # 1/12 3/12 5/12 7/12
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


url = 'https://www.jd.com/'

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
chrome_options = Options()
chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

driver.find_element_by_xpath('//*[@id="key"]').send_keys(search)
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
driver.implicitly_wait(10)
drop_down()

lis = driver.find_elements_by_css_selector('.gl-item')
for li in lis:
    price = li.find_element_by_css_selector('.gl-warp .p-price strong i').text
    name = li.find_element_by_css_selector('.gl-item .p-name em').text

    shop_name = li.find_element_by_css_selector('.p-shop .J_im_icon a').text
    comment = li.find_element_by_css_selector('.p-commit strong').text
    url = li.find_element_by_css_selector('.p-img a').get_attribute('href')
    dit = {
        '价格': price,
        '标题': name,
        '店铺': shop_name,
        '评论': comment,
        '链接': url,
    }
    csv_writer.writerow(dit)
print('保存完成')
