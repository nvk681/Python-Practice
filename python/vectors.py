"""This is the implementation of vectors"""
class Vector:
    """A class to use to make use of vectors"""
    def __init__(self, dimensions):
        """initilize the vectors and decide on the dimension"""
        if not int(dimensions): raise ValueError('invalid value for dimensions of the vector')
        self._coordinates = [0]*dimensions

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coordinates)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coordinates[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coordinates[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError("Dimensions must be equal")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coordinates == other._coordinates

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
