import numpy as np
import copy
# TODO: add summary in docstring
class UDFunction:
    #constructor that sets the value of the function and derivative
    def __init__(self, val, der=1):
        """
        This class is where we overload all the operators, which will be used to calculate the derivatives.

        Args:
            val (numeric or numpy ndarray): value of function
            der (int, optional): derivative of function. Defaults to 1.
        """
        self._val = val
        self._der = der
        if hasattr(self._val, 'shape'):
            self._shape = self._val.shape
        else:
            self._shape = 1
        self._left_child = None
        self._right_child = None

    @property
    def val(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if isinstance(self._val, float):
            return round(self._val, 2)
        elif isinstance(self._val, np.ndarray):
            return np.round(self._val, 2)
        else:
            return self._val

    @property
    def der(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if isinstance(self._der, float):
            return round(self._der, 2)
        elif isinstance(self._der, np.ndarray):
            return np.round(self._der, 3)
        else:
            return self._der
            
    def __str__(self):
        return f"value: {self.val} \n" + f"derivative: {self.der}"

    #overloading add method
    def __add__(self, other):
        """
        This allows to do addition with UDFunction instances or scalar numbers, and calculate the value after taking the derivative. 
        AttributeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to add with
        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val + other._val
            new_der = self._der + other._der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val + other
            new_der = self._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    #overloading multiplication method
    def __mul__(self, other):
        """
        This allows to do multification with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        AttributeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to multiply with
        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val * other._val
            new_der = self._der * other._val + self._val * other._der
        elif isinstance(other, (int, float, np.ndarray)):
            # TODO: check for vectors
            new_val = self._val * other
            new_der = self._der * other
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    #overloading radd method
    def __radd__(self, other):
        """
        This is called when int/float or UDFunction instances + an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to add with
        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val + other._val
            new_der = self._der + other._der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val + other
            new_der = self._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    #overloading rmul method
    def __rmul__(self, other):
        """
        This is called when int/float or UDFunction instances * an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to multiply with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val * other._val
            new_der = self._der * other._val + self._val * other._der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val * other
            new_der = self._der * other
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __neg__(self):
        """
        This allows to negate UDFunction instances itself.

        Returns:
            UDFunction: object with neg value
        """
        return -1 * self

    def __sub__(self, other):
        """
        This allows to do subtraction with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        AttributeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to subtract with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val - other._val
            new_der = self._der - other._der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val - other
            new_der = self._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __rsub__(self, other):
        """
        This is called when int/float or UDFunction instances - an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to subtract with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = other._val - self._val
            new_der = other._der - self._der
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other - self._val
            new_der = - self._der
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)
        
    def __truediv__(self, other): 
        """
        This allows to do true division with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        AttributeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to (true) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val / other._val
            new_der = (self._der * other._val - self._val * other._der) / (other._val * other._val)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val / other
            new_der = self._der / other
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __rtruediv__(self, other):
        """
        This is called when int/float or UDFunction instances / (divide) an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to (true) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = other._val / self._val
            new_der = (self._val * other._der - self._der * other._val) / (self._val * self._val)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other / self._val
            new_der = - 1 * other * self._der / (self._val * self._val)
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __floordiv__(self, other): # self // other
        """
        This allows to do floor division with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative.
        AttributeError will raise if none of the self or other are UDFunction instances. 

        Args:
            other (UDFunction or numeric): object to (floor) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = self._val // other._val
            new_der = (self._der * other._val - self._val * other._der) // (other._val * other._val)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = self._val // other
            new_der = self._der // other
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __rfloordiv__(self, other): # other // self
        """
        This is called when int/float or UDFunction instances // (floor divide) an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to (floor) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            new_val = other._val // self._val
            new_der = (self._val * other._der - self._der * other._val) // (self._val * self._val)
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other // self._val
            new_der = - 1 * other * self._der // (self._val * self._val)
        else:
            raise AttributeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __pow__(self, degree):
        """
        This allows to do "to the power" with UDFunction instances or scalar numbers, and calculate the value after taking the derivative.
        ** operator.
        AttributeError will raise if none of the self or other are UDFunction instances. 

        Args:
            degree (numeric): object to take power of.

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        udf = self
        for d in range(degree - 1):
            udf = udf * self
        return udf

if __name__ == "__main__":
    a = 2.0
    x = UDFunction(a)
    y = 1//x
    print(y)



