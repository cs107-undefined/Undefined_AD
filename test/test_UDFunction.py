import unittest
import sys
import numpy as np
sys.path.append("./src/")

from undefined.UDFunction import UDFunction
from undefined.Calculator import sin, cos, exp
import math

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
		self.f5 = 5 + 2 

		# substraction
		self.f6 = 2*x - beta
		self.f7 = beta - 2*x
		self.f8 = 5*x - 3*x
		self.f9 = x - 5*x - 3*x
		self.f10 = 5 - 2 

		# multiplication
		self.f11 = 2*x + beta
		self.f12 = x*6 + beta
		self.f13 = beta + x*2
		self.f14 = beta + 4*x
		self.f15 = (x + 1) * (x - 2)

		# true divide
		self.f16 = 3*x/2
		self.f17 = (x+1)/(x-5)
		self.f20 = 4/3*x
		self.f24 = 343 / x

		# floor divide
		self.f18 = 3*x//4
		self.f19 = (x+1)//(x-5)
		self.f21 = 4//3*x
		self.f25 = 343 // x

		# power
		self.f22 = 4*x**3
		self.f23 = 4**2
		self.f50 = exp(sin(x)) - cos(x**0.5) * sin((cos(x)**2.0 + x**2.0)**0.5)
		self.f60 = 2**x
		
		# define extreme cases
		self.a = 2
		self.b = -1.11
		self.c = 99999.99
		self.d = -99999.99
		self.e = np.array([[self.a,self.b]])
		self.f = np.array([[self.a,self.b,self.c,self.d]])
		self.s = "str"
		self.af = UDFunction(self.a)
		self.bf = UDFunction(self.b)
		self.cf = UDFunction(self.c)
		self.df = UDFunction(self.d)
		self.ef = UDFunction(self.e)
		self.ff = UDFunction(self.f)
		self.g = math.pi / 2
		self.h = math.e

	# tearDown is used to delete output files if applicable.
	def tearDown(self):
		pass

	# the convention is to name the testing function as "test_<meaningful name>",
	# otherwise the unittest will not run.
	def test_add_integration(self):

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

		with self.assertRaises(Exception):
			self.f5.val
		with self.assertRaises(Exception):
			self.f5.der
		
		with self.assertRaises(Exception):
			self.f30 = "1" + 2*x
		
		with self.assertRaises(Exception):
			self.f40 = 2*x + "1" 
	
	def test_add_only(self):
		self.assertEqual(round(self.a+self.b, 2), 0.89)
		result1 = self.af+self.bf
		self.assertEqual(result1.val, 0.89)
		self.assertEqual(result1.der, 2)
		self.assertEqual(self.af.val + 1, 3)
		self.assertEqual(self.af.der + 1, 2)
		result2 = self.ff + 1
		self.assertEqual(result2.val.tolist(), [[ 3.0000000e+00, -1.1000000e-01, 1.0000099e+05, -9.9998990e+04]])
		self.assertEqual(result2.der, 1)
	
	def test_radd_only(self):
		self.assertEqual(1+self.af.val, 3)
		self.assertEqual(1+self.af.der, 2)
		result1 = self.af.__radd__(self.bf)
		self.assertEqual(result1.val, 0.89)
		result2 = 1 + self.ff
		self.assertEqual(result2.val.tolist(), [[ 3.0000000e+00, -1.1000000e-01, 1.0000099e+05, -9.9998990e+04]])
		self.assertEqual(result2.der, 1)

	def test_radd_integration(self):
		a = 2.0
		x = UDFunction(a)
		y = UDFunction(a + 2)
		z = "1"
		a = y.__radd__(x)
		self.assertEqual(a.val, 6)
		self.assertEqual(a.der, 2)
		with self.assertRaises(Exception):
			x.__radd__(z)

	def test_sub_integration(self):

		a = 2.0
		x = UDFunction(a)

		self.assertEqual(self.f6.val, 1.0)
		self.assertEqual(self.f6.der, 2.0)

		self.assertEqual(self.f7.val, -1.0)
		self.assertEqual(self.f7.der, -2.0)

		self.assertEqual(self.f8.val, 4.0)
		self.assertEqual(self.f8.der, 2.0)

		self.assertEqual(self.f9.val, -14.0)
		self.assertEqual(self.f9.der, -7.0)

		with self.assertRaises(Exception):
			self.f10.val
		with self.assertRaises(Exception):
			self.f10.der

		with self.assertRaises(Exception):
			self.f31 = "1" - 2*x

		with self.assertRaises(Exception):
			self.f41 = 2*x - "1"

	def test_rsub_integration(self):
		a = 2.0
		x = UDFunction(a)
		y = UDFunction(a + 2)
		z = "1"
		a = y.__rsub__(x)
		self.assertEqual(a.val, -2)
		self.assertEqual(a.der, 0)
		with self.assertRaises(Exception):
			x.__rsub__(z)
	
	def test_sub_only(self):
		self.assertEqual(round(self.a-self.b, 2), 3.11)
		result1 = self.af-self.bf
		self.assertEqual(result1.val, 3.11)
		self.assertEqual(result1.der, 0)
		self.assertEqual(self.af.val - 1, 1)
		self.assertEqual(self.af.der - 1, 0)
		result2 = self.ff - 1
		self.assertEqual(result2.val.tolist(), [[1.0, -2.11, 99998.99, -100000.99]])
		self.assertEqual(result2.der, 1)
	
	def test_rsub_only(self):
		self.assertEqual(1-self.af.val, -1)
		self.assertEqual(1-self.af.der, 0)
		result1 = self.af.__rsub__(self.bf)
		self.assertEqual(result1.val, -3.11)
		result2 = 1 - self.ff
		self.assertEqual(result2.val.tolist(), [[-1.0, 2.11, -99998.99, 100000.99]])
		self.assertEqual(result2.der, -1)



	def test_mul_integration(self):

		a = 2.0
		x = UDFunction(a)

		self.assertEqual(self.f11.val, 7.0)
		self.assertEqual(self.f11.der, 2.0)

		self.assertEqual(self.f12.val, 15.0)
		self.assertEqual(self.f12.der, 6.0)

		self.assertEqual(self.f13.val, 7.0)
		self.assertEqual(self.f13.der, 2.0)

		self.assertEqual(self.f14.val, 11.0)
		self.assertEqual(self.f14.der, 4.0)

		with self.assertRaises(Exception):
			self.f32 = "2" * 4*x
		
		with self.assertRaises(Exception):
			self.f42 = 4*x * "2"
	
	def test_rmul_integration(self):
		a = 2.0
		x = UDFunction(a)
		y = UDFunction(a + 2)
		z = "1"
		a = y.__rmul__(x)
		self.assertEqual(a.val, 8)
		self.assertEqual(a.der, 6)
		with self.assertRaises(Exception):
			x.__rmul__(z)

	def test_mul_only(self):
		result1 = self.af*self.bf
		self.assertEqual(result1.val, -2.22)
		self.assertEqual(result1.der, 0.89)
		self.assertEqual(self.af.val * 2, 4)
		self.assertEqual(self.af.der * 2, 2)
		result2 = self.ff * 2
		self.assertEqual(result2.val.tolist(), [[4.0, -2.22, 199999.98, -199999.98]])
		self.assertEqual(result2.der, 2)

	def test_rmul_only(self):
		result1 = self.af.__rmul__(self.bf)
		self.assertEqual(result1.val, -2.22)
		self.assertEqual(result1.der, 0.89)
		self.assertEqual(2 * self.af.val, 4)
		self.assertEqual(2 * self.af.der, 2)
		result2 = 2 * self.ff
		self.assertEqual(result2.val.tolist(), [[4.0, -2.22, 199999.98, -199999.98]])
		self.assertEqual(result2.der, 2)
	
	
	def test_neg(self):
		a = 2.0
		x = UDFunction(a)

		self.assertEqual(str(x.__neg__()), "value: -2.0 \nderivative: -1")



	def test_truedev_integration(self):

		a = 2.0
		x = UDFunction(a)

		self.assertEqual(self.f16.val, 3)
		self.assertEqual(self.f16.der, 1.5)
		
		self.assertEqual(self.f17.val, -1.0)
		self.assertEqual(round(self.f17.der, 2), -0.67)

		self.assertEqual(round(self.f20.val,2), 2.67)
		self.assertEqual(round(self.f20.der, 2), 1.33)

		self.assertEqual(round(self.f24.val,2), 171.5)
		self.assertEqual(round(self.f24.der, 2), -85.75)

		with self.assertRaises(Exception):
			self.f35 = "2" / 4*x
		
		with self.assertRaises(Exception):
			self.f45 = 4*x / "2"
	
	def test_rtruediv_integration(self):
		a = 2.0
		x = UDFunction(a)
		y = UDFunction(a + 2)
		z = "1"
		a = y.__rtruediv__(x)
		self.assertEqual(a.val, 0.5)
		self.assertEqual(a.der, 0.125)
		with self.assertRaises(Exception):
			x.__rtruediv__(z)
	
	def test_truediv_only(self):
		result1 = self.af/self.bf
		self.assertEqual(result1.val, -1.8)
		self.assertEqual(result1.der, -2.524)
		self.assertEqual(self.af.val / 2, 1)
		self.assertEqual(self.af.der / 2, 0.5)
		result2 = self.ff / 2
		self.assertEqual(result2.val.tolist(), [[1.0, -0.56, 50000.0, -50000.0]])
		self.assertEqual(result2.der, 0.5)
	
	def test_rtruediv_only(self):
		result1 = self.af.__rtruediv__(self.bf)
		self.assertEqual(result1.val, -0.56)
		self.assertEqual(result1.der, 0.778)
		self.assertEqual(2 / self.af.val, 1)
		self.assertEqual(2 / self.af.der, 2)
		result2 = 2 / self.ff
		self.assertEqual(result2.val.tolist(), [[1.0, -1.8, 0.0, -0.0]])
		self.assertEqual(result2.der.tolist(), [[-0.5, -1.623, -0, -0]])


	def test_floordev_integration(self):

		a = 2.0
		x = UDFunction(a)

		self.assertEqual(self.f18.val, 1.0)
		self.assertEqual(self.f18.der, 0)
		
		self.assertEqual(self.f19.val, -1.0)
		self.assertEqual(round(self.f19.der, 2), -1.0)

		self.assertEqual(round(self.f21.val,2), 2)
		self.assertEqual(round(self.f21.der, 2), 1)

		self.assertEqual(round(self.f25.val,2), 171)
		self.assertEqual(round(self.f25.der, 2), -86)

		with self.assertRaises(Exception):
			self.f36 = "2" // 4*x
		
		with self.assertRaises(Exception):
			self.f46 = 4*x // "2"
	
	def test_rfloordev_integration(self):
		a = 2.0
		x = UDFunction(a)
		y = UDFunction(a + 2)
		z = "1"
		a = y.__rfloordiv__(x)
		self.assertEqual(a.val, 0)
		self.assertEqual(a.der, 0)
		with self.assertRaises(Exception):
			x.__rfloordiv__(z)
	
	def test_floordev_only(self):
		result1 = self.af // self.bf
		self.assertEqual(result1.val, -2)
		self.assertEqual(result1.der, -3)
		self.assertEqual(self.af.val // 2, 1)
		self.assertEqual(self.af.der // 2, 0)
		result2 = self.ff // 2
		self.assertEqual(result2.val.tolist(), [[1.0, -1.0, 49999.0, -50000.0]])
		self.assertEqual(result2.der, 0)
	
	def test_rfloordev_only(self):
		result1 = self.af.__rfloordiv__(self.bf)
		self.assertEqual(result1.val, -1)
		self.assertEqual(result1.der, 0)
		self.assertEqual(2 // self.af.val , 1)
		self.assertEqual(2 // self.af.der, 2)
		result2 = 2 // self.ff 
		self.assertEqual(result2.val.tolist(), [[1.0, -2.0, 0.0, -1.0]])
		self.assertEqual(result2.der.tolist(), [[-1.0, -2.0, -1.0, -1.0]])


	def test_power(self):

		self.assertEqual(self.f22.val, 32)
		self.assertEqual(self.f22.der, 48)

		self.assertEqual(round(self.f50.val, 2), 2.34)
		self.assertEqual(round(self.f50.der, 2), -0.64) # Value check

		with self.assertRaises(Exception):
			self.f23.val
		with self.assertRaises(Exception):
			self.f23.der

		# test other as ndarray
		a = 2.0
		x = UDFunction(a)
		y = UDFunction(np.array([a]))
		self.f51 = x**y
		self.assertEqual(self.f51.val,4)
		self.assertEqual(self.f51.der,6.773)

		x1 = UDFunction(np.array([[2]]))
		y1 = UDFunction(np.array([[2]]))


		self.f52 = x1 ** y1
		self.assertEqual(self.f52.val[0],4.0)
		self.assertEqual(self.f52.der[0],6.773)

		# raise value error
		x2 = UDFunction(np.array([1]))
		y2 = UDFunction(np.array([1,2]))
		
		with self.assertRaises(ValueError) as context:
			x2 ** y2

		x3 = UDFunction(np.array(2))
		y3 = UDFunction(2)

		self.f53 = x3 ** y3
		self.assertEqual(self.f53.val,4)
		self.assertEqual(self.f53.der,6.773)

		self.assertEqual(self.f60.val, 4)
		self.assertEqual(self.f60.der, 2.773)

	def test_rpow(self):
		a = 2
		# test __rpow__
		# This pa
		x = UDFunction(a)

		self.f60 = 2 ** x
		self.assertEqual(self.f60.val,4)
		self.assertEqual(self.f60.der,2.773)
	
	def test_eq(self):
		self.assertTrue(self.f22 == 32)
		self.assertTrue(self.f19 == -1)
		self.assertTrue(round(self.f25, 2) == 171)
		self.assertTrue(round(self.f20, 2) == 2.67) 

		self.assertTrue(self.f22 == self.f22)
		self.assertTrue(self.f11 == self.f13)

		with self.assertRaises(TypeError):
			self.f11 == "self.f13"
	
	def test_ne(self):
		self.assertTrue(self.f19 != -12)
		self.assertTrue(round(self.f25, 2) != 161)
		self.assertTrue(self.f22 != self.f19)

		with self.assertRaises(TypeError):
			self.f11 != "self.f13"
	
	def test_lt(self):
		self.assertTrue(self.f19 < 12)
		self.assertTrue(round(self.f25, 2) < 200)
		self.assertTrue(self.f19 < self.f25)

		with self.assertRaises(TypeError):
			self.f25 < "self.f19"
	
	def test_gt(self):
		self.assertTrue(self.f19 > -12)
		self.assertTrue(round(self.f25, 2) > -200)
		self.assertTrue(self.f25 > self.f19)

		with self.assertRaises(TypeError):
			self.f25 > "self.f19"
	
	def test_le(self):
		self.assertTrue(self.f19 <= 12)
		self.assertTrue(round(self.f25, 2) <= 200)
		self.assertTrue(self.f19 <= self.f25)

		self.assertTrue(self.f22 <= 32)
		self.assertTrue(self.f19 <= -1)

		with self.assertRaises(TypeError):
			self.f25 <= "self.f19"

	def test_ge(self):
		self.assertTrue(self.f19 >= -12)
		self.assertTrue(round(self.f25, 2) >= -200)
		self.assertTrue(self.f25 >= self.f19)

		self.assertTrue(self.f22 >= 32)
		self.assertTrue(self.f19 >= -1)

		with self.assertRaises(TypeError):
			self.f25 >= "self.f19"
		
	
	


# this will help to run the unittest directly. 
if __name__ == "__main__":
	unittest.main()





