# Dunder Methods are the methods that are used to define the behavior of the class.
# There are many dunder methods in Python

# OBJECT INITIALIZATION AND REPRESENTATION
# __init__ is a dunder method that is used to initialize the object.
# __new__ is a dunder method that is used to create a new instance of the object.
# __del__ is a dunder method that is used to destroy the object.
# __str__ is a dunder method that is used to return the string representation of the object.
# __repr__ is a dunder method that is used to return the official string representation of the object.
# __format__ is a dunder method that is used to format the object.

# COMPARISON OPERATORS
# __eq__ is a dunder method that is used to check equality between two objects.
# __ne__ is a dunder method that is used to check inequality between two objects.
# __lt__ is a dunder method that is used to check if one object is less than another.
# __le__ is a dunder method that is used to check if one object is less than or equal to another.
# __gt__ is a dunder method that is used to check if one object is greater than another.
# __ge__ is a dunder method that is used to check if one object is greater than or equal to another.

# ARITHMETIC OPERATORS
# __add__ is a dunder method that is used to add two objects.
# __sub__ is a dunder method that is used to subtract two objects.
# __mul__ is a dunder method that is used to multiply two objects.
# __truediv__ is a dunder method that is used to divide two objects (true division).
# __floordiv__ is a dunder method that is used to divide two objects (floor division).
# __mod__ is a dunder method that is used to get the modulo of two objects.
# __pow__ is a dunder method that is used to raise one object to the power of another.
# __divmod__ is a dunder method that is used to get quotient and remainder of two objects.

# REFLECTED ARITHMETIC OPERATORS (Right-hand side)
# __radd__ is a dunder method that is used for reflected addition.
# __rsub__ is a dunder method that is used for reflected subtraction.
# __rmul__ is a dunder method that is used for reflected multiplication.
# __rtruediv__ is a dunder method that is used for reflected true division.
# __rfloordiv__ is a dunder method that is used for reflected floor division.
# __rmod__ is a dunder method that is used for reflected modulo.
# __rpow__ is a dunder method that is used for reflected power.
# __rdivmod__ is a dunder method that is used for reflected divmod.

# AUGMENTED ASSIGNMENT OPERATORS
# __iadd__ is a dunder method that is used for in-place addition.
# __isub__ is a dunder method that is used for in-place subtraction.
# __imul__ is a dunder method that is used for in-place multiplication.
# __itruediv__ is a dunder method that is used for in-place true division.
# __ifloordiv__ is a dunder method that is used for in-place floor division.
# __imod__ is a dunder method that is used for in-place modulo.
# __ipow__ is a dunder method that is used for in-place power.

# UNARY OPERATORS
# __neg__ is a dunder method that is used to negate an object.
# __pos__ is a dunder method that is used to get the positive value of an object.
# __abs__ is a dunder method that is used to get the absolute value of an object.
# __invert__ is a dunder method that is used to invert (bitwise NOT) an object.

# BITWISE OPERATORS
# __and__ is a dunder method that is used for bitwise AND operation.
# __or__ is a dunder method that is used for bitwise OR operation.
# __xor__ is a dunder method that is used for bitwise XOR operation.
# __lshift__ is a dunder method that is used for left shift operation.
# __rshift__ is a dunder method that is used for right shift operation.
# __rand__ is a dunder method that is used for reflected bitwise AND.
# __ror__ is a dunder method that is used for reflected bitwise OR.
# __rxor__ is a dunder method that is used for reflected bitwise XOR.
# __rlshift__ is a dunder method that is used for reflected left shift.
# __rrshift__ is a dunder method that is used for reflected right shift.
# __iand__ is a dunder method that is used for in-place bitwise AND.
# __ior__ is a dunder method that is used for in-place bitwise OR.
# __ixor__ is a dunder method that is used for in-place bitwise XOR.
# __ilshift__ is a dunder method that is used for in-place left shift.
# __irshift__ is a dunder method that is used for in-place right shift.

# TYPE CONVERSION
# __int__ is a dunder method that is used to convert an object to an integer.
# __float__ is a dunder method that is used to convert an object to a float.
# __complex__ is a dunder method that is used to convert an object to a complex number.
# __bool__ is a dunder method that is used to convert an object to a boolean.
# __bytes__ is a dunder method that is used to convert an object to bytes.
# __hash__ is a dunder method that is used to get the hash value of an object.

# CONTAINER AND SEQUENCE METHODS
# __len__ is a dunder method that is used to get the length of a container.
# __getitem__ is a dunder method that is used to get an item from a container.
# __setitem__ is a dunder method that is used to set an item in a container.
# __delitem__ is a dunder method that is used to delete an item from a container.
# __contains__ is a dunder method that is used to check if an item is in a container.
# __iter__ is a dunder method that is used to create an iterator for a container.
# __next__ is a dunder method that is used to get the next item in an iterator.
# __reversed__ is a dunder method that is used to reverse the order of items in a container.

# CALLABLE OBJECTS
# __call__ is a dunder method that is used to make an object callable like a function.

# CONTEXT MANAGER METHODS
# __enter__ is a dunder method that is used to enter a context (with statement).
# __exit__ is a dunder method that is used to exit a context (with statement).

# ATTRIBUTE ACCESS
# __getattr__ is a dunder method that is used to get an attribute that doesn't exist.
# __setattr__ is a dunder method that is used to set an attribute of an object.
# __delattr__ is a dunder method that is used to delete an attribute of an object.
# __getattribute__ is a dunder method that is used to intercept all attribute access.

# DESCRIPTOR METHODS
# __get__ is a dunder method that is used to get the value of a descriptor.
# __set__ is a dunder method that is used to set the value of a descriptor.
# __delete__ is a dunder method that is used to delete the value of a descriptor.
# __set_name__ is a dunder method that is used to store the name of the descriptor.

# COPY METHODS
# __copy__ is a dunder method that is used to create a shallow copy of an object.
# __deepcopy__ is a dunder method that is used to create a deep copy of an object.

# OTHER METHODS
# __sizeof__ is a dunder method that is used to get the size of an object in memory.
# __reduce__ is a dunder method that is used for pickling an object.
# __reduce_ex__ is a dunder method that is used for pickling an object with protocol version.
# __doc__ is a dunder attribute that is used to store the documentation string.
# __class__ is a dunder attribute that is used to get the class of an object.
# __dict__ is a dunder attribute that is used to store the namespace of an object as a dictionary.


class Nums:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        self.other = other
        return self.num + other.num
    
    def __sub__(self, other):
        self.other = other
        return self.num - other.num

    def __mul__(self, other):
        self.other = other
        return self.num * other.num
    
    def __truediv__(self, other):
        self.other = other
        return self.num / other.num

num1 = Nums(10)
num2 = Nums(12)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
