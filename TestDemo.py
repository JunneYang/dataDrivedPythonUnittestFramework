#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2015/09/08

@author: yangjun
'''
import unittest 
import sys
import json
import logging

class ParametrizedTestCase(unittest.TestCase): 
    """ TestCase classes that want to be parametrized should 
        inherit from this class. 
    """
    def __init__(self, methodName='runTest', param=None): 
        super(ParametrizedTestCase, self).__init__(methodName) 
        self.param = param 
    @staticmethod 
    def parametrize(testcase_class, param=None): 
        """ Create a suite containing all tests taken from the given 
            subclass, passing them the parameter 'param'. 
        """ 
        testloader = unittest.TestLoader() 
        testnames = testloader.getTestCaseNames(testcase_class) 
        suite = unittest.TestSuite() 
        for name in testnames: 
            suite.addTest(testcase_class(name, param=param)) 
        return suite

class TestDemo(ParametrizedTestCase):
    def test_something(self):
        print 'param : ', self.param 
        assert(1 == 1)
    def test_something_else(self): 
        assert(2 == 2)

          
if __name__ == "__main__":
    try:
        param = sys.argv[1]
        print 'param : ', param
        param = json.loads(param)
        suite = unittest.TestSuite() 
        suite.addTest(ParametrizedTestCase.parametrize(TestDemo, param=param)) 
        unittest.TextTestRunner(verbosity=2).run(suite)
    except Exception as e:
        logging.error(e, exc_info=1)
        raise Exception(e)

