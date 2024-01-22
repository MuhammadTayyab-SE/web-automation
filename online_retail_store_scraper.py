from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars') #this will datable info bars.
    options.add_argument('start-maximized') #start browsers with maximized window size
    options.add_argument('disable-dev-shm-usage') #disable particular issues with browser on linux computers.
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=options)
    web_page_url = "https://titan22.com/account/login?return_url=%2Faccount"
    driver.get(web_page_url)
    return driver

def main():
    driver = get_driver()
    driver.find_element(by = 'id', value='CustomerEmail').send_keys('tayyab@gmail.com')
    driver.find_element(by = 'id', value='CustomerPassword').send_keys('damage123' + Keys.RETURN)
    time.sleep(3)
    
    driver.find_element(by = 'xpath', value='/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
    time.sleep(5)
main()