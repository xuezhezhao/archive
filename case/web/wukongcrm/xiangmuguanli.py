import unittest
from selenium import webdriver
import time
import os
from public.web.wukongcrm.login import Mylogin




class XiangMuguanli(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://101.133.169.100:8088/index.html')
        self.driver.maximize_window()
        time.sleep(3)
        print("start_time:"+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
    def tearDown(self):
        file_dir = "D:/test/悟空crm截图/"
        if not os.path.exists(file_dir):
            os.makedirs(os.path.join('D:/', 'test', '悟空crm截图'))
        print("end_time:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = file_dir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()
    def testXiangmu01_01(self):
        '''测快速创建项目后工作台显示信息是否正确'''
        Mylogin(self.driver).login()
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath('//i[@class="wukong wukong-project"]/../div').click()  #点击项目管理
        self.driver.find_element_by_xpath('//i[@class="button-mark el-icon-plus"]').click()    #点击创建项目
        self.driver.find_element_by_xpath('//div[@class="el-input el-input--prefix"]/input').send_keys('晚上登日项目')#输入项目名称
        self.driver.find_element_by_xpath('//div[@class="el-card__body"and@style="height: 100%;"]/div/div[2]/div[5]/button[1]').click()  #确定
        a=self.driver.find_element_by_xpath("//li[contains(text(),'登日')]").text
        print(a)

        self.assertEqual(a,'晚上登日项目')
if __name__=="__main__":
    unittest.main()
