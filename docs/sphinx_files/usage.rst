Usage 
========

3. How to use ``Undefined``
-----------------------------

This is the recommended usage. The users can interact with the package at their discretion. 

Download our wheel file (``undefined-1.0.0-py3-none-any.whl``) from the Github page. ``Link <https://github.com/cs107-undefined/cs107-FinalProject/releases/tag/v1.0.0>``
And save the file into your working directory.

Then, ``undefined`` provided esay installation by running this following command (Assuming your current directory is the working directory, which contains the wheel file):

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

3.1 Forward Model
^^^^^^^^^^^^^^^^^^^

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


3.2 Reverse Model
^^^^^^^^^^^^^^^^^^^

The ``trace`` function will also be able to calculate derivatives in reverse mode by specifying the ``mode`` parameters. Take the example below as a demo.

