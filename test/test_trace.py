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
        self.f8 = lambda x: log(x*3 + tan(2*x), np.e) + 2**x # raise error, need to fix __rpow__
        self.f10 = lambda x: log(x*3, np.e)
        self.f9 = lambda x, y: x**y
        self.f11 = lambda x: cos(exp(2*x))
        self.f12 = lambda x, y: log(1 + 6*x) * tan(4*x + 2*y)
        self.f13 = lambda x: log(6*x, 10) * tan(4*x)
        self.f1000 = lambda x, y: exp(1-6*x) * tan(4*x + 2*y) + x**2*y
    
    def assertNumpyArraysEqual(self, o1, o2):
        if o1.shape != o2.shape:
            raise AssertionError("Shapes don't match")
        if not np.allclose(o1, o2):
            raise AssertionError("Elements don't match!")

    def tearDown(self):
        pass

    def test_forward(self):
        # Please do not use string for testing any more!!!!
        result1 = trace(self.f1, x = 2)
        self.assertEqual(result1, (1.58, -0.328))
        self.assertEqual(trace(self.f2, x = 3), (9331.210, 46749.434))
        self.assertEqual(trace(self.f3, x = 3), (0.40, -15137.189))
        self.assertEqual(trace(self.f4, x = 3), (0.35, -0.003))
    
        self.assertEqual(trace(self.f5, x = 2, y = 3), (0.0, [[0.003], [0.002]]))
        self.assertEqual(trace(self.f7, x = 1, y = 2, z = 3), (0.01, [ [0.007],  [0.027], [-0.04] ]))

        self.assertEqual(trace(self.f8, x = 3), (10.16, 6.139))
        self.assertEqual(trace(self.f10, x = 2), (1.79, 0.5))
        self.assertEqual(trace(self.f9, x = 5, y = 3), (125, [[75.  ], [201.18]]))

        def f22(x):
            return x+cos(2*x)
        with self.assertRaises(TypeError):
            trace(f22(2), x = 2)
        f300 = lambda x: 2*x + sqrt(x)
        # print(trace([self.f1, f300], x = np.array([[1, 2]])))

    
    def test_forward_trace(self):
        result1 = trace(self.f1, x = np.array([[2]]))
        self.assertEqual(result1, (np.array([[1.58]]), np.array([[-0.328]])))
        self.assertEqual(trace(self.f2, x = np.array([[3]])), (np.array([[9331.21]]), np.array([[46749.434]])))
        self.assertEqual(trace(self.f8, x = np.array([[3]])), (np.array([[10.16]]), np.array([[6.139]]))) # raise error
        self.assertEqual(trace(self.f11, x = np.array([[2]])), (np.array([[-0.37]]), np.array([[101.418]])))
        # print(trace(self.f12, x = np.array([[2]]), y = np.array([[5]]))) # raise error
        self.assertEqual(trace(self.f13, x = np.array([[3]])), (np.array([[-0.8]]), np.array([[6.959]])))
        self.assertEqual(trace(self.f13, x = np.array([[3]])), (np.array([[-0.8]]), np.array([[6.959]])))
        with self.assertRaises(TypeError):
            trace(self.f1, x=np.array([]))
        
        # test multiple x values at the same time

        self.assertNumpyArraysEqual(trace(self.f1, x = np.array([[1, 2]]))[0], np.array([[1.52, 1.58]]))
        
        self.assertEqual(trace(self.f1, x = np.array([[1, 2]]))[1], [[ 0.411, -0.328]])

        with self.assertRaises(TypeError):
            trace(self.f1, x="2")
        
        self.assertNumpyArraysEqual(trace([self.f1, self.f2], x = 2)[0], np.array([1.58, 135.54]))
        self.assertNumpyArraysEqual(trace([self.f1, self.f2], x = 2)[1], np.array([-3.2800e-01,  4.8577e+02]))


    def test_reverse(self):
        result1 = trace(self.f1, mode = "reverse", x = 2)

        self.assertEqual(result1, (1.58, [-0.328]))

        result2 = trace(self.f2,mode = "reverse", x = 2)
        self.assertEqual(result2,(135.54, [485.77]))

        self.function_ =  lambda x: x+1

        result3 = trace(self.function_,mode = "reverse", x = 2)
        self.assertEqual(result3,(3, [1]))


        self.function_2 = lambda x:3*x - 1
        result4 = trace(self.function_2,mode = "reverse", x = 2)
        self.assertEqual(result4,(5, [3]))


        self.function_3 = lambda x:1 - x*3
        result5 = trace(self.function_3,mode = "reverse",x = 2)
        self.assertEqual(result5,(-5, [-3]))

        self.function_4 =  lambda x: 1 + x

        result6 = trace(self.function_4,mode = "reverse", x = 2)
        self.assertEqual(result6,(3, [1]))



        result7 = trace(self.f5,mode = "reverse",x = 2 , y = 1)
        self.assertEqual(result6,(3, [1]))

        result8 = trace(self.f6,mode = "reverse",x = 2)
        self.assertEqual(result8,(0.11, [-0.0]))

        result9 = trace(self.f7,mode = "reverse",x = 2 ,y = 1, z = 3)
        self.assertEqual(result6,(3, [1]))


        # result10 = trace(self.f8,mode = "reverse",x = 2)
        # self.assertEqual(result10,(3, [1]))

        # result11 = trace(self.f9,mode = "reverse",x = 2,y =1)
        # self.assertEqual(result11,(3, [1]))

        result12 = trace(self.f10,mode = "reverse",x = 2)
        self.assertEqual(result12,(1.79, [0.5]))

        result13 = trace(self.f11,mode = "reverse",x = 2)
        self.assertEqual(result13,(-0.37, [101.418]))

        result14 = trace(self.f12,mode = "reverse",x = 2, y = 1)
        self.assertEqual(result14,(1.66, [[14.872], [7.286]]))

        result15 = trace(self.f13,mode = "reverse",x = 2)
        self.assertEqual(result15,(-7.34, [[202.429]]))  

        self.f100 = lambda x: 1+x**2
        result16 = trace(self.f100,mode = "reverse",x = 2)
        self.assertEqual(result16,(5, [4]))

        self. f101 = lambda x,y: x*y
        result17 = trace(self.f101,mode = "reverse",x = 2,y =  1)
        self.assertEqual(result17,(2, [[1], [2]]))

        self.f102  =  lambda x,y:-x*y
        result18  =  trace(self.f102,mode = "reverse",x = 2,y = 1)
        self.assertEqual(result18,(-2, [[-1], [-2]]))

        self.f103 =  lambda x: - x + 1
        result19 =  trace(self.f103,mode = "reverse",x = 2)
        self.assertEqual(result19,(-1, [-1]))

    def test_multiple_function(self):
        f1 = lambda x: sqrt(exp(sin(x)))
        f2 = lambda x: 2*x + sqrt(x)

        self.assertEqual(trace([f1, f2], x = np.array([[1, 2]]))[1].tolist(), [[[0.411, -0.328]], [[ 2.5  ,  2.354]]])
        self.assertEqual(trace([f1, f2], x = np.array([[1, 2, 3]]))[0].tolist(), [[[1.52, 1.58, 1.07]], [[3.  , 5.41, 7.73]]])
        self.assertEqual(trace([f1, f2], x = np.array([[1, 2, 3]]))[1].tolist(), [[[ 0.411, -0.328, -0.531]], [[ 2.5  ,  2.354,  2.289]]])

    def test_multiple_variable_function(self):
        
        f3 = lambda x, y: x**2 + 2**y
        f4 = lambda x, y: 2*x - 2/y

        # print(trace([f3, f4], mode = "reverse", x = np.array([[1,2]]), y = 4))
        self.assertEqual(trace([f3, f4], x = np.array([[1,2]]), y = 4)[0].tolist(), [[[17. , 20. ]], [[ 1.5,  3.5]]])
        self.assertEqual(trace([f3, f4], x = np.array([[1,2]]), y = 4)[1].tolist(), [[[ 2.   ,  4.   ], [11.09 , 11.09 ]],[[ 2.   ,  2.   ],[ 0.125,  0.125]]])

        self.assertEqual(trace([f3, f4], mode = "reverse", x = np.array([[1,2]]), y = 4)[0].tolist(), [[[17. , 20. ]], [[ 1.5,  3.5]]])
        self.assertEqual(trace([f3, f4], mode = "reverse", x = np.array([[1,2]]), y = 4)[1].tolist(), [[[ 2.   ,  4.   ], [11.09 , 11.09 ]],[[ 2.   ,  2.   ],[ 0.125,  0.125]]])

        self.assertEqual(trace([f3, f4], x = 4 , y = np.array([[1,2]]))[0].tolist(), [[[18., 20.]], [[ 6.,  7.]]])
        self.assertEqual(trace([f3, f4], x = 4 , y = np.array([[1,2]]))[1].tolist(), [[[8.   , 8.   ], [1.386, 2.773]], [[2.   , 2.   ], [2.   , 0.5  ]]])

        self.assertEqual(trace([f3, f4], mode = "reverse", x = 4 , y = np.array([[1,2]]))[0].tolist(), [[[18., 20.]], [[ 6.,  7.]]])
        self.assertEqual(trace([f3, f4], mode = "reverse", x = 4 , y = np.array([[1,2]]))[1].tolist(), [[[8.   , 8.   ], [1.386, 2.773]], [[2.   , 2.   ], [2.   , 0.5  ]]])

if __name__ == "__main__":
    unittest.main()
