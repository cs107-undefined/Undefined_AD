# import logging
from enum import Enum
from datetime import datetime
import numpy as np


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
    ACOS = 20
    ASIN = 21
    ATAN = 22


def time():
    """[summary]

    Returns:
        [type]: [description]
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    return current_time


def check_division_by_zero(val):
    """[summary]

    Args:
        val ([type]): [description]

    Raises:
        ZeroDivisionError: [description]
        ZeroDivisionError: [description]
    """
    if isinstance(val, np.ndarray):
        if not np.all(np.round(val, 7)):
            raise ZeroDivisionError("error raised by undefined: divide by zero encountered")
    elif isinstance(val, (int, float)):
        if round(val,7) == 0:
            raise ZeroDivisionError("error raised by undefined: divide by zero encountered")


def check_pow(val, degree):
    """[summary]

    Args:
        val ([type]): [description]
        degree ([type]): [description]

    Raises:
        ValueError: [description]
        ValueError: [description]
    """
    try:
        temp = np.power(val, degree)
        if np.any(np.isnan(temp)):
            raise ValueError("error raised by undefined: invalid inputs for pow()")
    except ValueError as e:
        raise ValueError(f"error raised by undefined: {e}")


def check_log(val, base):
    """[summary]

    Args:
        val ([type]): [description]
        base ([type]): [description]

    Raises:
        ValueError: [description]
        ValueError: [description]
        ValueError: [description]
    """
    if base <= 0:
        raise ValueError(f"error raised by undefined: invalid base {base} for log")
    if isinstance(val, np.ndarray):
        if np.any(val <= 0):
            raise ValueError(f"error raised by undefined: invalid value {val} for log")
    elif isinstance(val, (int, float)):
        if val <= 0:
            raise ValueError(f"error raised by undefined: invalid value {val} for log")


def check_arc(val):
    """[summary]

    Args:
        val ([type]): [description]

    Raises:
        ValueError: [description]
        ValueError: [description]
    """
    if isinstance(val, np.ndarray):
        if not np.all(val > -1 and val < 1):
            raise ValueError(
                f"error raised by undefined: invalid values {val}, which should all be within (-1, 1)")
    elif isinstance(val, (int, float)):
        if not (val > -1 and val < 1):
            raise ValueError(
                f"error raised by undefined: invalid value {val}, which should be within (-1, 1)")
#     logging.basicConfig(level=logging.INFO)
#     if level == logging.INFO:
#         logging.info(information)
#     elif level == logging.ERROR:
#         logging.error(information)
#     elif level == logging.WARNING:
#         logging.warning(information)
#     else:
#         raise TypeError
