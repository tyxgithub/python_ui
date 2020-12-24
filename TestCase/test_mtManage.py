from selenium.webdriver.common.keys import Keys

from BasePage.baseTestCase import BaseTestCase
from PageObject.loginPage import LoginPage
from PageObject.mtManagePage import Mtmanage
import unittest

class mtManage(BaseTestCase):
    def mtObject(self):
        mt=Mtmanage(self.driver)
        return mt
    def lgObject(self):
        lg=LoginPage(self.driver)
        return lg
    def test_01_login(self):     #登录
        lg=self.lgObject()
        lg.open_url()
        lg.input_username('tyx')
        lg.input_password('tyx')
        lg.login_click()
        print ("用例：登录成功")
    def test_02_mt(self):
        mt=self.mtObject()
        mt.clickMt()
        self.assertEqual(mt.mtName(),'多租户管理')
        print ("用例：点击进入多租户管理页面")
    def test_03_spaceStr(self):  #租户名称为空
        mt = self.mtObject()
        mt.createTenant()
        mt.selectMp()
        mt.insertMp('tyx')
        mt.firstCheckBox()
        mt.sureButton0()
        mt.tenantFunction()
        mt.tenantQx()
        mt.qxSure()
        mt.tableSelect()
        mt.qx1Button()
        mt.qx1Sure()
        mt.tenantDesc('zuhumiaoshushdhshdh')
        mt.sureLoc()
        self.assertEqual(mt.tenantNameerror(),'请输入租户名称')
        print ("用例：租户名称为空，新建失败")
    def test_04_zeroStr(self):  #租户名称，空字符
        mt = self.mtObject()
        mt.tenantName(Keys.SPACE)
        mt.sureLoc()
        self.assertEqual(mt.alertText(),'租户名称、描述不能为空')
        print ("用例:租户名称为空字符，新建失败")
    def test_05_createTenantSc(self):  #租户名称新建成功
        mt = self.mtObject()
        name="haq11"
        mt.tenantName(name)
        mt.sureLoc()
        self.assertIn('新建成功',mt.tenantScAlert())
        print ("用例：租户%s创建成功"%name)
    def test_06_deletefalse(self):
        mt = self.mtObject()
        mt.deleteTenantButton()
        mt.deleteTenantSure()
        self.assertIn('无法删除',mt.deleteFalse())
        print ('用例：租户存在元表，删除失败')






if __name__=='__main__':
    unittest.main()

