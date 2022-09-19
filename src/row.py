class Row:
    """
    The Row class recieves a csv row which is one record of the csv.
    
    :param cells: contains one record of the csv 
    : type cells: list
    
    :param cooked: duplicate of the csv record
    :type cooked: list
    
    :param isEvaled: used to determine if y-values are evaluated
    :type isEvaled: boolean
    
    """

    def __init__(self, row: list):
        self.cells = row
        self.cooked = row.copy()
        self.isEvaled = False
