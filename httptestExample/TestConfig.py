#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json

#测试用例路径
TestCaseFilePath=u"../CaseSuite/Items.case"
paseTestCase=json.load(open(TestCaseFilePath, "r"),encoding='utf-8')

#服务器参数配置
HOST=u"localhost"
PORT=18080

#URL参数
HTTP_Method=u"POST"
HTTP_URL=u"/lbs/da/openservice"

#日志路径设置
TestLogFilePath=u"./TestLog.txt"
