import math
import random


class Num:
    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self.has = []
        self.lo = float("inf")
        self.hi = float("-inf")
        self.isSorted = True
        self.w = -1 if "-$" in s else 1

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
            if len(self.has):
                pos = 1 + len(self.has)
            elif self.n > 512:
                pos = random.randint(0, len(self.has))

            if pos:
                self.isSorted = False

            self.has[pos] = int(v)

    def per(self, t, p=0.5):
        p = math.floor((p * len(t)) + 0.5)
        return t[max(1, min(len(t), p))]

    def div(self):
        a = self.nums()
        return (self.per(a, 0.9) - self.per(a, 0.1)) / 2.58

    def mid(self):
        return self.per(self.nums(), 0.5)
