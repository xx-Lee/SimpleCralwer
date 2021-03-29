import time
from bs4 import BeautifulSoup
import subprocess
from selenium import webdriver
import shutil
import datetime


def KS_Crawler():
    print("Start: ksCrawler")

    #Chrome 쿠키 삭제
    try:
        shutil.rmtree(r"c:\chrometemp")
    except FileNotFoundError:
        pass



    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    #option.add_argument('window-size=1920x1080')
    option.add_argument("disable-gpu")
    driver = webdriver.Chrome('c:/chromedriver/chromedriver', options=option)

    url = 'https://klayswap.com/dashboard'
    driver.get(url)

    # 데이터 로딩 시간 대기
    time.sleep(10)

    html = driver.page_source
    driver.close()
    driver.quit()

    # chormder 드라이버 프로세스 죽이기
    subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")

    bs = BeautifulSoup(html, 'html.parser')
    pools = bs.find_all('div', {'class': 'dashboard-page__pairs-table__row'})

    listVal = []
    listName = []

    now = datetime.datetime.now()
    format = '%Y-%m-%d %H:%M:%S'
    now = now.strftime(format)

    for pool in pools:
        name = pool.find('div', {'class': 'dashboard-page__pairs-table__col dashboard-page__pairs-table__col--pair'}).p.strong.text
        kspDistriRatio = float(pool.find('p', {'class': 'total-mining'}).span.span.text.strip().replace(" ", "")[:-1])
        feeDistriRatio = float(pool.find('p', {'class': 'annual-fee'}).span.span.text.strip()[:-1])
        listVal.append((now, name, kspDistriRatio, feeDistriRatio))
        listName.append(name)

    #출력 테스트(크롤링 시간, KSP 분배율, 수수료 분배율)
    for i in range(len(listVal)):
        print(listVal[i])

KS_Crawler()