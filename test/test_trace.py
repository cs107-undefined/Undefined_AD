# we are going to test the forward model, reverse model and multiple vector functions here. 
import unittest
import sys

sys.path.append("./src/")
from undefined.API import trace
from undefined.UDFunction import UDFunction
from undefined.Calculator import sin, cos, exp, tan, sqrt, log
import numpy as np

class TestTrace(unittest.TestCase):

    def setUp(self):
        self.f1 = lambda x: sqrt(exp(sin(x)))
        self.f2 = lambda x: exp(x**2 + sin(x))
        self.f3 = lambda x: sin(exp(2**x))
        self.f4 = lambda x: x**sin(x+2)
        self.f5 = lambda x, y: exp(1-6*x) * tan(4*x + 2*y)
        self.f6 = lambda x: 1 / (8 + cos(2*np.pi*x))
        self.f7 = lambda x, y, z: x*exp(y**2 - z**2)
        self.f8 = lambda x: log(x*3 + tan(2*x), np.e) + 2**x
        self.f10 = lambda x: log(x*3, np.e)
        self.f9 = lambda x, y: x**y
    
    def tearDown(self):
        pass

    def test_forward(self):
        result1 = trace(self.f1, x = 2)
        self.assertEqual(result1, (1.58, -0.33))
        self.assertEqual(trace(self.f2, x = 3), (9331.210, 46749.43))
        # self.assertEqual(trace(self.f3, x = 3), (0.40, -15137.2))
        self.assertEqual(trace(self.f4, x = 3), (0.35, -0.00))
    
        self.assertEqual(str(trace(self.f5, x = 2, y = 3)), "(0.0, array([0.003, 0.002]))")
        # print(trace(self.f7, x = 1, y = 2, z = 3))
        self.assertEqual(str(trace(self.f7, x = 1, y = 2, z = 3)), "(0.01, array([ 0.007,  0.027, -0.04 ]))")
        # self.assertEqual(trace(self.f8, x = 3), (2.16, 0.59))
        self.assertEqual(trace(self.f10, x = 2), (1.79, 0.5))
        self.assertEqual(str(trace(self.f9, x = 5, y = 3)), "(125, array([ 75.  , 201.18]))")



    # def test_reverse(self):
    #     result1 = trace(self.f1, mode = "reverse", x = 2)
    #     self.assertEqual(result1, (1.58, [-0.3278445959597162]))

if __name__ == "__main__":
    unittest.main()
