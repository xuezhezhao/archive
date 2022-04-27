from selenium import webdriver
import time
import os
import unittest
from public.web.wukongcrm.login import Mylogin
from public.web.wukongcrm.kuaisuchuangjian import Kuaisuchuangjian

class GongGao(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://101.133.169.100:8088/index.html')
        self.driver.maximize_window()
        time.sleep(3)
        print('start_time:'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
    def tearDown(self):
        file_dir='D:/test/悟空crm截图/'
        if not os.path.exists(file_dir):
            os.makedirs(os.path.join('D:/','test','悟空crm截图'))
            screen_name=file_dir+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()
    def testGonggao01_01(self):
        '''测试公告为空时提示是否显示正确'''
        Mylogin(self.driver).login()
        self.driver.implicitly_wait(60)
        Kuaisuchuangjian(self.driver).gonggao()
        self.driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()  #点击提交
        a=self.driver.find_element_by_xpath('//div[@class="el-form-item is-error is-required el-form-itemtitle"]/div/div[2]').text  #公告标题不能为空
        print(a)
        b=self.driver.find_element_by_xpath('//div[@class="el-form-item is-error is-required el-form-itemstartTime"]/div/div[2]').text  #不能为空
        print(b)
        c=self.driver.find_element_by_xpath('//div[@class="el-form-item is-error is-required el-form-itemcontent"]/div/div[2]').text  #  公告正文不能为空
        print(c)
        self.assertIn('公告标题不能为空',a)
        self.








        ('不能为空',b)
        self.assertEqual('公告正文不能为空',c)
    def testGonggao01_02(self):
        '''测试快速创建公告后工作台是否显示正确'''
        Mylogin(self.driver).login()
        self.driver.implicitly_wait(60)
        Kuaisuchuangjian(self.driver).gonggao()
        self.driver.find_element_by_xpath('//form[@class="el-form"]/div[1]/div/div/input').send_keys("热烈庆祝中国共产党成立100周年")  #输入公告标题
        self.driver.find_element_by_xpath('//div[@class="add-item"]').click()  #点击添加
        self.driver.find_element_by_id('tab-dep').click()   #点击部门

        self.driver.find_element_by_xpath('//div[@id="pane-dep"]/div[2]/div[2]/label/span/span').click()   #点击总经办
        self.driver.find_element_by_xpath('//div[@class="popover-footer"]/button[1]').click()     #点击确定
        # self.driver.find_element_by_xpath('//div[@class="el-form-item is-error is-required el-form-itemstartTime"]/div/div[1]/input').clear()  #清除开始时间

        self.driver.find_element_by_xpath('//div[@class="el-form-item is-error is-required el-form-itemstartTime"]/div/div[1]/input').send_keys('2021-07-02')#输入开始时间

        # self.driver.find_element_by_xpath('//div[@class="el-form-item is-required el-form-itemendTime"]/div/div[1]/input').clear()    #清除结束时间

        self.driver.find_element_by_xpath('//div[@class="el-form-item is-required el-form-itemendTime"]/div/div[1]/input').send_keys('2021-07-05')   #输入结束时间
        self.driver.find_element_by_xpath('//textarea[@class="el-textarea__inner"]').send_keys("觉醒年代")   #输入公告正文
        self.driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()  # 点击提交
        self.driver.find_element_by_xpath('//i[@class="wukong wukong-workbench"]/../span').click    #点击工作台
        a=self.driver.find_element_by_xpath('//div[@id="pane-0"]/div/div[1]/div[2]/div[1]/p/span[1]').text   #工作台第一个   创建人文本
        print(a)
        b=self.driver.find_element_by_xpath('//div[@id="pane-0"]/div/div[1]/div[2]/div[1]/p/span[2]').text    #工作台第一个  “添加了XX文本”
        print(b)
        c=self.driver.find_element_by_xpath('//div[@id="pane-0"]/div/div[1]/div[2]/div[3]/span').text    #工作台第一个   内容文本
        print(c)
        self.assertEqual("薛哲曌",a)
        self.assertEqual("添加了公告",b)
        self.assertIn("共产党",c)
        # a=self.driver.find_element_by_xpath('//div[@id="notice-cell0"]/div/div[2]/p[1]').text   # 公告下第一个公告得发起人名字
        # print(a)
        # b=self.driver.find_element_by_xpath('//div[@id="notice-cell0"]/div[2]').text    #公告下第一条公告得标题
        # print(b)
        # c=self.driver.find_element_by_xpath('//div[@id="notice-cell0"]/div[3]').text     #公告下第一条公告得内容
        # print(c)
        # self.assertIn('庆祝',b)
        # self.assertIn('年代',c)


    # def testGonggao01_03(self):
    #     Mylogin(self.driver).login()
    #     Kuaisuchuangjian(self.driver).gonggao()
    #









if __name__=="__main__":
    unittest.main()