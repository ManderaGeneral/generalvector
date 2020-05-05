
from math import sqrt

class Vec:
    """
    Immutable vector2
    """
    def __init__(self, x, y=None, z=None):
        if z is None:
            if y is None:
                y = x
                z = x
            else:
                raise AttributeError(f"X and Y were defined but not Z, either only X should be defined or all three")

        for key, value in {"x": x, "y": y, "z": z}.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"{key} value {value} is not a number")

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vec[{self.x}, {self.y}, {self.z}]"

    def __eq__(self, other):
        if isinstance(other, Vec):
            return self.x == other.x and self.y == other.y and self.z == other.z
        elif isinstance(other, (int, float)):
            return self.x == other and self.y == other and self.z == other
        else:
            raise TypeError(f"{other} is not a Vec or number")

    def __add__(self, other):
        if isinstance(other, Vec):
            return Vec(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vec(self.x + other, self.y + other, self.z + other)
        else:
            raise TypeError(f"{other} is not a Vec or number")

    def __neg__(self):
        return Vec(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if isinstance(other, Vec):
            raise NotImplementedError
        if isinstance(other, (int, float)):
            return Vec(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError(f"{other} is not a number or vec")

    def __truediv__(self, other):
        if isinstance(other, Vec):
            raise NotImplementedError
        if isinstance(other, (int, float)):
            return Vec(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError(f"{other} is not a number or vec")

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalized(self):
        length = self.length()
        if length == 0:
            return Vec(0)
        return self / length
