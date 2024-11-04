import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "path_to_chromedriver"  
service = Service(chrome_driver_path)

# 웹 드라이버 실행
driver = webdriver.Chrome()

# Watcha 영화 리뷰 페이지로 이동
url = 'https://pedia.watcha.com/ko-KR/contents/mdEmwEl/comments'
driver.get(url)

# 페이지 로딩 대기
time.sleep(3)

with open('watcha_reviews_rebeca.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(['평점', '리뷰'])

    # 페이지 로딩 대기
    time.sleep(3)

    # 스크롤을 내려서 추가 리뷰를 로딩
    for i in range(40):  # 원하는 만큼 스크롤 (숫자를 늘리면 더 많은 리뷰를 가져옴)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # 리뷰 평점과 내용 크롤링
    reviews = driver.find_elements(By.CLASS_NAME, 'NrA8QHzP')  # 리뷰가 들어 있는 클래스 
    ratings = driver.find_elements(By.CLASS_NAME, "aytsxOVO")  # 평점이 들어 있는 클래스

    # 리뷰와 평점을 출력 및 CSV에 저장
    for i in range(min(len(reviews), len(ratings))):
        review_text = reviews[i].text
        rating_score = ratings[i].text
        
        
        writer.writerow([rating_score, review_text])

        if i% 50 == 0:
            print(f"평점: {rating_score}, 리뷰: {review_text}")
            print("-" * 50)

# 드라이버 종료
driver.quit()
