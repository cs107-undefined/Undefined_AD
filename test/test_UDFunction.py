import unittest
import sys
sys.path.append("../src/undefined")

import UDFunction

class TestUDFunction(unittest.TestCase):

	# the following classmethods are designed for something you just need to run once
	# such as populate some data.
	# @classmethod
	# def setUpClass(cls):
	# 	pass 

	# @classmethod
	# def tearDownClass(cls):
	# 	pass

	# the setUp and tearDown are the methods to keep the code dry.
	def setUp(self):

		alpha = 2.0
		beta  = 3.0

		a = 2.0
		x = UDFunction.<class_name>(a)
		
		# addition
		self.f1 = 2x + beta
		self.f2 = beta + 2x
		self.f3 = 5x + 3x
		self.f4 = x + 5x + 3x
		self.f5 = 5 + 2 

		# substraction
		self.f6 = 2x - beta
		self.f7 = beta - 2x
		self.f8 = 5x - 3x
		self.f9 = x - 5x - 3x
		self.f10 = 5 - 2 

		# multiplication
		self.f11 = 2*x + beta
		self.f12 = x*6 + beta
		self.f13 = beta + x*2
		self.f14 = beta + 4*x
		self.f15 = (x + 1) * (x - 2)

		# divide
		self.f16 = 3x/2
		self.f17 = (x+1)/(x-5)


	# tearDown is used to delete output files if applicable.
	def tearDown(self):
		pass

	# the convention is to name the testing function as "test_<meaningful name>",
	# otherwise the unittest will not run.
	def test_add(self):

		result1 = UDFunction.add(self.f1)
		self.assertEqual(self.f1, 2.0)
		result2 = UDFunction.add(self.f2)
		self.assertEqual(result2, 2.0)
		result3 = UDFunction.add(self.f3)
		self.assertEqual(result3, 8.0)
		result4 = UDFunction.add(self.f4)
		self.assertEqual(result4, 9.0)
		result5 = UDFunction.add(self.f5)
		self.assertEqual(result5, 0.0)


	def test_sub(self):

		result6 = UDFunction.sub(self.f6)
		self.assertEqual(result6, 2.0)
		result7 = UDFunction.sub(self.f7)
		self.assertEqual(result7, 2.0)
		result8 = UDFunction.sub(self.f8)
		self.assertEqual(result8, 2.0)
		result9 = UDFunction.sub(self.f9)
		self.assertEqual(result9, -7.0)
		result10 = UDFunction.sub(self.f10)
		self.assertEqual(result9, 0.0)

	def test_mul(self):

		self.assertEqual(self.f11, 2.0)
		self.assertEqual(self.f12, 6.0)
		self.assertEqual(self.f13, 2.0)
		self.assertEqual(self.f14, 4.0)
		self.assertEqual(self.f15, 3.0)

	def test_dev(self):
		self.assertEqual(self.f16, 1.5)
		self.assertEqual(self.f17, -4.0)





# this will help to run the unittest directly. 
if __name__ == "__main__":
	unittest.main()