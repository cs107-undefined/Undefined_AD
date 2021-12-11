import sys
# # temp solution for directory.
sys.path.append("./src/")
import matplotlib.pyplot as plt
import networkx as nx
import math
import numpy as np
from undefined.Utils import UDPrimitive, time, check_division_by_zero, check_pow


class UDGraph:
    def __init__(self, val, func=UDPrimitive.VAR, varname="intermediate"):
        # TODO
        """
        This class is where we overload all the operators, which will be used to calculate the derivatives.

        Args:
            val (numeric or numpy ndarray): value of function
            der (int, optional): derivative of function. Defaults to 1.
        """
        self._val = val
        self._func = func
        self._varname = varname
        if hasattr(self._val, 'shape'):
            self._valshape = self._val.shape
        else:
            self._valshape = 1
        self._parents = []
        self._params = {}

    @property
    def val(self):
        # TODO
        """
        This is a decorator return rouded input self.val

        Returns:
            array: 4 decimal rounded input of self.value
        """
        if isinstance(self._val, float):
            return round(self._val, 2)
        elif isinstance(self._val, np.ndarray):
            return np.round(self._val, 2)
        else:
            return self._val

    def __str__(self):
        """return the results in format. 
        Used in building the computational graph in the reverse mode.

        Returns:
            formatted string with the value.
        """
        return f"{self._func}\n".replace("UDPrimitive.", "") + f"Value:{self.val}\n"

    def __repr__(self):
        """return the computational graph root.

        Returns:
            formatted string with the value for the computational graph root. 
        """
        res = f'Computational Graph ({self.val}, {self._func})'
        for parent in self._parents:
            res += '\n|\n|<-(parent)-' + \
                '\n|      '.join(repr(parent).split('\n'))
        return res

    def __add__(self, other):
        """
        This allows to do addition with UDFunction instances or scalar numbers, and calculate the value after taking the derivative. 
        TypeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to add with
        Returns:
            UDFunction: a new object with new_val and new_der
        """

        if isinstance(other, UDGraph):
            new_val = self._val + other._val
            new_func = UDPrimitive.ADD
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._parents.append(other)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val + other
            new_func = UDPrimitive.ADD
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __mul__(self, other):
        """
        This allows to do multification with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        TypeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to multiply with
        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDGraph):
            new_val = self._val * other._val
            new_func = UDPrimitive.MUL
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._parents.append(other)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val * other
            new_func = UDPrimitive.MUL
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __radd__(self, other):
        """
        This is called when int/float or UDFunction instances + an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to add with
        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDGraph):
            new_val = self._val + other._val
            new_func = UDPrimitive.RADD
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(other)
            udgraph._parents.append(self)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val + other
            new_func = UDPrimitive.RADD
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __rmul__(self, other):
        """
        This is called when int/float or UDFunction instances * an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to multiply with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDGraph):
            new_val = self._val * other._val
            new_func = UDPrimitive.RMUL
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(other)
            udgraph._parents.append(self)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val * other
            new_func = UDPrimitive.RMUL
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __neg__(self):
        """
        This allows to negate UDFunction instances itself.

        Returns:
            UDFunction: object with neg value
        """
        return -1 * self

    def __sub__(self, other):
        """
        This allows to do subtraction with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        TypeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to subtract with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDGraph):
            new_val = self._val - other._val
            new_func = UDPrimitive.SUB
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._parents.append(other)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val - other
            new_func = UDPrimitive.SUB
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __rsub__(self, other):
        """
        This is called when int/float or UDFunction instances - an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to subtract with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDGraph):
            new_val = other._val - self._val
            new_func = UDPrimitive.RSUB
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(other)
            udgraph._parents.append(self)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other - self._val
            new_func = UDPrimitive.RSUB
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __truediv__(self, other):
        """
        This allows to do true division with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        TypeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to (true) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDGraph):
            check_division_by_zero(other._val)
            new_val = self._val / other._val
            new_func = UDPrimitive.TRUEDIV
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._parents.append(other)
        elif isinstance(other, (int, float, np.ndarray)):
            check_division_by_zero(other)
            new_val = self._val / other
            new_func = UDPrimitive.TRUEDIV
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __rtruediv__(self, other):
        """
        This is called when int/float or UDFunction instances / (divide) an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to (true) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        check_division_by_zero(self._val)
        if isinstance(other, UDGraph):
            new_val = other._val / self._val
            new_func = UDPrimitive.RTRUEDIV
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(other)
            udgraph._parents.append(self)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other / self._val
            new_func = UDPrimitive.RTRUEDIV
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __floordiv__(self, other):  # self // other
        """
        This allows to do floor division with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative.
        TypeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to (floor) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDGraph):
            check_division_by_zero(other._val)
            new_val = self._val // other._val
            new_func = UDPrimitive.FLOORDIV
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._parents.append(other)
        elif isinstance(other, (int, float, np.ndarray)):
            check_division_by_zero(other)
            new_val = self._val // other
            new_func = UDPrimitive.FLOORDIV
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __rfloordiv__(self, other):
        """
        This is called when int/float or UDFunction instances // (floor divide) an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to (floor) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        check_division_by_zero(self._val)
        if isinstance(other, UDGraph):
            new_val = other._val // self._val
            new_func = UDPrimitive.RFLOORDIV
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(other)
            udgraph._parents.append(self)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other // self._val
            new_func = UDPrimitive.RFLOORDIV
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["constant"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __pow__(self, other):
        """
        This allows to do "to the power" with UDFunction instances or scalar numbers, and calculate the value after taking the derivative.
        ** operator.

        Args:
            degree (numeric): object to take power of.

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        new_func = UDPrimitive.POW
        if isinstance(other, UDGraph):
            check_pow(self._val, other._val)
            if isinstance(self._val, (int, float)):
                new_val = self._val ** other._val
            else:
                if isinstance(other._val, np.ndarray):
                    if other._val.shape[0] != self._val.shape[0]:
                        raise ValueError(
                            f"error raised by undefined: operands could not be broadcast together with shapes {other._val.shape} {self._val.shape}")
                    else:
                        new_val = self._val ** other._val
                else:
                    new_val = self._val ** other._val
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._parents.append(other)
        elif isinstance(other, (int, float, np.ndarray)):
            check_pow(self._val, other)
            if isinstance(self._val, np.ndarray):
                new_val = np.power(self._val, other)
            elif isinstance(self._val, (int, float)):
                new_val = self._val ** other
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["degree"] = other
        return udgraph

    def __rpow__(self, other):
        """
        This allows to do "to the power" with UDFunction instances or scalar numbers, and calculate the value after taking the derivative.
        ** operator.
        TypeError will raise if none of the self or other are UDFunction instances. 

        Args:
            degree (numeric): object to take power of.

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        new_func = UDPrimitive.RPOW
        if isinstance(other, UDGraph):
            check_pow(other._val, self._val)
            if isinstance(other._val, (int, float)):
                new_val = other._val ** self._val
            else:
                if isinstance(self._val, np.ndarray):
                    if other._val.shape[0] != self._val.shape[0]:
                        raise ValueError(
                            f"error raised by undefined: operands could not be broadcast together with shapes {other._val.shape} {self._val.shape}")
                    else:
                        new_val = other._val ** self._val
                else:
                    new_val = other._val ** self._val
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(other)
            udgraph._parents.append(self)
        elif isinstance(other, (int, float, np.ndarray)):
            check_pow(other, self._val)
            new_val = other ** self._val
            udgraph = UDGraph(new_val, new_func)
            udgraph._parents.append(self)
            udgraph._params["base"] = other
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")
        return udgraph

    def __eq__(self, other):
        """compare whether the two UDGraph objects have the same values.
        Return true if equal, and false otherwise.

        raise TypeError is other is not a UDGraph object.

        Args:
            other ([UDGraph])

        Returns:
            True if equal. Otherwise False
        """
        if isinstance(other, UDGraph):
            return self.val == other.val
        elif isinstance(other, (int, float)):
            return self.val == other
        else:
            raise TypeError(
                "error raised by undefined: Need a UDGraph object to compare")

    def __ne__(self, other):
        """compare whether the two UDGraph objects have different values.
        raise TypeError is other is not a UDGraph object.

        Args:
            other ([UDGraph])

        Returns:
            True if not equal. Otherwise False
        """
        if isinstance(other, UDGraph):
            return self.val != other.val
        elif isinstance(other, (int, float)):
            return self.val != other
        else:
            raise TypeError(
                "error raised by undefined: Need a UDGraph object to compare")

    def __lt__(self, other):
        """overload the < operator
        raise TypeError is other is not a UDGraph object.

        Args:
            other ([UDGraph])

        Returns:
            True if less than. Otherwise False            
        """
        if isinstance(other, UDGraph):
            return self.val < other.val
        elif isinstance(other, (int, float)):
            return self.val < other
        else:
            raise TypeError(
                "error raised by undefined: Need a UDGraph object to compare")

    def __gt__(self, other):
        """overload the > operator
        raise TypeError is other is not a UDGraph object.

        Args:
            other ([UDGraph])

        Returns:
            True if greater than. Otherwise False
        """
        if isinstance(other, UDGraph):
            return self.val > other.val
        elif isinstance(other, (int, float)):
            return self.val > other
        else:
            raise TypeError(
                "error raised by undefined: Need a UDGraph object to compare")

    def __le__(self, other):
        """overload the > operator
        raise TypeError is other is not a UDGraph object.

        Args:
            other ([UDGraph])

        Returns:
            True if less than or equal to. Otherwise False
        """
        if isinstance(other, UDGraph):
            return self.val <= other.val
        elif isinstance(other, (int, float)):
            return self.val <= other
        else:
            raise TypeError(
                "error raised by undefined: Need a UDGraph object to compare")

    def __ge__(self, other):
        """overload the > operator
        raise TypeError is other is not a UDGraph object.

        Args:
            other ([UDGraph])

        Returns:
            True if greater than or equal to. Otherwise False
        """
        if isinstance(other, UDGraph):
            return self.val >= other.val
        elif isinstance(other, (int, float)):
            return self.val >= other
        else:
            raise TypeError(
                "error raised by undefined: Need a UDGraph object to compare")

    def __hash__(self):
        """hash function for udgraph

        Returns:
            int: hash value for udgraph
        """
        return hash((str(self._val), self._func))


class GeneratorHelper:
    @classmethod
    def _var(self, udgraph: UDGraph, variable: UDGraph, seed_dic):
        """This private helper function for UDGraph is used to get the values. This is used in the primitive.
        Generally speaking, this is the function to get node value in the computational graph. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            node value
        """
        if seed_dic and len(seed_dic) > 0:
            seed = seed_dic[udgraph._varname][variable._varname]
            if isinstance(udgraph._val, np.ndarray):
                return seed * np.ones(udgraph._valshape)
            else:
                return seed
        else:
            if variable._varname is not udgraph._varname:
                if isinstance(udgraph._val, np.ndarray):
                    return np.zeros(udgraph._valshape)
                else:
                    return 0
            else:
                if isinstance(udgraph._val, np.ndarray):
                    return np.ones(udgraph._valshape)
                else:
                    return 1

    @classmethod
    def _add(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for addition operation's derivative result. This is used in the primitive and __add__() in UDGraph.
        If there is one parent node, return the parental node value
        Otherwise, return the two parental nodes' addition result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the addition derivative result. 
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]

            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) + GraphGenerator.function_dic[g2._func](g2, variable, seed_dic)

    @classmethod
    def _radd(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for addition operation's derivative result. This is used in the primitive and __radd__() in UDGraph.
        If there is one parent node, return the parental node value
        Otherwise, return the two parental nodes' addition result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the right addition derivative result. 
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) + GraphGenerator.function_dic[g2._func](g2, variable, seed_dic)

    @classmethod
    def _mul(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for multiplication operation's derivative result. This is used in the primitive and __mul__() in UDGraph.
        If there is one parent node, return node multiplication result to the constant.
        Otherwise, return the two parental node multiplication result.

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the multiplication derivative result. 
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return udgraph._params["constant"] * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) * g2._val + GraphGenerator.function_dic[g2._func](g2, variable, seed_dic) * g1._val

    @classmethod
    def _rmul(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for multiplication operation's derivative result. This is used in the primitive and __rmul__() in UDGraph.
        If there is one parent node, return node multiplication result to the constant.
        Otherwise, return the two parental node multiplication result.

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the right multiplication derivative result.
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return udgraph._params["constant"] * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) * g2._val + GraphGenerator.function_dic[g2._func](g2, variable, seed_dic) * g1._val

    @classmethod
    def _neg(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """ This is a helper function to convert the value to negative. Used in __ne__() function in UDGraph

        Args:
            udgraph (UDGraph): [description]
            variable (UDGraph): [description]

        Returns:
            the negative value of the node value.
        """
        g1 = udgraph._parents[0]
        return -1 * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)

    @classmethod
    def _sub(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for subtraction operation's derivative result. This is used in the primitive and __sub__() in UDGraph.
        If there is one parent node, return the parental node value
        Otherwise, return the two parental nodes' subtraction result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the subtraction derivative result. 
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) - GraphGenerator.function_dic[g2._func](g2, variable, seed_dic)

    @classmethod
    def _rsub(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for subtraction operation's derivative result. This is used in the primitive and __rsub__() in UDGraph.
        If there is one parent node, return the parental node value
        Otherwise, return the two parental nodes' subtraction result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the right subtraction derivative result.
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return -1 * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) - GraphGenerator.function_dic[g2._func](g2, variable, seed_dic)

    @classmethod
    def _truediv(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for true division operation's derivative result. This is used in the primitive and __truediv__() in UDGraph.
        If there is one parent node, return the parental node value
        Otherwise, return the two parental nodes' true division result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the true division derivative result.
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) / udgraph._params["constant"]
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return (GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) * g2._val - GraphGenerator.function_dic[g2._func](g2, variable, seed_dic) * g1._val) / (g2._val * g2._val)

    @classmethod
    def _rtruediv(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for true division operation's derivative result. This is used in the primitive and __rtruediv__() in UDGraph.
        If there is one parent node, return the parental node value
        Otherwise, return the two parental nodes' true division result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the right true division derivative result.
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return -1 * udgraph._params["constant"] * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) / (g1._val * g1._val)
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return (GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) * g2._val - GraphGenerator.function_dic[g2._func](g2, variable, seed_dic) * g1._val) / (g2._val * g2._val)

    @classmethod
    def _floordiv(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for floor division operation's derivative result. This is used in the primitive and __floordiv__() in UDGraph.
        If there is one parent node, return the parental node value
        Otherwise, return the two parental nodes' floor division result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the floor division derivative result.
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) // udgraph._params["constant"]
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return (GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) * g2._val - GraphGenerator.function_dic[g2._func](g2, variable, seed_dic) * g1._val) // (g2._val * g2._val)

    @classmethod
    def _rfloordiv(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for floor division operation's derivative result. This is used in the primitive and __rfloordiv__() in UDGraph.
        If there is one parent node, return the parental node value
        Otherwise, return the two parental nodes' floor division result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the right floor division derivative result.
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) // udgraph._params["constant"]
        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]
            return (GraphGenerator.function_dic[g1._func](g1, variable, seed_dic) * g2._val - GraphGenerator.function_dic[g2._func](g2, variable, seed_dic) * g1._val) // (g2._val * g2._val)

    @classmethod
    def _pow(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for power operation's derivative result. This is used in the primitive and __pow__() in UDGraph.
        If there is one parent node, return the parental node power derivative result
        Otherwise, return the two parental nodes' power derivative result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the power derivative result.
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            if isinstance(g1._val, np.ndarray):
                return udgraph._params["degree"] * np.power(g1._val, udgraph._params["degree"] - 1) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
            else:
                return udgraph._params["degree"] * g1._val ** (udgraph._params["degree"] - 1) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)

        else:  # len == 2
            g1, g2 = udgraph._parents[0], udgraph._parents[1]

            if isinstance(g2._val, np.ndarray):
                if isinstance(g1._val, np.ndarray):
                    der1 = g2._val * np.power(
                        g1._val, g2._val - 1) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
                    der2 = np.log(g1._val) * udgraph._val * \
                        GraphGenerator.function_dic[g2._func](
                            g2, variable, seed_dic)
                    return der1 + der2
                else:
                    der1 = g2._val * g1._val ** (
                        g2._val - 1) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
                    der2 = math.log(g1._val) * udgraph._val * \
                        GraphGenerator.function_dic[g2._func](
                            g2, variable, seed_dic)
                    return der1 + der2
            else:  # g2._val is int
                if isinstance(g1._val, np.ndarray):
                    der1 = g2._val * \
                        np.power(g1._val, g2._val - 1) * \
                        GraphGenerator.function_dic[g1._func](
                            g1, variable, seed_dic)
                    der2 = np.log(g1._val) * udgraph._val * \
                        GraphGenerator.function_dic[g2._func](
                            g2, variable, seed_dic)
                    return der1 + der2
                else:
                    der1 = g2._val * g1._val ** (
                        g2._val - 1) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
                    der2 = math.log(g1._val) * udgraph._val * \
                        GraphGenerator.function_dic[g2._func](
                            g2, variable, seed_dic)
                    return der1 + der2

    @classmethod
    def _rpow(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """This private helper function is used for power operation's derivative. This is used in the primitive and __rpow__() in UDGraph.
        If there is one parent node, return the parental node power derivative result
        Otherwise, return the two parental nodes' power derivative result

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            the right power derivative result.
        """
        if len(udgraph._parents) == 1:
            g1 = udgraph._parents[0]
            return math.log(udgraph._params["base"]) * udgraph._val * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            g1, g2 = udgraph._parents[0], udgraph._parents[1]

            if isinstance(g2._val, np.ndarray):
                if isinstance(g1._val, np.ndarray):
                    der1 = g2._val * np.power(
                        g1._val, g2._val - 1) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
                    der2 = np.log(g1._val) * udgraph._val * \
                        GraphGenerator.function_dic[g2._func](
                            g2, variable, seed_dic)
                    return der1 + der2
                else:
                    der1 = g2._val * g1._val ** (
                        g2._val - 1) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
                    der2 = math.log(g1._val) * udgraph._val * \
                        GraphGenerator.function_dic[g2._func](
                            g2, variable, seed_dic)
                    return der1 + der2
            else:  # g2._val is int
                if isinstance(g1._val, np.ndarray):
                    der1 = g2._val * \
                        np.power(g1._val, g2._val - 1) * \
                        GraphGenerator.function_dic[g1._func](
                            g1, variable, seed_dic)
                    der2 = np.log(g1._val) * udgraph._val * \
                        GraphGenerator.function_dic[g2._func](
                            g2, variable, seed_dic)
                    return der1 + der2
                else:
                    der1 = g2._val * g1._val ** (
                        g2._val - 1) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
                    der2 = math.log(g1._val) * udgraph._val * \
                        GraphGenerator.function_dic[g2._func](
                            g2, variable, seed_dic)
                    return der1 + der2

    @classmethod
    def _cos(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """Calculate the derivative for cosine in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Raises:
            TypeError: if unlawful input to the cosine function

        Returns:
            cosine's derivatives results calculated in reverse mode. 
        """
        g1 = udgraph._parents[0]
        if isinstance(g1._val, (int, float)):
            return - 1 * math.sin(g1._val) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        elif isinstance(g1._val, np.ndarray):
            return -1 * np.sin(g1._val) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")

    @classmethod
    def _sin(self, udgraph: UDGraph, variable: UDGraph, seed_dic):
        """Calculate the derivative for sine in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Raises:
            TypeError: if unlawful input to the sine function

        Returns:
            sine's derivatives results calculated in reverse mode. 
        """
        g1 = udgraph._parents[0]
        if isinstance(g1._val, (int, float)):
            return math.cos(g1._val) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        elif isinstance(g1._val, np.ndarray):
            return np.cos(g1._val) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")

    @classmethod
    def _tan(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """Calculate the derivative for tangent in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Raises:
            TypeError: if unlawful input to the tangent function

        Returns:
            tangent's derivatives results calculated in reverse mode. 
        """
        g1 = udgraph._parents[0]
        if isinstance(g1._val, (int, float)):
            return (1 / (math.cos(g1._val)) ** 2) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        elif isinstance(g1._val, np.ndarray):
            return (1 / (np.cos(g1._val)) ** 2) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")

    @classmethod
    def _arccos(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """Calculate the derivative for arccosine in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Raises:
            TypeError: if unlawful input to the arccosine function

        Returns:
            arccosine's derivatives results calculated in reverse mode. 
        """
        g1 = udgraph._parents[0]
        if isinstance(g1._val, (int, float)):
            return (-1 / math.sqrt(1 - g1._val**2)) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        elif isinstance(g1._val, np.ndarray):
            return (-1 / np.sqrt(1 - g1._val**2)) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")

    @classmethod
    def _arcsin(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """Calculate the derivative for arcsine in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Raises:
            TypeError: if unlawful input to the arcsine function

        Returns:
            arcsine's derivatives results calculated in reverse mode. 
        """
        g1 = udgraph._parents[0]
        if isinstance(g1._val, (int, float)):
            return (1 / math.sqrt(1 - g1._val**2)) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        elif isinstance(g1._val, np.ndarray):
            return (1 / np.sqrt(1 - g1._val**2)) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")

    @classmethod
    def _arctan(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """Calculate the derivative for arctangent in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Raises:
            TypeError: if unlawful input to the arctangent function

        Returns:
            arctangent's derivatives results calculated in reverse mode. 
        """
        g1 = udgraph._parents[0]
        if isinstance(g1._val, (int, float, np.ndarray)):
            return (1 / (1 + g1._val**2)) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")

    @classmethod
    def _sqrt(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """Calculate the derivative for squared root in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Raises:
            TypeError: if unlawful input to the squared root function

        Returns:
            squared root's derivatives results calculated in reverse mode. 
        """
        g1 = udgraph._parents[0]
        if isinstance(g1._val, (int, float)):
            return 0.5 * math.pow(g1._val, -0.5) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        elif isinstance(g1._val, np.ndarray):
            return 0.5 * np.power(g1._val, -0.5) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")

    @classmethod
    def _exp(self, udgraph: UDGraph, variable: UDGraph, seed_dic=None):
        """Calculate the derivative for exponential in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Raises:
            TypeError: if unlawful input to the exponential function

        Returns:
            exponential's derivatives results calculated in reverse mode.
        """
        g1 = udgraph._parents[0]
        if isinstance(g1._val, (int, float)):
            return math.exp(g1._val) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        elif isinstance(g1._val, np.ndarray):
            return np.exp(g1._val) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)
        else:
            raise TypeError(
                "error raised by undefined: unsupported attribute type.")

    @classmethod
    def _log(self, udgraph: UDGraph, variable: UDGraph, seed_dic):
        """Calculate the derivative for log in reverse mode. 

        Args:
            udgraph (UDGraph)
            variable (UDGraph)

        Returns:
            log's derivatives results calculated in reverse mode.
        """
        g1 = udgraph._parents[0]
        return 1 / (math.log(udgraph._params["base"]) * g1._val) * GraphGenerator.function_dic[g1._func](g1, variable, seed_dic)


class GraphGenerator:
    function_dic = {
        UDPrimitive.VAR: GeneratorHelper._var,
        UDPrimitive.ADD: GeneratorHelper._add,
        UDPrimitive.RADD: GeneratorHelper._radd,
        UDPrimitive.MUL:  GeneratorHelper._mul,
        UDPrimitive.RMUL:  GeneratorHelper._rmul,
        UDPrimitive.NEG:  GeneratorHelper._neg,
        UDPrimitive.SUB: GeneratorHelper._sub,
        UDPrimitive.RSUB: GeneratorHelper._rsub,
        UDPrimitive.TRUEDIV: GeneratorHelper._truediv,
        UDPrimitive.RTRUEDIV: GeneratorHelper._rtruediv,
        UDPrimitive.FLOORDIV: GeneratorHelper._floordiv,
        UDPrimitive.RFLOORDIV: GeneratorHelper._rfloordiv,
        UDPrimitive.POW: GeneratorHelper._pow,
        UDPrimitive.RPOW: GeneratorHelper._rpow,
        UDPrimitive.COS: GeneratorHelper._cos,
        UDPrimitive.SIN: GeneratorHelper._sin,
        UDPrimitive.TAN: GeneratorHelper._tan,
        UDPrimitive.SQRT: GeneratorHelper._sqrt,
        UDPrimitive.EXP: GeneratorHelper._exp,
        UDPrimitive.LOG: GeneratorHelper._log,
        UDPrimitive.ACOS: GeneratorHelper._arccos,
        UDPrimitive.ASIN: GeneratorHelper._arcsin,
        UDPrimitive.ATAN: GeneratorHelper._arctan,
    }

    def __init__(self, g, variables, seeds_dic=None):
        """initialize the input instances.
        """
        self._udgraph = g
        self._variables = variables
        self._nxgraph = None
        self._seeds_dic = seeds_dic

    def _generate_inner(self, g: UDGraph, nxgraph: nx.DiGraph):
        """build the computational graph
        """
        for parent in g._parents:
            nxgraph.add_edge(parent, g)
        for k, v in g._params.items():
            nxgraph.add_edge(f"{k}: {v}", g)
        for parent in g._parents:
            self._generate_inner(parent, nxgraph)

    def generate_graph(self):
        """
        generate the visualization graph

        """

        if not self._nxgraph:
            self._nxgraph = nx.DiGraph()
            self._generate_inner(self._udgraph, self._nxgraph)
        nx.draw_networkx(self._nxgraph, with_labels=True, font_size=6)
        plt.savefig(f"{time()}.png")

    def generate_str(self):
        """Output the computational graph in str and maintain the structure.
        """
        return repr(self._udgraph)

    def generate_derivative(self, var_name):
        """A wrapper function to generate the derivative given the input key value. 
        Used in the trace function. 
        """
        if var_name not in self._variables.keys():
            raise TypeError(
                "error raised by undefined: variable not defined in function")
        variable = self._variables[var_name]
        return np.round(GraphGenerator.function_dic[self._udgraph._func](self._udgraph, variable, self._seeds_dic), 3)
