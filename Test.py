from selenium import webdriver
import time

driver_path = './chromedriver'
browser = webdriver.Chrome(driver_path)

url = 'http://www.ygfamily.com/'
browser.get(url)

print('標題', browser.title)
print('網址', browser.current_url)
print('內容', browser.page_source[:50])
print('視窗', browser.get_window_rect())

browser.save_screenshot('./screenshot.jpg')
time.sleep(3)
browser.set_window_rect(200,100,500,250)
time.sleep(3)
browser.fullscreen_window()