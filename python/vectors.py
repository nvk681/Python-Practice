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

    def __radd__(self, other):
        """Return sum of two vectors, when vector is on thr right of the operation"""
        if len(self) != len(other):
            raise ValueError("Dimensions must be equal")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __neg__(self):
        """Return negative/reverse of the vector."""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __mul__(self, other):
        """Return multiplication of two vectors."""
        self_lenght = len(self)
        result = Vector(self_lenght)
        if type(other) is int:
            for j in range(self_lenght):
                result[j] = self[j] * other
        else:
            if self_lenght == len(other):
                for item in range(self_lenght):
                    result[item] = self[item] * other[item]
            else:
                raise ValueError("Dimensions must be equal")
        return result

    def __rmul__(self, other):
        """Return multiplication of two vectors, when vector is on thr right of the operation"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * other
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coordinates == other._coordinates

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

test_vector = Vector(3)
test_vector_other = Vector(3)
test_vector[0] = test_vector_other[2] = 4
test_vector[1] = test_vector_other[1] = 5
test_vector[2] = test_vector_other[0] = 6
test_vector = 3*test_vector
print(test_vector[0])
print(test_vector[1])
print(test_vector[2])
