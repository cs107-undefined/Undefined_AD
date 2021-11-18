import unittest
import sys
# # temp solution for directory.

sys.path.append("./src/")

from undefined.API import trace
from undefined.Calculator import *



class TestAPI(unittest.TestCase):

    def setUp(self):

        self.f1 = lambda x: x + 2
        self.f2 = lambda x, y: x + y - 1
        self.f3 = lambda x, y: 2*x + sqrt(y)

    def test_trace(self):

        self.assertEqual(str(trace(self.f1, x = 2)), f"value: 4 \n" + f"derivative: 1")
        self.assertEqual(str(trace(self.f1, mode = 'forward', x = 2)), f"value: 4 \n" + f"derivative: 1")
        
        with self.assertRaises(NotImplementedError) as context:
            trace(self.f1, mode = 'backward', x = 2)
            # self.assertTrue('This is broken' in context.exception)
        with self.assertRaises(AttributeError) as context:
            trace(self.f1, mode = 'undefined', x = 2)
            # self.assertTrue('This is broken' in context.exception)

        self.assertEqual(str(trace(self.f2, x = 2, y = 4)), f"value: 5 \n" + f"derivative: [1 1]")
        self.assertEqual(str(trace(self.f2, y = 4, x = 2)), f"value: 5 \n" + f"derivative: [1 1]")

        self.assertEqual(str(trace(self.f3, x = 2, y = 4)), f"value: 6.0 \n" + f"derivative: [2.   0.25]")


if __name__ == "__main__":
    unittest.main()
    # f1 = lambda x, y: sqrt(exp(x*y))
    # x = UDFunction(1, np.array([1,0]))
    # y = UDFunction(2, np.array([0,1]))
    # trace(f1, x = 2, y = 4)