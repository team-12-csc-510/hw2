import src.utils as utils
from src.cols import Cols
from src.row import Row


class Data:
    """Data class processes takes the file to be processed as input ,
     opens it and performs respective operations line by line.
     If it the line happens to have Column information then it is
     handled by cols class and if the line happens
     to have Row information then its data is handled by row class

    :param str src : address of the file to be processed"""

    def __init__(self, src):
        """Constructor method

        :param str src : address of the file to be processed
        """

        self.cols = None
        self.rows = []
        if isinstance(src, str):
            utils.csv(src, self.add)
        else:
            if src is None:
                src = []
            for x in range(src):
                self.add(self.rows)

    def add(self, xs):
        """Forms a Row or Col object from the input lists and processes
         it further as per the functionality

        This method first checks if a Col object has been created or not
        because to assign the row values to correct
        Columns it will be required later. After creating the col class
        object in the right manner, the lists that are
        passed later to this method are used to form row objects and
        these objects are appended into a list called
         ''rows'' of the Data class.

         The row object stores the list of element (of row in the input
         file) in its instance variable 'cells' which is
         used to put the value of the respective columns (independent
         column x or dependent columns y)

        :param list xs : pre- processed data of each line of the input
        file in the form of a list where each
        element belongs to a different Column (it can be name of the
        Column or the data of the column

        """

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
        """Performs the required stat operation on the columns data

        This method performs the stat operation, passed as the argument
        on the columns data and return the list of
        having results of operation on each column(columns are passed
        as argument with default values as dependent
        columns)

        :param int places: number of decimal places to be rounded off
        :param list showCols: list of columns on which stat operation
         will be performed(it can be either dependent or independent columns

        :param str fun: name of the stat function to be performed among
         div or mid (which have separate defination for numeric or
         symbolic data)

        :returns: list of results of operations on each required column.
        :rtype: list

        """
        if showCols is None:
            showCols = self.cols.y
        t = {}
        for col in showCols:
            if isinstance(fun, str):
                v = getattr(col, fun)()
            else:
                v = fun(col)
            if isinstance(v, int):
                v = utils.rnd(v, places)
            t[col.name] = v
        return t
