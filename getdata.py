import pandas as pd
import requests as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 🔹 Chrome WebDriver 설정 및 실행
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 브라우저 창 없이 실행하려면 활성화 (테스트 후 제거 가능)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

data = []

# 웹 요청시 차단 방비 agent 추가
headers = {"User_Agent": "Mozilla/5.0"}
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# for page in range(1, 112):
    
for page in range(1, 2):
    # YES24 베스트셀러 페이지 URL(1페이지)
    url = f"https://www.jobkorea.co.kr/Search/?stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&tabType=recruit&Page_No={page}"

    driver.get(url)

    # 응답 확인
    for i in range(1, 21):
        print(f"Page {page} - company {i} is start!")
        driver.implicitly_wait(5)
        company = driver.find_element(By.CSS_SELECTOR, f"#dev-content-wrap > article > section.content-recruit.on > article.list > article:nth-child({i}) > div.list-section-information > div > a")
        company.click()
        driver.switch_to.window(driver.window_handles[-1])

        try:
            company_name = driver.find_element(By.CSS_SELECTOR, f"#container > section > div.readSumWrap.clear > article > div.sumTit > h3 > div > span").text
        except:
            company_name = ""

        try:
            job_notice_title = driver.find_element(By.XPATH, '/html/body/div[5]/section/section/div[1]/article/div[1]/h3').text
            job_notice_title = job_notice_title.split("\n")[-1]
        except:
            job_notice_title = ""

        try:
            career = driver.find_element(By.CSS_SELECTOR, f"#container > section > div.readSumWrap.clear > article > div.tbRow.clear > div:nth-child(1) > dl > dd:nth-child(2) > strong").text
        except:
            career = ""

        try:
            education = driver.find_element(By.CSS_SELECTOR, f"#container > section > div.readSumWrap.clear > article > div.tbRow.clear > div:nth-child(1) > dl > dd:nth-child(4) > strong").text
        except:
            education = ""

        try:
            permanent_worker = driver.find_element(By.CSS_SELECTOR, f"#container > section > div.readSumWrap.clear > article > div.tbRow.clear > div:nth-child(2) > dl > dd:nth-child(2) > ul > li > strong").text
        except:
            permanent_worker = ""

        try:
            company_location = driver.find_element(By.CSS_SELECTOR, f"#container > section > div.readSumWrap.clear > article > div.tbRow.clear > div:nth-child(2) > dl > dd:nth-child(6) > a").text
        except:
            company_location = ""

        
        data.append({"company_name": company_name, "job_notice_title": job_notice_title, "career": career,
                        "education": education, "permanent_worker": permanent_worker, "company_location": company_location})

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        print(f"Page {page} - company {i} is finished!")

driver.close()
print("All Works are Finished!")

df = pd.DataFrame(data)
df.to_csv("test.csv")
