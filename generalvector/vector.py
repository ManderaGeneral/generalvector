
from math import sqrt

import random

from generallibrary.values import clamp


class Vec:
    """
    Immutable vector2
    """
    def __init__(self, x, y=None, z=None):
        if isinstance(x, Vec):
            z = x.z
            y = x.y
            x = x.x
        elif z is None:
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

    def __repr__(self):
        return self.__str__()

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
            return Vec(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, (int, float)):
            return Vec(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError(f"{other} is not a number or vec")

    def __truediv__(self, other):
        if isinstance(other, Vec):
            return Vec(self.x / other.x, self.y / other.y, self.z / other.z)
        if isinstance(other, (int, float)):
            return Vec(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError(f"{other} is not a number or vec")

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z

    def length(self):
        """
        Get the length of this vector using pythagorean theorem
        """
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalized(self):
        """
        Get this vector normalized by dividing each value by it's length
        """
        length = self.length()
        if length == 0:
            return Vec(0)
        return self / length

    def round(self):
        """
        Get this vector with each value rounded
        """
        return Vec(round(self.x), round(self.y), round(self.z))

    @staticmethod
    def random(value1, value2=None):
        """
        Get a vector with random values.

        :param float or Vec value1: Minimum value if value2 is specified too. Otherwise it's the maximum value and minimum becomes 0
        :param float or Vec value2: Optional maximum value
        """
        if value2 is None:
            value2 = Vec(value1)
            value1 = Vec(0)
        else:
            value2 = Vec(value2)
            value1 = Vec(value1)
        return Vec(random.uniform(value1.x, value2.x), random.uniform(value1.y, value2.y), random.uniform(value1.z, value2.z))

    def min(self, minimum):
        """
        Get a new vector containing the minimum value for each value in the two vectors.

        :param float or Vec minimum: Minimum value, floats are converted to Vec
        """
        minimum = Vec(minimum)
        return Vec(min(self.x, minimum.x), min(self.y, minimum.y), min(self.z, minimum.z))

    def max(self, maximum):
        """
        Get a new vector containing the maximum value for each value in the two vectors.

        :param float or Vec maximum: Minimum value, floats are converted to Vec
        """
        maximum = Vec(maximum)
        return Vec(max(self.x, maximum.x), max(self.y, maximum.y), max(self.z, maximum.z))

    def clamp(self, minimum, maximum):
        """
        Get this vector clamped between two values as a new vector.

        :param float or Vec minimum: Minimum value, floats are converted to Vec
        :param float or Vec maximum: Maximum value, floats are converted to Vec
        """
        minimum = Vec(minimum)
        maximum = Vec(maximum)
        return Vec(clamp(self.x, minimum.x, maximum.x), clamp(self.y, minimum.y, maximum.y), clamp(self.z, minimum.z, maximum.z))

    def hex(self):
        """
        Get a hex based on each value. Rounded and clamped between 0 and 255.
        """
        rounded = self.round().clamp(0, 255)
        return f"#{'%02x' % rounded.x}{'%02x' % rounded.y}{'%02x' % rounded.z}"





















