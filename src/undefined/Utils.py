# import logging
from enum import Enum


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
    
# def time(operation):
#     raise NotImplementedError

# def log(level, information):
#     logging.basicConfig(level=logging.INFO)
#     if level == logging.INFO:
#         logging.info(information)
#     elif level == logging.ERROR:
#         logging.error(information)
#     elif level == logging.WARNING:
#         logging.warning(information)
#     else:
#         raise TypeError
