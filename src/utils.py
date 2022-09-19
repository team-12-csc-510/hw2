import logging
import math
import os.path
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
        p = [str(i) for i in t]
        return "{" + "".join(p) + "}"

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


def csv(fname: str, fun):
    """Performs the pre- processing on each line of the input file

    This method opens the input file and converts each line into
    a list of elements.If the line is having information of the
    Columns then it converts the line into a list of string
    elements which will later be used to form the column names
    and if the line contains the information of rows then it will
    convert the it into a list having integer or float type element
    depending on which type of data they have.This conversion is
    performed by passing the elements to `` coerce `` function
    in utils.
    Each of these lists are passed as an argument to the add
    function of data class to be processed further.

    :param str fname : address of the file to be processed
    """
    path = os.path.dirname(os.path.abspath(__file__))
    f_path = os.path.join(path, "../data", fname)
    with open(f_path, "r+") as input_file:
        for line in input_file:
            newLine = line.replace("\n", "").rstrip().split(",")
            t = []
            for i in newLine:
                t.append(coerce(i))
            fun(t.copy())
