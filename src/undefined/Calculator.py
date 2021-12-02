import sys
# # temp solution for directory.
sys.path.append("./src")

from undefined.Utils import UDPrimitive
from undefined.GraphGenerator import UDGraph
from undefined.UDFunction import UDFunction
import math
import numpy as np

def cos(udobject):
    """calculate the cosine 

    Args:
        udfunction ([type]): [description]

    Raises:
        AttributeError: [description]

    Returns:

    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.cos(udobject._val)
            new_der = - 1 * math.sin(udobject._val) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.cos(udobject._val)
            new_der = -1 * np.sin(udobject._val) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    elif isinstance(udobject, UDGraph):
        new_func = UDPrimitive.COS
        if isinstance(udobject._val, (int, float)):
            new_val = math.cos(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.cos(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        return np.cos(udobject)

    elif isinstance(udobject, (int, float)):
        return math.cos(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def sin(udobject):
    """[summary]

    Args:
        udfunction ([type]): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.sin(udobject._val)
            new_der = math.cos(udobject._val) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.sin(udobject._val)
            new_der = np.cos(udobject._val) * udobject._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)
    elif isinstance(udobject, UDGraph):
        new_func = UDPrimitive.SIN
        if isinstance(udobject._val, (int, float)):
            new_val = math.sin(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.sin(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        return np.sin(udobject)

    elif isinstance(udobject, (int, float)):
        return math.sin(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def tan(udobject):
    """[summary]

    Args:
        udfunction (UDFunction): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.tan(udobject._val)
            new_der = (1 / (math.cos(udobject._val)) ** 2) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.tan(udobject._val)
            new_der = (1 / (np.cos(udobject._val)) ** 2) * udobject._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)
    elif isinstance(udobject, UDGraph):
        new_func = UDPrimitive.TAN
        if isinstance(udobject._val, (int, float)):
            new_val = math.tan(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.tan(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        return np.tan(udobject)

    elif isinstance(udobject, (int, float)):
        return math.tan(udobject)


def sqrt(udobject):
    """[summary]

    Args:
        udfunction (UDFunction): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.sqrt(udobject._val)
            new_der = 0.5 * math.pow(udobject._val, -0.5) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.sqrt(udobject._val)
            new_der = 0.5 * np.power(udobject._val, -0.5) * udobject._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    elif isinstance(udobject, UDGraph):
        new_func = UDPrimitive.SQRT
        if isinstance(udobject._val, (int, float)):
            new_val = math.sqrt(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.sqrt(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        return np.sqrt(udobject)

    elif isinstance(udobject, (int, float)):
        return math.sqrt(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def exp(udobject):
    """[summary]

    Args:
        udfunction (UDFunction): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.exp(udobject._val)
            new_der = math.exp(udobject._val) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.exp(udobject._val)
            new_der = np.exp(udobject._val) * udobject._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    elif isinstance(udobject, UDGraph):
        new_func = UDPrimitive.EXP
        if isinstance(udobject._val, (int, float)):
            new_val = math.exp(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.exp(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        return np.exp(udobject)

    elif isinstance(udobject, (int, float)):
        return math.exp(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def log(udobject, base):
    """[summary]

    Args:
        udfunction (UDFunction): [description]
        base ([type]): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.log(udobject._val, base)
            new_der = 1 / (math.log(base) * udobject._val) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.log(udobject._val) / math.log(base)
            new_der = 1 / (math.log(base) * udobject._val) * udobject._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    elif isinstance(udobject, UDGraph):
        new_func = UDPrimitive.LOG
        if isinstance(udobject._val, (int, float)):
            new_val = math.log(udobject._val, base)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.log(udobject._val) / math.log(base)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        udgraph._params["base"] = base
        return udgraph

    elif isinstance(udobject, np.ndarray):
        return np.log(udobject) / math.log(base)

    elif isinstance(udobject, (int, float)):
        return math.log(udobject, base)

    else:
        raise TypeError("unsupported attribute type.")


if __name__ == "__main__":
    beta = 3.0
    x = UDGraph(2)
    y = UDGraph(2)
    f = sin(x)**0.5 + cos(exp(y) + cos(2)) + log(y, 4) / x
    print(f)
