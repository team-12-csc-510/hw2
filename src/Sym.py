import math

class Sym():
    """the symbol class"""

    def __init__(self, c=0, s="") -> None:
        self.n = 0
        self.at = c
        self.name = s
        self._has = dict()
    
    def add(self, v):
        if v != '?':
            self.n += 1
            if self._has.get(v) != None:
                self._has[v] = self._has.get(v) + 1
            else:
                self._has[v] = 1
    
    def mid(self, most=-1, mode=0):
        for key in self._has:
            if self._has[key] > most:
                mode = key
                most = self._has[key]
        return mode
    
    def div(self, e=0, fun=None):
        def fun(p):
            return p * math.log2(p)
        for key in self._has:
            e = e - fun(self._has[key]/self.n)
        return e
