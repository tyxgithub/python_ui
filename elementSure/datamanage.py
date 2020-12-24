from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from funtionTools.functionTools import elementWait

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get('http://10.100.2.32:8117/#/angularpanel/model/login')
        self.driver.maximize_window()
    @classmethod
    def tearDownClass(self):
        sleep(2)
        # self.driver.close()
    def test_a_usertrue(self):
        self.driver.find_element(By.CSS_SELECTOR, ".adinpt:nth-child(1) .lgipm").send_keys("tyx")   #输入用户名
        self.driver.find_element(By.CSS_SELECTOR, ".adinpt:nth-child(2) .lgipm").send_keys("tyx")   #输入密码
        self.driver.find_element(By.CLASS_NAME,'login-btn').click()                                 #点击登录
        sleep(1)
        muti_tenant_loc=(By.CSS_SELECTOR, ".icon-multi-tenant")  #多租户管理定位
        elementWait(self.driver,"多租户管理",muti_tenant_loc)
        self.driver.find_element(*muti_tenant_loc).click()
        sleep(1)

        #定位第一个租户的名称 loc=(By.XPATH,'//*[@id="j-container"]/app-tenant-management/div[1]/div[2]/div[1]/div/div[2]/span[2]/span')
        # print (self.driver.find_element(*loc).text)

        edit_tenant_loc=(By.XPATH,'//*[@id="j-container"]/app-tenant-management/div[1]/div[2]/div[1]/div/div[4]/span[1]')
        elementWait(self.driver,'编辑租户按钮',edit_tenant_loc)
        self.driver.find_element(*edit_tenant_loc).click()
        sleep(1)

        data_manage_loc=(By.ID, "202")  #数据管理
        elementWait(self.driver,'数据管理',data_manage_loc)
        self.driver.find_element(*data_manage_loc).click()
        sleep(1)

        # data_processing_loc=(By.CSS_SELECTOR, ".icon-analysis")  #数据加工
        # elementWait(self.driver,'数据加工',data_processing_loc)
        # self.driver.find_element(*data_processing_loc).click()
        # sleep(1)
        #
        # ai_laboratory_loc=(By.CSS_SELECTOR, ".icon-xiangmuguanli")  #AI实验室
        # elementWait(self.driver,'AI实验室',ai_laboratory_loc)
        # self.driver.find_element(*ai_laboratory_loc).click()
        # sleep(1)
        #
        # note_book_loc=(By.CSS_SELECTOR, ".icon-jupyter")    #notebook
        # elementWait(self.driver,'notebook',note_book_loc)
        # self.driver.find_element(*note_book_loc).click()
        # sleep(1)
        #
        # rule_laboratory_loc=(By.XPATH,'//*[@id="205"]/span[2]')
        # elementWait(self.driver,'规则实验',rule_laboratory_loc)
        # self.driver.find_element(*rule_laboratory_loc).click()
        # sleep(1)
        #
        # config_manage_loc=(By.XPATH,'//*[@id="206"]/span[2]')
        # elementWait(self.driver, '配置管理', config_manage_loc)
        # self.driver.find_element(*config_manage_loc).click()
        # sleep(1)
        #
        # parameter_manage_loc=(By.XPATH,'//*[@id="209"]/span[2]')
        # elementWait(self.driver, '参数管理', parameter_manage_loc)
        # self.driver.find_element(*parameter_manage_loc).click()
        # sleep(1)
        #
        # decision_make_loc=(By.XPATH,'//*[@id="207"]/span[2]')
        # elementWait(self.driver, '生产决策', decision_make_loc)
        # self.driver.find_element(*decision_make_loc).click()
        # sleep(1)
        #
        # system_settings_loc=(By.XPATH,'//*[@id="201"]/span[2]')
        # elementWait(self.driver, '系统设置', system_settings_loc)
        # self.driver.find_element(*system_settings_loc).click()
        # sleep(1)

        meta_table_loc=(By.ID,'T_TABLE_ORI_LIST')
        elementWait(self.driver,'数据元表',meta_table_loc)
        self.driver.find_element(*meta_table_loc).click()
        sleep(1)

        middle_table_loc=(By.ID,'T_TABLE_TMP_LIST')
        elementWait(self.driver,'中间表',middle_table_loc)
        self.driver.find_element(*middle_table_loc).click()
        sleep(1)

        local_table_loc=(By.ID,'T_TABLE_LOCAL_LIST')
        elementWait(self.driver,'本地文件',local_table_loc)
        self.driver.find_element(*local_table_loc).click()
        sleep(1)










if __name__=="__main__":
    suit=unittest.TestSuite()
    suit.addTest(Test('test_a_usertrue'))

    runner=unittest.TextTestRunner()
    runner.run(suit)