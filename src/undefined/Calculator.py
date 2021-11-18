import sys
# # temp solution for directory.
sys.path.append("./src/")

import numpy as np
import math
from undefined.UDFunction import UDFunction

def cos(udfunction):
    """calculate the cosine 

    Args:
        udfunction ([type]): [description]

    Raises:
        AttributeError: [description]

    Returns:
        
    """

    if isinstance(udfunction._val, (int, float)):
        new_val = math.cos(udfunction._val)
        new_der = - 1 * math.sin(udfunction._val) * udfunction._der
    # elif isinstance(udfunction._val, np.ndarray):
    #     new_val = np.cos(udfunction._val)
    #     new_der = -1 * np.sin(udfunction._val) * udfunction._der
    else:
        raise AttributeError("unsupported attribute type.")
    return UDFunction(new_val, new_der)

def sin(udfunction):
    """[summary]

    Args:
        udfunction ([type]): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    
    if isinstance(udfunction._val, (int, float)):
        new_val = math.sin(udfunction._val)
        new_der = math.cos(udfunction._val) * udfunction._der
    # elif isinstance(udfunction._val, np.ndarray):
    #     new_val = np.sin(udfunction._val)
    #     new_der = np.cos(udfunction._val) * udfunction._der
    else:
        raise AttributeError("unsupported attribute type.")
    return UDFunction(new_val, new_der)

def tan(udfunction: UDFunction):
    """[summary]

    Args:
        udfunction (UDFunction): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udfunction._val, (int, float)):
        new_val = math.tan(udfunction._val)
        new_der = (1 / (math.cos(udfunction._val)) ** 2) * udfunction._der
    # elif isinstance(udfunction._val, np.ndarray):
    #     new_val = np.tan(udfunction._val)
    #     new_der = (1 / (np.cos(udfunction._val)) ** 2) * udfunction._der
    else:
        raise AttributeError("unsupported attribute type.")
    return UDFunction(new_val, new_der)

def sqrt(udfunction: UDFunction):
    """[summary]

    Args:
        udfunction (UDFunction): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udfunction._val, (int, float)):
        new_val = math.sqrt(udfunction._val)
        new_der = 0.5 * math.pow(udfunction._val, -0.5) * udfunction._der
    # elif isinstance(udfunction._val, np.ndarray):
    #     new_val = np.sqrt(udfunction._val)
    #     new_der = 0.5 * np.poly(udfunction._val, -0.5) * udfunction._der
    else:
        raise AttributeError("unsupported attribute type.")
    return UDFunction(new_val, new_der)

def exp(udfunction: UDFunction):
    """[summary]

    Args:
        udfunction (UDFunction): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udfunction._val, (int, float)):
        new_val = math.exp(udfunction._val)
        new_der = math.exp(udfunction._val) * udfunction._der
    # elif isinstance(udfunction._val, np.ndarray):
    #     new_val = np.exp(udfunction._val)
    #     new_der = np.exp(udfunction._val) * udfunction._der
    else:
        raise AttributeError("unsupported attribute type.")
    return UDFunction(new_val, new_der)

def log(udfunction: UDFunction, base):
    """[summary]

    Args:
        udfunction (UDFunction): [description]
        base ([type]): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if isinstance(udfunction._val, (int, float)):
        new_val = math.log(udfunction._val, base)
        new_der = 1 / (math.log(base) * udfunction._val) * udfunction._der
    # elif isinstance(udfunction._val, np.ndarray):
    #     new_val = np.log(udfunction._val, base)
    #     new_der = 1 / (math.log(base) * udfunction._val) * udfunction._der
    else:
        raise AttributeError("unsupported attribute type.")
    return UDFunction(new_val, new_der)



# if __name__=="__main__":
#     a = 2.0
#     x = UDFunction(a)
#     f45 = sin("2*x") + x 