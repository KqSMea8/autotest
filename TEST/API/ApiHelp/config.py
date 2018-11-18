import sys,time
KEY = ''
TOKEN = ''
class conf:
	Logs = []
	Title = 'IBU Hotel API Report'
	# Project = 'pj name'
	Domain = 'http://ws.global.uat.qa.nt.ctripcorp.com/'

	excute_time = "%0.f"%time.time()
	logPath = 'Test/Api/ApiResult/caseInfo/'
	
	apiDataPath = 'TEST/API/TestData/'
	
	report_dir = 'Test/API/ApiResult/index.html'
	file_dir = 'Test/API/ApiResult/' + excute_time
	report_name =  'index.html'
	apiReportName = 'allApiReport.html'
	apiReportDir = 'Test/API/ApiResult/caseInfo/'
	apiReport = apiReportDir + apiReportName

	FatSubEnv = ''

	title = 'IBU-Hotel Api Test'
	description = 'IBU-Hotel Api Run Result'

	tester = 'RUNNER SYSTEM'
	mailSubject = 'API自动化测试报告邮件'
	mailContent =  '自动化测试系统所发邮件,非本人所发,请勿直接回复,详情请点击连接查看\n\
					\n\
				http://10.2.61.236:8080/job/IBU-HOTEL-API/RunnerReport/'