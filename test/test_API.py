import sys
# # temp solution for directory.

sys.path.append(
    "./src/")


from undefined.Calculator import *
from undefined.API import trace
import unittest

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.a = 2
        self.b = - 1.11
        self.c = 99999.99
        self.d = -99999.99
        self.e = np.array([[self.a,self.b]])
        self.f = np.array([[self.a,self.b,self.c,self.d]])
        self.g = math.pi / 2
        self.h = math.e
        self.j = np.array([[self.a, self.b, self.g, self.h]])
        self.s = "str"

        self.f0 = lambda x: sqrt(x)
        self.f1 = lambda x: x + 2
        self.f2 = lambda x, y: x + y - 1
        self.f3 = lambda x, y: 2*x + sqrt(y)
        self.f12 = lambda x, y: sqrt(x) + sqrt(y)

    def test_trace_forward(self):
        # Stop using string comparing!!!!!!!
        self.assertEqual(trace(self.f1, x=2), (4, 1))
        self.assertEqual(trace(self.f1, mode='forward', x=2), (4, 1))

        self.assertEqual(trace(self.f2, x=2, y=4), (5, [[1], [1]]))
        self.assertEqual(trace(self.f2, y=4, x=2), (5, [[1], [1]]))
        self.assertEqual(trace(self.f3, x=2, y=4), (6.0, [[2.], [0.25]]))
        self.assertEqual(trace(self.f3, x=2, y=4, seeds = np.array([[2,2],[1,1]])), (6.0, [[4.25], [4.25]]))

        with self.assertRaises(TypeError):
            trace(self.f1,seeds = "1",x=np.array([[999]]))

        with self.assertRaises(TypeError):
            trace(self.f2,seeds = "1",x=np.array([[999]]),y=np.array([[99]]))

        with self.assertRaises(TypeError):
            trace(self.f2,seeds = np.array([1,2]),x=np.array([[999]]),y=np.array([[99]]))


        self.assertEqual(trace(self.f12, seeds= np.array([[1,2],[0,1]]), x = 1,y = 2)[1],[[0.5], [1.354]])
        self.assertEqual(trace(self.f0, seeds = 1, x = np.array([[10,1]]))[1],[[0.158, 0.5]])


    def test_trace_with_incompatible_inputs(self):
        with self.assertRaises(AttributeError):
            trace(self.f2, mode='undefined', x=np.array(
                [[1, 2, 3]]), y=np.array([[1, 2]]))

    def test_trace_with_different_moded(self):
        self.assertEqual(trace(self.f1, x=2), (4, 1))
        self.assertEqual(trace(self.f1, mode='forward', x=2), (4, 1))
        self.assertEqual(trace(self.f1, mode='reverse', x=2), (4, 1))
        with self.assertRaises(AttributeError):
            trace(self.f1, mode='undefined', x=2)

    def test_trace_reverse(self):
        self.assertEqual(trace(self.f1, mode='reverse', x=2), (4, 1))
        self.assertEqual(trace(self.f1, mode='reverse', x=2), (4, 1))
        with self.assertRaises(AttributeError):
            trace(self.f1, mode='undefined', x=2)
        self.assertEqual(trace(self.f2, mode='reverse',
                         x=2, y=4), (5, [[1], [1]]))
        self.assertEqual(trace(self.f2, mode='reverse',
                         y=4, x=2), (5, [[1], [1]]))
        self.assertEqual(trace(self.f3, mode='reverse',
                         x=2, y=4), (6.0, [[2.], [0.25]]))


        self.assertEqual(str(trace(self.f1, x = 2)), '(4, 1)')
        self.assertEqual(str(trace(self.f1, mode = 'forward', x = 2)), '(4, 1)')
        # print(trace(self.f3,mode='reverse',x=np.array([[2, 2]]), y=np.array([[1, 1]]))) 
        # print(trace(self.f3,mode='reverse',plot = True, x=2, y=3))
        # with self.assertRaises(TypeError) as context:
        #     trace(self.f1, mode = 'undefined', x = 2)

        with self.assertRaises(AttributeError) as context:
            trace(self.f1, mode = 'undefined', x = 2)

        with self.assertRaises(TypeError) as context:
            (trace(self.f1, mode = 'reverse', x = np.array([2,1])))

        with self.assertRaises(TypeError) as context:
            (trace(self.f1, mode = 'reverse', x = "1"))
            # self.assertTrue('This is broken' in context.exception)

    def test_trace_multiple_vector_inputs(self):
        self.assertEqual(trace(self.f3, x=np.array([[2, 2]]), y=np.array([[4, 4]]))[
                         1], [[2., 2.], [0.25, 0.25]])
        self.assertEqual(trace(self.f3, mode='reverse', x=np.array(
            [[2, 2]]), y=np.array([[4, 4]]))[1], [[2., 2.], [0.25, 0.25]])

    def test_trace_single_vector_inputs(self):
        self.assertEqual(trace(self.f1, x=np.array([[2, 2]]))[1], [[1, 1]])


    def test_mixed_inputs(self):
        self.assertEqual(trace(self.f3, x=np.array([[2, 2]]), y=4)[
                         0].tolist(), [[6, 6]])
        self.assertEqual(trace(self.f3, mode='reverse', x=np.array([[2, 2]]), y=4)[
                         0].tolist(), [[6, 6]])

        self.assertEqual(trace(self.f3, x=np.array([[2, 2]]), y=4)[
                         1], [[2., 2.], [0.25, 0.25]])
        self.assertEqual(trace(self.f3, mode='reverse', x=np.array([[2, 2]]), y=4)[
                         1], [[2., 2.], [0.25, 0.25]])


if __name__ == "__main__":
    unittest.main()
