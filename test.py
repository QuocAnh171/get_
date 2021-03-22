from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests


#sign in
get_data = webdriver.Chrome()
get_data.get("https://dasuperstore1.myshopify.com/admin")
username = get_data.find_element_by_name('account[email]')
username.clear()
username.send_keys('dangquocanh171@gmail.com')
sleep(3)
username.send_keys(Keys.ENTER)
sleep(5)
password = get_data.find_element_by_name('account[password]')
password.clear()
password.send_keys('anh17111998')
sleep(3)
password.send_keys(Keys.ENTER)
sleep(10)

#get_cookies:
cookies_list = get_data.get_cookies()
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies_list:
    jar.set(cookie['name'], cookie['value'], domain = cookie['domain'], path = cookie['path'])
sleep(10)
get_data.close()

#get_du_lieu
url_api = "https://dasuperstore1.myshopify.com/admin/products.json"
data = requests.get(url_api, headers = {'User-agent': 'your bot 0.1'}, cookies = jar).json()

#convert_du_lieu
products = list()
product_data = dict()
for product in data['products']:
    product_data['id'] = product['id']
    product_data['name'] = product['title']
    products.append(product_data)

print(products)
