import utils

from cols import Cols
from row import Row


class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []
        if isinstance(src, str):
            self.csv(src)
        else:
            if src is None:
                src = []
            for x in range(src):
                self.add(self.rows)

    def csv(self, fname: str):
        with open(fname, "r+") as input_file:
            for line in input_file:
                newLine = line.replace("\n", "").rstrip().split(",")
                t = []
                for i in newLine:
                    t.append(utils.coerce(i))
                self.add(t.copy())
                # print(t)

    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)

        else:
            row = Row(xs)
            self.rows.append(row.cells)
            for td in self.cols.x:
                td.add(row.cells[td.at])

            for td in self.cols.y:
                td.add(row.cells[td.at])

    def stat(self, places, showCols, fun="mid"):
        if showCols is None:
            showCols = self.cols.y
        t = []
        for col in showCols:
            v = getattr(col, fun)()
            if isinstance(v, int):
                v = utils.rnd(v, places)
            t[col.name] = v
        return t
