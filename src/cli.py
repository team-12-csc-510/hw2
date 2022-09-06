import sys

import misc

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


def cli(arg_dict):
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


misc.default_args(help, misc.the)
print("Before:", misc.the)
cli(misc.the)
print(sys.argv)
print("After:", misc.the)
