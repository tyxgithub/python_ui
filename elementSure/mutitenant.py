'''多租户管理'''

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

        tenant_search_loc=(By.XPATH, '//*[@id="j-container"]/app-tenant-management/div[1]/div[1]/div[2]/div/input')   #租户搜索按钮定位
        elementWait(self.driver,"多租户搜索按钮",tenant_search_loc)
        self.driver.find_element(*tenant_search_loc).send_keys("tyxtyx")
        self.driver.find_element(*tenant_search_loc).send_keys(Keys.ENTER)    #按住回车搜索
        sleep(1)

        create_button_loc=(By.CSS_SELECTOR, ".bsbtncolor")    #新建按钮元素定位
        elementWait(self.driver,"新建按钮",create_button_loc)
        self.driver.find_element(*create_button_loc).click()
        sleep(1)

        input_tenant_loc1=(By.XPATH,'//*[@id="newTenant"]/div/div/div[2]/div[1]/input')  #输入租户名称
        elementWait(self.driver,"新建租户-输入租户名称",input_tenant_loc1)
        self.driver.find_element(*input_tenant_loc1).send_keys("hahaha")
        sleep(1)

        select_tenantPeople_loc=(By.XPATH,'//*[@id="newTenant"]/div/div/div[2]/div[2]/div/span')  #点击选择负责人
        elementWait(self.driver,"选择负责人",select_tenantPeople_loc)
        self.driver.find_element(*select_tenantPeople_loc).click()
        sleep(1)

        insert_tenantPeople_loc=(By.XPATH,'//*[@id="tenantAdmin"]/div/div/div[2]/input')  #添加租户负责人 tyx
        elementWait(self.driver,"添加租户负责人",insert_tenantPeople_loc)
        self.driver.find_element(*insert_tenantPeople_loc).send_keys("tyx")
        self.driver.find_element(By.XPATH,'//*[@id="tenantAdmin"]/div/div/div[2]/input').send_keys(Keys.ENTER)
        sleep(1)

        first_select_loc=(By.XPATH,'//*[@id="tenantAdmin"]/div/div/div[2]/div[1]/div[2]/div/div[1]/input')     #第一个勾选框
        elementWait(self.driver,"第一个勾选框",first_select_loc)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*first_select_loc)).perform() # 移动到定位元素
        self.driver.find_element(*first_select_loc).click()   #移动到定位元素然后点击勾选
        sleep(1)

        sure_button_loc0=(By.XPATH,'//*[@id="tenantAdmin"]/div/div/div[3]/button')
        elementWait(self.driver,"选择租户负责任-确定按钮",sure_button_loc0)
        self.driver.find_element(*sure_button_loc0).click() #确定按钮
        sleep(1)

        tenant_func_loc=(By.XPATH,'//*[@id="newTenant"]/div/div/div[2]/div[4]/div')
        elementWait(self.driver,"选择租户功能按钮",tenant_func_loc)
        self.driver.find_element(*tenant_func_loc).click()  #选择租户功能
        sleep(1)

        qx_loc=(By.XPATH,'//*[@id="qxqx"]')    #选择租户功能-全选
        elementWait(self.driver,"选择租户功能-全选",qx_loc)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*qx_loc)).perform()
        sleep(1)
        self.driver.find_element(*qx_loc).click()
        sleep(1)

        qx_sure_loc=(By.XPATH,'//*[@id="addTenantRigth"]/div/div/div[3]/button')  #全选-确定
        self.driver.find_element(*qx_sure_loc).click()  #点击确定
        sleep(1)

        tenant_tableSelect_loc=(By.XPATH,'//*[@id="newTenant"]/div/div/div[2]/div[6]/div')  #请选择租户表
        elementWait(self.driver,"请选择租户表按钮",tenant_tableSelect_loc)
        self.driver.find_element(*tenant_tableSelect_loc).click()
        sleep(2)

        qx1_loc=(By.XPATH,'//*[@id="addTenantTable"]/div/div/div[2]/div/div[1]/div[1]/input')
        elementWait(self.driver,'添加租户表-全选按钮',qx1_loc)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*qx1_loc)).perform()
        self.driver.find_element(*qx1_loc).click()
        sleep(1)

        qx1_sure_loc=(By.XPATH,'//*[@id="addTenantTable"]/div/div/div[3]/button')
        elementWait(self.driver,'添加租户表-确定',qx1_sure_loc)
        self.driver.find_element(*qx1_sure_loc).click()
        sleep(1)

        tenant_descrip_loc=(By.XPATH,'//*[@id="newTenant"]/div/div/div[2]/div[8]/textarea')  #租户描述
        elementWait(self.driver,'租户描述',tenant_descrip_loc)
        self.driver.find_element(*tenant_descrip_loc).send_keys("hahahahahahha")
        sleep(1)

        sure_loc=(By.XPATH,'//*[@id="newTenant"]/div/div/div[3]/button[2]')  #确定
        elementWait(self.driver,'确定按钮',sure_loc)
        self.driver.find_element(*sure_loc).click()
        sleep(1)


if __name__=="__main__":
    suit=unittest.TestSuite()
    suit.addTest(Test('test_a_usertrue'))

    runner=unittest.TextTestRunner()
    runner.run(suit)