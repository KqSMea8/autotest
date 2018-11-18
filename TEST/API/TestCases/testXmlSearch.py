import sys,unittest,os
sys.path.append(os.path.abspath("TEST/Public"))
import DataRead,unittest
from ApiHelp.config import conf
from parameterized import parameterized, param
from ApiMaps import api
from ApiHelp import request,unit
import MyLog as log

class TestXmlHotelSearchService(unittest.TestCase):

    @parameterized.expand(DataRead.load_test_cases(conf.apiDataPath + 'AllXmlCase.yaml'))
    def  test_xmlCases(self,caseId,caseName,apiKey,Author,requestBody,respect):
        xmlfile = conf.apiDataPath+requestBody['Body']
      
        print(caseId['caseId'],'caseName:',caseName['caseName'],Author['Author'],"')")
        
        logfile = conf.logPath + caseId['caseId'] + '.html'
        log.LogStart(apiKey['apiKey'],caseId['caseId']+caseName['caseName']+Author['Author'],logfile)
        
        response = request.xmlpost(apiKey['apiKey'],xmlfile)
        
        
        if response == None:
            self.assertEqual('resError',1,"请求无响应")
            log.info('请求无响应')
        else:
            try:
                log.info("response msg:")
                log.info("期望值:")
                log.info(respect['respect'])
                for k,v in respect['respect'].items():
                    self.assertEqual(unit.getXmlNote(response,k),v)
                log.info('用例通过')
            except Exception as e:
                log.err(e)
                raise
