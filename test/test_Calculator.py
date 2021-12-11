import sys
sys.path.append("./src/")
import numpy as np
import math
from undefined.GraphGenerator import UDGraph
from undefined.UDFunction import UDFunction
from undefined import Calculator as cal
from typing import Type
import unittest



class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.a = 2
        self.b = - 1.11
        self.c = 99999.99
        self.d = -99999.99
        self.e = np.array([[self.a, self.b]])
        self.f = np.array([[self.a, self.b, self.c, self.d]])
        self.g = math.pi / 2
        self.h = math.e
        self.j = np.array([[self.a, self.b, self.g, self.h]])
        self.s = "str"

        self.af = UDFunction(self.a)
        self.bf = UDFunction(self.b)
        self.cf = UDFunction(self.c)
        self.df = UDFunction(self.d)
        self.ef = UDFunction(self.e)
        self.ff = UDFunction(self.f)
        self.gf = UDFunction(self.g)
        self.hf = UDFunction(self.h)
        self.jf = UDFunction(self.j)

        self.ag = UDGraph(self.a)
        self.bg = UDGraph(self.b)
        self.cg = UDGraph(self.c)
        self.dg = UDGraph(self.d)
        self.eg = UDGraph(self.e)
        self.fg = UDGraph(self.f)
        self.gg = UDGraph(self.g)
        self.hg = UDGraph(self.h)
        self.jg = UDGraph(self.j)

        x = UDFunction(1.0)
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

    def assertListAlmostEqual(self, o1, o2):
        for i, o in enumerate(o1):
            if round(o, 2) != o2[i]:
                return False
        return True

    def test_cos(self):
        self.assertEqual(round(cal.cos(self.a), 2), - 0.42)
        self.assertEqual(round(cal.cos(self.b), 2), 0.44)
        self.assertEqual(round(cal.cos(self.c), 2), - 1.00)
        self.assertEqual(round(cal.cos(self.d), 2), - 1.00)

        self.assertListAlmostEqual(cal.cos(self.e)[0], [-0.42, 0.44])
        self.assertListAlmostEqual(cal.cos(self.f)[0], [-1.00, -1.00])

        self.assertEqual(round(cal.cos(self.g), 2), 0.00)
        self.assertEqual(round(cal.cos(self.h), 2), -0.91)
        self.assertListAlmostEqual(
            cal.cos(self.j)[0], [-0.42, 0.44, 0.00, -0.91])

        with self.assertRaises(TypeError):
            cal.cos(self.s)

        self.assertEqual(cal.cos(self.af).val, - 0.42)
        self.assertEqual(cal.cos(self.bf).val, 0.44)
        self.assertEqual(cal.cos(self.cf).val, - 1.00)
        self.assertEqual(cal.cos(self.df).val, - 1.00)

        self.assertListAlmostEqual(cal.cos(self.ef).val[0], [-0.42, 0.44])
        self.assertListAlmostEqual(cal.cos(self.ff).val[0], [-1.00, -1.00])

        self.assertEqual(cal.cos(self.gf).val, 0.00)
        self.assertEqual(cal.cos(self.hf).val, -0.91)
        self.assertListAlmostEqual(
            cal.cos(self.jf).val[0], [-0.42, 0.44, 0.00, -0.91])

        self.assertEqual(cal.cos(self.ag).val, - 0.42)
        self.assertEqual(cal.cos(self.bg).val, 0.44)
        self.assertEqual(cal.cos(self.cg).val, - 1.00)
        self.assertEqual(cal.cos(self.dg).val, - 1.00)

        self.assertListAlmostEqual(cal.cos(self.eg).val[0], [-0.42, 0.44])
        self.assertListAlmostEqual(cal.cos(self.fg).val[0], [-1.00, -1.00])

        self.assertEqual(cal.cos(self.gg).val, 0.00)
        self.assertEqual(cal.cos(self.hg).val, -0.91)
        self.assertListAlmostEqual(
            cal.cos(self.jg).val[0], [-0.42, 0.44, 0.00, -0.91])

    def test_sin(self):
        self.assertEqual(round(cal.sin(self.a), 2), 0.91)
        self.assertEqual(round(cal.sin(self.b), 2), - 0.90)
        self.assertEqual(round(cal.sin(self.c), 2), 0.05)
        self.assertEqual(round(cal.sin(self.d), 2), - 0.05)

        self.assertListAlmostEqual(cal.sin(self.e)[0], [0.91, - 0.90])
        self.assertListAlmostEqual(cal.sin(self.f)[0], [0.05, -0.05])
        self.assertEqual(round(cal.sin(self.g), 2), 1.00)
        self.assertEqual(round(cal.sin(self.h), 2), 0.41)
        self.assertListAlmostEqual(
            cal.sin(self.j)[0], [-0.42, 0.44, 1.00, 0.41])

        with self.assertRaises(TypeError):
            cal.sin(self.s)

        self.assertEqual(cal.sin(self.af).val, 0.91)
        self.assertEqual(cal.sin(self.bf).val, - 0.90)
        self.assertEqual(cal.sin(self.cf).val, 0.05)
        self.assertEqual(cal.sin(self.df).val, - 0.05)

        self.assertListAlmostEqual(cal.sin(self.ef).val[0], [0.91, - 0.90])
        self.assertListAlmostEqual(cal.sin(self.ff).val[0], [0.05, -0.05])
        self.assertEqual(cal.sin(self.gf).val, 1.00)
        self.assertEqual(cal.sin(self.hf).val, 0.41)
        self.assertListAlmostEqual(
            cal.sin(self.jf).val[0], [-0.42, 0.44, 1.00, 0.41])

        self.assertEqual(cal.sin(self.ag).val, 0.91)
        self.assertEqual(cal.sin(self.bg).val, - 0.90)
        self.assertEqual(cal.sin(self.cg).val, 0.05)
        self.assertEqual(cal.sin(self.dg).val, - 0.05)

        self.assertListAlmostEqual(cal.sin(self.eg).val[0], [0.91, - 0.90])
        self.assertListAlmostEqual(cal.sin(self.fg).val[0], [0.05, -0.05])
        self.assertEqual(cal.sin(self.gg).val, 1.00)
        self.assertEqual(cal.sin(self.hg).val, 0.41)
        self.assertListAlmostEqual(
            cal.sin(self.jg).val[0], [-0.42, 0.44, 1.00, 0.41])

    def test_sqrt(self):
        self.assertEqual(round(cal.sqrt(self.a), 2), 1.41)
        with self.assertRaises(ValueError):
            cal.sqrt(self.b)
        with self.assertRaises(ValueError):
            cal.sqrt(self.e)
        with self.assertRaises(ValueError):
            cal.sqrt(self.f)

        with self.assertRaises(TypeError):
            cal.sqrt(self.s)
        self.assertEqual(round(cal.sqrt(self.g), 2), 1.25)

        self.assertEqual(cal.sqrt(self.af).val,  1.41)
        with self.assertRaises(ValueError):
            cal.sqrt(self.bf)

        with self.assertRaises(ValueError):
            cal.sqrt(self.ef)
        with self.assertRaises(ValueError):
            cal.sqrt(self.ff)
        self.assertEqual(cal.sqrt(self.ag).val,  1.41)
        with self.assertRaises(ValueError):
            cal.sqrt(self.bg)
        with self.assertRaises(ValueError):
            cal.sqrt(self.eg)
        with self.assertRaises(ValueError):
            cal.sqrt(self.fg)

    def test_tan(self):
        self.assertEqual(round(cal.tan(self.a), 2), -2.19)
        self.assertEqual(round(cal.tan(self.b), 2), - 2.01)
        self.assertEqual(round(cal.tan(self.c), 2), - 0.05)
        self.assertEqual(round(cal.tan(self.d), 2), 0.05)

        self.assertListAlmostEqual(cal.tan(self.e)[0], [-2.19, - 2.01])
        self.assertListAlmostEqual(cal.tan(self.f)[0], [- 0.05, 0.05])
        with self.assertRaises(TypeError):
            cal.tan(self.s)
        with self.assertRaises(ZeroDivisionError):
            cal.tan(self.g)
        self.assertEqual(round(cal.tan(self.h), 2), -0.45)
        with self.assertRaises(ZeroDivisionError):
            cal.tan(self.j)

        self.assertEqual(cal.tan(self.af).val,  -2.19)
        self.assertEqual(cal.tan(self.bf).val, - 2.01)
        self.assertEqual(cal.tan(self.cf).val, - 0.05)
        self.assertEqual(cal.tan(self.df).val, 0.05)

        self.assertListAlmostEqual(cal.tan(self.ef).val[0], [-2.19, - 2.01])
        self.assertListAlmostEqual(cal.tan(self.ff).val[0], [- 0.05, 0.05])
        with self.assertRaises(ZeroDivisionError):
            cal.tan(self.gf)
        self.assertEqual(cal.tan(self.hf).val, -0.45)
        with self.assertRaises(ZeroDivisionError):
            cal.tan(self.jf)

        self.assertEqual(cal.tan(self.ag).val,  -2.19)
        self.assertEqual(cal.tan(self.bg).val, - 2.01)
        self.assertEqual(cal.tan(self.cg).val, - 0.05)
        self.assertEqual(cal.tan(self.dg).val, 0.05)

        self.assertListAlmostEqual(cal.tan(self.eg).val[0], [-2.19, - 2.01])
        self.assertListAlmostEqual(cal.tan(self.fg).val[0], [- 0.05, 0.05])
        with self.assertRaises(ZeroDivisionError):
            cal.tan(self.gg)
        self.assertEqual(cal.tan(self.hg).val, -0.45)
        with self.assertRaises(ZeroDivisionError):
            cal.tan(self.jg)

    def test_log(self):
        self.assertEqual(round(cal.log(self.a), 2), 0.69)
        self.assertEqual(round(cal.log(self.a, 10), 2), 0.30)
        with self.assertRaises(ValueError):
            cal.log(self.b)
        with self.assertRaises(ValueError):
            cal.log(self.e)
        with self.assertRaises(ValueError):
            cal.log(self.f)

        with self.assertRaises(TypeError):
            cal.log(self.s)
        self.assertEqual(round(cal.log(self.g), 2), 0.45)
        self.assertEqual(cal.log(self.af).val,  0.69)
        self.assertEqual(cal.log(self.af, 10).val,  0.30)
        with self.assertRaises(ValueError):
            cal.log(self.bf)

        with self.assertRaises(ValueError):
            cal.log(self.ef)
        with self.assertRaises(ValueError):
            cal.log(self.ff)
        self.assertEqual(cal.log(self.ag).val,  0.69)
        self.assertEqual(cal.log(self.ag, 10).val,  0.30)
        with self.assertRaises(ValueError):
            cal.log(self.bg)
        with self.assertRaises(ValueError):
            cal.log(self.eg)
        with self.assertRaises(ValueError):
            cal.log(self.fg)
        with self.assertRaises(ValueError):
            cal.log(self.fg, -1)

    def test_sine_integration(self):

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

        # need to check the calculation
        self.assertEqual(np.round(self.f252.val), np.array([1.]))

        with self.assertRaises(TypeError):
            cal.sin(UDGraph("3/np.pi"))

    def test_cosine_integration(self):
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

        # UDgraph input

        self.f250 = cal.cos(UDGraph(2))
        self.f251 = cal.cos(UDGraph(np.array([2])))
        self.assertEqual(round(self.f250.val, 2), -0.42)
        self.assertEqual(self.f251.val, np.array([-0.42]))

        with self.assertRaises(TypeError):
            self.f0001 = cal.cos(UDGraph(a))

    def test_tangent_integration(self):

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

        # UDgraph input

        self.f250 = cal.tan(UDGraph(2))
        self.f251 = cal.tan(UDGraph(np.array([2])))
        self.assertEqual(round(self.f250.val, 2), -2.19)
        self.assertEqual(self.f251.val, np.array([-2.19]))

        with self.assertRaises(TypeError):
            self.f0001 = cal.tan(UDGraph(a))

    def test_sqrt_integration(self):
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

    def test_exp_integration(self):

        a = "2.0"
        x = UDFunction(a)
        x1 = UDFunction(1)
        y = UDGraph(np.array([1]))
        f_logist = cal.standard_logistic(x1)

        self.assertEqual(f_logist.val, 0.73)
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

    def test_log_integration(self):
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

    def test_hs_integration(self):
        a = 1
        x = UDFunction(a)

        self.f255 = cal.sinh(x)

        self.assertEqual(self.f255.val, 1.18)

        self.f255 = cal.cosh(x)

        self.assertEqual(self.f255.val, 1.54)

        self.f255 = cal.tanh(x)

        self.assertEqual(self.f255.val, 0.76)

        self.f255 = cal.coth(x)

        self.assertEqual(self.f255.val, 1.31)

        self.f255 = cal.sech(x)

        self.assertEqual(self.f255.val, 0.65)

        self.f255 = cal.csch(x)

        self.assertEqual(self.f255.val, 0.85)

        # test logistic

        self.f255 = cal.standard_logistic(x)

        self.assertEqual(round(self.f255.val, 2), 0.73)

    def test_arc(self):

        a = 0.5
        x = UDFunction(a)
        b = "0.5"
        y = UDFunction(b)
        # test arccos
        c = 99
        d = -99
        e = -1
        z1 = UDFunction(c)
        z2 = UDFunction(np.array([[a, c, d]]))
        z3 = UDGraph(c)
        z4 = UDGraph(np.array([[a, c, e]]))
        self.assertEqual(round(cal.arccos(x), 2), 1.05)
        self.assertEqual(round(cal.arccos(0.5), 2), 1.05)
        self.assertEqual(
            np.round(cal.arccos(UDFunction(np.array([0.5]))).val), 1)
        self.assertEqual(np.round(cal.arccos(np.array([0.5]))), 1)

        with self.assertRaises(TypeError):
            cal.arccos(y)
        with self.assertRaises(ValueError):
            cal.arccos(c)
        with self.assertRaises(ValueError):
            cal.arccos(z1)
        with self.assertRaises(ValueError):
            cal.arccos(z2)
        with self.assertRaises(ValueError):
            cal.arccos(z4)
        with self.assertRaises(ValueError):
            cal.arcsin(c)
        with self.assertRaises(ValueError):
            cal.arcsin(z1)
        with self.assertRaises(ValueError):
            cal.arcsin(z2)
        with self.assertRaises(ValueError):
            cal.arcsin(z3)
        with self.assertRaises(ValueError):
            cal.arcsin(z4)
        with self.assertRaises(TypeError):
            self.f000 = cal.arccos("3/np.pi")

        # UDgraph
        self.f256 = cal.arccos(UDGraph(0.5))
        self.f252 = cal.arccos(UDGraph(np.array([0.5])))

        # need to check the calculation
        self.assertEqual(round(self.f256.val), np.array([1.]))
        self.assertEqual(np.round(self.f252.val), np.array([1.]))

        with self.assertRaises(TypeError):
            cal.arccos(UDGraph("3/np.pi"))

        # test arcsin

        self.assertEqual(round(cal.arcsin(x), 2), 0.52)
        self.assertEqual(round(cal.arcsin(0.5), 2), 0.52)
        self.assertEqual(
            np.round(cal.arcsin(UDFunction(np.array([0.5]))).val), 1)
        self.assertEqual(np.round(cal.arcsin(np.array([0.5]))), 1)

        with self.assertRaises(TypeError):
            cal.arcsin(y)

        with self.assertRaises(TypeError):
            self.f000 = cal.arcsin("3/np.pi")

        # UDgraph
        self.f256 = cal.arcsin(UDGraph(0.5))
        self.f252 = cal.arcsin(UDGraph(np.array([0.5])))

        # need to check the calculation
        self.assertEqual(round(self.f256.val), np.array([1.]))
        self.assertEqual(np.round(self.f252.val), np.array([1.]))

        with self.assertRaises(TypeError):
            cal.arcsin(UDGraph("3/np.pi"))

        # test arctan

        self.assertEqual(round(cal.arctan(x), 2), 0.46)
        self.assertEqual(round(cal.arctan(0.5), 2), 0.46)
        self.assertEqual(np.round(cal.arctan(UDFunction(
            np.array([0.5]))).val, 2), np.array([0.46]))
        self.assertEqual(
            np.round(cal.arctan(np.array([0.5])), 2), np.array([0.46]))

        with self.assertRaises(TypeError):
            cal.arctan(y)

        with self.assertRaises(TypeError):
            self.f000 = cal.arctan("3/np.pi")

        # UDgraph
        self.f256 = cal.arctan(UDGraph(0.5))
        self.f252 = cal.arctan(UDGraph(np.array([0.5])))

        # need to check the calculation
        self.assertEqual(round(self.f256.val, 2), 0.46)
        self.assertEqual(np.round(self.f252.val, 2), 0.46)

        with self.assertRaises(TypeError):
            cal.arctan(UDGraph("3/np.pi"))


if __name__ == "__main__":
    unittest.main()
