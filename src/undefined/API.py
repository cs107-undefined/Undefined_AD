import sys

# # temp solution for directory.
sys.path.append("./src/")
from undefined.GraphGenerator import GraphGenerator
from undefined.UDFunction import UDFunction
from undefined.Calculator import *
import numpy as np
from types import LambdaType



def trace(f, mode='forward', seeds=None, plot=False, **kwargs):
    """This is the main function that the users will interact with.

    Args:
        f ([LambdaType]): [This is the user defined function. Use list if there are multiple input functions]
        mode (str, optional): Defaults to 'forward'. Determine with mode to use to calculate the derivatives.
        seeds ([type], optional): Defaults to None. Used to calculate the Jacobian matrix
        plot (bool, optional):  Defaults to False. Need to use in combination with "reverse" mode. If True, it will save the computational graph to your current working directory.

    Raises:
        Errors will raise if unlawful inputs are given.

    Returns:
        The function values and the derivatives results will be saved in a tuple as the output.
    """
    if type(f) is list:
        vals, ders = [], []
        for f_ in f:
            val, der = trace(f_, mode, seeds, plot, **kwargs)
            vals.append(val)
            ders.append(der)

        return np.array(vals), np.stack(ders)
    elif type(f) is not LambdaType:
        raise TypeError("error raised by undefined: cannot handle non lambda functions.")
    fix_len = -1
    num_variables = len(kwargs)
    variables = {}
    varnames = f.__code__.co_varnames
    if len(varnames) != num_variables:
        raise AttributeError("error raised by undefined: inconsistent number of variables.")
    if mode == 'forward':
        for i, varname in enumerate(varnames):
            variable = kwargs[varname]
            
            if isinstance(variable, np.ndarray):
                # 【【vector input】】
                if len(variable.shape) <= 1 or variable.shape[0] != 1:
                    raise TypeError(
                        f"error raised by undefined: only support vector inputs of shape (1,n), invalid input {varname} has shape {variable.shape}")
                # 【single vector input】
                if num_variables == 1:
                    if seeds is not None:
                        if type(seeds) not in (int, float):
                            raise TypeError("error raised by undefined: incorrect type of seed vector, expect int or float")
                        seed = seeds
                    else:
                        seed = 1
                    variables[varname] = UDFunction(
                        variable, np.ones(variable.shape) * seed)
                # 【multiple vector inputs】
                else:
                    # check if all the vector inputs has the same len
                    if fix_len != -1:
                        if fix_len != variable.shape[1]:
                            raise AttributeError("error raised by undefined: cannot handle multiple vector inputs with different lengths")
                    else:
                        fix_len = variable.shape[1]
                    if seeds is not None:
                        if type(seeds) is not np.ndarray:
                            raise TypeError("error raised by undefined: at least one seed vector incorrectly defined")
                        seed = seeds[i]
                        if type(seed) is not np.ndarray:
                            raise TypeError("error raised by undefined: at least one seed vector incorrectly defined")
                        if len(seed) != num_variables:
                            raise AttributeError(f"error raised by undefined: incorrect shape for seed vectors, expect ({num_variables, num_variables})")
                        seed_vector = seed.reshape(num_variables,1) * np.ones(
                        (num_variables, fix_len), dtype=int)
                    else:
                        seed_vector = np.zeros(
                        (num_variables, fix_len), dtype=int)
                        seed_vector[i, :] += 1
                    variables[varname] = UDFunction(variable, seed_vector)

            elif isinstance(variable, (int, float)):
                # 【【single scalar input】】
                if num_variables == 1:
                    if seeds is not None:
                        if type(seeds) not in (int, float):
                            raise TypeError("error raised by undefined: incorrect type of seed vector, expect int or float")
                        seed = seeds
                        variables[varname] = UDFunction(variable, seed)
                    else:
                        variables[varname] = UDFunction(variable)
                # 【【multiple scalar inputs】】
                else:
                    if seeds is not None:
                        if type(seeds) is not np.ndarray:
                            raise TypeError("error raised by undefined: incorrect type of seed vectors, expect numpy.ndarray")
                        seed = seeds[i]
                        if len(seed) != num_variables:
                            raise AttributeError(f"error raised by undefined: incorrect shape for seed vector, expect ({num_variables, num_variables})")
                        seed_vector = seed.reshape(num_variables,1)
                    else:
                        seed_vector = np.zeros((num_variables,1), dtype=int)
                        seed_vector[i,:] = 1
                    variables[varname] = UDFunction(variable, seed_vector)
            else:
                raise TypeError(
                    "error raised by undefined: variable type not in (int, float, np.ndarray).")

        f = f(**variables)
        return f.val, f.der.tolist() if type(f.der) is np.ndarray else f.der

    elif mode == 'reverse':
        for i, varname in enumerate(varnames):
            variable = kwargs[varname]
            if isinstance(variable, np.ndarray):
                if variable.shape[0] != 1 or variable.shape[0] != 1:
                    raise TypeError(
                        f"error raised by undefined: only support vector inputs of shape (1, ), invalid input {varname} has shape {variable.shape}")
                variables[varname] = UDGraph(variable, varname = varname)
            elif isinstance(variable, (int, float)):
                variables[varname] = UDGraph(variable, varname = varname)
            else:
                raise TypeError(
                    "error raised by undefined: variable type not in (int, float, np.ndarray).")
        g = f(**variables)
        # check format of seeds
        seeds_dic = {}
        if seeds is not None:
            if num_variables == 1:
                # single input
                if type(seeds) not in (int, float):
                    raise TypeError("error raised by undefined: incorrect type of seed vector, expect int or float")
                seeds_dic[varnames[i]] = {varnames[i]:seeds}
            else:
                # multiple inputs
                if type(seeds) is not np.ndarray:
                    raise TypeError("error raised by undefined: incorrect type of seed vectors, expect numpy.ndarray")
                if seeds.shape[0] != num_variables or seeds.shape[1] != num_variables :
                    raise AttributeError(f"error raised by undefined: incorrect shape for seed vector, expect ({num_variables, num_variables})")

                for i in range(num_variables):
                    seeds_dic[varnames[i]] = {}
                    for j in range(num_variables):
                        seeds_dic[varnames[i]][varnames[j]] = seeds[i][j]
        udgenerator = GraphGenerator(g, variables, seeds_dic)
        if plot:
            print(udgenerator.generate_str())
            udgenerator.generate_graph()

        res_der = []
        for var_name in variables.keys():
            res_var = udgenerator.generate_derivative(var_name)
            if type(res_var) is np.ndarray:
                res_der.append(res_var.tolist()[0])
            elif type(res_var) is not list:
                res_der.append([res_var])
            else:
                res_der.append(res_der)

        # 【single scalar input】
        if len(res_der) == 1 and len(res_der[0]) == 1:
            return g.val, res_der[0][0]
        return g.val, res_der
    else:
        raise AttributeError("error raised by undefined: unsupported mode.")


