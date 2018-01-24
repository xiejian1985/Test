# coding=utf-8

import unittest
from TestCase import test_baidu

suite = unittest.TestSuite
suite.addTest(test_baidu.BaiduTest('test_baidu'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner
    runner.run(suite)