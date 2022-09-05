import re
from cli import args as cmd_args

help = """CSV : summarized csv file 
(c) 2022 Tim Menzies <timm@ieee.org> BSD−2 license 

USAGE: lua seen.lua [OPTIONS] 

OPTIONS: 
 -e --eg          start-up example                         = nothing 
 -d --dump        on test failure, exit with stack dump    = false 
 -f --file        file with csv data                       = ../data/auto93.csv 
 -h --help        show help                                = false  
 -n --nums        number of nums to keep                   = 512 
 -s --seed        random number seed                       = 10019 
 -S --seperator   feild seperator                          = ,]]"""

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


def cli(arg_dict):
    
    keys = list(arg_dict.keys())
    for key in keys:
        if cmd_args[key] != None:
            arg_dict[key] = coerce(cmd_args[key])
        
    



the = {}

options = re.findall(r"\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)" , help)
for option in options:
    the[option[0]] = coerce(option[1])
    

print(the)
print("From cli.py")
print(cmd_args)
# cli(the)


