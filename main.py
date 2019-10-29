import requests
from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://kurs.kz"
browser = webdriver.Firefox()
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')
result = ''

for price in soup.find_all('td', 'currency null'):
    result += 'Покупка: ' + price.find_next('span', {'title': 'USD - покупка'}).text + '   Продажа: ' + price.find_next('span', {'title': 'USD - продажа'}).text + '\n'

browser.close()

browser = webdriver.Firefox()

browser.get('https://mail.protonmail.com/')

time.sleep(3)
auth = browser.find_element_by_name('username')
auth.send_keys('user9181')

auth = browser.find_element_by_name('password')
auth.send_keys('!QA2ws3ed')

auth.send_keys(Keys.RETURN)

time.sleep(15)
browser.find_element_by_css_selector('.sidebar-btn-compose').click()

# Здесь он меняет формат отображения содержимого письма для возможности передавать данные в <textarea>, иначе не получилось
#
time.sleep(3)
browser.find_element_by_css_selector('.squireDropdown-item-label').click()
browser.find_element_by_xpath('/html/body/div[2]/form[1]/div/section/div/div[3]/div[2]/div[1]/nav/div[1]/div[4]/ul/li[5]').click()

time.sleep(1)
send_mail = browser.find_element_by_name('autocomplete')
send_mail.send_keys('some@dmail1.net')
send_mail = browser.find_element_by_xpath('/html/body/div[2]/form[1]/div/div[2]/div[5]/input')
send_mail.send_keys('Курс доллара к тенге')
send_mail = browser.find_element_by_xpath('/html/body/div[2]/form[1]/div/section/div/div[3]/div[2]/textarea')
send_mail.send_keys(result)

time.sleep(1)
browser.find_element_by_class_name('btnSendMessage-btn-action').click()

time.sleep(3)
browser.close()