from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# options.add_argument("--window-size = 200, 300")
# options.add_argument("--start-fullscreen")
# options.add_argument("--blink-settings=imagesEnabled=false")
# options.add_argument("--mute-audio")

options = Options()
options.add_argument("--window-size = 1600, 900") # 브라우저 최대화
options.add_experimental_option("detach", True) # 실행이 끝나도 화면이 꺼지지 않음
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 불필요한 오류메시지 제거

driver = webdriver.Chrome(options = options)

driver.implicitly_wait(3)

# driver = webdriver.Chrome()
driver.get("https://www.google.com/")
# driver.find_element(By.CSS_SELECTOR, "#q").send_keys("파이썬")
# driver.find_element(By.CSS_SELECTOR, ".btn_ksearch").click()
# items = driver.find_elements(By.CSS_SELECTOR, "a.keyword")

search_box = driver.find_element(By.CSS_SELECTOR, "textarea.gLFyf")
search_box.click()
search_box.send_keys("푸바오 레전드")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
# <h3 class="LC20lb MBeuO DKV0Md">[Python] selenium 엔터키 입력 - Developer_TaeHui - 티스토리</h3>
items = driver.find_elements(By.CSS_SELECTOR, "h3.LC20lb MBeuO DKV0Md")
for item in items:
    print(item.text)
    print(item.get_attribute("class"))
    print("--------------------------------")

