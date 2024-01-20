from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars') #this will datable info bars.
    options.add_argument('start-maximized') #start browsers with maximized window size
    options.add_argument('disable-dev-shm-usage') #disable particular issues with browser on linux computers.
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=options)
    web_page_url = "https://automated.pythonanywhere.com/"
    driver.get(web_page_url)
    return driver
def main():
    driver = get_driver()
    element = driver.find_element(by = 'xpath', value="/html/body/div[1]/div/h1[1]")

    return element.text
print(main())
