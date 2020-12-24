'''测试系统日志'''
from time import sleep
import unittest

from BasePage.baseTestCase import BaseTestCase
from PageObject.systemLogPage import systemLogPage
from TestCase.test_login import TestLogin


class TestSystemLog(unittest.TestCase):
    def syslogObject(self):
        self.driver=TestLogin().returnDriver()
        sl=systemLogPage(self.driver)
        return sl
    def test_04_syslog(self):
        sl=self.syslogObject()
        sl.clickSysLog()
        sl.clickModule()    #点击模块
        sl.clickOption("平台层/导入管理")  #选择导入管理
        sl.clickButton()  #点击确定按钮
        text=sl.getOperaValue()
        self.assertIn("平台层/导入管理@平台层: ",text)
        print('用例:测试选择操作模块，日志正确打印，执行成功')

