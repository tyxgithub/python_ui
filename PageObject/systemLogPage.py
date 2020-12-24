'''系统日志模块'''
from selenium.webdriver.common.by import By
from funtionTools.functionTools import elementWait
from time import sleep

class systemLogPage():
    system_log_loc=(By.CSS_SELECTOR, ".icon-log")            #平台层-系统日志
    module_loc=(By.NAME, "module")                           #操作模块
    bsbtncolor_loc=(By.CSS_SELECTOR, ".bsbtncolor")          #确定按钮
    first_value_loc=(By.CSS_SELECTOR,".table-row:nth-child(1) > .col-md-4 > span")#第一行的具体操作的值
    reset_loc=(By.CSS_SELECTOR,".btn-default")               #重置按钮
    first_page_loc=(By.CSS_SELECTOR,".icon-jiantou-shouye")  #箭头首页
    last_page_loc=(By.CSS_SELECTOR,".icon-weiye")            #箭头尾页
    left_page_loc=(By.CSS_SELECTOR,".icon-xiangzuo")         #向左跳转
    right_page_loc=(By.CSS_SELECTOR,".icon-goright")         #向右跳转
    page_skip_input=(By.CSS_SELECTOR,".page-input")          #跳转的页面输入
    page_skip_click=(By.CSS_SELECTOR,".ascertain-button")    #跳转按钮
    operatime_asc_loc=(By.CSS_SELECTOR,".icon-bs-up")        #时间排序,从小到大
    operatime_desc_loc=(By.CSS_SELECTOR,".icon-bs-down")     #时间排序,从大到小

    def __init__(self,driver):
        self.driver=driver
    def clickSysLog(self):   #点击系统日志
        elementWait(self.driver,'系统日志',self.system_log_loc)
        self.driver.find_element(*self.system_log_loc).click()
        sleep(1)
    def clickModule(self):   #点击操作模块-
        elementWait(self.driver,'操作模块',self.module_loc)
        self.driver.find_element(*self.module_loc).click()
        sleep(1)
    def clickOption(self,value):   #选择具体的日志模块
        elementWait(self.driver,'操作模块',self.module_loc)
        if value in "平台层/多租户管理":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '平台层/多租户管理']").click()
        elif value in "平台层/导入管理":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '平台层/导入管理']").click()
        elif value in "平台层/系统设置":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '平台层/系统设置']").click()
        elif value in "租户层/数据管理":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/数据管理']").click()
        elif value in "租户层/数据加工":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/数据加工']").click()
        elif value in "租户层/AI实验室":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/AI实验室']").click()
        elif value in "租户层/NOTEBOOK":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/NOTEBOOK']").click()
        elif value in "租户层/规则实验室":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/规则实验室']").click()
        elif value in "租户层/配置管理":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/配置管理']").click()
        elif value in "租户层/生产决策":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/生产决策']").click()
        elif value in "租户层/参数管理":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/参数管理']").click()
        elif value in "租户层/系统管理":
            dropdown = self.driver.find_element(*self.module_loc)
            dropdown.find_element(By.XPATH, "//option[. = '租户层/系统']").click()
        else:
            print ("请输入正确的模块")
        sleep(1)
    def clickButton(self):         #点击确定按钮
        elementWait(self.driver,'确定按钮',self.bsbtncolor_loc)
        self.driver.find_element(*self.bsbtncolor_loc).click()
        sleep(1)
    def getOperaValue(self):       #第一行的具体操作的值
        elementWait(self.driver,'第一行的具体操作的值',self.first_value_loc)
        value=self.driver.find_element(*self.first_value_loc).text
        print ("当前所属模块:%s"%value)
        sleep(1)
        return value
    def clickreset(self):          #点击重置按钮
        elementWait(self.driver,'重置按钮',self.reset_loc)
        self.driver.find_element(*self.reset_loc).click()
        sleep(1)
    def clickFirstPage(self):      #点击首页
        elementWait(self.driver,'首页',self.first_page_loc)
        self.driver.find_element(*self.first_page_loc).click()
    def clickLastPage(self):       #点击尾页
        elementWait(self.driver,'尾页',self.last_page_loc)
        self.driver.find_element(*self.last_page_loc).click()
        sleep(1)
    def clickRightPage(self):      #向右跳转
        elementWait(self.driver,'向右跳转',self.right_page_loc)
        self.driver.find_element(*self.right_page_loc).click()
        sleep(1)
    def clickLeftPage(self):       #向左跳转
        elementWait(self.driver,'向左跳转',self.left_page_loc)
        self.driver.find_element(*self.left_page_loc).click()
        sleep(1)
    def inputPageSkip(self,value): #输入跳转的页面数
        elementWait(self.driver,'跳转页面数',self.page_skip_input)
        self.driver.find_element(*self.page_skip_input).click()
        self.driver.find_element(*self.page_skip_input).send_keys(value)
        sleep(1)
    def getSkipValue(self):        #获取当前跳转的页的page值
        elementWait(self.driver,'当前页面的page值',self.page_skip_input)
        value=self.driver.find_element(*self.page_skip_input).text
        sleep(1)
        return value
    def clickSkipButton(self):     #点击跳转按钮
        elementWait(self.driver,'跳转按钮',self.page_skip_click)
        self.driver.find_element(*self.page_skip_click).click()
        sleep(1)
    def clickUp(self):             #点击正序按钮，从小到大排序
        elementWait(self.driver,'正序按钮',self.operatime_asc_loc)
        self.driver.find_element(*self.operatime_asc_loc).click()
        sleep(1)
    def clickDown(self):           #点击逆序按钮,从大到小排序
        elementWait(self.driver,'逆序按钮'.self.operatime_desc_loc)
        self.driver.find_element(*self.operatime_desc_loc).click()


