import sys,os,codecs

def setMailBody(filePath,mailData):
    pf = codecs.open(filePath,'w+','utf-8')
    pf.write('<?xml version="1.0" encoding="UTF-8"?>')
    pf.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">')
    pf.write('<html>')
    pf.write('<head>')
    pf.write('  <title>'+mailData['title'] +'</title>')
    pf.write(  "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>")
    pf.write("<style>\
        .MsoNormal {\
        color:black;mso-style-unhide: no;\
        margin: 0cm; margin-bottom: .0001pt; text-justify: inter-ideograph;\
        mso-pagination: widow-orphan; font-size: 10.5pt;font-family: '微软雅黑','sans-serif';\
        }\
        table{border-spacing: 0; border: 2px solid #4F81BD;border-collapse: separate;\
        border-left: 0; border-radius: 2px;} \
        th, td {\
        border-left: 1px solid #4F81BD;\
         padding: 6px 12px; line-height: 20px;text-align: left;vertical-align: top; \
         border-top: 1px solid #4F81BD; }\
         </style>   "
    )
    pf.write('</head>')
    pf.write('<body>')
    pf.write('<br/>')
    pf.write('<div>')
    pf.write("<p class='MsoNormal'>Job Name: <b> "+mailData['title'] +"</b></p>")
    pf.write("<p class='MsoNormal'>Start Time：<b> "+ mailData['startTime']+"</b></p>")
    pf.write("<p class='MsoNormal'>Execute Env: <b>"+mailData['ENV']+"</b></p>")
    pf.write('<br/>')
    pf.write("<p class='MsoNormal'>\
        AssertTotal: <b>"+mailData['AsTotal']+"</b>&nbsp;&nbsp;\
        AssertSuccess: <b>"+mailData['AsSucc']+"</b>&nbsp;&nbsp;\
        AssertFailed: <b>"+mailData['AsFail']+"</b></p>")
    pf.write('</div>')
    pf.write('<br/>')
    pf.write('<div>')
    pf.write('\
        <table>\
            <tr>\
                <th>SuiteName</th>\
                <th>CaseNums</th>\
                <th>Case PassNums</th>\
                <th>Case faileNums</th>\
                <th>Status</th>\
            </tr>\
    ')
    pf.write("\
            <tr>\
                <td>"+mailData['suiteName']+"</td>\
                <td>"+mailData['caseCount']+"</td>\
                <td><p style='color:green;'>"+mailData['casePass']+"</p></td>\
                <td><p style='color:red;'>"+mailData['failedNum']+"</p></td>\
                <td>"+mailData['status']+"</td>\
            </tr>\
    </table>\
    ")
    pf.write('</div>')
    pf.write("<p class='MsoNormal'><a href='http://ci.ibuhotel.dev.qa.nt.ctripcorp.com/job/IBU-HOTEL-Online-UI/WebReport/' target='_blank'>Check Detail</a></p>")
    pf.write("<br/>\
    <br/>\
    <br/>\
    <br/>\
    <p class = 'MsoNormal'>自动化测试系统所发邮件,请勿直接回复</p>\
    <p class = 'MsoNormal'>UI自动化测试平台的问题联系：<a href='mailto:xx@xx.com?subject=UIautoTest Service'>Mafia</a></p>\
    ")
    pf.write('</body>')
    pf.write('</html>')
    
