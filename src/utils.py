import logging
import math
import re
import traceback
from typing import Dict

# Data Structure which holds all the default arguments
the: Dict = {"nums": 512, "dump": False}


# Identifies the input string to be a number
#  int , boolean or simply a  string
def coerce(in_str):
    if in_str == "true":
        return True
    elif in_str == "false":
        return False
    # checks if number is an integer
    elif in_str.isnumeric():
        return int(in_str)
    # checks if in_str is a non-integer number
    elif re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$", in_str) is not None:
        return float(in_str)
    else:
        return in_str


def rnd(x, places=2):
    mult = pow(10, places)
    return math.floor(x * mult + 5) / mult


# Updates the variable
def default_args(def_str, arg_dict):
    regex = r"\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
    options = re.findall(regex, def_str)
    for option in options:
        arg_dict[option[0]] = coerce(option[1])


# Our implementation of the custom print of a dictionary
# def my_print(my_dict):
#     print_str = "{"
#     keys = list(my_dict.keys())
#     for key in keys:
#         print_str += ":" + str(key) + " " + str(my_dict[key])

#     print_str += "}"
#     print(print_str)

# Generates a string from nested table
def o(t):
    def show(k, v):

        if not re.search("^_", k):
            v = o(v)
            return f":{k} {v}"

    if not (type(t).__name__ == "dict" or type(t).__name__ == "list"):
        return str(t)

    if type(t).__name__ == "list":
        return "{" + "".join(t) + "}"

    u = []
    keys = list(t.keys())
    for key in keys:
        val = show(key, t[key])
        if val:
            u.append(val)

    print("Before sorting -> ", u)
    u.sort()
    print("After sorting -> ", u)
    return "{" + "".join(u) + "}"


# Prints the string from function o
def oo(t):
    print(o(t))
    return t


def custom_assert_equals(val1, val2, msg=""):
    if val1 != val2:
        logging.error(msg)
        traceback.print_stack()
        return False
    else:
        return True


def custom_assert_greater(val1, val2, msg=""):
    if val1 <= val2:
        logging.error(msg)
        traceback.print_stack()
        return False
    else:
        return True


def custom_assert_greater_equals(val1, val2, msg=""):
    if val1 < val2:
        logging.error(msg)
        traceback.print_stack()
        return False
    else:
        return True
