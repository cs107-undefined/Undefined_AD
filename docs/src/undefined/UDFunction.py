# TODO: add summary in docstring
class UDFunction:
    def __init__(self, val, der=1):
        """[summary]

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

    def __add__(self, other):
        """[summary]

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

    def __mul__(self, other):
        """[summary]

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

    def __radd__(self, other):
        """[summary]

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

    def __rmul__(self, other):
        """[summary]

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
        """[summary]

        Returns:
            UDFunction: object with neg value
        """
        return -1 * self

