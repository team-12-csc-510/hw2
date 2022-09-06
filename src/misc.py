import re

# Data Structure which holds all the default arguments
the = {}

# Identifies the input string to be a number ; int ; boolean or simply a  string
def coerce(in_str):
    
    if in_str == "true":
        return True
    elif in_str == "false":
        return False
    # checks if number is an integer
    elif in_str.isnumeric():
        return int(in_str)
    # checks if in_str is a non-integer number
    elif re.search("[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$", in_str) != None:
        return float(in_str)
    else:
        return in_str

# Updates the variable     
def default_args(def_str , arg_dict):
    options = re.findall(r"\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)" , def_str)
    for option in options:
        arg_dict[option[0]] = coerce(option[1])
        
# Our implementation of the custom print of a dictionary
def my_print(my_dict):
    
    print_str = "{"
    keys = list(my_dict.keys())
    for key in keys:
        print_str += ":" + str(key) + " " + str(my_dict[key])
        
    print_str += "}"
    print(print_str)


