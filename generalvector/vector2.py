
from math import sqrt


class Vec2:
    """
    Immutable vector2
    """
    def __init__(self, x, y = None):
        if y is None:
            y = x

        if not isinstance(x, (int, float)):
            raise TypeError(f"x value {x} is not a number")
        if not isinstance(y, (int, float)):
            raise TypeError(f"y value {y} is not a number")

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
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        length = self.length()
        if length == 0:
            return Vec2(0)
        self.x = self.x / length
        self.y = self.y / length
        return self



































