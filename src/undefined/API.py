import sys

# # temp solution for directory.
sys.path.append("/Users/xinran/Desktop/Harvard/Courses/cs107/cs107-FinalProject/src/")
from undefined.GraphGenerator import GraphGenerator
from undefined.UDFunction import UDFunction
from undefined.Calculator import *
import numpy as np
from types import LambdaType



def trace(f, mode='forward', seeds=None, plot=False, **kwargs):
    # """trace function in undefined's API

    # Args:
    #     f (function): user defined function
    #     mode (str, optional): Automatic Differenciation mode. Defaults to 'forward'.

    # Raises:
    #     NotImplementedError: raised if mode is set to reverse
    #     AttributeError: raised if other form of modes are given

    # Returns:
    #     (any, any): tuple of the values and derivatives
    # """
    """[summary]

    Args:
        f ([type]): [description]
        mode (str, optional): [description]. Defaults to 'forward'.
        seeds ([type], optional): [description]. Defaults to None.
        plot (bool, optional): [description]. Defaults to False.

    Raises:
        TypeError: [description]
        AttributeError: [description]
        TypeError: [description]
        AttributeError: [description]
        TypeError: [description]
        AttributeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    if type(f) is list:
        vals, ders = [], []
        for f_ in f:
            val, der = trace(f_, mode, **kwargs)
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
                        seed = seeds[i]
                        if type(seeds) is not np.ndarray:
                            raise TypeError("error raised by undefined: incorrect type of seed vectors, expect numpy.ndarray")
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


# <<<<<<< HEAD
# if __name__ == "__main__":
#     f1 = lambda x, y: sqrt(exp(x*y)) + cos(np.array([1, 2]))
#     f2 = lambda x, y: log(exp(x*y), 2)
#     f3 = lambda x, y: x - x * y
#     f4 = lambda x, y: x - 3 * (x - y) / 2
#     f5 = lambda x, y: (x - 1) / (y * 2) - x / 2
#     print(trace(f3, x = 1, y = 2))
#     print(trace(f3, mode='reverse', plot=True, x = 1, y = 2))
#     print(trace(f4, x = 1, y = 2))
#     print(trace(f4, mode='reverse', plot=True, x = 1, y = 2))
#     print(trace(f5, x = 1, y = 2))
#     print(trace(f5, mode='reverse', x = 1, y = 2))
# =======
if __name__ == "__main__":
    f0 = lambda x ,y : x * y
    f1 = lambda x: sqrt(x)
    f11 = lambda y: sqrt(y)
    f12 = lambda x, y: sqrt(x) + sqrt(y)
    f2 = lambda x, y: log(exp(x**y), 2)
    f3 = lambda x, y: x - x * y
    f4 = lambda x, y: x - 3 * (x - y) / 2
    f5 = lambda x, y: (x - 1) / (y * 2) - x / 2
    print(trace(f0, mode = 'reverse', x = 1, y = 2))
    # print(trace(f1, seeds = 1, x = np.array([[10,1]]))[1])
    # print(trace(f1, mode = 'reverse', seeds = 1, plot=True, x = np.array([[10,1]]))[1])
#     print("*")
#     print(trace(f11, y = 2)[1])
#     print(trace(f11, mode = 'reverse',  y = 2)[1])
#     print("**")
    print(trace(f12, seeds= np.array([[1,2],[0,1]]), x = 1,y = 2)[1])
    print(trace(f12, mode = 'reverse', x = 1, y=2)[1])
#     print(trace(f3, x = 1, y = 2))
#     print(trace(f3, mode='reverse', x = 1, y = 2))
#     print(trace(f4, x = 1, y = 2))
#     print(trace(f4, mode='reverse', x = 1, y = 2))
#     print(trace(f5, x = 1, y = 2))
#     print(trace(f5, mode='reverse', x = 1, y = 2))
# >>>>>>> 35396b2991ee285b274024c1a0322905f18265ef
    # x = UDFunction(np.array([[2, 2]]), np.array([[1, 1], [0, 0]]))
    # y = UDFunction(np.array([[1, 1]]), np.array([[0, 0], [1, 1]]))
    # print("1. test vector inputs:")
    # print("manual:")
    # print("f1:")
    # print(str(sqrt(exp(x*y))))
    # print("f2:")
    # print(str(log(exp(x*y), 2)))
    # print("using trace() function:")
    # print("f1:")
    # print(trace(f1, x=np.array([[2, 2]]), y=np.array([[1, 1]])))
    # print("f2:")
    # print(trace(f2, x=np.array([[2, 2]]), y=np.array([[1, 1]])))
    # print()

    # print("2. test vector functions on scalar inputs:")
    # f = [f1, f2, f3]
    # print(trace(f, x=2, y=1))

    # print("3. Test different user input:")
    # try:
    #     trace(sum, x=1)
    # except TypeError as e:
    #     print(e)
    # print(trace(f3, 'forward', x=np.array([[2, 2]]), y=np.array([[1, 1]])))
    # print(trace(f3, x=np.array([[2, 2]]), y=np.array([[1, 1]])))
    # print(trace(f3, mode='forward', x=np.array(
    #     [[2, 2]]), y=np.array([[1, 1]])))
    # print(trace(f3, mode='forward', x=np.array(
    #     [[2, 2]]), y=np.array([[1, 1]])))

    # # x = UDFunction(np.array([2,2]), np.array([[1,1],[0,0]]))
    # # y = UDFunction(np.array([1,1]), np.array([[0,0],[1,1]]))
    # print("4. test scalar funciton on scalar inputs:")
    # x = UDFunction(1, np.array([1, 0]))
    # y = UDFunction(2, np.array([0, 1]))
    # print("manual:")
    # print("f1:")
    # print(str(sqrt(exp(x*y))))
    # print("f2:")
    # print(str(log(exp(x*y), 2)))
    # print("using trace() function:")
    # print("f1:")
    # print(trace(f1, x=1, y=2))
    # print(trace(f1, mode = 'reverse', x=1, y=2))
    # print("f2:")
    # print(trace(f2, x=1, y=2))
    # print(trace(f2, mode = 'reverse', x=1, y=2))
    # print()

    # print("5. test complex functions on vector input:")
    # def f1(x): return sin((1 / x + 1)**2)
    # def f2(x): return log((tan(sin(x + 10 / x)) + cos(2 / x))**2, 3)
    # print("using trace() function:")
    # print("f1:")
    # print(trace(f1, x=1))
    # print(trace(f1, mode = 'reverse', x=1))
    # print("f2:")
    # print(trace(f2, x=1))
    # print(trace(f2, mode = 'reverse', x=1))
    # f = [f1, f2]
    # print(trace(f, x=np.array([[2, 2]])))
    # print(trace(f, mode = 'reverse', x=np.array([[2, 2]])))
