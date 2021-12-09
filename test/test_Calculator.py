import unittest
import sys
# import undefined
sys.path.append("./src/")
from undefined import Calculator as cal
from undefined.UDFunction import UDFunction
import math
import numpy as np


class TestCalculator(unittest.TestCase):
    # TODO: arccos, arcsin, ..., not tested!!!!
    def setUp(self):

        alpha = 2.0
        beta  = 3.0

        a = 1.0
        x = UDFunction(a)

        # test cosine
        self.f1 = cal.cos(x)
        self.f2 = cal.cos(2*x + 1)

        # test sine
        self.f3 = cal.sin(x)
        self.f4 = cal.sin(2*x + 2)

        # test tangent
        self.f5 = cal.tan(x)
        self.f6 = cal.tan(2*x + 2)

        # test sqrt
        self.f7 = cal.sqrt(x)
        self.f8 = 2*x + cal.sqrt(2*x)

        # test exp
        self.f9 = cal.exp(x)
        self.f10 = 2*x - cal.exp(x) + 1

        # test log
        self.f11 = cal.log(x, math.e)
        self.f12 = 5*x + cal.log(x+1, math.e) - 2/x

        self.f13 = cal.log(x, 2)
        self.f1000 = cal.log(x, np.e)


    def test_sine(self):

        a = "2.0"
        x = UDFunction(a)

        self.assertEqual(round(self.f3.val, 2), 0.84)
        self.assertEqual(round(self.f3.der, 2), 0.54)

        self.assertEqual(round(self.f4.val, 2), -0.76)
        self.assertEqual(round(self.f4.der, 2), -1.31)

        with self.assertRaises(TypeError):
            self.f45 = cal.sin(2*x) + x 
        
        self.assertEqual(cal.sin(np.array([np.pi/2])), 1)
        self.assertEqual(cal.sin(np.pi/2), 1)

        with self.assertRaises(TypeError):
            self.f000 = cal.sin("3/np.pi")

    
    def test_cosine(self):
        a = "2.0"
        x = UDFunction(a)

        self.assertEqual(round(self.f1.val, 2), 0.54)
        self.assertEqual(round(self.f1.der, 2), -0.84)

        self.assertEqual(round(self.f2.val, 2), -0.99)
        self.assertEqual(round(self.f2.der, 2), -0.28)

        with self.assertRaises(TypeError):
            self.f46 = cal.cos(2*x) + x 
        
        self.assertEqual(cal.cos(np.array([np.pi])), -1)
        self.assertEqual(cal.cos(np.pi), -1)

        with self.assertRaises(TypeError):
            self.f000 = cal.cos("3/np.pi")

    def test_tangent(self):

        a = "2.0"
        x = UDFunction(a)

        self.assertEqual(round(self.f5.val, 2), 1.56)
        self.assertEqual(round(self.f5.der, 2), 3.43)

        self.assertEqual(round(self.f6.val, 2), 1.16)
        self.assertEqual(round(self.f6.der, 2), 4.68)

        with self.assertRaises(TypeError):
            self.f47 = cal.tan(2*x) + x 
        
        self.assertEqual(cal.tan(np.array([0])), 0)
        self.assertEqual(cal.tan(0), 0)

        with self.assertRaises(TypeError):
            self.f000 = cal.tan("3/np.pi")
    
    def test_sqrt(self):
        a = "2.0"
        x = UDFunction(a)

        self.assertEqual(round(self.f7.val, 2), 1)
        self.assertEqual(round(self.f7.der, 2), 0.5)

        self.assertEqual(round(self.f8.val, 2), 3.41)
        self.assertEqual(round(self.f8.der, 2), 2.71)

        with self.assertRaises(TypeError):
            self.f48 = cal.sqrt(2*x) + x 
        
        self.assertEqual(cal.sqrt(np.array([4])), 2)
        self.assertEqual(cal.sqrt(4), 2)

        with self.assertRaises(TypeError):
            self.f000 = cal.sqrt("3/np.pi")

    def test_exp(self):

        a = "2.0"
        x = UDFunction(a)

        self.assertEqual(round(self.f9.val, 2), 2.72)
        self.assertEqual(round(self.f9.der, 2), 2.72)

        self.assertEqual(round(self.f10.val, 2), 0.28)
        self.assertEqual(round(self.f10.der, 2), -0.72)

        with self.assertRaises(TypeError):
            self.f49 = cal.exp(2*x) + x 
        
        self.assertEqual(cal.exp(np.array([1])), np.e)
        self.assertEqual(cal.exp(1), np.e)

        with self.assertRaises(TypeError):
            self.f000 = cal.exp("3/np.pi")

    def test_log(self):
        a = "2.0"
        x = UDFunction(a)

        self.assertEqual(round(self.f11.val, 2), 0)
        self.assertEqual(round(self.f11.der, 2), 1)

        self.assertEqual(round(self.f12.val, 2), 3.69)
        self.assertEqual(round(self.f12.der, 2), 7.5)

        self.assertEqual(round(self.f13.val, 2), 0)
        self.assertEqual(round(self.f13.der, 2), 1.44)

        with self.assertRaises(TypeError):
            self.f50 = cal.log(2*x, 2) + x 
        
        self.assertEqual(cal.log(np.array([1]), np.e), 0)
        self.assertEqual(cal.log(1, np.e), 0)

        with self.assertRaises(TypeError):
            self.f000 = cal.log("3/np.pi", np.e)


if __name__ == "__main__":
    unittest.main()