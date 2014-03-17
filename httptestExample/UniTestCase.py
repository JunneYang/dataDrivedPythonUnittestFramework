#-*- coding: utf-8 -*-
#!/usr/bin/env python
import unittest
import httplib
import json

import TestConfig
from LogLib import *

class Items_UniTestCase(unittest.TestCase):
    def TestServiceProc(self,testCaseID):
        try:
            CaseName=TestConfig.paseTestCase[testCaseID]['info']['name']
            SubService=TestConfig.paseTestCase[testCaseID]['params']['subservice']
            SecretKey=TestConfig.paseTestCase[testCaseID]['params']['secretkey']
            ServiceKey=TestConfig.paseTestCase[testCaseID]['params']['servicekey']
            AlItems=TestConfig.paseTestCase[testCaseID]['params']['algorithmId']
            ItemsID=TestConfig.paseTestCase[testCaseID]['params']['item_ids']

            logging.debug(u"Start Log of Case:"+CaseName+"*"*20)
            conn = httplib.HTTPConnection(TestConfig.HOST+u":"+str(TestConfig.PORT))
            headers = {"Content-type":"application/json"}
            params = ({
	                   "service": "ItemService",
                    	"method": "GetItemsByItem",
	                   "request": {
	                	  "header": {
	                   	   "subservice":SubService,
	                   	   "secretkey": SecretKey,
	                   	   "servicekey": ServiceKey
	               	   },
                	   "algorithmId": AlItems,
                	   "item_ids": ItemsID
            	   }
            })
            conn.request(TestConfig.HTTP_Method, TestConfig.HTTP_URL, json.JSONEncoder().encode(params), headers)

            if((SubService,SecretKey,ServiceKey) != ('sub','pass','key1')):
                try:
                    response = conn.getresponse()
                    logging.error(u"Error WhiteSheet, Should No Response")
                    raise Exception(u"Should No Response")
                except:
                    conn.close()
                    return

            response = conn.getresponse()
            data = response.read()
            exp_data=TestConfig.paseTestCase[testCaseID]['exp_data']
            logging.debug(u"ExpData:"+str(exp_data))

            if response.status == 200:
                Ret=json.loads(data,encoding='UTF-8')
                Ret=Ret['response']['items']
                Ret=sorted(Ret,key=lambda x:(len(x['value']),x['value'][0],x['id']),reverse=True)
                if(len(Ret)==0):
                    Ret=''
                logging.debug(u"ActData:"+str(Ret))

                try:
                    assert(Ret == exp_data)
                except Exception as e:
                    logging.error(u"Verify ERROR:ExpData Not Equal ActData")
                    raise Exception(str(e))
            else:
                logging.error(u"ERROR:Not 200OK")
                raise Exception("ERROR,Not 200OK")
        except Exception as e:
            logging.error(str(e))
            raise Exception(str(e))
        finally:
            conn.close()
            logging.debug(u"End Log of Case:"+CaseName+"*"*20+"\r\n\r\n")

    for testCaseID in TestConfig.paseTestCase:
        exec("def test_%s(self): self.TestServiceProc('%s')" %(testCaseID,testCaseID))


if __name__ == '__main__':
    logging.debug(u"Task Start"+u"*"*100+"\r\n\r\n")
    TestSuit=unittest.TestLoader().loadTestsFromTestCase(Items_UniTestCase)
    unittest.TextTestRunner(verbosity=2).run(TestSuit)
    logging.debug(u"Task End"+u"*"*100+"\r\n\r\n")

