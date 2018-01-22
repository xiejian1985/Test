# coding=utf-8

import unittest

class Test(unittest.TestCase):
	"""docstring for Test"""
	def setUp(self):
		self.number = int(input('Enter your number:'))

	def test_case1(self):
		print(self.number)
		self.assertEqual(self.number, 10, msg='Your number is not 10.')

	def test_case2(self):
		print(self.number)
		self.assertEqual(self.number, 20, msg='Your number is not 20.')

	@unittest.skip('暂时跳过该条用例')
	def test_case3(self):
		print(self.number)
		self.assertEqual(self.number, 30, msg='Your number is not 30.')

	def tearDown(self):
		print('Test Over.')

# 执行测试用例第 1 种方式
# if __name__ == '__main__':
# 	unittest.main()


# 执行测试用例第 2 种方式
suite = unittest.TestSuite()

suite.addTest(Test('test_case2'))
suite.addTest(Test('test_case1'))
suite.addTest(Test('test_case3'))

runner = unittest.TextTestRunner()
runner.run(suite)