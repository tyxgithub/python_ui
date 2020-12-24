'''多租户管理页面'''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from funtionTools.functionTools import elementWait
from time import sleep

class Mtmanage():

    muti_tenant_loc=(By.XPATH, '//*[@id="103"]/span[2]')     #多租户管理
    operatime_asc_loc = (By.CSS_SELECTOR, ".icon-bs-up")         # 时间排序,从小到大
    operatime_desc_loc = (By.CSS_SELECTOR, ".icon-bs-down")      # 时间排序,从大到小
    tenant_search_loc = (By.XPATH, '//*[@id="j-container"]/app-tenant-management/div[1]/div[1]/div[2]/div/input')  # 租户搜索按钮定位
    create_button_loc=(By.CSS_SELECTOR, ".bsbtncolor")    #新建按钮元素定位
    input_tenant_loc = (By.XPATH, '//*[@id="newTenant"]/div/div/div[2]/div[1]/input')  # 输入租户名称
    select_tenantPeople_loc = (By.XPATH, '//*[@id="newTenant"]/div/div/div[2]/div[2]/div/span')  # 点击选择负责人
    insert_tenantPeople_loc = (By.XPATH, '//*[@id="tenantAdmin"]/div/div/div[2]/input')  # 添加租户负责人 tyx
    first_select_loc = (By.XPATH, '//*[@id="tenantAdmin"]/div/div/div[2]/div[1]/div[2]/div/div[1]/input')  # 第一个勾选框
    sure_button_loc0 = (By.XPATH, '//*[@id="tenantAdmin"]/div/div/div[3]/button')
    tenant_func_loc = (By.XPATH, '//*[@id="newTenant"]/div/div/div[2]/div[4]/div')
    qx_loc = (By.XPATH, '//*[@id="qxqx"]')  # 选择租户功能-全选
    qx_sure_loc = (By.XPATH, '//*[@id="addTenantRigth"]/div/div/div[3]/button')  # 全选-确定
    tenant_tableSelect_loc = (By.XPATH, '//*[@id="newTenant"]/div/div/div[2]/div[6]/div')  # 请选择租户表
    qx1_loc = (By.XPATH, '//*[@id="addTenantTable"]/div/div/div[2]/div/div[1]/div[1]/input') #添加租户-全选按钮
    qx1_sure_loc = (By.XPATH, '//*[@id="addTenantTable"]/div/div/div[3]/button')  #全选-确定
    tenant_descrip_loc = (By.XPATH, '//*[@id="newTenant"]/div/div/div[2]/div[8]/textarea')  # 租户描述
    sure_loc = (By.XPATH, '//*[@id="newTenant"]/div/div/div[3]/button[2]')  # 确定
    jump_input_loc=(By.XPATH,"(//input[@type='text'])[2]")
    xiangzuo_loc=(By.CSS_SELECTOR,'.table-pagination .icon-xiangzuo')
    xiangyou_loc=(By.CSS_SELECTOR,'.table-pagination .icon-goright')
    skip_button_loc=(By.XPATH,"//button[contains(.,'跳转')]")
    shouye_loc=(By.CSS_SELECTOR,'.table-pagination .page-button:nth-child(1)')
    weiye_loc=(By.CSS_SELECTOR,'.table-pagination .page-button:nth-child(5)')
    tenant_name_alert=(By.XPATH,'//*[@id="bsmodalmachine4"]/div/p')
    delete_tenant_alert_loc=(By.XPATH,'//*[@id="bsmodalmachine6"]/div/p')
    delete_tenant_loc=(By.CSS_SELECTOR,'.pai-template-item:nth-child(1) .icon-delete')
    delete_tenant_sure=(By.ID,'confirmWindow_sure')
    delete_tenant_cancel=(By.ID,'confirmWindow_cancel')
    tenant_name_error=(By.CSS_SELECTOR,'.tenantName-error')
    create_success_loc=(By.XPATH,'//body/div/div/p')
    delete_success_loc=(By.XPATH,'//div[2]/div/p')  #适用于租户名称重复提示框
    delete_false_loc=(By.XPATH,'//*[@id="bsmodalmachine6"]/div/p')

    def __init__(self,driver):
        self.driver=driver
    def jumpInput(self,value):  #输入框
        elementWait(self.driver,'跳转输入',self.jump_input_loc)
        self.driver.find_element(*self.jump_input_loc).send_keys(value)
        sleep(1)
    def jumpInputgetValue(self): #获取输入框的值
        elementWait(self.driver, '跳转输入', self.jump_input_loc)
        return self.driver.find_element(*self.jump_input_loc).text
        sleep(1)
    def xiangzuo(self):        #向左跳转
        elementWait(self.driver,'向左跳转',self.xiangzuo_loc)
        self.driver.find_element(*self.xiangzuo_loc).click()
        sleep(1)
    def xiangyou(self):      #向右跳转
        elementWait(self.driver,'向右跳转',self.xiangyou_loc)
        self.driver.find_element(*self.xiangyou_loc).click()
        sleep(1)
    def skipButton(self):   #跳转输入框
        elementWait(self.driver,'跳转输入框',self.skip_button_loc)
        self.driver.find_element(*self.skip_button_loc).click()
        sleep(1)
    def firtPage(self):   #首页
        elementWait(self.driver,'首页',self.shouye_loc)
        self.driver.find_element(*self.shouye_loc).click()
        sleep(1)
    def lastPage(self):   #尾页
        elementWait(self.driver,'尾页',self.weiye_loc)
        self.driver.find_element(*self.weiye_loc).click()
        sleep(1)
    def clickMt(self):        #点击多租户管理
        elementWait(self.driver, "多租户管理", self.muti_tenant_loc)
        self.driver.find_element(*self.muti_tenant_loc).click()
        sleep(1)
    def mtName(self):   #多租户管理名称
        elementWait(self.driver,'多租户管理',self.muti_tenant_loc)
        return self.driver.find_element(*self.muti_tenant_loc).text
        sleep(1)
    def clickInput(self,value):   #多租户搜索按钮
        elementWait(self.driver, "多租户搜索按钮", self.tenant_search_loc)
        self.driver.find_element(*self.tenant_search_loc).send_keys(value)
        self.driver.find_element(*self.tenant_search_loc).send_keys(Keys.ENTER)
        sleep(1)
    def createTenant(self):     #新建租户
        self.driver.find_element(*self.create_button_loc).click()
        elementWait(self.driver, "新建按钮", self.create_button_loc)
        sleep(1)
    def tenantName(self,value):    #租户名称
        elementWait(self.driver,"新建租户-输入租户名称",self.input_tenant_loc)
        self.driver.find_element(*self.input_tenant_loc).send_keys(value)
        sleep(1)
    def selectMp(self):
        elementWait(self.driver,"选择负责人",self.select_tenantPeople_loc)
        self.driver.find_element(*self.select_tenantPeople_loc).click()
        sleep(1)
    def insertMp(self,value):
        elementWait(self.driver,"添加租户负责人",self.insert_tenantPeople_loc)
        self.driver.find_element(*self.insert_tenantPeople_loc).send_keys(value)
        self.driver.find_element(By.XPATH,'//*[@id="tenantAdmin"]/div/div/div[2]/input').send_keys(Keys.ENTER)
        sleep(1)
    def firstCheckBox(self):
        elementWait(self.driver,"第一个勾选框",self.first_select_loc)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.first_select_loc)).perform() # 移动到定位元素
        self.driver.find_element(*self.first_select_loc).click()   #移动到定位元素然后点击勾选
        sleep(1)
    def sureButton0(self):
        elementWait(self.driver,"选择租户负责任-确定按钮",self.sure_button_loc0)
        self.driver.find_element(*self.sure_button_loc0).click() #确定按钮
        sleep(1)
    def tenantFunction(self):
        elementWait(self.driver,"选择租户功能按钮",self.tenant_func_loc)
        self.driver.find_element(*self.tenant_func_loc).click()  #选择租户功能
        sleep(1)
    def tenantQx(self):
        elementWait(self.driver,"选择租户功能-全选",self.qx_loc)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.qx_loc)).perform()
        sleep(1)
        self.driver.find_element(*self.qx_loc).click()
        sleep(1)
    def qxSure(self):
        elementWait(self.driver,'全选-确定',self.qx_sure_loc)
        self.driver.find_element(*self.qx_sure_loc).click()  #点击确定
        sleep(1)
    def tableSelect(self):
        elementWait(self.driver, "请选择租户表按钮", self.tenant_tableSelect_loc)
        self.driver.find_element(*self.tenant_tableSelect_loc).click()
        sleep(2)
    def qx1Button(self):
        elementWait(self.driver,'添加租户表-全选按钮',self.qx1_loc)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.qx1_loc)).perform()
        self.driver.find_element(*self.qx1_loc).click()
        sleep(1)
    def qx1Sure(self):
        elementWait(self.driver,'添加租户表-确定',self.qx1_sure_loc)
        self.driver.find_element(*self.qx1_sure_loc).click()
        sleep(1)
    def tenantDesc(self,value):
        elementWait(self.driver,'租户描述',self.tenant_descrip_loc)
        self.driver.find_element(*self.tenant_descrip_loc).send_keys(value)
        sleep(1)
    def sureLoc(self):
        elementWait(self.driver,'确定按钮',self.sure_loc)
        self.driver.find_element(*self.sure_loc).click()
        sleep(1)
    def alertText(self):   #租户描述提示框
        elementWait(self.driver,'租户名称、描述不能为空',self.tenant_name_alert)
        return self.driver.find_element(*self.tenant_name_alert).text
        sleep(4)
    def deleteTenantAlert(self):    #删除租户提示
        elementWait(self.driver,'无法删除该租户',self.delete_tenant_alert_loc)
        return self.driver.find_element(*self.delete_tenant_alert_loc).text
        sleep(4)
    def deleteTenantButton(self):    #删除租户按钮
        elementWait(self.driver,'删除租户按钮',self.delete_tenant_loc)
        self.driver.find_element(*self.delete_tenant_loc).click()
        sleep(1)
    def deleteTenantSure(self):   #删除租户确定按钮
        elementWait(self.driver,'删除租户-确定按钮',self.delete_tenant_sure)
        self.driver.find_element(*self.delete_tenant_sure).click()
        sleep(1)
    def deleteTenantCancel(self):   #删除租户按钮-取消
        elementWait(self.driver,'删除租户-取消按钮',self.delete_tenant_cancel)
        self.driver.find_element(*self.delete_tenant_cancel).click()
        sleep(1)
    def tenantNameerror(self):
        elementWait(self.driver,'租户名称为空报错',self.tenant_name_error)
        return self.driver.find_element(*self.tenant_name_error).text
        sleep(4)
    def tenantScAlert(self):
        elementWait(self.driver,'新建成功',self.create_success_loc)
        return self.driver.find_element(*self.create_success_loc).text
        sleep(4)
    def deleteFalse(self):
        elementWait(self.driver,'删除失败',self.delete_false_loc)
        return self.driver.find_element(*self.delete_false_loc).text
        sleep(4)
    def deleteSuccess(self):
        elementWait(self.driver,'删除成功',self.delete_success_loc)
        return self.driver.find_element(*self.delete_success_loc).text
        sleep(4)