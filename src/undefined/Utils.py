# import logging
from enum import Enum
from datetime import datetime
import numpy as np
from numpy.lib.arraysetops import isin
from numpy.lib.index_tricks import nd_grid

class UDPrimitive(Enum):
    VAR = 0
    ADD = 1
    RADD = 2
    MUL = 3
    RMUL = 4
    NEG = 5
    SUB = 6
    RSUB = 7
    TRUEDIV = 8
    RTRUEDIV = 9
    FLOORDIV = 10
    RFLOORDIV = 11
    POW = 12
    RPOW = 13
    COS = 14
    SIN = 15
    TAN = 16
    SQRT = 17
    EXP = 18
    LOG = 19

def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def check_division_by_zero(val):
    if isinstance(val, np.ndarray):
        if not np.all(val):
            raise ZeroDivisionError("divide by zero encountered")
    elif isinstance(val, (int, float)):
        if val == 0:
            raise ZeroDivisionError("divide by zero encountered")

def check_pow(val, degree):
    if isinstance(val, np.ndarray):
        if isinstance(degree, np.ndarray):
            if val.shape[0] != degree.shape[0]:
                raise ValueError(f"operands could not be broadcast together with shapes {val.shape}, {degree.shape}")
            if np.any(1 / degree % 2 == 0):
                if np.any(val < 0):
                    raise ValueError(f"negative values not allowed for degree {degree}")
        elif isinstance(degree, (int, float)):
            if 1 / degree % 2 == 0:
                if np.any(val < 0):
                    raise ValueError(f"negative values not allowed for degree {degree}")
    elif isinstance(val, (int, float)):
        if isinstance(degree, np.ndarray):
            if np.any(1 / degree % 2 == 0):
                if val < 0:
                    raise ValueError(f"negative value not allowed for degree {degree}")
        elif isinstance(degree, (int, float)):
            if 1 / degree % 2 == 0:
                if val < 0:
                    raise ValueError(f"negative value not allowed for degree {degree}")

def check_log(val, base):
    if base <= 0:
        raise ValueError(f"invalid base {base} for log")
    if isinstance(val, np.ndarray):
        if np.any(val <= 0):
            raise ValueError(f"invalid value {val} for log")
    elif isinstance(val, (int, float)):
        if val <= 0:
            raise ValueError(f"invalid value {val} for log")
            
#     logging.basicConfig(level=logging.INFO)
#     if level == logging.INFO:
#         logging.info(information)
#     elif level == logging.ERROR:
#         logging.error(information)
#     elif level == logging.WARNING:
#         logging.warning(information)
#     else:
#         raise TypeError
