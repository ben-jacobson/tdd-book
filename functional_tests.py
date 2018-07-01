from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
sleep(2)

browser.set_page_load_timeout(30)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

browser.close()
