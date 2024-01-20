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
    web_page_url = "https://automated.pythonanywhere.com/login"
    driver.get(web_page_url)
    return driver

def extract_number_from_txt(string):
    return string.split(": ")[1]

def main():
    driver = get_driver()
    
    # defining username and password
    username = "automated"
    password = "automatedautomated"
    
    # adding username to username field
    driver.find_element(by = 'id', value="id_username").send_keys(username)
    driver.find_element(by = 'id', value="id_password").send_keys(password + Keys.RETURN)    
        
    time.sleep(2)

    driver.find_element(by = 'xpath', value="/html/body/nav/div/a")
    print(driver.current_url) # checking the current url of the webpage.

    # scraping the value single time after login
    element = driver.find_element(by='id',value = 'displaytimer')
    return "scraped value is: " + extract_number_from_txt(element.text)

print(main())
