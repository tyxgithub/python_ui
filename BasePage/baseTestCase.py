from selenium import webdriver
import unittest
from time import sleep


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print ("测试开始")
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
    @classmethod
    def tearDownClass(self):
        sleep(3)
        self.driver.close()
        print("测试结束\n")
