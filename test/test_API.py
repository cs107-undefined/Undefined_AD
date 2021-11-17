import unittest
import sys


# temp solution for directory.
sys.path.append("../src/undefined")
sys.path.append("src/undefined")
from UDFunction import UDFunction
from API import trace
from Calculator import *
import numpy as np


class TestAPI(unittest.TestCase):

    def setUp(self):

        self.f1 = lambda x: x + 2
        self.f2 = lambda x, y: x + y - 1
        self.f3 = lambda x, y: 2*x + sqrt(y)

        x = UDFunction(2, np.array([1, 0]))
        y = UDFunction(4, np.array([0, 1]))

    def test_trace(self):

        self.assertEqual(str(trace(self.f1, x = 2)), f"value: 4 \n" + f"derivative: 1")
        self.assertEqual(str(trace(self.f2, x = 2, y = 4)), f"value: 5 \n" + f"derivative: [1 1]")
        self.assertEqual(str(trace(self.f3, x = 2, y = 4)), f"value: 6.0 \n" + f"derivative: [2.   0.25]")


if __name__ == "__main__":
    unittest.main()
    # f1 = lambda x, y: sqrt(exp(x*y))
    # x = UDFunction(1, np.array([1,0]))
    # y = UDFunction(2, np.array([0,1]))
    # trace(f1, x = 2, y = 4)