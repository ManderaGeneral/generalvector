
from math import sqrt

import random

from generallibrary.values import clamp


class Vec2:
    """
    Immutable vector2
    """
    def __init__(self, x, y=None):
        if isinstance(x, Vec2):
            y = x.y
            x = x.x
        elif y is None:
            y = x

        for key, value in {"x": x, "y": y}.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"{key} value {value} is not a number")

        self.x = x
        self.y = y

    def __str__(self):
        return f"Vec2[{self.x}, {self.y}]"

    def __eq__(self, other):
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, (int, float)):
            return self.x == other and self.y == other
        else:
            raise TypeError(f"{other} is not a Vec2 or number")

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vec2(self.x + other, self.y + other)
        else:
            raise TypeError(f"{other} is not a Vec2 or number")

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if isinstance(other, Vec2):
            raise NotImplementedError
        if isinstance(other, (int, float)):
            return Vec2(self.x * other, self.y * other)
        else:
            raise TypeError(f"{other} is not a number or vec2")

    def __truediv__(self, other):
        if isinstance(other, Vec2):
            raise NotImplementedError
        if isinstance(other, (int, float)):
            return Vec2(self.x / other, self.y / other)
        else:
            raise TypeError(f"{other} is not a number or vec2")

    def length(self):
        """
        Get the length of this vector using pythagorean theorem
        """
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        """
        Get this vector2 normalized by dividing each value by it's length
        """
        length = self.length()
        if length == 0:
            return Vec2(0)
        return self / length

    def round(self):
        """
        Get this vector2 with each value rounded
        """
        return Vec2(round(self.x), round(self.y))

    @staticmethod
    def random(value1, value2=None):
        """
        Get a vector2 with random values.

        :param float or Vec2 value1: Minimum value if value2 is specified too. Otherwise it's the maximum value and minimum becomes 0
        :param float or Vec2 value2: Optional maximum value
        """
        if value2 is None:
            value2 = Vec2(value1)
            value1 = Vec2(0)
        else:
            value2 = Vec2(value2)
            value1 = Vec2(value1)
        return Vec2(random.uniform(value1.x, value2.x), random.uniform(value1.y, value2.y))

    def clamp(self, minimum, maximum):
        """
        Get this vector2 clamped between two values.
        :param float or Vec2 minimum: Minimum value, floats are converted to Vec2
        :param float or Vec2 maximum: Maximum value, floats are converted to Vec2
        """
        minimum = Vec2(minimum)
        maximum = Vec2(maximum)
        return Vec2(clamp(self.x, minimum.x, maximum.x), clamp(self.y, minimum.y, maximum.y))

































