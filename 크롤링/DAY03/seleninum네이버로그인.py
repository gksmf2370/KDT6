from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# User agnet 정보 추가
agent_option = webdriver.ChromeOptions()
user_agent_string = 'Mozilla/5.0'
agent_option.add_argument('user-agent=' + user_agent_string)

driver = webdriver.Chrome(options=agent_option)
driver.get('https://nid.naver.com/nidlogin.login')

# <input>의 이름이 id를 검색
driver.find_element(By.NAME, 'id').send_keys('gksmf2370')
driver.find_element(By.NAME, 'pw').send_keys('xxxxxxxxx')


#//*[@id="log.login"]
#driver.find_element(By.XPATH,'//*[@id="log.login"]').click()
driver.find_element(By.ID, 'log.login').click()
time.sleep(3)
driver.quit()