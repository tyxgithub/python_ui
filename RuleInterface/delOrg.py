from DUOWEI_AUTO.RuleInterface.baseHttp import *
import time
import json

def delete(number):
    post_url = 'http://10.100.1.153:16705/bs/rule/rs/org/del'

    headers = {"Accept": "*/*"
        , "Accept-Encoding": "gzip, deflate"
        , "Accept-Language": "zh-CN,zh;q=0.9"
        , "Connection": "keep-alive"
        ,
          "Cookie":cookie
        , "Host": "10.100.1.153:16705"
        ,
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        , "X-Requested-With": "XMLHttpRequest"
        , "Content-Type": "application/json"
        , "Content-Length": "120"
        }

    data = {

        "allowDrag": "true"
        , "allowDrop": "true"
        , "checked": "null"
        , "children": "null"
        , "cls": ""
        , "contact": "15252993571"
        , "createBy": "admin"
        , "depth": "2"
        , "description": "这是一级机构描述"
        , "expandable": "true"
        , "expanded": "false"
        , "handleOrg": "1"
        , "href": ""
        , "hrefTarget": ""
        , "icon": ""
        , "iconCls": ""
        , "id": "id_116"
        , "index": "0"
        , "isFirst": "true"
        , "isLast": "false"
        , "leaf": "false"
        , "loaded": "true"
        , "loading": "false"
        , "orgName": "orgName_116"
        , "orgPath": "1.id_116"
        , "parentDeptName": ""
        , "parentId": "1"
        , "picName": "汤宇翔"
        , "qshowDelay": "0"
        , "qtip": ""
        , "qtitle": ""
        , "root": "false"
        , "text": "orgName_116"
        , "updateBy": "admin"
        , "visible": "true"
    }

    time1 = time.time()
    for i in range(0, number):
        if i % 4 == 0:
            data["id"] = "id_" + str(i)
            data["orgPath"] = "1.id_" + str(i)
            data["orgName"] = "orgName_" + str(i)
            data["text"] = "orgName_" + str(i)
            data = json.dumps(data)
            r = requests.post(url=del_org_url, headers=headers, data=data)
            data = json.loads(data)
            # print(r.status_code)
            if "true" in r.text:
                print(r.text+",一级机构以及所有子机构%s删除成功"%data["id"])
    time2 = time.time()
    print("success,总共删除耗时%s秒" % (time2 - time1))
