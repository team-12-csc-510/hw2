class Row:
    """ 
        The Row class
        Recieves an object and encpulates it as a csv row
        The Row constructor takes a dictionary 'row' as input. 
    """
    def __init__(self, row: list):
        self.cells = row
        self.cooked = row.copy()
        self.isEvaled = False
        

    
        