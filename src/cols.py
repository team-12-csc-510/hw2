from num import Num
from sym import Sym
import re


class Cols:
    def __init__(self, names):
        self.names = names
        self.all = list()
        self.klass = None
        self.x = list()
        self.y = list()
        
        for c,s in zip(range(len(names), names)):
            if re.search('^[A-Z]', s):
                col = Num(c, s)
            else:
                col = Sym(c, s)
            self.all.append(col)

            if re.search(':$'):
                if re.search('\+$', s) or re.search('\-$', s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.find('!$', s):
                    self.klass = col
