import re

import num
import sym


class Cols:
    def __init__(self, names):
        self.names = names
        self.all = list()
        self.klass = None
        self.x = list()
        self.y = list()

        for c, s in enumerate(names):
            if re.match("^[A-Z]*", s):
                col = num.Num(c, s)
            else:
                col = sym.Sym(c, s)
            self.all.append(col)

            if re.match(".*:$", s):
                if re.match(r".*\+$", s) or re.match(r".*\-$", s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.match("!$", s):
                    self.klass = col
