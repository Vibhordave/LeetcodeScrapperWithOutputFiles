from bs4 import BeautifulSoup
import time
# from openpyxl import Workbook
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

siteUrl = 'https://leetcode.com/problemset/all/'
questionNameList = []
questionUrlList = []
questionDifficultyList = []


def xcelSheet():
    df = pd.DataFrame({
        'Question Url': questionUrlList
    })
    wordfilename = 'Leetcode.txt'
    
    with open(wordfilename, 'w') as f:
        for i in range(0, df.__len__()):
            f.write(df['Question Url'][i] + '\n')
    
    print("-----------> Word file created")


def openBrowser(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument("--disable-javascript")
    s = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get(url)
    driver.maximize_window()
    return driver


def closeBrowser(driver):
    driver.close()



def fetchPageData(pageUrl,x):
    sleepTime = 3
    driver = openBrowser(pageUrl)
    # Wait for 7 seconds to ensure the page is fully loaded
    time.sleep(5)
    if pageUrl != driver.current_url:
        print("wrong case terminating")
        print(pageUrl)
        print(driver.current_url)
        fetchPageData(pageUrl,x)
    links = driver.find_elements(By.TAG_NAME, "a")
    for i in links:
        try:
            # Check if '/problems/' is in the href of the 'a' element
            if "/problems/" in i.get_attribute("href") and "/editorial/" not in i.get_attribute("href"):
                questionUrl = i.get_attribute("href")
                questionUrl = 'https://leetcode.com' + questionUrl
                questionUrlList.append(questionUrl)
        except:
            pass
    closeBrowser(driver)
    print(f"-----------> Done{x}")
    x+=1

def getData():
    browser = openBrowser(siteUrl)
    time.sleep(2)
    pageSource = browser.page_source
    print(f"title is: {browser.title}")
    soup = BeautifulSoup(pageSource, 'html.parser')

    nav_component = soup.find('nav', class_='mb-6 md:mb-0 flex flex-nowrap items-center space-x-2')
    buttons = nav_component.find_all('button')

    totalPage = int(buttons[-2].text)
    print(f"Total {totalPage} pages available")
    closeBrowser(browser)

    for page in range(1, totalPage + 1):
        pageUrl = siteUrl + '?page=' + str(page)
        fetchPageData(pageUrl,page)

    print("-----------> Done all pages")
    print(f"Total {questionUrlList.__len__()} questions fetched")
    


getData()
questionUrlList=list(set(questionUrlList))
xcelSheet()
