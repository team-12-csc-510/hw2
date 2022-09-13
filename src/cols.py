import num
import sym
import re

class Cols():
    
    def __init__(self, names):
        self.names = names
        self.all = list()
        self.klass = None
        self.x = list()
        self.y = list()
        
        for c,s in zip(range(len(names), names)):
            if re.match('^[A-Z]*', s):
                col = num.Num(c, s)
            else:
                col = sym.Sym(c, s)
            self.all.append(col)

            if re.match('.*:$', s):
                if re.match('.*\+$', s) or re.match('.*\-$', s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.find('!$', s):
                    self.klass = col
