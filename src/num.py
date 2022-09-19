import math
import random

from src.utils import the


class Num:
    """This is a class that summarizes a stream of numbers
    :param int c : Stores the position of the column
    :param str s : Stores the name of the column
    :raises AnyError: If anything bad happens"""

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
        """ This method returns the element of instance
         variable _has

        This method returns the element of _has(sorted).
        The position of this element is computed according
        to the input argument p.

        :param int p : Stores the parameter used to compute
        returned elements position in _has.

        :param list t: Stored the instance variable _has
        in sorted form

        :returns: The element of _has at computed position
        :rtype: int
        :raises AnyError: If anything bad happens
        """
        p = math.floor((p * len(t)) + 0.5)
        return t[max(1, min(len(t), p))]

    def nums(self):
        """ This method returns the instance variable _has
        in sorted form

        :return: _has list in sorted form.
        :rtype: list
        :raises AnyError: If anything bad happens
        """
        if not self.isSorted:
            self.has.sort()

        self.isSorted = True
        return self.has

    def add(self, v):
        """ The method adds element passed to it
        in _has instance variable along with maintaining
        the correct value for the other instance variables
        of Num class i.e. lo and hi

        :param int v: input element to be added to _has
        :raises AnyError: If anything bad happens"""

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
        """ This method calculates the standard deviation
        from the data of the columns(i.e. _has in sorted form)

        :return: standard deviation of columns data
        :rtype: float
        :raises AnyError: If anything bad happens
        """
        a = self.nums()
        return (self.per(a, 0.9) - self.per(a, 0.1)) / 2.58

    def mid(self):
        """ This method calculates the median of the
         Column data by using _has(sorted state)

         :return: median value of the column data
         :rtype: flaot or Int depending upon the Column
         :raises AnyError: If anything bad happens"""

        return self.per(self.nums(), 0.5)
