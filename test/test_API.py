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

        self.assertEqual(str(trace(self.f1, x = 2)), '(4, 1)')
        self.assertEqual(str(trace(self.f1, mode = 'forward', x = 2)), '(4, 1)')
        print(trace(self.f3,mode='reverse',x=np.array([[2, 2]]), y=np.array([[1, 1]]))) 
        print(trace(self.f3,mode='reverse',plot = True, x=2, y=3))
        # with self.assertRaises(TypeError) as context:
        #     trace(self.f1, mode = 'undefined', x = 2)

        with self.assertRaises(AttributeError) as context:
            trace(self.f1, mode = 'undefined', x = 2)

        with self.assertRaises(TypeError) as context:
            (trace(self.f1, mode = 'reverse', x = np.array([2,1])))

        with self.assertRaises(TypeError) as context:
            (trace(self.f1, mode = 'reverse', x = "1"))
            # self.assertTrue('This is broken' in context.exception)

        self.assertEqual(str(trace(self.f2, x = 2, y = 4)), "(5, array([1, 1]))")
        self.assertEqual(str(trace(self.f2, y = 4, x = 2)), "(5, array([1, 1]))")

        self.assertEqual(str(trace(self.f3, x = 2, y = 4)), "(6.0, array([2.  , 0.25]))")


if __name__ == "__main__":
    unittest.main()
    # f1 = lambda x, y: sqrt(exp(x*y))
    # x = UDFunction(1, np.array([1,0]))
    # y = UDFunction(2, np.array([0,1]))
    # trace(f1, x = 2, y = 4)