import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
class Mylogin(object):
    def __init__(self,driver):
        self.driver=driver
    def login(self):
        self.driver.find_element_by_name('username').send_keys('17835422046')
        self.driver.find_element_by_name('password').send_keys('123456')
        self.driver.find_element_by_xpath("//button[@class='el-button submit-btn el-button--default']").click()


