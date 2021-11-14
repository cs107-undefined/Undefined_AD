import unittest
import sys

# temp solution for directory.
sys.path.append("../src/undefined")
sys.path.append("src/undefined")

import Calculator as cal
from UDFunction import UDFunction


class TestCalculator(unittest.TestCase):

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

    def test_sine(self):

        self.assertEqual(round(self.f3.val, 2), 0.84)
        self.assertEqual(round(self.f3.der, 2), 0.54)

        self.assertEqual(round(self.f4.val, 2), -0.76)
        self.assertEqual(round(self.f4.der, 2), -1.31)
    
    def test_cosine(self):

        self.assertEqual(round(self.f1.val, 2), 0.54)
        self.assertEqual(round(self.f1.der, 2), -0.84)

        self.assertEqual(round(self.f2.val, 2), -0.99)
        self.assertEqual(round(self.f2.der, 2), -0.28)

    def test_tangent(self):

        self.assertEqual(round(self.f5.val, 2), 1.56)
        self.assertEqual(round(self.f5.der, 2), 3.43)

        self.assertEqual(round(self.f6.val, 2), 1.16)
        self.assertEqual(round(self.f6.der, 2), 4.68)
    
    def test_sqrt(self):

        self.assertEqual(round(self.f7.val, 2), 1)
        self.assertEqual(round(self.f7.der, 2), 0.5)

        self.assertEqual(round(self.f8.val, 2), 3.41)
        self.assertEqual(round(self.f8.der, 2), 2.71)

   


if __name__ == "__main__":
    unittest.main()