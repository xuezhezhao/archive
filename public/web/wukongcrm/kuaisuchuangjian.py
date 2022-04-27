import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd




class Kuaisuchuangjian(object):
    def __init__(self,driver):
        self.driver=driver
    def gonggao(self):
        ele = self.driver.find_element_by_xpath('//div[@class="button-name"]')  # 鼠标停在快速创建上
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@class="quick-add-content"]/p[5]/span').click()  # 点击公告
        time.sleep(3)

    def rizhi(self):
        ele = self.driver.find_element_by_xpath('//div[@class="button-name"]')  # 鼠标停在快速创建上
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@class="quick-add-content"]/p[1]/span').click()  # 点击公告
        time.sleep(3)
    def shenpi(self):
        ele = self.driver.find_element_by_xpath('//div[@class="button-name"]')  # 鼠标停在快速创建上
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@class="quick-add-content"]/p[2]/span').click()  # 点击公告
        time.sleep(3)
    def renwu(self):
        ele = self.driver.find_element_by_xpath('//div[@class="button-name"]')  # 鼠标停在快速创建上
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@class="quick-add-content"]/p[3]/span').click()  # 点击公告
        time.sleep(3)
    def richeng(self):
        ele = self.driver.find_element_by_xpath('//div[@class="button-name"]')  # 鼠标停在快速创建上
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@class="quick-add-content"]/p[4]/span').click()  # 点击公告
        time.sleep(3)