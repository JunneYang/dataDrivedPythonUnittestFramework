#-*- coding: utf-8 -*-
#!/usr/bin/env python
import unittest
testData=[{'inputData':1,'expData':2},
{'inputData':2,'expData':4},
{'inputData':3,'expData':6}]

class under_testClass():
    def X2(self,data):
        return data*2

class dataDrived_testCase(unittest.TestCase):
    def setUp(self):
        #数据预置
        pass
    def tearDown(self):
        #清理工作
        pass

    def procTest(self,testCaseID):
        inputData=testData[testCaseID]['inputData']
        expData=testData[testCaseID]['expData']
        actData=under_testClass().X2(inputData)
        assert(actData == expData)

    for testCaseID in xrange(len(testData)):
        exec("def test_case%s(self): self.procTest(%d)" %(testCaseID,testCaseID))

if __name__ == '__main__':
    TestSuit=unittest.TestLoader().loadTestsFromTestCase(dataDrived_testCase)
    unittest.TextTestRunner(verbosity=2).run(TestSuit)

