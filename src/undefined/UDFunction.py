import numpy as np
import math

class UDFunction:
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
        """
        This is a decorator return rouded input self.val

        Returns:
            array: 2 decimal rounded input of self.value
        """
        if isinstance(self._val, float):
            return round(self._val, 2)
        elif isinstance(self._val, np.ndarray):
            return np.round(self._val, 2)
        else:
            return self._val

    @property
    def der(self):
        """
        This is a decorator return rouded input self.der

        Returns:
            array: 2 decimal rounded input of self.der
        """
        if isinstance(self._der, float):
            return round(self._der, 2)
        elif isinstance(self._der, np.ndarray):
            return np.round(self._der, 3)
        else:
            return self._der
            
    def __str__(self):
        return f"value: {self.val} \n" + f"derivative: {self.der}"

    def __add__(self, other):
        """
        This allows to do addition with UDFunction instances or scalar numbers, and calculate the value after taking the derivative. 
        TypeError will raise if none of the self or other are UDFunction instances. 

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
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __mul__(self, other):
        """
        This allows to do multification with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        TypeError will raise if none of the self or other are UDFunction instances. 

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
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

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
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

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
            raise TypeError("unsupported attribute type.")
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
        TypeError will raise if none of the self or other are UDFunction instances. 

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
            raise TypeError("unsupported attribute type.")
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
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)
        
    def __truediv__(self, other): 
        """
        This allows to do true division with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        TypeError will raise if none of the self or other are UDFunction instances. 

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
            raise TypeError("unsupported attribute type.")
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
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __floordiv__(self, other): # self // other
        """
        This allows to do floor division with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative.
        TypeError will raise if none of the self or other are UDFunction instances. 

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
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __rfloordiv__(self, other):
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
            raise TypeError("unsupported attribute type.")
        return UDFunction(new_val, new_der)

    def __pow__(self, other):
        """
        This allows to do "to the power" with UDFunction instances or scalar numbers, and calculate the value after taking the derivative.
        ** operator.

        Args:
            other (any): object to take power of.

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        if isinstance(other, UDFunction):
            if isinstance(self._val, (int, float)):
                new_val = self._val ** other._val
                if isinstance(other._val, np.ndarray):
                    new_der_1 = other._val * np.power(self._val, other._val - 1) * self._der
                    new_der_2 = math.log(self._val) * new_val * other._der
                    new_der = new_der_1 + new_der_2
                else:
                    new_der_1 = other._val * self._val ** (other._val - 1) * self._der
                    new_der_2 = math.log(self._val) * new_val * other._der
                    new_der = new_der_1 + new_der_2
            else: # self._val is of type ndarray
                if isinstance(other._val, np.ndarray):
                    if other._val.shape[0] != self._val.shape[0]:
                        raise ValueError(f"operands could not be broadcast together with shapes {other._val.shape} {self._val.shape}")
                    else:
                        new_val = self._val ** other._val
                        new_der_1 = other._val * np.power(self._val, other._val - 1) * self._der
                        new_der_2 = np.log(self._val) * new_val * other._der
                        new_der = new_der_1 + new_der_2
                else:
                    new_val = self._val ** other._val
                    new_der_1 = other._val * self._val ** (other._val - 1) * self._der
                    new_der_2 = np.log(self._val) * new_val * other._der
                    new_der = new_der_1 + new_der_2

        elif isinstance(other, (int, float, np.ndarray)):
            if isinstance(self._val, np.ndarray):
                new_val = np.power(self._val, other)
                new_der = other * np.power(self._val, other - 1) * self._der
            elif isinstance(self._val, (int, float)):
                new_val = self._val ** other
                new_der = other * self._val**(other - 1) * self._der
        
        return UDFunction(new_val, new_der)

    def __rpow__(self, other):
        """
        This allows to do "to the power" with UDFunction instances or scalar numbers, and calculate the value after taking the derivative.
        ** operator.
        TypeError will raise if none of the self or other are UDFunction instances. 

        Args:
            degree (numeric): object to take power of.

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        # other ^ self
        if isinstance(other, UDFunction):
            if isinstance(other._val, (int, float)):
                new_val = other._val ** self._val
                new_der_1 = np.log(other._val) * new_val * self._der
                new_der_2 = self._val * other._val ** (self._val - 1) * other._der
                new_der = new_der_1 + new_der_2
            else:
                if isinstance(self._val, np.ndarray):
                    if other._val.shape[0] != self._val.shape[0]:
                        raise ValueError(f"operands could not be broadcast together with shapes {other._val.shape} {self._val.shape}")
                    else:
                        new_val = other._val ** self._val
                        new_der_1 = np.log(other._val) * new_val * self._der
                        new_der_2 = self._val * np.power(other._val, (self._val - 1)) * other._der
                else:
                    new_val = other._val ** self._val
                    new_der_1 = np.log(other._val) * new_val * self._der
                    new_der_2 = self._val * other._val ** (self._val - 1) * other._der
        
        elif isinstance(other, (int, float, np.ndarray)):
            new_val = other ** self._val
            new_der_1 = math.log(other) * new_val * self._der
        
        else:
            raise TypeError("unsupported attribute type.")
        

        return UDFunction(new_val, new_der)


    def __eq__(self, other):
        """compare whether the two UDFunction objects have the same values.
        Return true if equal, and false otherwise.

        raise TypeError is other is not a UDFunction object.

        Args:
            other ([UDFunction])
        """
        if isinstance(other, UDFunction):
            return self.val == other.val
        elif isinstance(other, (int, float)):
            return self.val == other
        else:
            raise TypeError("Need a UDFunction object to compare")
    
    def __ne__(self, other):
        """compare whether the two UDFunction objects have different values.
        raise TypeError is other is not a UDFunction object.

        Args:
            other ([UDFunction])
        """
        if isinstance(other, UDFunction):
            return self.val != other.val
        elif isinstance(other, (int, float)):
            return self.val != other
        else:
            raise TypeError("Need a UDFunction object to compare")
    
    def __lt__(self, other):
        """overload the < operator
        raise TypeError is other is not a UDFunction object.

        Args:
            other ([UDFunction])
            
        """
        if isinstance(other, UDFunction):
            return self.val < other.val
        elif isinstance(other, (int, float)):
            return self.val < other
        else:
            raise TypeError("Need a UDFunction object to compare")
    
    def __gt__(self, other):
        """overload the > operator
        raise TypeError is other is not a UDFunction object.

        Args:
            other ([UDFunction])
            
        """
        if isinstance(other, UDFunction):
            return self.val > other.val
        elif isinstance(other, (int, float)):
            return self.val > other
        else:
            raise TypeError("Need a UDFunction object to compare")
    
    def __le__(self, other):
        """overload the > operator
        raise TypeError is other is not a UDFunction object.

        Args:
            other ([UDFunction])
            
        """
        if isinstance(other, UDFunction):
            return self.val <= other.val
        elif isinstance(other, (int, float)):
            return self.val <= other
        else:
            raise TypeError("Need a UDFunction object to compare")

    def __ge__(self, other):
        """overload the > operator
        raise TypeError is other is not a UDFunction object.

        Args:
            other ([UDFunction])
            
        """
        if isinstance(other, UDFunction):
            return self.val >= other.val
        elif isinstance(other, (int, float)):
            return self.val >= other
        else:
            raise TypeError("Need a UDFunction object to compare")

    def __round__(self, digit):
        '''overwrite the round method.
        '''
        return round(self.val, digit)

# if __name__ == "__main__":
#     alpha = 2.0
#     beta  = 3.0

#     a = np.array(2.5)
#     x = UDFunction(a)

#     b = 5.0
#     y = UDFunction(b)

#     f1 = -2*x + beta
#     f2 = -2*y + beta

#     # print(x >= y)
#     print(f1.val, f2.val)
#     print(f1 == -0.5)

