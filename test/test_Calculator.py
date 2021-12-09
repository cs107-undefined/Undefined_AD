import unittest
import sys
# import undefined
sys.path.append("./src/")
from undefined import Calculator as cal
from undefined.UDFunction import UDFunction
from undefined.GraphGenerator import UDGraph
import math
import numpy as np


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

        # UDgraph
        self.f252 = cal.sin(UDGraph(np.array([np.pi/2])))

        ## need to check the calculation
        self.assertEqual(np.round(self.f252.val),np.array([1.]))

        with self.assertRaises(TypeError):
            cal.sin(UDGraph("3/np.pi"))

    
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

        ### UDgraph input

        self.f250 = cal.cos(UDGraph(2))
        self.f251 = cal.cos(UDGraph(np.array([2])))
        self.assertEqual(round(self.f250.val, 2), -0.42)
        self.assertEqual(self.f251.val, np.array([-0.42]))

        with self.assertRaises(TypeError):
            self.f0001 = cal.cos(UDGraph(a))

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

        ### UDgraph input

        self.f250 = cal.tan(UDGraph(2))
        self.f251 = cal.tan(UDGraph(np.array([2])))
        self.assertEqual(round(self.f250.val, 2), -2.19)
        self.assertEqual(self.f251.val, np.array([-2.19]))

        with self.assertRaises(TypeError):
            self.f0001 = cal.tan(UDGraph(a))

    
    def test_sqrt(self):
        a = "2.0"
        x = UDFunction(a)
        y = UDFunction(UDGraph("abc"))

        self.assertEqual(round(self.f7.val, 2), 1)
        self.assertEqual(round(self.f7.der, 2), 0.5)

        self.assertEqual(round(self.f8.val, 2), 3.41)
        self.assertEqual(round(self.f8.der, 2), 2.71)

        with self.assertRaises(TypeError):
            self.f48 = cal.sqrt(2*x) + x


        with self.assertRaises(TypeError):
            cal.sqrt(2*x) + x
        
        with self.assertRaises(TypeError):
            cal.sqrt(y)


        self.assertEqual(cal.sqrt(np.array([4])), 2)
        self.assertEqual(cal.sqrt(4), 2)

        with self.assertRaises(TypeError):
            self.f000 = cal.sqrt("3/np.pi")

    def test_exp(self):

        a = "2.0"
        x = UDFunction(a)
        y = UDGraph(np.array([1]))

        self.assertEqual(round(self.f9.val, 2), 2.72)
        self.assertEqual(round(self.f9.der, 2), 2.72)

        self.assertEqual(round(self.f10.val, 2), 0.28)
        self.assertEqual(round(self.f10.der, 2), -0.72)

        self.assertEqual(np.round(cal.exp(y).val, 2), 2.72)

        with self.assertRaises(TypeError):
            cal.exp(UDGraph("str"))

        with self.assertRaises(TypeError):
            self.f49 = cal.exp(2*x) + x 
        
        self.assertEqual(cal.exp(np.array([1])), np.e)
        self.assertEqual(cal.exp(1), np.e)

        with self.assertRaises(TypeError):
            self.f000 = cal.exp("3/np.pi")

    def test_log(self):
        a = "2.0"
        x = UDFunction(a)
        y = UDGraph(1)
        z = UDGraph(np.array([1]))
        b = UDGraph("a")

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

        self.assertEqual(np.round(cal.log(y).val, 2), 0.0)
        self.assertEqual(np.round(cal.log(z).val, 2), np.array([0.]))

        with self.assertRaises(TypeError):
            self.f000 = cal.log(b)



    def test_hs(self):
        a = 1
        x = UDFunction(a)

        self.f255 = cal.sinh(x)

        self.assertEqual(self.f255.val,1.18)

        self.f255 = cal.cosh(x)

        self.assertEqual(self.f255.val,1.54)

        self.f255 = cal.tanh(x)

        self.assertEqual(self.f255.val,0.76)

        self.f255 = cal.coth(x)

        self.assertEqual(self.f255.val,1.31)

        self.f255 = cal.sech(x)

        self.assertEqual(self.f255.val,0.65)

        self.f255 = cal.csch(x)

        self.assertEqual(self.f255.val,0.85)

        # test logistic 

        self.f255 = cal.standard_logistic(x)

        self.assertEqual(round(self.f255.val,2),0.73)





    def test_arc(self):

        a = 0.5
        x = UDFunction(a)
        b = "0.5"
        y = UDFunction(b)


        
        # test arccos




        self.assertEqual(round(cal.arccos(x),2), 1.05)
        self.assertEqual(round(cal.arccos(0.5),2), 1.05)
        self.assertEqual(np.round(cal.arccos(UDFunction(np.array([0.5]))).val), 1)
        self.assertEqual(np.round(cal.arccos(np.array([0.5]))), 1)

        with self.assertRaises(TypeError):
            cal.arccos(y)


        with self.assertRaises(TypeError):
            self.f000 = cal.arccos("3/np.pi")

        # UDgraph
        self.f256 = cal.arccos(UDGraph(0.5))
        self.f252 = cal.arccos(UDGraph(np.array([0.5])))

        ## need to check the calculation
        self.assertEqual(round(self.f256.val),np.array([1.]))
        self.assertEqual(np.round(self.f252.val),np.array([1.]))

        with self.assertRaises(TypeError):
            cal.arccos(UDGraph("3/np.pi"))


        # test arcsin


        self.assertEqual(round(cal.arcsin(x),2), 0.52)
        self.assertEqual(round(cal.arcsin(0.5),2), 0.52)
        self.assertEqual(np.round(cal.arcsin(UDFunction(np.array([0.5]))).val), 1)
        self.assertEqual(np.round(cal.arcsin(np.array([0.5]))), 1)

        with self.assertRaises(TypeError):
            cal.arcsin(y)


        with self.assertRaises(TypeError):
            self.f000 = cal.arcsin("3/np.pi")

        # UDgraph
        self.f256 = cal.arcsin(UDGraph(0.5))
        self.f252 = cal.arcsin(UDGraph(np.array([0.5])))

        ## need to check the calculation
        self.assertEqual(round(self.f256.val),np.array([1.]))
        self.assertEqual(np.round(self.f252.val),np.array([1.]))

        with self.assertRaises(TypeError):
            cal.arcsin(UDGraph("3/np.pi"))   

        # test arctan

        self.assertEqual(round(cal.arctan(x),2), 0.46)
        self.assertEqual(round(cal.arctan(0.5),2), 0.46)
        self.assertEqual(np.round(cal.arctan(UDFunction(np.array([0.5]))).val,2), np.array([0.46]))
        self.assertEqual(np.round(cal.arctan(np.array([0.5])),2), np.array([0.46]))

        with self.assertRaises(TypeError):
            cal.arctan(y)


        with self.assertRaises(TypeError):
            self.f000 = cal.arctan("3/np.pi")

        # UDgraph
        self.f256 = cal.arctan(UDGraph(0.5))
        self.f252 = cal.arctan(UDGraph(np.array([0.5])))

        ## need to check the calculation
        self.assertEqual(round(self.f256.val,2),0.46)
        self.assertEqual(np.round(self.f252.val,2),0.46)

        with self.assertRaises(TypeError):
            cal.arctan(UDGraph("3/np.pi")) 


if __name__ == "__main__":
    unittest.main()