import numpy as np
import sys
# # temp solution for directory.
sys.path.append("./src/")
import math
from undefined.UDFunction import UDFunction
from undefined.GraphGenerator import UDGraph
from undefined.Utils import UDPrimitive, check_division_by_zero, check_log, check_pow, check_arc



def cos(udobject):
    """calculate the cosine operation of input

    Args:
        udobject (udfunction object,UDGraph object,ndarray,ndarray,int,float): User defined function

    Raises:

        TypeError:raised if input is not compatiable with cosine operation

    Returns:
        if input is udfunction object,update val and der by cosine operation.
        if input is UDGraph object,update notes and function by cosine operation.
        if input is int,float,ndarray object,update them in cosine operation by their own types. 
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
    """calculate the sin operation of input

    Args:
        udobject (udfunction object,UDGraph object,ndarray,ndarray,int,float): User defined function/number

    Raises:

        TypeError:raised if input is not compatiable with sin operation

    Returns:
        if input is udfunction object,update val and der by sin operation.
        if input is UDGraph object,update notes and function by sin operation.
        if input is int,float,ndarray object,update them in sin operation by their own types. 
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.sin(udobject._val)
            new_der = math.cos(udobject._val) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.sin(udobject._val)
            new_der = np.cos(udobject._val) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
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
    """calculate the tangent operation of input

    Args:
        udobject (udfunction object,UDGraph object,ndarray,ndarray,int,float): User defined function/number

    Raises:

        TypeError:raised if input is not compatiable with tangent operation

    Returns:
        if input is udfunction object,update val and der by tangenr operation.
        if input is UDGraph object,update notes and function by tangent operation.
        if input is int,float,ndarray object,update them in tangent operation by their own types. 
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            check_division_by_zero(math.cos(udobject._val))
            new_val = math.tan(udobject._val)
            new_der = (1 / (math.cos(udobject._val)) ** 2) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            check_division_by_zero(np.cos(udobject._val))
            new_val = np.tan(udobject._val)
            new_der = (1 / (np.cos(udobject._val)) ** 2) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)
    elif isinstance(udobject, UDGraph):
        new_func = UDPrimitive.TAN
        if isinstance(udobject._val, (int, float)):
            check_division_by_zero(math.cos(udobject._val))
            new_val = math.tan(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            check_division_by_zero(np.cos(udobject._val))
            new_val = np.tan(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        check_division_by_zero(np.cos(udobject))
        return np.tan(udobject)

    elif isinstance(udobject, (int, float)):
        check_division_by_zero(math.cos(udobject))
        return math.tan(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def sinh(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Returns:
        [type]: [description]
    """
    return (exp(udobject) - exp(-udobject)) / 2


def cosh(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Returns:
        [type]: [description]
    """
    return (exp(udobject) + exp(-udobject)) / 2


def tanh(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Returns:
        [type]: [description]
    """
    return sinh(udobject) / cosh(udobject)


def coth(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Returns:
        [type]: [description]
    """
    return cosh(udobject) / sinh(udobject)


def sech(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Returns:
        [type]: [description]
    """
    return 1 / cosh(udobject)


def csch(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Returns:
        [type]: [description]
    """
    return 1 / sinh(udobject)


def arccos(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Raises:
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udobject, UDFunction):
        check_arc(udobject._val)
        if isinstance(udobject._val, (int, float)):
            new_val = math.acos(udobject._val)
            new_der = (-1 / math.sqrt(1 - udobject._val**2)) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.arccos(udobject._val)
            new_der = (-1 / np.sqrt(1 - udobject._val**2)) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    elif isinstance(udobject, UDGraph):
        check_arc(udobject._val)
        new_func = UDPrimitive.ACOS
        if isinstance(udobject._val, (int, float)):
            new_val = math.acos(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.arccos(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        check_arc(udobject)
        return np.arccos(udobject)

    elif isinstance(udobject, (int, float)):
        check_arc(udobject)
        return math.acos(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def arcsin(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Raises:
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udobject, UDFunction):
        check_arc(udobject._val)
        if isinstance(udobject._val, (int, float)):
            new_val = math.asin(udobject._val)
            new_der = (1 / math.sqrt(1 - udobject._val**2)) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.arcsin(udobject._val)
            new_der = (1 / np.sqrt(1 - udobject._val**2)) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)
    elif isinstance(udobject, UDGraph):
        check_arc(udobject._val)
        new_func = UDPrimitive.ASIN
        if isinstance(udobject._val, (int, float)):
            new_val = math.asin(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.arcsin(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        check_arc(udobject)
        return np.arcsin(udobject)

    elif isinstance(udobject, (int, float)):
        check_arc(udobject)
        return math.asin(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def arctan(udobject):
    """[summary]

    Args:
        udobject ([type]): [description]

    Raises:
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.atan(udobject._val)
            new_der = (1 / (1 + udobject._val ** 2)) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.arctan(udobject._val)
            new_der = (1 / (1 + udobject._val ** 2)) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)
    elif isinstance(udobject, UDGraph):
        new_func = UDPrimitive.ATAN
        if isinstance(udobject._val, (int, float)):
            new_val = math.atan(udobject._val)
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.arctan(udobject._val)
        else:
            raise TypeError("unsupported attribute type.")
        udgraph = UDGraph(new_val, new_func)
        udgraph._parents.append(udobject)
        return udgraph

    elif isinstance(udobject, np.ndarray):
        return np.arctan(udobject)

    elif isinstance(udobject, (int, float)):
        return math.atan(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def sqrt(udobject):
    """calculate the square root operation of input

    Args:
        udobject (udfunction object,UDGraph object,ndarray,ndarray,int,float): User defined function/number

    Raises:

        TypeError:raised if input is not compatiable with square root operation

    Returns:
        if input is udfunction object,update val and der by square root operation.
        if input is UDGraph object,update notes and function by square root operation.
        if input is int,float,ndarray object,update them in square root operation by their own types. 
    """
    if isinstance(udobject, UDFunction):
        check_pow(udobject._val, 0.5)
        if isinstance(udobject._val, (int, float)):
            new_val = math.sqrt(udobject._val)
            new_der = 0.5 * math.pow(udobject._val, -0.5) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.sqrt(udobject._val)
            new_der = 0.5 * np.power(udobject._val, -0.5) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    elif isinstance(udobject, UDGraph):
        check_pow(udobject._val, 0.5)
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
        check_pow(udobject, 0.5)
        return np.sqrt(udobject)

    elif isinstance(udobject, (int, float)):
        check_pow(udobject, 0.5)
        return math.sqrt(udobject)

    else:
        raise TypeError("unsupported attribute type.")


def exp(udobject):
    """calculate the square exponential of input

    Args:
        udobject (udfunction object,UDGraph object,ndarray,ndarray,int,float): User defined function/number

    Raises:

        TypeError:raised if input is not compatiable with exponential operation

    Returns:
        if input is udfunction object,update val and der by exponential operation.
        if input is UDGraph object,update notes and function by exponential operation.
        if input is int,float,ndarray object,update them in exponential operation by their own types. 
    """
    if isinstance(udobject, UDFunction):
        if isinstance(udobject._val, (int, float)):
            new_val = math.exp(udobject._val)
            new_der = math.exp(udobject._val) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.exp(udobject._val)
            new_der = np.exp(udobject._val) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
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


def standard_logistic(udobject):
    return 1 / (1 + exp(-udobject))


def log(udobject, base=math.e):
    """calculate the log of input

    Args:
        udobject (udfunction object,UDGraph object,ndarray,ndarray,int,float): User defined function/number

    Raises:
        TypeError:raised if input is not compatiable with log operation

    Returns:
        if input is udfunction object,update val and der by log operation.
        if input is UDGraph object,update notes and function by log operation.
        if input is int,float,ndarray object,update them in log operation by their own types. 
    """
    if isinstance(udobject, UDFunction):
        check_log(udobject._val, base)
        if isinstance(udobject._val, (int, float)):
            new_val = math.log(udobject._val, base)
            new_der = 1 / (math.log(base) * udobject._val) * udobject._der
        elif isinstance(udobject._val, np.ndarray):
            new_val = np.log(udobject._val)
            new_val = new_val / math.log(base)
            new_der = 1 / (math.log(base) * udobject._val) * udobject._der
        else:
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    elif isinstance(udobject, UDGraph):
        check_log(udobject._val, base)
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
        check_log(udobject, base)
        return np.log(udobject) / math.log(base)

    elif isinstance(udobject, (int, float)):
        check_log(udobject, base)
        return math.log(udobject, base)

    else:
        raise TypeError("unsupported attribute type.")


# if __name__ == "__main__":
    # beta = 3.0
    # x = UDFunction(2)
    # y = UDFunction(2)
    # f = sin(x)**0.5 + cos(exp(y) + cos(2)) + log(y, 4) / x
    # f1 = sinh(f)
    # f2 = cosh(f)
    # f3 = tanh(f)
    # f4 = csch(f)
    # f5 = coth(f)
    # f6 = sech(f)
    # print(f)
    # print(f1)
    # print(f2)
    # print(f3)
    # print(f4)
    # print(f5)
    # print(f6)
