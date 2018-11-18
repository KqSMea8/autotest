
from ApiHelp import unit,report
from ApiHelp.config import conf
from TestCases import *

import sys,unittest,os
sys.path.append(os.path.abspath("TEST/Public"))
import BaseRun,getReleaseEnv


# for i in range(0,len(sys.argv)):
# 	print(sys.argv[i])
subenv = sys.argv[1]
if subenv == 'FAT':
	subenv = conf.FatSubEnv = getReleaseEnv.getFatSubenv('330304')
conf.Domain = "http://ws.global."+ subenv +".qa.nt.ctripcorp.com/"
if subenv == 'PROD':
	conf.Domain = "http://ws.global.ctripcorp.com/"

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestGaHotel))
# suite.addTest(unittest.makeSuite(TestXmlHotelSearchService))

BaseRun.baseRun(report,conf.report_dir,suite,conf.title,conf.description,conf.tester)

unit.makeDetailReport(conf.apiReport,conf.report_name,conf.excute_time,conf.Title,conf.Logs)
