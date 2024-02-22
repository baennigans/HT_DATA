import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


print("Practice #1")
driver.get("http://www.naver.com")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/ul/li[3]/a").click()
time.sleep(1)
title = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/ul/li[4]/a").text
print(title)


time.sleep(2)
print("Practice #2")
driver.get("https://m.land.naver.com/search")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div/form/div/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div/form/div/div/input").send_keys("압구정동 현대3차")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div/form/div/button/span").click()
time.sleep(1)
salesPrices = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]").text
jeonse = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]").text
print(salesPrices)
print(jeonse)


time.sleep(2)
print("Practice #3")
driver.get("https://m.finance.daum.net/quotes/A005380/influential_investors/trader")
time.sleep(1)
name = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/article[2]/div[1]/div[1]/div/div/p/a").text
money = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/article[2]/div[1]/div[1]/div/div/div[2]/strong").text
print(name)
print(money)


time.sleep(2)
print("Practice #4")
driver.get("https://finance.naver.com/sise/")
time.sleep(1)
for i in range(1,9):
    company = driver.find_element(By.XPATH, f"/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/ul[1]/li[{i}]/a").text
    price = driver.find_element(By.XPATH, f"/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/ul[1]/li[{i}]/span").text
    print('company : ',company)
    print('price   : ',price)
    print('---------------------------')