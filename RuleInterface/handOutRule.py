import time
from RuleInterface.baseHttp import *

def handOutRule(number):
    get_send(cookie,)
    data={  "orgIds": ["id_0"]
            ,"0":"id_0"
            ,"pkgIds": ["972XWLXvvw"]
            ,"0":"972XWLXvvw"
            ,"type":"add"
    }
    start_time=time.time()
    for i in range(0,number):
        list1=[]
        list1.insert(0,"id_"+str(i))
        print (list1)
        data["orgIds"]=list1
        data["0"]="id_"+str(i)
        r=post_send(data, cookie, handle_rule_url)
        if "true" in r:
            print (r)
        elif "false" in r:
            print ("下发失败，检查参数")
    end_time=time.time()
    print ("success,下发所有机构的总共耗时%s秒"%(end_time-start_time))


