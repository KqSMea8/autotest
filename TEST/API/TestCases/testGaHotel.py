import DataRead
from ApiHelp.config import conf
from parameterized import parameterized, param
from .BaseTest import BaseTest


class TestGaHotel(BaseTest):
    '''综合测试用例'''

    # @parameterized.expand(DataRead.load_test_cases(conf.apiDataPath + 'GaHotelSingle.yaml'))
    # def  test_SingleCases(self,caseId,caseName,apiKey,Author,requestBody,respect):
    #     self.baseCases(caseId,caseName,apiKey,Author,requestBody,respect)

    # @parameterized.expand(DataRead.load_test_cases(conf.apiDataPath + 'GaHotelPolicy.yaml'))
    # def  test_PolicyCases(self,caseId,caseName,apiKey,Author,requestBody,respect):
    #     self.baseCases(caseId,caseName,apiKey,Author,requestBody,respect)

    # @parameterized.expand(DataRead.load_test_cases(conf.apiDataPath + 'GaHotelSearch.yaml'))
    # def  test_SearchCases(self,caseId,caseName,apiKey,Author,requestBody,respect):
    #     self.baseCases(caseId,caseName,apiKey,Author,requestBody,respect)

    def test_jsonMethod(self):
        '''json数据测试'''
        files = DataRead.load_test_cases(conf.apiDataPath+'AllJsonCase.yaml')

        def testsub(file):
            datas = DataRead.load_test_cases(conf.apiDataPath + 'JsonSubCase/' +file)
            for data in datas:
                caseinfo = data[0]['caseId'] + " "+'caseName:' + data[1]['caseName'] + data[3]['Author']
                with self.subTest(data=caseinfo):
                    self.baseCases(data[0],data[1],data[2],data[3],data[4],data[5])

        for file in files:
            testsub(file[0])
    
    def test_xmlMethod(self):
        '''xml数据测试'''
        files = DataRead.load_test_cases(conf.apiDataPath+'AllXmlCase.yaml')
        
        def testsub(file):
            datas = DataRead.load_test_cases(conf.apiDataPath + 'XmlSubCase/' + file)
            for data in datas:
                caseinfo = data[0]['caseId'] + " "+'caseName:' + data[1]['caseName'] + data[3]['Author']
                with self.subTest(data=caseinfo):
                    self.xmlBaesCase(data[0],data[1],data[2],data[3],data[4],data[5])
        
        for file in files:
            testsub(file[0])