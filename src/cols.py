import re

import src.num as num
import src.sym as sym


class Cols:

    """
    The Cols class iterates over a list of column
    names and determines whether the Column name
    is that of a Numeric column opr that of a Symbols
    column. Based on the name of the column the Cols
    class also determines whether the Column is
    dependent or independent. Lastly it also determines
    whether the column is a simgle dependent klass column.

    :param names: List of all column names
    :type names: list

    :param all: List of all the column objects
    :type all: list

    :param klass: Sym or Num object
    :type klass: Sym or Num object

    :param x: List of independent columns
    :type x: list

    :param y: List of depenedent columns
    :type: y: list
    """

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

            if not re.match(".*:$", s):
                if re.match(r".*\+$", s) or re.match(r".*\-$", s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.match("!$", s):
                    self.klass = col
