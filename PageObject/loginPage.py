'''登录页面'''
from selenium.webdriver.common.by import By
from time import sleep
from funtionTools.functionTools import elementWait


class LoginPage():
    url='http://10.100.2.32:8117/#/angularpanel/model/login'
    username_input_loc=(By.CSS_SELECTOR, ".adinpt:nth-child(1) .lgipm")
    password_input_loc=(By.CSS_SELECTOR, ".adinpt:nth-child(2) .lgipm")
    button_loc=(By.CLASS_NAME,'login-btn')
    alert_loc=(By.CSS_SELECTOR, "p")
    def __init__(self,driver):
        self.driver=driver
    def open_url(self):
        self.driver.get(self.url)
    def input_username(self,username):
        elementWait(self.driver,'用户名',self.username_input_loc)
        self.driver.find_element(*self.username_input_loc).send_keys(username)
        sleep(1)
    def clear_username(self):  #清除用户名
        elementWait(self.driver, '用户名', self.username_input_loc)
        self.driver.find_element(*self.username_input_loc).clear()
    def input_password(self,password):   #输入密码
        elementWait(self.driver,'输入密码',self.password_input_loc)
        self.driver.find_element(*self.password_input_loc).send_keys(password)
        sleep(1)
    def clear_password(self):
        elementWait(self.driver, '输入密码', self.password_input_loc)
        self.driver.find_element(*self.password_input_loc).clear()
        sleep(1)
    def alert(self):
        elementWait(self.driver,'弹出提示',self.alert_loc)
        return self.driver.find_element(*self.alert_loc).text
        sleep(4)
    def login_click(self):
        elementWait(self.driver,'登录按钮',self.button_loc)
        self.driver.find_element(*self.button_loc).click()
        sleep(1)




