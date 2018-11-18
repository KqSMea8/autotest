import DataRead
from ApiHelp.config import conf
from parameterized import parameterized,param
from .BaseTest import BaseTest

class TestTemp(BaseTest):
	'''单接口测试用例'''
	def test_excelData(self):
		files =  DataRead.load