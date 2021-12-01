
import sys
# # temp solution for directory.
sys.path.append("./src/")

from types import LambdaType
import numpy as np
from undefined.Calculator import *
from undefined.UDFunction import UDFunction
from undefined.GraphGenerator import GraphGenerator


def trace(f, mode='forward', **kwargs):
    """trace function in undefined's API

    Args:
        f (function): user defined function
        mode (str, optional): Automatic Differenciation mode. Defaults to 'forward'.

    Raises:
        NotImplementedError: raised if mode is set to reverse
        AttributeError: raised if other form of modes are given

    Returns:
        (any, any): tuple of the values and derivatives
    """
    if type(f) is list:
        vals, ders = [], []
        for f_ in f:
            val, der = trace(f_, mode, **kwargs)
            vals.append(val)
            ders.append(der)

        return np.array(vals,dtype=object), np.stack(ders)
    elif type(f) is not LambdaType:
        raise TypeError("cannot handle non lambda functions.")
    num_variables = len(kwargs)
    variables = {}
    varnames = f.__code__.co_varnames
    if mode == 'forward':
        for i, varname in enumerate(varnames):
            variable = kwargs[varname]
            if isinstance(variable, np.ndarray):
                # vector input
                if variable.shape[0] != 1:
                    raise TypeError(
                        f"only support vector inputs of shape (1, ), invalid input {varname} has shape {variable.shape}")
                # single vector input
                if num_variables == 1:
                    variables[varname] = UDFunction(
                        variable, np.ones(variable.shape))
                # multiple vector inputs
                else:
                    seed_vector = np.zeros(
                        (num_variables, variable.shape[1]), dtype=int)
                    seed_vector[i, :] += 1
                    variables[varname] = UDFunction(variable, seed_vector)

            elif isinstance(variable, (int, float)):
                # single scalar input
                if num_variables == 1:
                    variables[varname] = UDFunction(variable)
                # multiple scalar inputs
                else:
                    seed_vector = np.zeros(num_variables, dtype=int)
                    seed_vector[i] = 1
                    variables[varname] = UDFunction(variable, seed_vector)
            else:
                raise TypeError(
                    "variable type not in (int, float, np.ndarray).")
        f = f(**variables)
        return f.val, f.der

    elif mode == 'reverse':
        for i, varname in enumerate(varnames):
            variable = kwargs[varname]
            if isinstance(variable, np.ndarray):
                if variable.shape[0] != 1:
                    raise TypeError(
                        f"only support vector inputs of shape (1, ), invalid input {varname} has shape {variable.shape}")
                variables[varname] = UDGraph(variable)
            elif isinstance(variable, (int, float)):
                variables[varname] = UDGraph(variable)
            else:
                raise TypeError(
                    "variable type not in (int, float, np.ndarray).")
        g = f(**variables)
        udgenerator = GraphGenerator(g, variables)

        return g.val, [udgenerator.generate_derivative(var_name) for var_name in variables.keys()]

    else:
        raise AttributeError("unsupported mode.")

# def stack_trace(f_vector, mode = 'forward'):
#     """[summary]

#     Args:
#         f_vector (list): list of user defined functions
#         mode (str, optional): Automatic Differenciation mode. Defaults to 'forward'.
#     """
#     raise NotImplementedError


if __name__ == "__main__":
    f1 = lambda x, y: sqrt(exp(x*y)) + cos(np.array([1, 2]))
    f2 = lambda x, y: log(exp(x*y), 2)
    f3 = lambda x, y: x - x * y
    f4 = lambda x, y: x - 3 * (x - y) / 2
    f5 = lambda x, y: (x - 1) / (y * 2) - x / 2
    print(trace(f3, x = 1, y = 2))
    print(trace(f3, mode='reverse', x = 1, y = 2))
    print(trace(f4, x = 1, y = 2))
    print(trace(f4, mode='reverse', x = 1, y = 2))
    print(trace(f5, x = 1, y = 2))
    print(trace(f5, mode='reverse', x = 1, y = 2))
    x = UDFunction(np.array([[2, 2]]), np.array([[1, 1], [0, 0]]))
    y = UDFunction(np.array([[1, 1]]), np.array([[0, 0], [1, 1]]))
    print("1. test vector inputs:")
    print("manual:")
    print("f1:")
    print(str(sqrt(exp(x*y))))
    print("f2:")
    print(str(log(exp(x*y), 2)))
    print("using trace() function:")
    print("f1:")
    print(trace(f1, x=np.array([[2, 2]]), y=np.array([[1, 1]])))
    print("f2:")
    print(trace(f2, x=np.array([[2, 2]]), y=np.array([[1, 1]])))
    print()

    print("2. test vector functions on scalar inputs:")
    f = [f1, f2, f3]
    print(trace(f, x=2, y=1))

    print("3. Test different user input:")
    try:
        trace(sum, x=1)
    except TypeError as e:
        print(e)
    print(trace(f3, 'forward', x=np.array([[2, 2]]), y=np.array([[1, 1]])))
    print(trace(f3, x=np.array([[2, 2]]), y=np.array([[1, 1]])))
    print(trace(f3, mode='forward', x=np.array(
        [[2, 2]]), y=np.array([[1, 1]])))
    print(trace(f3, mode='forward', x=np.array(
        [[2, 2]]), y=np.array([[1, 1]])))

    # x = UDFunction(np.array([2,2]), np.array([[1,1],[0,0]]))
    # y = UDFunction(np.array([1,1]), np.array([[0,0],[1,1]]))
    print("4. test scalar funciton on scalar inputs:")
    x = UDFunction(1, np.array([1, 0]))
    y = UDFunction(2, np.array([0, 1]))
    print("manual:")
    print("f1:")
    print(str(sqrt(exp(x*y))))
    print("f2:")
    print(str(log(exp(x*y), 2)))
    print("using trace() function:")
    print("f1:")
    print(trace(f1, x=1, y=2))
    print(trace(f1, mode = 'reverse', x=1, y=2))
    print("f2:")
    print(trace(f2, x=1, y=2))
    print(trace(f2, mode = 'reverse', x=1, y=2))
    print()

    print("5. test complex functions on vector input:")
    def f1(x): return sin((1 / x + 1)**2)
    def f2(x): return log((tan(sin(x + 10 / x)) + cos(2 / x))**2, 3)
    print("using trace() function:")
    print("f1:")
    print(trace(f1, x=1))
    print(trace(f1, mode = 'reverse', x=1))
    print("f2:")
    print(trace(f2, x=1))
    print(trace(f2, mode = 'reverse', x=1))
    f = [f1, f2]
    print(trace(f, x=np.array([[2, 2]])))
    print(trace(f, mode = 'reverse', x=np.array([[2, 2]])))