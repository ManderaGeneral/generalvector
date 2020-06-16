
from generallibrary.values import confineTo


class General:
    """
    General class that Vec2 and Vec inherits for shared functions, end-goal is that all methods are moved here to make package dry
    """
    def __init__(self, *axis):
        for n in axis:
            if not isinstance(n, (int, float)):
                raise TypeError(f"{n} is not a number")

        self.axis = axis

    def __getitem__(self, item):
        return self.axis[item]

    def sanitize(self, ints=False, positive=False, positiveOrZero=False, negative=False, negativeOrZero=False, minimum=None, maximum=None):
        """
        Sanitize this vector with a bunch of optional flags

        :param generalvector.Vec or generalvector.Vec2 self:
        :param ints:
        :param positive:
        :param positiveOrZero:
        :param negative:
        :param negativeOrZero:
        :param generalvector.Vec or generalvector.Vec2 minimum:
        :param generalvector.Vec or generalvector.Vec2 maximum:
        :return: self
        """
        if ints and self != self.round():
            raise ValueError(f"{self} failed 'ints' sanitizing")

        if positive and not self > 0:
            raise ValueError(f"{self} failed 'positive' sanitizing")
        if positiveOrZero and not self >= 0:
            raise ValueError(f"{self} failed 'positiveOrZero' sanitizing")

        if negative and not self < 0:
            raise ValueError(f"{self} failed 'negative' sanitizing")
        if negativeOrZero and not self <= 0:
            raise ValueError(f"{self} failed 'negativeOrZero' sanitizing")

        if minimum and not self >= minimum:
            raise ValueError(f"{self} failed 'minimum' sanitizing")
        if maximum and not self <= maximum:
            raise ValueError(f"{self} failed 'maximum' sanitizing")

        return self

    def confineTo(self, pos, size, margin=0):
        """
        Confine this vector to an area, but unlike clamp it subtracts axis * n to create an 'infinite' area effect.

        :param generalvector.Vec or generalvector.Vec2 self:
        :param generalvector.Vec or generalvector.Vec2 pos: Lowest point of area
        :param generalvector.Vec or generalvector.Vec2 size: Size of area, has to be positive
        :param float margin: Margin of confinement
        """
        pos = self.__class__(pos)
        size = self.__class__(size).sanitize(positive=True)
        maximum = pos + size

        return self.__class__(*[confineTo(axis, pos[i], maximum[i], margin) for i, axis in enumerate(self.axis)])














