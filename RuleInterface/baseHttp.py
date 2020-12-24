import json
import requests
import re

'''福建银行规则平台V6.7.0.5'''
baseUrl='http://10.100.1.153:16715'
''''''
'''新建用户接口'''
create_user_url=baseUrl+"/bs/rule/rs/user/insert?"
'''删除用户接口'''
del_user_url=baseUrl+'/bs/rule/rs/user/remove'
'''新建机构接口'''
create_org_url=baseUrl+'/bs/rule/rs/org/add'
'''删除机构接口'''
del_org_url=baseUrl+'/bs/rule/rs/org/del'
'''下发规则包接口'''
handle_rule_url=baseUrl+'/bs/rule/rs/dm/pkg/assignFromList'
'''cookie值'''
cookie='portal_bizline_code=BANK; portal_index_view=/sysconfpanel/portal/; theme=bangsun; SESSION=YmM4YmE0N2MtYTE5NC00Y2M0LWEwYWQtZGEzMWVkNTQyMTY2'
def post_send(data,cookie,url):
    headers={"Accept":"*/*"
    ,"Accept-Encoding":"gzip, deflate"
    ,"Accept-Language":"zh-CN,zh;q=0.9"
    ,"Connection":"keep-alive"
    ,"Cookie":cookie
    ,"Host":"10.100.1.153:16705"
    ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    ,"X-Requested-With":"XMLHttpRequest"
    ,"Content-Type":"application/json"
    ,"Content-Length":"120"
    }

    data=json.dumps(data)
    r=requests.post(url=url,headers=headers,data=data)
    return r.text


'''这是获取规则包的包ID接口'''
pkgid_get_url=baseUrl+'/bs/rule/rs/dm/pkg/list?orgId=&applyId=&bizId=&pkgType='
def get_send(cookie,url):
    headers={"Accept":"*/*"
    ,"Accept-Encoding":"gzip, deflate"
    ,"Accept-Language":"zh-CN,zh;q=0.9"
    ,"Connection":"keep-alive"
    ,"Cookie":cookie
    ,"Host":"10.100.1.153:16705"
    ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    ,"X-Requested-With":"XMLHttpRequest"
    ,"Content-Type":"application/json"
    ,"Content-Length":"120"
    }
    r=requests.get(url=url,headers=headers)
    return r.text
r=get_send(cookie,pkgid_get_url)
print (re.findall("id(.*?)",r))
