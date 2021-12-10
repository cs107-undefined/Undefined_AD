Usage 
========

3. How to use ``Undefined``
-----------------------------

This is the recommended usage. The users can interact with the package at their discretion. 

Download our wheel file (``undefined-1.0.0-py3-none-any.whl``) from the Github page. ``Link <https://github.com/cs107-undefined/cs107-FinalProject/releases/tag/v1.0.0>``
And save the file into your working directory.

Then, ``undefined`` provided easy installation by running this following command (Assuming your current directory is the working directory, which contains the wheel file):

.. code-block:: bash
    :linenos:
    
    pip install undefined-1.0.0-py3-none-any.whl

Users should import the package by the following in their Python script:

.. code-block:: 
    :linenos:

    from undefined.API import trace

Also, if the users are planning to use the exponential and trig functions, they should do:

.. code-block:: 
    :linenos:

    from undefined.Calculator import sin, cos, tan, exp, log, sqrt

**Note:** Our package will not work with the functions in other libraries, such as np.sin. Please use our customized functions.

Once imported successfully, users can calculate the derivative of a given function by using the syntax from the section below. 

Here, we will demo the R -> R cases in the 3.1 and 3.2 to illustrate the basic usage of ``Undefined``. In 3.3, we will demo the higher order inputs and outputs.

3.1 Forward Model Demo
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``trace`` function will calculate the derivative, which will intake a user defined function using ``lambda``, the mode (default is **forward** mode), and associated values. The ``trace`` function will return the derivatives of the function.

Here, we showed a demo with :math:`\mathbb{R}`` -> :math:`\mathbb{R}`:

***Note:***
In our design, the users do not need to instantiate an ``undefined`` object. They can just develop the function using Python build-in ``lambda``, and we will not accept other types of input functions.

.. code-block:: 
    :linenos:

    # R -> R implementation
    # assuming undefined has been installed. 

    from undefined.API import trace
    from undefined.Calculator import sin, cos, exp, log, sqrt

    # define the user input function using lambda
    f1 = lambda x, y: sqrt(exp(x*y)) + 1

    # calculate the derivative when x = 2 and y = 1 for the input function
    output_f1 = trace(f1, x = 2, y = 1)

    # print out the forward mode derivative
    print(output_f1)

    # output summary results for f1
    >>>value: 3.72
    >>>derivative: [1.359 2.718]

The users can also access the Jacobian results by using the ``val`` for the function value and ``der`` for the function's derivative value(s).

.. code-block:: 
    :linenos:

    # use val to access the function value
    print(output_f1.val)
    >>>3.72

    # use der to access the derivative value of the function
    >>>array([1.359, 2.718])

The ``trace`` function can also handle multiple dimensional calculation. Assume we need to calculate :math:`\mathbb{R}^m`` -> :math:`\mathbb{R}`, we will input the values for :math:`{x}` and :math:`{y}`. 

.. code-block:: 
    :linenos:

    from undefined.API import trace
    from undefined.Calculator import sqrt

    # user defined function
    f = lambda x, y: 2*x + sqrt(y)

    # call the trace function in undefined, and provide input x = 1 and y = 4
    print(trace(f, x = 2, y = 4))

    # the function will return the 1st derivative when x = 1 and y = 4.
    >>> value: 6.0 
    >>> derivative: [2.   0.25]

Our function will handle other multiple dimensional calculations, including :math:`\mathbb{R}`` -> :math:`\mathbb{R}^n`, :math:`\mathbb{R}^m`` -> :math:`\mathbb{R}^n`. The difference will be the number of input values. 


3.2 Reverse Model Demo
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``trace`` function will also be able to calculate derivatives in reverse mode by specifying the ``mode`` parameters. Take the example below as a demo.

.. code-block:: 
    :linenos:

    from undefined.API import trace
    from undefined.Calculator import sqrt, exp, sin

    # user defined function
    f = lambda x: sqrt(exp(sin(x)))

    # call the trace function in reverse mode, and provide input x = 2
    print(trace(f, mode = "reverse", x = 2))

    # the function will return the function value and the derivative when x = 2. 
    >>> (1.58, [-0.328])

In the example, we can see that our reverse mode can output the function and the derivative values rounded in 3 decimal places, if applicable. 
Another feature we developed in our reverse mode is to output the computational graph.

First, let's look at the graph structure we generated. I will use the same function as example.

.. code-block:: 
    :linenos:

    from undefined.API import trace
    from undefined.Calculator import sqrt, exp, sin

    # user defined function
    f = lambda x: sqrt(exp(sin(x)))

    # call the trace function in reverse mode, and provide input x = 2
    # set plot equals to True so that it will generate the computational graph
    print(trace(f, mode = "reverse", plot = True, x = 2))

    # Output: the function will return the function value and the derivative when x = 2. 
    Computational Graph (1.58, UDPrimitive.SQRT)
    |
    |<-(parent)-Computational Graph (2.48, UDPrimitive.EXP)
    |      |
    |      |<-(parent)-Computational Graph (0.91, UDPrimitive.SIN)
    |      |      |
    |      |      |<-(parent)-Computational Graph (2, UDPrimitive.VAR)
    (1.58, [-0.328])

Moreover, the reverse mode will auto save the plot to your current working directory. The associated graph generated from the function above is shown below.

.. image:: ../resources/reverse_mode_example1.png
    :width: 600
    :alt: reverse_mode_example1

From the graph above, we can see that the graph correctly reflects to computation from the VAR to SIN to EXP and to SQRT. 

Undefined, like the name suggested, has unlimited boundary. Let's try a complicated example:


.. code-block:: 
    :linenos:

    from undefined.API import trace
    from undefined.Calculator import sqrt, exp, sin

    # user defined function
    f = lambda x, y: exp(1-6*x) * tan(4*x + 2*y) + x**2*y

    # call the trace function in reverse mode, and provide input x = 2
    # set plot equals to True so that it will generate the computational graph
    print(trace(f, mode = "reverse", plot = True, x = 1, y = 2))

    # Output: the function will return the function value and the derivative when x = 1, y = 2.
    Computational Graph (1.95, UDPrimitive.ADD)
    |
    |<-(parent)-Computational Graph (-0.05, UDPrimitive.MUL)
    |      |
    |      |<-(parent)-Computational Graph (0.01, UDPrimitive.EXP)
    |      |      |
    |      |      |<-(parent)-Computational Graph (-5, UDPrimitive.RSUB)
    |      |      |      |
    |      |      |      |<-(parent)-Computational Graph (6, UDPrimitive.RMUL)
    |      |      |      |      |
    |      |      |      |      |<-(parent)-Computational Graph (1, UDPrimitive.VAR)
    |      |
    |      |<-(parent)-Computational Graph (-6.8, UDPrimitive.TAN)
    |      |      |
    |      |      |<-(parent)-Computational Graph (8, UDPrimitive.ADD)
    |      |      |      |
    |      |      |      |<-(parent)-Computational Graph (4, UDPrimitive.RMUL)
    |      |      |      |      |
    |      |      |      |      |<-(parent)-Computational Graph (1, UDPrimitive.VAR)
    |      |      |      |
    |      |      |      |<-(parent)-Computational Graph (4, UDPrimitive.RMUL)
    |      |      |      |      |
    |      |      |      |      |<-(parent)-Computational Graph (2, UDPrimitive.VAR)
    |
    |<-(parent)-Computational Graph (2, UDPrimitive.MUL)
    |      |
    |      |<-(parent)-Computational Graph (1, UDPrimitive.POW)
    |      |      |
    |      |      |<-(parent)-Computational Graph (1, UDPrimitive.VAR)
    |      |
    |      |<-(parent)-Computational Graph (2, UDPrimitive.VAR)
    (1.95, [5.548, 1.637])

.. image:: ../resources/reverse_mode_example2.png
    :width: 600
    :alt: reverse_mode_example2

From the results above, we can see that that undefined package can handle complicated functions. However, we do have some limitations. We will discuss that in the section below. 
**Of note**: as we used the ``networkx`` library to achieve the graph, the graph will be different even if you run the same code twice or many different times.

3.3 Multiple Vectors Inputs and Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here, I will use the forward mode to demo how to use ``Undefined`` using multiple inputs. The reverse mode would result the same. 

:math:`\mathbb{R}^m -> \mathbb{R}`

This means that we will need to calculate for multiple x input for the same function. We designed our function to use ``numpy.array`` to take multiple inputs. 
See the example below on how to pass in multiple inputs. Note: you will need to use the **double bracket**. 


.. code-block:: 
    :linenos:

    from undefined.API import trace
    from undefined.Calculator import sqrt
    import numpy as np

    # user defined function
    f = lambda x: 2*x + sqrt(x)

    # call the trace function in undefined, and provide input x = 1 and 2.
    print(trace(f, x = np.array([[1,2]]))

    # Output
    (array([[3.  , 5.41]]), array([[2.5  , 2.354]]))

In the output above, the first array shows the function values after plugin the x values. The second array is the derivative values. 

:math:`\mathbb{R} -> \mathbb{R}^n`

This means that we will need to calculate for a single x input for the multiple functions. In this case, we designed our function to use a list to take multiple functions as inputs. 
See the example below on how to pass in multiple functions as input.

.. code-block:: 
    :linenos:

    from undefined.API import trace
    from undefined.Calculator import sqrt, exp, sin

    # user defined functions
    f1 = lambda x: sqrt(exp(sin(x)))
    f2 = lambda x: 2*x + sqrt(x)

    # call the trace function in undefined, and provide input functions f1 and f2, and the x value.
    print(trace([f1, f2], x = 2))

    # Output
    (array([1.58, 5.41]), array([-0.328,  2.354]))

In the output above, the first array represents the function values and the second array represents the derivative values. I bet you have noticed already that the two functions I used here are the same ones I used in the previous demo. Check out the values with the previous demo and you will see the values are the same. 

:math:`\mathbb{R}^m -> \mathbb{R}^n`

This means that we will need to calculate for multiple x inputs for the multiple functions. It is the combination of both conditions above. 
See the example below on how to pass in multiple functions and values as input.

.. code-block:: 
    :linenos:

    from undefined.API import trace
    from undefined.Calculator import sqrt, exp, sin

    # user defined functions
    f1 = lambda x: sqrt(exp(sin(x)))
    f2 = lambda x: 2*x + sqrt(x)

    # call the trace function in undefined, and provide input functions f1 and f2, and the x values.
    print(trace([f1, f2], x = np.array([[1, 2]])))

    # Output
    (array([[[1.52, 1.58]], [[3.  , 5.41]]]), array([[[ 0.411, -0.328]], [[ 2.5  ,  2.354]]]))

In the output above, the first array represents the function values and the second array represents the derivative values.
The first 2D list in the first tuple is the function value from the first function, and the first 2D list in the second tuple is the derivative from the first section. The second 2D list corresponding to the second function from the input. 

**Additional Demo**
To maximize the flexibility for the users, our function can take a mixture as input, meaning the number of input values for variables do not need to be the same. 
For example, in the :math:`\mathbb{R}^m -> \mathbb{R}^n`, the users could input a function of x and y and give 2 values for x and 1 value for y. Our function would still work. See the example below:

.. code-block:: 
    :linenos:

    from undefined.API import trace
    from undefined.Calculator import sqrt, exp, sin

    # user defined functions
    f3 = lambda x, y: x**2 + 2**y
    f4 = lambda x, y: 2*x - 2/y

    # call the trace function in undefined, and provide input functions f3 and f4, and the x and y values.
    print(trace([f3, f4], x = np.array([[1,2]]), y = 4)

    # Output
    (array([[[17. , 20. ]], [[ 1.5,  3.5]]]), array([[[ 2.,  4.], [11.09 , 11.09 ]], [[ 2.,  2.], [ 0.125,  0.125]]]))

When there are multiple input variables, in this case x and y, our program will order the results in the same order that it's been passed into the function. 
In this case, the first item in the first list in the first array represents the function value from the f3 when x = 1 y = 4, and the second item is from f3 when x = 2, y = 4, etc. 
The second array represents the derivative value. The first list represent the derivative value of f3 when x = 1, y = 4 with respect to x and y, 
and the second list is the derivative value of f4 when x = 1, y = 4 with respect to x and y. The last two lists represent when x = 2, y = 4 for derivative values for f3 and f4 in that order.


**Attention**

Although our package is smart and can handle many different scenarios and cases, there are exceptions. 

- We cannot unpack more number of input variables than the user defined functions have. For example, if the user defined function is the following:

.. code-block:: 
    :linenos:

    f = lambda x, y: x + exp(x)

Then the user passed additional variable into the ``trace`` function:

.. code-block:: 
    :linenos:

    trace(f, mode = "reverse", x = 2, y = 3)

In this case, we will not throw an error, but no guarantee the results are legit because the inputs does not make sense. So, please double check!

- If you are using the ``forward`` mode, set the ``plot = True`` will not work as we do not store the intermediate values in the forward mode. 

- We have tested our package with extreme values and edge cases to increase the robustness of our package. However, there is chance that we did not cover every case. So please do not be surprised if your goal is the break the package and see an error.




3.4 Debugging
^^^^^^^^^^^^^^^

Since the forward model does not store the intermediate values, we recommend the users to use reverse mode for their debugging propose. We offer the graph structure and the computational graph as output to facilitate with the process. 
Moreover, we also provide the source codes for the users to examine our workflow. Please refer to the **Source Code Details** section.
Since our design is encapsulated and modularized, it is easy for the users to spot the possible error(s).
