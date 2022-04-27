from selenium import webdriver
import time
import os
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from public.web.wukongcrm.login import Mylogin



class TestShouye(unittest.TestCase):
    def setUp(self):  #初始化方法，每次都会最先执行
        self.driver=webdriver.Chrome()
        self.driver.get('http://101.133.169.100:8088/index.html')
        self.driver.maximize_window()
        time.sleep(10)

        print("start_time:"+time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time())))  #打印用例开始执行时间
    def tearDown(self):   #最后执行。每次用例执行完后都会截图
        file_dir="D:/test/screenshot/"   #截图路径
        if not os.path.exists(file_dir):    #路径不存在就创建一个该路径
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
            screen_name = file_dir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"  #截图以结束时间命名，以防止覆盖
            self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()
    def testShouye01_01(self):
        '''测试首页导航文案是否显示正确'''
        Mylogin(self.driver).login()
        self.driver.implicitly_wait(60)
        # 主页导航栏
        bangong = self.driver.find_element_by_xpath('//a[@class="nav-item router-link-active"]/div').text
        print(bangong)  # 办公
        kehuguanli= self.driver.find_element_by_xpath('//i[@class="wukong wukong-customer"]/../div').text
        print(kehuguanli)  # 客户管理
        shangyezhineng= self.driver.find_element_by_xpath('//i[@class="wukong wukong-statistics"]/../div').text
        print(shangyezhineng)  # 商业智能
        xiangmuguanli= self.driver.find_element_by_xpath('//i[@class="wukong wukong-project"]/../div').text
        print(xiangmuguanli)  # 项目管理
        kaitongshouquan= self.driver.find_element_by_xpath('//button[@class="auth-button el-popover__reference"]').text
        print(kaitongshouquan)  # 开通授权
        # zhezhao = self.driver.find_element_by_xpath(
        #     '//div[@style="justify-content: center; align-items: center; font-size: 12.16px;"]/div').text
        # print(zhezhao)  # 哲曌
        self.assertEqual("办公",bangong)
        self.assertEqual("客户管理",kehuguanli)
        self.assertEqual("商业智能",shangyezhineng)
        self.assertEqual("项目管理",xiangmuguanli)
        self.assertEqual("开通授权",kaitongshouquan)
        # self.assertEqual("哲曌",zhezhao)

    def testShouye01_02(self):
        '''测试首页办公文案是否显示正确'''
        Mylogin(self.driver).login()
        self.driver.implicitly_wait(60)
        # self.driver.find_element_by_xpath('//a[@class="nav-item router-link-active"]/div').click()
        # 办公界面导航栏
        kuaisuchuangjian = self.driver.find_element_by_xpath('//div[@class="button-name"]').text
        print(kuaisuchuangjian)  # 快速创建
        gongzuotai = self.driver.find_element_by_xpath('//i[@class="wukong wukong-workbench"]/../span').text
        print(gongzuotai)  # 工作台
        richeng = self.driver.find_element_by_xpath(
            '//i[@class="wukong wukong-schedule"and@style="color: rgb(190, 190, 192); font-size: 16px;"]/../span').text
        print(richeng)  # 日程
        renwu = self.driver.find_element_by_xpath(
            '//i[@class="wukong wukong-task"and@style="color: rgb(190, 190, 192); font-size: 16px;"]/../span').text
        print(renwu)  # 任务
        gonggao = self.driver.find_element_by_xpath(
            '//i[@class="wukong wukong-notice"and@style="color: rgb(190, 190, 192); font-size: 16px;"]/../span').text
        print(gonggao)  # 公告
        self.assertEqual("快速创建", kuaisuchuangjian)
        self.assertEqual("工作台", gongzuotai)
        self.assertEqual("日程", richeng)
        self.assertEqual("任务", renwu)
        self.assertEqual("公告", gonggao)

    def testShouye01_03(self):
        '''测试首页快速创建文案是否显示正确'''
        Mylogin(self.driver).login()
        self.driver.implicitly_wait(60)
        ele = self.driver.find_element_by_xpath('//div[@class="button-name"]')
        ActionChains(self.driver).move_to_element(ele).perform()  # 鼠标放在快速创建
        quanbu = self.driver.find_element_by_id('tab-0').text
        print(quanbu)  # 全部
        rizhi = self.driver.find_element_by_id('tab-1').text
        print(rizhi)  # 日志
        shenpi = self.driver.find_element_by_id('tab-5').text
        print(shenpi)  # 审批
        renwu = self.driver.find_element_by_id('tab-4').text
        print(renwu)  # 任务
        richeng = self.driver.find_element_by_id('tab-2').text
        print(richeng)  # 日程
        gonggao = self.driver.find_element_by_id('tab-3').text
        print(gonggao)  # 公告
        self.assertEqual("全部", quanbu)
        self.assertEqual("日志", rizhi)
        self.assertEqual("审批", shenpi)
        self.assertEqual("任务", renwu)
        self.assertEqual("日程", richeng)
        self.assertEqual("公告", gonggao)
if __name__=="_main_":
    unittest.main()



