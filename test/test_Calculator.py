import unittest
import sys

sys.path.append("../src/undefined")
import Calculator as cal
from UDFunction import UDFunction


class TestCalculator(unittest.TestCase):

    def setUp(self):

        alpha = 2.0
        beta  = 3.0

        a = 1.0
        x = UDFunction(a)

        # try cosine
        self.f1 = cal.cos(x)
        self.f2 = cal.cos(2*x + 1)

        # try sine
        self.f3 = cal.sin(x)
        self.f4 = cal.sin(2*x + 2)

        # try tangent
        self.f5 = cal.tan(x)
        self.f6 = cal.tan(2*x + 2)

    def test_sine(self):

        self.assertEqual(round(self.f3.val, 2), 0.84)
        self.assertEqual(round(self.f3.der, 2), 0.54)

        self.assertEqual(round(self.f4.val, 2), -0.76)
        self.assertEqual(round(self.f4.der, 2), -1.31)
    


if __name__ == "__main__":
    unittest.main()