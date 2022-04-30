#main.py
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from bs4 import BeautifulSoup

DRIVER_PATH = "'your driver path"
main_url = 'https://www.escapefromtarkov.com/cash'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

def find_results(url, result):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    titles = soup.find_all(class_='title')
    count = 0
    for title in titles:
        result.extend(title.find(class_='text'))
        if count < 1:
            result.extend(soup.find(class_='count'))
            result.extend(soup.find(class_='count_left'))
            count += 1

    return result

if __name__ == '__main__':
    print(find_results(main_url, []))
