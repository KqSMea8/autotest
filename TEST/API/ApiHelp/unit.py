import json,codecs,time,csv,sys,hashlib,os
import xml.etree.cElementTree as ET

#构建rest风格接口URL资源参
def makeResultUrl(url,params):
    uSplit = url.split('$')
    result = ''
    for x in range(0,len(uSplit)):
        result += uSplit[x]
        if x < len(params):
            result += str(params[x])
    return result

 #生成详细报告
def makeDetailReport(fileDir,reportName,excuteTime,title,Logs):
    pf = codecs.open(fileDir,'w+','utf-8')
    pf.write('<html>')
    pf.write('<head>')
    pf.write('  <title>'+title+'</title>')
    pf.write('  <meta charset="utf-8"/>')
    pf.write('  <script type="text/javascript" src="http://10.2.74.140:81/runnerRes/jquery.min.js"></script>')    #可以下载这个js 放到指定路径下这里获取
    pf.write('  <link rel="stylesheet" type="text/css" href="http://10.2.74.140:81/runnerRes/amazeui.min.css">')  #可以下载这个css 放到指定路径下这里获取
    pf.write('</head>')
    pf.write('<body>')
    pf.write('<div class="am-container" style="background-color:white;">')
    pf.write('<h1 style="text-align: center; margin-top: 20px;">'+title+'</h1>')
    pf.write('<hr>')
    pf.write("<h2> 报告生成时间："+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"</h2>")
    pf.write('<hr>')
    # pf.write('<iframe src="'+reportName+'" style="height:400px;width:120%"></iframe>')
    for item in Logs:
        result = '<span style = "color:green">调用成功</span>'
        if item['error']:
          result = '<span style = "color:green">调用失败</span>'
        try:
            if item['result']['error']:
                result = '<span style = "color:green">调用失败</span>'
        except Exception as e:
            pass
        pf.write("<h2>测试接口："+item['apiName']+"</h2>")
        pf.write("<div>调用类型："+item['type']+"</div>")
        pf.write("<div>调用结果："+result+"</div>")
        pf.write("<div>调用方法："+item['method']+"</div>")
        pf.write("<div>调用时间："+item['startTime']+"</div>")
        pf.write("<div>接口响应时间：<code>"+str(item['wasteTime'])+"</code></div>")
        pf.write("<div>接口地址:<br/><pre>"+item['address']+"</pre></div>")
        pf.write("<div>head:<br/><pre>"+json.dumps(item['header'],sort_keys=True,indent=4)+"</pre></div>")
        pf.write("<div>request:<br/><pre>"+json.dumps(item['payload'],sort_keys=True,indent=4)+"</pre></div>")
        pf.write("<div>respons:<br/><pre>"+json.dumps(item['result'],sort_keys=True,indent=4,ensure_ascii=False)+"</pre></div>")
        pf.write('<div>错误信息：'+str(item['error'])+'</div>')
        pf.write('<br/><hr>')
    # pf.write('</div>')
    pf.write('</body>')
    pf.write('<script type="text/javascript">')
    pf.write('</script>')
    pf.write('</html>')
    
 
 #从csv 读取数据 转换成数组
def makeCsvData(dataPath):
    data = []
    for value in csv.reader(open(dataPath,"r",encoding='utf-8')):
        data.append(value)
    return data
#从txt读取数据
def makeTxtData(dataPath):
    return open(dataPath,'r',encoding='utf=8')
    

#组合查询条件
#querys:enable/username/nickname datas:true/tangqi/suer
def makeSearchConditions(querys,datas):
    _querys = querys.split("/")
    _datas = datas.split("/")
    queryObject = {}
    for index in range(0,len(_querys)):
        queryObject[_querys[index]]= _datas[index]
    return queryObject
     
 #清理操作
def clearTestData():
    print("\n clear")
     
 #hashlib md5 字符串
def md5(str):
    _str = str.encode('utf-8')
    return hashlib.md5(_str).hexdigest()

def dictCmp(dictA,dictB):
    '''比较两个字典 a是否在b中 '''

    DictA , ak = dictA , dictA.keys()
    DictB , bk = dictB , dictB.keys()
    bv = list(dictB.values())
    if len(dictA) > len(dictB):
        # print("交换两个字典数据")
        DictA , ak = dictB , dictB.keys()
        DictB , bk = dictA , dictA.keys()
        bv = list(dictA.values())
    flag = True
    for i in ak:
        if DictA[i] == DictB.get(i,'no the key'):
            flag =  True
        else:
            flag = False
            for subDic in bv:
                if type(subDic) == type(dict()):
                    if DictA[i] == subDic.get(i,'no the key'):
                        flag = True
                # else:
                    # print("子json 不是dict形式,无法比较")
    return flag

def xmlRead(xmlfile):
    """读取xml文档"""
    return ET.ElementTree(file = xmlfile)

def getXmlNote(xmlfile,note):
    '''获取xml节点文本值'''
    # tree = xmlRead(xmlfile)
    #(通过xmlpost return的已经是elementtree对象)
    tree = xmlfile
    for elem in tree.iter():
        if note in elem.tag:
            return elem.text
    else:
        return None

def delFiles(filetobeDel):
    '''删除文件'''
    os.remove(filetobeDel)