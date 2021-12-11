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
    """get current time at the most precision in seconds

    Returns:
        return the current time in string in Hour:Minute:Seconds:precise time format
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    return current_time


def check_division_by_zero(val):
    """Used to check if unlawful division is executed by users
    raise errors if happened.

    Args:
        val ([int or float])

    Raises:
        ZeroDivisionError raised if dividing by 0.
    """
    if isinstance(val, np.ndarray):
        if not np.all(np.round(val, 7)):
            raise ZeroDivisionError("error raised by undefined: divide by zero encountered")
    elif isinstance(val, (int, float)):
        if round(val,7) == 0:
            raise ZeroDivisionError("error raised by undefined: divide by zero encountered")


def check_pow(val, degree):
    """Used to check if unlawful power is executed by users
    raise errors if happened.

    Args:
        val ([int or float])
        degree ([int or float])

    Raises:
        raise ValueError if any of the val or degree is NA type.
    """
    try:
        temp = np.power(val, degree)
        if np.any(np.isnan(temp)):
            raise ValueError("error raised by undefined: invalid inputs for pow()")
    except ValueError as e:
        raise ValueError(f"error raised by undefined: {e}")


def check_log(val, base):
    """Used to check if unlawful log is executed by users
    raise errors if happened. Cannot take log for number that is less or equal to 0
    log base also needs to be greater than 0.

    Args:
        val ([int or float])
        base ([int or float])

    Raises:
        raise ValueError if any of the base or val is less than 0.
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
    """Used to check if unlawful inverse trig function is executed by users
    raise errors if happened. Cannot take inverse trig function that is not between -1 and 1

    Args:
        val ([int or float])

    Raises:
        raise error if number is not between -1 and 1
    """
    if isinstance(val, np.ndarray):
        if not np.all(val > -1 and val < 1):
            raise ValueError(
                f"error raised by undefined: invalid values {val}, which should all be within (-1, 1)")
    elif isinstance(val, (int, float)):
        if not (val > -1 and val < 1):
            raise ValueError(
                f"error raised by undefined: invalid value {val}, which should be within (-1, 1)")

