Implementation
=================

Here, we describe the implementation details of ``Undefined`` on how we achieve the automatic differentiation.

5.1 Core Data Structure
-------------------------

To calculate the derivative in ``forward`` mode, we used the dual number approach. In the ```UDFunction``` class inside the ``UDFunction.py``, we overloaded the operators and accommdated the dual number (as the core data structure) approach following the formula below:

:math:`{z}_j = {v}_j + D_p v_j \epsilon`

where :math:`{v}_j` is the real part corresponding to the primal trace, and the :math:`{D_p v_j}` is the dual part corresponding to the tangent trace.

(Reverse mode)

5.2 Core Classes
------------------

We used ``numpy`` and ``math`` libraries to help with the math and used ``matplotlib`` and ``networkx`` libraries for plot the computational graph. 

**API.py:**

This class contains methods that can be called by the users. Such as ``trace()``.


+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Method                                 | Description                                                                                                  |
+========================================+==============================================================================================================+
| trace(lambda_function, mode='forward') | given a user defined function, calculate the derivative using auto differentiation. Default mode is forward. |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+

**UDFunction.py:**

This class wraps the core data structure in our library. Objects instanciated from this class are the most basic computing units in our library.

- Name Attributes:

+----------------+-----------------------------------------------------+
| Name Attribute | Description                                         |
+================+=====================================================+
| values         | values of a elementary function                     |
+----------------+-----------------------------------------------------+
| derivatives    | derivatives of a elementary function                |
+----------------+-----------------------------------------------------+
| shape          | a tuple that declares the shape of values attribute |
+----------------+-----------------------------------------------------+

- Methods:

**Calculator.py:**

This class contains util functions to perform elementary functions calculation on UDFunction such as $sin$, $sqrt$, $log$, $exp$, which cannot be implemented by overloaded functions in UDFunction.

+----------------------------+----------------------------------------------------------------+
| Method                     | Description                                                    |
+============================+================================================================+
| cos(UDFunction)            | calculate cos value of a UDFunction                            |
+----------------------------+----------------------------------------------------------------+
| sin(UDFunction)            | calculate sin value of a UDFunction                            |
+----------------------------+----------------------------------------------------------------+
| tan(UDFunction)            | is calculated tan by using sin(UDFunction) and cos(UDFunction) |
+----------------------------+----------------------------------------------------------------+
| sqrt(UDFunction)           | square root performed on UDFunction                            |
+----------------------------+----------------------------------------------------------------+
| exp(UDFunction)            | exponential performed on UDFunction                            |
+----------------------------+----------------------------------------------------------------+
| log(UDFunction, base=np.e) | logarithms of base: base. Default base is np.e                 |
+----------------------------+----------------------------------------------------------------+

**GraphGenerator.py:**


**Utils.py:**