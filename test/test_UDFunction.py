import unittest
import sys
sys.path.append("../src/undefined")
from UDFunction import UDFunction

class TestUDFunction(unittest.TestCase):

	# the setUp and tearDown are the methods to keep the code dry.
	def setUp(self):

		alpha = 2.0
		beta  = 3.0

		a = 2.0
		x = UDFunction(a)
		
		# addition
		self.f1 = -2*x + beta
		self.f2 = beta + 2*x
		self.f3 = 5*x + 3*x
		self.f4 = x + 5*x + 3*x
		#self.f5 = 5 + 2 

		# substraction
		# self.f6 = 2*x - beta
		# self.f7 = beta - 2*x
		# self.f8 = 5*x - 3*x
		# self.f9 = x - 5*x - 3*x
		# self.f10 = 5 - 2 

		# multiplication
		self.f11 = 2*x + beta
		self.f12 = x*6 + beta
		self.f13 = beta + x*2
		self.f14 = beta + 4*x
		# self.f15 = (x + 1) * (x - 2)

		# divide
		#self.f16 = 3*x/2
		# self.f17 = (x+1)/(x-5)


	# tearDown is used to delete output files if applicable.
	def tearDown(self):
		pass

	# the convention is to name the testing function as "test_<meaningful name>",
	# otherwise the unittest will not run.
	def test_add(self):

		a = 2.0
		x = UDFunction(a)

		self.assertEqual(self.f1.val, -1.0)
		self.assertEqual(self.f1.der, -2.0)
		self.assertEqual(self.f2.val, 7.0)
		self.assertEqual(self.f2.der, 2.0)
		self.assertEqual(self.f3.val, 16.0)
		self.assertEqual(self.f3.der, 8.0)
		self.assertEqual(self.f4.val, 18.0)
		self.assertEqual(self.f4.der, 9.0)
		#self.assertEqual(self.f5.val, 7.0)
		#self.assertEqual(self.f5.der, 0.0)


		# result1 = UDFunction.add(self.f1)
		# self.assertEqual(self.f1, 2.0)
		# # result2 = UDFunction.add(self.f2)
		# self.assertEqual(self.f2, 2.0)
		# # result3 = UDFunction.add(self.f3)
		# self.assertEqual(self.f3, 8.0)
		# # result4 = UDFunction.add(self.f4)
		# self.assertEqual(self.f4, 9.0)
		# # result5 = UDFunction.add(self.f5)
		# self.assertEqual(self.f5, 0.0)


	# def test_sub(self):

		
		# self.assertEqual(self.f6.val, 1.0)
		# result7 = UDFunction.sub(self.f7)
		# self.assertEqual(result7, 2.0)
		# result8 = UDFunction.sub(self.f8)
		# self.assertEqual(result8, 2.0)
		# result9 = UDFunction.sub(self.f9)
		# self.assertEqual(result9, -7.0)
		# result10 = UDFunction.sub(self.f10)
		# self.assertEqual(result9, 0.0)

	def test_mul(self):

		self.assertEqual(self.f11.val, 7.0)
		self.assertEqual(self.f11.der, 2.0)

		self.assertEqual(self.f12.val, 15.0)
		self.assertEqual(self.f12.der, 6.0)

		self.assertEqual(self.f13.val, 7.0)
		self.assertEqual(self.f13.der, 2.0)

		self.assertEqual(self.f14.val, 11.0)
		self.assertEqual(self.f14.der, 4.0)

		# self.assertEqual(self.f13, 2.0)
		# self.assertEqual(self.f14, 4.0)
		# self.assertEqual(self.f15, 3.0)

	# def test_dev(self):
	# 	self.assertEqual(self.f16.val, 3)
	# 	self.assertEqual(self.f16.der, 1.5)
		
		# self.assertEqual(self.f17, -4.0)





# this will help to run the unittest directly. 
if __name__ == "__main__":
	unittest.main()





