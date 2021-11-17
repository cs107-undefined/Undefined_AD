import UDFunction
from Calculator import *
import numpy as np

def trace(f, **kwargs): 
    """[summary]

    Args:
        f (function): user defined function
        mode (str, optional): Automatic Differenciation mode. Defaults to 'forward'.
    """
    if 'mode' in kwargs:
        mode = kwargs['mode']
        kwargs.pop('mode')
    else:
        mode = 'forward'
    if mode == 'forward':
        num_variables = len(kwargs)
        variables = []
        for i, (_, v) in enumerate(kwargs.items()):
            if num_variables == 1:
                variables.append(UDFunction(v))
            else:
                seed_vector = np.zeros(num_variables, dtype = int)
                seed_vector[i] = 1
                variables.append(UDFunction(v, seed_vector))
        f = f(*tuple(variables))
        # print(f)
        return f

def stack_trace(f_vector, mode = 'forward'):
    """[summary]

    Args:
        f_vector (list): list of user defined functions
        mode (str, optional): Automatic Differenciation mode. Defaults to 'forward'.
    """
    raise NotImplementedError


if __name__ == "__main__":

    f1 = lambda x, y: sqrt(exp(x*y))
    f2 = lambda x, y: log(exp(x*y), 2)
    x = UDFunction(1, np.array([1,0]))
    y = UDFunction(2, np.array([0,1]))

    f3 = lambda x, y: x + y - 1

    print(trace(f3, x = 1, y = 2))


    # x = UDFunction(np.array([2,2]), np.array([[1,1],[0,0]]))
    # y = UDFunction(np.array([1,1]), np.array([[0,0],[1,1]]))

    # print("manual:")
    # print("f1:")
    # print(str(sqrt(exp(x*y))))
    # print("f2:")
    # print(str(log(exp(x*y), 2)))
    # print("using trace() function:")
    # print("f1:")
    # trace(f1, x = 1, y = 2)
    # print("f2:")
    # trace(f2, x = 1, y = 2)
    # print()
    
    # f1 = lambda x: sin((1 / x + 1)**2)
    # f2 = lambda x: log((tan(sin(x + 10 / x)) + cos(2 / x))**2, 3)
    # x = UDFunction(1)
    # print("manual:")
    # print("f1:")
    # print(sin((1 / x + 1)**2))
    # print("f2:")
    # print(log((tan(sin(x + 10 / x)) + cos(2 / x))**2, 3))
    # print("using trace() function:")
    # print("f1:")
    # print(trace(f1, x = 1))
    # # print("f2:")
    # # trace(f2, x = 1)

