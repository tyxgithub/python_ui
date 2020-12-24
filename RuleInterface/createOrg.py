import time
from DUOWEI_AUTO.RuleInterface.baseHttp import *


def create(number2,number1=0):
    data_one={
    "id":"id_01"
    ,"orgName":"orgName_01"
    ,"orgPath":"1"
    ,"pare    ntOrgId":"1"
    ,"picName":"汤宇翔"
    ,"contact":"15252993571"
    ,"handleOrg":"1"
    ,"description":"这是一级机构描述"
    }

    data_two={
     "id":"id_01"
    ,"orgName":"orgName_02"
    ,"orgPath":"1"
    ,"parentOrgId":"1"
    ,"picName":"汤宇翔"
    ,"contact":"15252993571"
    ,"handleOrg":"1"
    ,"description":"这是二级机构描述"
    }

    data_three={
     "id":"id_01"
    ,"orgName":"orgName_02"
    ,"orgPath":"1"
    ,"parentOrgId":"1"
    ,"picName":"汤宇翔"
    ,"contact":"15252993571"
    ,"handleOrg":"1"
    ,"description":"这是三级机构描述"
    }

    data_four={
     "id":"id_01"
    ,"orgName":"orgName_02"
    ,"orgPath":"1"
    ,"parentOrgId":"1"
    ,"picName":"汤宇翔"
    ,"contact":"15252993571"
    ,"handleOrg":"1"
    ,"description":"这是四级机构描述"
    }


    time1=time.time()
    for i in range(number1,number2):
        if i%4==0:
            data_one["id"]="id_"+str(i)
            data_one["orgName"]="orgName_"+str(i)

            data_two["id"]="id_"+str(i+1)
            data_two["orgName"] = "orgName_" + str(i+1)
            data_two["orgPath"] ="1."+data_one["id"]
            data_two["parentOrgId"]=data_one["id"]
            data_two["handleOrg"]=data_one["id"]

            data_three["id"]="id_"+str(i+2)
            data_three["orgName"] = "orgName_" + str(i+2)
            data_three["orgPath"] ="1."+data_one["id"]+"."+data_two["id"]
            data_three["parentOrgId"]=data_two["id"]
            data_three["handleOrg"]=data_two["id"]

            data_four["id"] = "id_" + str(i+3)
            data_four["orgName"] = "orgName_" + str(i+3)
            data_four["orgPath"] ="1."+data_one["id"]+"."+data_two["id"]+"."+data_three["id"]
            data_four["parentOrgId"]=data_three["id"]
            data_four["handleOrg"]=data_three["id"]

            # print (data_one)
            # print (data_two)
            # print (data_three)
            # print (data_four)
            r1=post_send(data_one, cookie, create_org_url)
            if "true" in r1:
                print ("机构%s，新建成功"%data_one["orgName"])
            elif "false" in r1:
                print ("机构%s,已经存在"%data_one["orgName"])
            r2=post_send(data_two,cookie,create_org_url)
            if "true" in r2:
                print("机构%s，新建成功"%data_two["orgName"])
            elif "false" in r2:
                print ("机构%s,已经存在"%data_two["orgName"])
            r3=post_send(data_three,cookie,create_org_url)
            if "true" in r3:
                print("机构%s，新建成功"%data_three["orgName"])
            elif "false" in r3:
                print ("机构%s,已经存在"%data_three["orgName"])
            r4=post_send(data_four,cookie,create_org_url)
            if "true" in r4:
                print("机构%s，新建成功"%data_four["orgName"])
            elif "false" in r4:
                print ("机构%s,已经存在"%data_four["orgName"])
    time2=time.time()
    print ("success,总共耗时%s秒"%(time2-time1))
