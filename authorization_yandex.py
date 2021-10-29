import time
from yandex import login, password
from selenium import webdriver

def authorization_yandex():
    driver = webdriver.Chrome(executable_path=r'C:\Program Files\webdriver\chromedriver.exe')
    driver.get('https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fpassport.yandex.ru%2Fprofile&noreturn=1')
    elem = driver.find_element_by_name('login')
    time.sleep(2)
    elem.send_keys(login)
    elem.send_keys(webdriver.common.keys.Keys.ENTER)
    time.sleep(3)
    elem = driver.find_element_by_name('passwd')
    elem.send_keys(password)
    elem.send_keys(webdriver.common.keys.Keys.ENTER)
    time.sleep(2)
    driver.close()
    driver.quit()
    return

if __name__ == '__main__':
    authorization_yandex()