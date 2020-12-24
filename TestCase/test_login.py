'''登录测试'''
from selenium.webdriver.common.by import By
from BasePage.baseTestCase import BaseTestCase
from PageObject.loginPage import LoginPage
import unittest
from PageObject.mtManagePage import Mtmanage
from selenium import webdriver
from time import sleep
import unittest
from PageObject.systemLogPage import systemLogPage



class TestLogin(BaseTestCase):
    def lgObject(self):
        lg =LoginPage(self.driver)
        return lg
    def syslogObject(self):
        sl=systemLogPage(self.driver)
        return sl
    def returnDriver(self):
        return self.driver
    def test_01_falseusername(self):
        lg=self.lgObject()
        lg.open_url()
        lg.input_username('tyx1')
        lg.input_password('tyx')
        lg.login_click()
        text="用户[tyx1]不存在,请检查用户名是否正确"
        self.assertIn(lg.alert(), text)
        sleep(2)
        lg.clear_password()
        lg.clear_username()
        # try:
        #     self.assertIn(lg.alert(),text)
        #     sleep(2)
        # except Exception as msg:
        #     print ("断言失败")
        #     raise
        # else:
        #     lg.clear_password()
        #     lg.clear_username()
        print('用例:测试错误用户名登录失败报错，执行成功')
        sleep(5)
    def test_02_falsepasswd(self):
        lg = self.lgObject()
        lg.input_username('tyx')
        lg.input_password('tyx1')
        lg.login_click()
        text="密码错误"
        self.assertIn(lg.alert(),text)
        lg.clear_username()
        lg.clear_password()
        print('用例:测试错误密码登录失败报错，执行成功')
        sleep(3)
    def test_03_trueusername(self):
        lg = self.lgObject()
        lg.input_username('tyx')
        lg.input_password('tyx')
        lg.login_click()

        print('用例:测试用户名密码正确登录成功，执行成功')
    def test_04_syslog(self):
        sl=self.syslogObject()
        sl.clickSysLog()
        sl.clickModule()    #点击模块
        sl.clickOption("平台层/导入管理")  #选择导入管理
        sleep(1)
        sl.clickButton()  #点击确定按钮
        sleep(2)
        text=sl.getOperaValue()
        self.assertIn("平台层/导入管理@平台层: ",text)
        print('用例:测试选择操作模块，日志正确打印，执行成功')






#
if __name__=='__main__':
    suit=unittest.TestSuite()
    suit.addTest(TestLogin('test_01_falseusername'))
    suit.addTest(TestLogin('test_02_falsepasswd'))
    suit.addTest(TestLogin('test_03_trueusername'))
    suit.addTest(TestLogin('test_04_syslog'))

    runner=unittest.TextTestRunner()
    runner.run(suit)
