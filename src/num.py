import math
import random

from src.utils import the

"""Add up two integer numbers.

This function simply wraps the ``+`` operator, and does not
do anything interesting, except for illustrating what
the docstring of a very simple function looks like.

:param int num1: First number to add.
:param int num2: Second number to add.
:returns:  The sum of ``num1`` and ``num2``.
:rtype: int
:raises AnyError: If anything bad happens.
"""


class Num:
    """This is a class that summarizes a stream of numbers
    :param int c : Stores the position of the column
    :param str s : Stores the name of the column"""

    def __init__(self, c=0, s=""):
        """Constructor method"""

        self.n = 0
        self.at = c
        self.name = s
        self.has = []
        self.lo = float("inf")
        self.hi = float("-inf")
        self.isSorted = True
        self.w = -1 if (len(s) > 0 and s[-1] == "-") else 1

    @staticmethod
    def per(t, p=0.5):
        p = math.floor((p * len(t)) + 0.5)
        return t[max(1, min(len(t), p))]

    def nums(self):
        if not self.isSorted:
            self.has.sort()

        self.isSorted = True
        return self.has

    def add(self, v):

        if not v == "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            pos = None
            if len(self.has) < the["nums"]:
                pos = 1 + len(self.has)
                self.has.append(int(v))
            elif self.n > the["nums"]:
                pos = random.randint(0, len(self.has))
                self.has[pos - 1] = int(v)

            if pos:
                self.isSorted = False

    def div(self):
        a = self.nums()
        return (self.per(a, 0.9) - self.per(a, 0.1)) / 2.58

    def mid(self):
        return self.per(self.nums(), 0.5)
