import UDFunction
from Calculator import *
import numpy as np

def trace(f, mode = 'forward'):
    """[summary]

    Args:
        f (function): user defined function
        mode (str, optional): Automatic Differenciation mode. Defaults to 'forward'.
    """
    raise NotImplementedError

def stack_trace(f_vector, mode = 'forward'):
    """[summary]

    Args:
        f_vector (list): list of user defined functions
        mode (str, optional): Automatic Differenciation mode. Defaults to 'forward'.
    """
    raise NotImplementedError

# x = UDFunction(np.array([2,2]), np.array([[1,1],[0,0]]))
# y = UDFunction(np.array([1,1]), np.array([[0,0],[1,1]]))


x = UDFunction(1, np.array([1,0]))
y = UDFunction(1, np.array([0,1]))
f1 = sqrt(exp(x*y))
f2 = log(exp(x*y), math.e)
print("val:", f1.val)
print("der:", f1.der)

print("val:", f2.val)
print("der:", f2.der)
