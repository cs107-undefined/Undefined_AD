import numpy as np
import math
from UDFunction import UDFunction
# TODO: test and check for errors
def cos(udfunction):
    try:
        new_val = np.cos(udfunction.val)
        new_der = -1 * np.sin(udfunction.val) * udfunction.der
    except AttributeError:
        new_val = math.cos(udfunction.val)
        new_der = - 1 * math.sin(udfunction.val) * udfunction.der
    finally:
        return UDFunction(new_val, new_der)

def sin(udfunction):
    try:
        new_val = np.sin(udfunction.val)
        new_der = np.cos(udfunction.val) * udfunction.der
    except AttributeError:
        new_val = math.sin(udfunction.val)
        new_der = math.cos(udfunction.val) * udfunction.der
    finally:
        return UDFunction(new_val, new_der)

def tan(udfunction: UDFunction):
    try:
        new_val = np.tan(udfunction.val)
        new_der = (1 / (np.cos(udfunction.val)) ** 2) * udfunction.der
    except AttributeError:
        new_val = math.tan(udfunction.val)
        new_der = (1 / (math.cos(udfunction.val)) ** 2) * udfunction.der
    finally:
        return UDFunction(new_val, new_der)

def sqrt(udfunction: UDFunction):
    try:
        new_val = np.sqrt(udfunction.val)
        new_der = 0.5 * np.poly(udfunction.val, -0.5) * udfunction.der
    except TypeError:
        new_val = math.sqrt(udfunction.val)
        new_der = 0.5 * math.pow(udfunction.val, -0.5) * udfunction.der
    finally:
        return UDFunction(new_val, new_der)

def exp(udfunction: UDFunction):
    try:
        new_val = np.exp(udfunction.val)
        new_der = np.exp(udfunction.val) * udfunction.der
    except AttributeError:
        new_val = math.exp(udfunction.val)
        new_der = math.exp(udfunction.val) * udfunction.der
    finally:
        return UDFunction(new_val, new_der)

def log(udfunction: UDFunction, base):
    try:
        new_val = np.log(udfunction.val, base)
        new_der = 1 / (math.log(base) * udfunction.val) * udfunction.der
    except TypeError:
        new_val = math.log(udfunction.val, base)
        new_der = 1 / (math.log(base) * udfunction.val) * udfunction.der
    finally:
        return UDFunction(new_val, new_der)