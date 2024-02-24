# 5페이지까지 한번에 가기 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

service = Service()
options = webdriver.ChromeOptions()
#url = "https://www.e-himart.co.kr/app/display/showDisplayCategory?dispNo=1011030000#pageCount=2"
driver = webdriver.Chrome(service=service,options=options)

prdLinks=[]
prdNames = []
prdPrices = []
prdDelivery = []
prdRatings = []
prdImages = []
imageNames = []
# time.sleep(sec)
pages = []


for i in range(0,5):
    try:
        
        url = "https://www.e-himart.co.kr/app/display/showDisplayCategory?dispNo=1011030000#pageCount={}".format(i+1)
        driver.get(url)
        top = driver.find_element(By.CLASS_NAME,"cateWrap")
        uls = top.find_element(By.ID,"productList")
        lis = uls.find_elements(By.TAG_NAME,"li")

        for idx, li in enumerate(lis):
            page = i+1          
            pages.append(page)

            imgs = li.find_element(By.TAG_NAME,"img")
            imgsrc = imgs.get_attribute("src")
            imgres = requests.get(imgsrc)
            imageName = "./02.Selenium_himart/page{1}_prd{0}.jpg".format(idx+1,page)
            with open(imageName,"wb") as f:
                f.write(imgres.content)
            prdImages.append(imageName)            
            time.sleep(0.2)
            prdNames.append(li.find_element(By.CLASS_NAME,"prdName").text)
            prices = li.find_elements(By.CLASS_NAME,"discountPrice")
            if len(prices) % 2 == 0:
                prdPrices.append(prices[1].text)
            else:
                prdPrices.append(prices[0].text)
            prdLinks.append(li.find_element(By.TAG_NAME,"a").get_attribute("href"))
            try:
                prdDelivery.append(li.find_element(By.CLASS_NAME,"delivery").text)
            except:
                prdDelivery.append("-")
            try:
                rating = li.find_element(By.CLASS_NAME,"ratingPoint").text
                prdRatings.append(rating)        
            except:
                prdRatings.append("-")    
            time.sleep(0.2)
    except Exception as e:  
        pass


import pandas as pd

final = pd.DataFrame({'페이지':page,'이름':prdNames,'가격':prdPrices,'별점':prdRatings,'링크':prdLinks})
final.to_csv('하이마트_냉장고.csv',encoding='euc-kr')
final