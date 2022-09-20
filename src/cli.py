import sys

import src.utils as utils

help = """CSV : summarized csv file

OPTIONS:
 -e --eg          start-up example                         = nothing
 -d --dump        on test failure, exit with stack dump    = False
 -f --file        file with csv data                       = ../data/auto93.csv
 -h --help        show help                                = False
 -n --nums        number of nums to keep                   = 512
 -s --seed        random number seed                       = 10019
 -S --seperator   field seperator                          = ,]]"""


def cli(arg_dict):
    
    """
    The function updates the settings based on command-line flags. If the provided flag is boolean, the existing boolean value is just flipped. Otherwise, the default settings are updated from the command-line flag values.  
    """
    
    keys = list(arg_dict.keys())
    for key in keys:
        v = arg_dict[key]
        usr_args_ls = sys.argv
        for ind in range(len(usr_args_ls)):
            val = usr_args_ls[ind]
            if val == "-" + key[0] or val == "--" + key:
                if type(v).__name__ == "bool":
                    v = not v
                else:
                    v = usr_args_ls[ind + 1]

            arg_dict[key] = v


utils.default_args(help, utils.the)
# print("Before:", utils.the)
cli(utils.the)
# print(sys.argv)
# print("After:", utils.the)
