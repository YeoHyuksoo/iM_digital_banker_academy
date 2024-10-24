from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv

# options.add_argument("--window-size = 200, 300")
# options.add_argument("--start-fullscreen")
# options.add_argument("--blink-settings=imagesEnabled=false")
# options.add_argument("--mute-audio")

def page_crawling(driver, csv_wr):
    items = driver.find_elements(By.CSS_SELECTOR, "div.product_info_area__xxCTi")
    time.sleep(1)

    print("items = ", len(list(items)))

    for item in items:
        name = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K").text
        print(name)
        try:
            price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
            print(price)
            link = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K > a") \
                .get_attribute("href")
            print(link)
            csv_wr.writerow([name, price, link])
        except:
            price = "NaN"
            link = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K > a") \
                .get_attribute("href")
            csv_wr.writerow([name, price, link])
        print("----------------------------------------------")
    return len(list(items))

def page_scroll(driver, before_h):
    while True:
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
        time.sleep(2)
        after_h = driver.execute_script("return window.scrollY")
        if after_h == before_h:
            break
        before_h = after_h

if __name__ == "__main__":

    options = Options()
    options.add_argument("--start-maximized") # 브라우저 최대화
    options.add_experimental_option("detach", False) # 실행이 끝나도 화면이 꺼지지 않음
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 불필요한 오류메시지 제거

    driver = webdriver.Chrome(options = options)

    f = open("selenium_data.csv", "wt", encoding = "utf-8", newline = '')
    csv_wr = csv.writer(f)

    driver.implicitly_wait(3)
    driver.get("https://shopping.naver.com/home")

    # search_box = driver.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
    # search_box = driver.find_element(By.CLASS_NAME, "_searchInput_search_text_3CUDs")
    search_box = driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
    search_box.click()
    search_box.send_keys("아이폰 16 프로")
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)

    total_n = 0
    page_n = 1
    while total_n <= 300:

        before_h = driver.execute_script("return window.scrollY")
        page_scroll(driver, before_h)

        n = page_crawling(driver, csv_wr)
        total_n += n

        page_n += 1

        for p_data in driver.find_elements(By.CSS_SELECTOR, ".pagination_num__b1BF2 > a"):
            if int(p_data.text) == page_n:
                p_data.click()
        # break

    driver.quit()
    f.close()

