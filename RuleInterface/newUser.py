from RuleInterface.baseHttp import *
import json
import time

def newUser(number):
    data={
         "createBy": ""
        , "createTime": ""
        , "department": "1"
        , "email": "123456@qq.com"
        , "enabled": 1
        , "groupName": ""
        , "mobile": "15252889098"
        , "multiloginEnabled": "0"
        , "password": ""
        , "permission": 0
        , "realname": "汤宇翔"
        , "roles": ["admin"]
        , "0": "admin"
        , "title": ""
        , "updateBy": ""
        , "updateTime": ""
        , "username": "tyx3"
    }
    # data=json.dumps(data)???
    time_start=time.time()
    for i in range(0,number):
        data["username"]="tyx"+str(i)
        r=post_send(data,cookie,create_user_url)
        if "true" in r:
            print ("用户%s,新建成功"%data["username"])
        elif "false" in r:
            print ("用户%s,已经存在"%data["username"])
    time_end=time.time()
    print ("success,新建用户耗时%s秒"%(time_end-time_start))