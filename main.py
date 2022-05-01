#main.py
from time import sleep
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from bs4 import BeautifulSoup

DRIVER_PATH = 'C:\\Users\\rmrey\\shitty apps\\ChromeDriver\\chromedriver.exe'
main_url = 'https://www.escapefromtarkov.com/cash'

options = Options()
options.headless = True
options.add_argument('--window-size=1920,1200')

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

def find_results(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    titles = soup.find_all(class_='title')

    result = [title.find(class_='text').text for title in titles]
    result.extend(soup.find(class_='count'))
    result.extend(soup.find(class_='count_left'))

    return result

if __name__ == '__main__':
    while True:
        driver.refresh()
        main_result =datetime.now(), '--', find_results(main_url)
        final_result = ' '.join(str(v) for v in main_result)

        print(final_result, end='\r')
        sleep(10)
