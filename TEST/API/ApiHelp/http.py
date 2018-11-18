import sys,json,time,random

def generateUrl(url,params):        #组合url地址
    return unit.makeRestRrl(url,params)
    
# def generateHeader(conf):           #组合head 值（某些需要权限验证的接口）
#     return{
#       'Content-Type':'application/json'
#       #'Authorization':'beares' + conf.TOKEN
#     }
def jsonHeader():
    return {'Content-Type':'application/json'}

def XmlHeader():
    return {'Content-Type':'application/xml'}

def formatParams(data):       #格式化post put 请求参数
    # data['nonce'] = unit.md5(str(time.time()+random.randint(1,99999)))  #请求参数中需要添加nonce的参数
    return json.dumps(data)   #json格式化参数