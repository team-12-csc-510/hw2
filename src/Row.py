class Row:
    
    """ 
        The Row class
        Recieves an object and encpulates it as a csv row
        The Row constructor takes a dictionary 'row' as input. 
    """
    
    def __init__(row):
        
        cells = row
        cooked = t.copy()
        isEvaled = False
        
        return cells, cooked, isEvaled
    
        