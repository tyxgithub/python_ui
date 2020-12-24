from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def elementWait(driver,message,loc):
    try:
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(loc))
        print ("元素:%s,已经定位到"%message)
    except:
        print ("Error:元素:%s,未找到"%message)