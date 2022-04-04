from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

s = Service('/Users/shakayahaya/Desktop/chromedriver')
driver = webdriver.Chrome(service=s)
IG_USERNAME = 'thechillnationsweden'
IG_PASSWORD = 'childofgod1'
IG_URL = 'https://www.instagram.com/'
driver.get(IG_URL)
time.sleep(10)
cookie_accept = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
cookie_accept.click()
time.sleep(10)
user_name = driver.find_element(By.NAME, 'username')
user_name.send_keys(IG_USERNAME)
time.sleep(10)
password = driver.find_element(By.NAME, 'password')
password.send_keys(IG_PASSWORD)
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(5)
search = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('djlvpage')
time.sleep(10)
search.send_keys(Keys.ENTER)
time.sleep(3)
search.send_keys(Keys.ENTER)
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(10)
followers = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[1]/div/h1')
followers.click()
time.sleep(10)
i_frame = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
time.sleep(5)
follow_btn = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul/div/li[2]/div/div[2]')
time.sleep(10)
while True:
    Follow_Button = driver.find_elements(By.XPATH, "//*[text()='Follow']")
    print(Follow_Button)
    # Follow_Button.click()
    num = 0
    for x in Follow_Button:
        time.sleep(5)
        x.click()
        num += 1
        time.sleep(60)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", i_frame)
    time.sleep(random.randint(500, 1000) / 1000)

# follow_btn=driver.find_elements(By.XPATH,'//*[@id="f5a97473a5c54c"]/button')
# print(len(follow_btn))
