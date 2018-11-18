import sys,time,json,requests,copy
from ApiHelp import http,config,unit
from ApiMaps import api
conf = config.conf()
import MyLog


'''
 发送请求 apikey: api,data的key值
 payload post参数
 urlParam:get参数
 precondition：是否前置接口
 file method file 上传文件
 header:json or xml...使用不同header
 '''
def action(apikey,payload=None,urlParam=None,precondition=False,file=None):
    startTime = time.time()
    localTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    error = None
    result = None
    r = api.get(apikey)#封装请求url
    MyLog.info("request address:")
    MyLog.info(r['address'])
    # headers = http.generateHeader(config)  #封装header
    headers = http.jsonHeader()
    payloadClone = ''
    #组合get rest参数
    if urlParam and len(urlParam)>0:
        r['address'] = http.generateUrl(r['address'],urlParam)
    try:
        if r['method'] == 'get' or r['method'] == 'delete':
            if r['method'] == 'get':
                result = requests.get(r['address'],headers=headers)
            if r['method'] == 'delete':
                result = requests.delete(r['address'],headers=headers)
        if r['method'] == 'post' or r['method'] == 'put' or r['method'] == 'file':
            payload = payload or eval('req.'+apikey)
            payload = http.formatParams(payload)
            payloadClone = copy.deepcopy(payload)
            if r['method'] == 'post':
                result = requests.post(r['address'],data = payload,headers=headers)
            if r['method'] == 'put':
                result = requests.put(r['address'],data = payload,headers=headers)
            if r['method'] == 'file':
                result = requests.post(r['address'],headers = headers,file=file)
    except Exception as e:
        error = e
    finally:
        log = {}
        if precondition:
            log['type'] = '前置接口'
        else:
            log['type'] = '被测接口'
            
        log['startTime'] = localTime
        log['wasteTime'] = time.time() -startTime
        log['apiName'] = r['desc']
        log['address'] = r['address']
        log['method'] = r['method']
        log['header'] = headers
        if log['method'] == 'put' or log['method'] == 'post':
            log['payload'] = json.loads(payloadClone)
        else:
            log['payload'] = None
        log['error'] = error
        log['result'] = None
        try:
            log['result'] = result.json()
        except Exception as e:
            pass
        conf.Logs.append(log)
        try:
            return result.json()
        except Exception as e:
            return None

def xmlpost(apiKey,xmlfile):
    '''利用requets 进行soa协议请求 使用xml文件作为参数
        结果保存到临时文档 返回xml对象数据'''
    r = api.get(apiKey)
    header = http.XmlHeader()
    with open(xmlfile,'rb') as xmldata:
        result = requests.post(r['address'],data=xmldata,headers=header)
    with open(conf.apiReportDir+'result.xml','w',encoding='utf-8') as f:
        f.write(result.text)
    resultXMLdata = unit.xmlRead(conf.apiReportDir+'result.xml')
    unit.delFiles(conf.apiReportDir+'result.xml')
    
    return resultXMLdata
