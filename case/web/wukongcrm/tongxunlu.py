from selenium import webdriver
import time
from public.web.wukongcrm.login import Mylogin
from selenium.webdriver.common.keys import Keys
import unittest
import os


class TestTongxunlu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://101.133.169.100:8088/index.html')
        self.driver.maximize_window()
        time.sleep(3)
        print("start_time:"+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
    def tearDown(self):
        file_dir="D:/test/悟空crm截图/"
        if not os.path.exists(file_dir):
            os.makedirs(os.path.join('D:/', 'test', '悟空crm截图'))
            print("end_time:"+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
            screen_name=file_dir+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+".png"
            self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()
    def testTongxunlu01_01(self):
        '''测试通讯录搜索框使用是否正常'''
        Mylogin(self.driver).login()
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/div/ul/a[7]/li').click()
        self.driver.find_element_by_xpath('//div[@id="pane-1"]/div/input').send_keys('admin')
        self.driver.find_element_by_xpath('//div[@id="pane-1"]/div/input').send_keys(Keys.ENTER)
        user=self.driver.find_element_by_xpath("//div[@id='pane-1']/div[2]/div[2]/div[2]/div/div[1]").text
        print(user)
        bumen=self.driver.find_element_by_xpath("//div[@id='pane-1']/div[2]/div[2]/div[2]/div/div[2]/div[1]/span").text
        print(bumen)
        shoujihao=self.driver.find_element_by_xpath("//div[@id='pane-1']/div[2]/div[2]/div[2]/div/div[2]/div[3]/span").text
        print(shoujihao)
        self.assertEqual("admin",user)
        self.assertEqual("总经办",bumen)
        self.assertEqual("12312341234",shoujihao)
if __name__=="__main__":
    unittest.main()