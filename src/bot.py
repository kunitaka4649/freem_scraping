import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Bot():
    def __init__(self, driver):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--lang=ja')
        self.driver = webdriver.Chrome(executable_path=driver, options=options)

    def get(self, url):
        try:
            self.driver.get(url)
        except:
            self.driver.quit()

    def back(self):
        try:
            self.driver.back()
        except:
            self.driver.quit()

    def login(self, login_page, login_id_xpath, login_id, login_pw_xpath, login_pw, login_done_xpath):
        try:
            self.driver.get(login_page)
            time.sleep(1)
            # ID/PASSを入力
            id = self.driver.find_element_by_xpath(login_id_xpath)
            id.send_keys(login_id)
            password = self.driver.find_element_by_xpath(login_pw_xpath)
            password.send_keys(login_pw)

            time.sleep(1)

            # ログインボタンをクリック
            login_button = self.driver.find_element_by_xpath(login_done_xpath)
            login_button.click()
        except:
            self.driver.quit()