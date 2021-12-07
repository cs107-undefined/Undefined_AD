
import sys
# # temp solution for directory.
sys.path.append("./src/")

from types import LambdaType
import numpy as np
from undefined.Calculator import *
from undefined.UDFunction import UDFunction
from undefined.GraphGenerator import GraphGenerator


def trace(f, mode='forward', graph=False, **kwargs):
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

        return np.array(vals), np.stack(ders)
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
                if len(variable.shape) <= 1:
                    raise TypeError(
                        f"only support vector inputs of shape (1,n), invalid input {varname} has shape {variable.shape}")
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
        if graph:
            udgenerator.generate_graph()
            print(udgenerator.generate_str())
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


