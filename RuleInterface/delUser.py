from DUOWEI_AUTO.RuleInterface.baseHttp import *
import time


def delUser(number):
    data={
        "createBy": "admin"
        , "department": "1"
        , "email": "123456@qq.com"
        , "enabled": 1
        , "groupName": "admin"
        , "mobile": "15252889098"
        , "multiloginEnabled": 0
        , "password": ""
        , "permission": 0
        , "realname": "汤宇翔"
        , "roles": ["admin"]
        , "0": "admin"
        , "title": ""
        , "updateBy": "admin"
        , "username": "tyx0"
    }
    start_time=time.time()
    for i in range(0,number):
        data["username"] ="tyx"+str(i)
        r=post_send(data, cookie, del_user_url)
        if "true" in r:
            print ("用户%s删除成功"%data["username"])
    end_time=time.time()
    print ("success,删除所有用户总共耗时:%s"%(start_time-end_time))