import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner
from TestCase.test_login import TestLogin
from TestCase.test_systemlog import TestSystemLog

class Createreport():
    def cre(self,*args):
        suit=unittest.TestSuite()
        for arg in args:
            suit.addTest(arg)
        # suit.addTest(Test("test_02"))
        # discover=unittest.TestLoader().discover(start_dir=path,pattern="test_*")
        now=time.strftime("%Y-%m-%d %H-%M-%S")
        print (now)
        report_dir="./report/"
        dirname=report_dir+now+"report.html"
        with open(dirname,"wb") as f:
            runner=HTMLTestRunner(stream=f,title="Test Report",description='s')
            # runner.run(discover)
            runner.run(suit)
list=[TestLogin("test_01_falseusername"),TestLogin("test_02_falsepasswd"),
      TestLogin("test_03_trueusername"),TestLogin("test_04_syslog")]
Createreport().cre(*list)

