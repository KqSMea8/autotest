import unittest
from ApiHelp import request,unit
from ApiHelp.config import conf
# from parameterized import parameterized, param
import MyLog as log

class BaseTest(unittest.TestCase):



    def baseCases(self,caseId,caseName,apiKey,Author,requestBody,respect):
        '''json格式请求 baes方法'''
        logfile = conf.logPath + caseId['caseId'] + '.html'
        log.LogStart(apiKey['apiKey'],caseId['caseId']+caseName['caseName']+Author['Author'],logfile)
        
        postData = requestBody['Body']

        response = request.action(apiKey['apiKey'],postData)
        
        log.info('request body:')
        log.info(postData)

        if response == None:
            self.assertEqual('resError',1,"请求无响应")
            log.info('请求无响应')
        else:
            try:
                log.info("response msg:")
                log.info(response)
                log.info("期望值:")
                log.info(respect['respect'])
                self.assertTrue(unit.dictCmp(respect['respect'],response),'期望json数据不在response json数据中')
                log.info('用例通过')
            except Exception as e:
                log.err(e)
                raise

    def xmlBaesCase(self,caseId,caseName,apiKey,Author,requestBody,respect):
        '''xml格式请求 base方法'''
        xmlfile = conf.apiDataPath + 'XmlSubCase/xmlData/' + requestBody['Body']
         
        logfile = conf.logPath + caseId['caseId'] + '.html'
        log.LogStart(apiKey['apiKey'],caseId['caseId']+caseName['caseName']+Author['Author'],logfile)

        log.info('request body:')
        # rqinfo = unit.makeTxtData(xmlfile)
        log.info(xmlfile)

        response = request.xmlpost(apiKey['apiKey'],xmlfile)
        
        if response == None:
            self.assertEqual('resError',1,"请求无响应")
            log.info('请求无响应')
        else:
            try:
                log.info("response msg:")
                log.info(str(type(response)))
                log.info("期望值:")
                log.info(respect['respect'])
                for k,v in respect['respect'].items():
                    self.assertEqual(unit.getXmlNote(response,k),v)
                log.info('用例通过')
            except Exception as e:
                log.err(e)
                raise

