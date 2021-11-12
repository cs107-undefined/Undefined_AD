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
        self.val = val
        self.der = der
        try:
            self.shape = val.shape
        except AttributeError:
            self.shape = 1
        self.left_child = None
        self.right_child = None

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
        try:
            new_val = self.val + other.val
            new_der = self.der + other.der
        except AttributeError:
            new_val = self.val + other
            new_der = self.der
        finally:
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
        try:
            new_val = self.val * other.val
            new_der = self.der * other.val + self.val * other.der
        except AttributeError:
            # TODO: check for vectors
            new_val = self.val * other
            new_der = self.der * other
        finally:
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
        try:
            new_val = self.val + other.val
            new_der = self.der + other.der
        except AttributeError:
            new_val = self.val + other
            new_der = self.der
        finally:
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
        try:
            new_val = self.val * other.val
            new_der = self.der * other.val + self.val * other.der
        except AttributeError:
            new_val = self.val * other
            new_der = self.der * other
        finally:
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
        try:
            new_val = self.val - other.val
            new_der = self.der - other.der
        except AttributeError:
            new_val = self.val - other
            new_der = self.der
        finally:
            return UDFunction(new_val, new_der)

    def __rsub__(self, other):
        """
        This is called when int/float or UDFunction instances - an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to subtract with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        try:
            new_val = other.val - self.val
            new_der = other.der - self.der
        except AttributeError:
            new_val = other - self.val
            new_der = - self.der
        finally:
            return UDFunction(new_val, new_der)
        
    def __truediv__(self, other): # bc - ad / c**2
        """
        This allows to do true division with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative. 
        AttributeError will raise if none of the self or other are UDFunction instances. 


        Args:
            other (UDFunction or numeric): object to (true) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        try:
            new_val = self.val / other.val
            new_der = (self.der * other.val - self.val * other.der) / (other.val * other.val)
        except AttributeError:
            new_val = self.val / other
            new_der = self.der / other
        finally:
            return UDFunction(new_val, new_der)

    def __rtruediv__(self, other):
        """
        This is called when int/float or UDFunction instances / (divide) an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to (true) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        try:
            new_val = other.val / self.val
            new_der = (self.val * other.der - self.der * other.val) / (self.val * self.val)
        except AttributeError:
            new_val = other / self.val
            new_der = - 1 * other * self.der / (self.val * self.val)
        finally:
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
        try:
            new_val = self.val // other.val
            new_der = (self.der * other.val - self.val * other.der) // (other.val * other.val)
        except AttributeError:
            new_val = self.val // other
            new_der = self.der // other
        finally:
            return UDFunction(new_val, new_der)

    def __rfloordiv__(self, other): # other // self
        """
        This is called when int/float or UDFunction instances // (floor divide) an instance of Variable class.

        Args:
            other (UDFunction or numeric): object to (floor) divide with

        Returns:
            UDFunction: a new object with new_val and new_der
        """
        try:
            new_val = other.val // self.val
            new_der = (self.val * other.der - self.der * other.val) // (self.val * self.val)
        except AttributeError:
            new_val = other // self.val
            new_der = - 1 * other * self.der / (self.val * self.val)
        finally:
            return UDFunction(new_val, new_der)

    def __pow__(self, degree):
        """
        This allows to do "to the power" with UDFunction instances or scalar numbers, , and calculate the value after taking the derivative.
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
    y = 4*x**3
    print(y)



