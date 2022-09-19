# import os

# abs_file_path = os.path.abspath(__file__)
# path_ls = abs_file_path.split("/")[:-3]
# new_path = "/".join(path_ls)
# sys.path.append(new_path)

from src import utils
from src.num import Num
from src.utils import csv, custom_assert_equals, oo

# import sys


def test_the() -> None:
    return custom_assert_equals(utils.the.get("nums"), 512, "Utils the error")


def test_big_num() -> None:
    num: Num = Num()
    for i in range(1, 1001):
        num.add(i)
    return custom_assert_equals(len(num.has), 512, "Big num error")


def test_csv() -> bool:
    csv_file_name = "auto93.csv"

    def helper_func():
        n = 0

        def _(row):
            nonlocal n
            n = n + 1
            if n <= 10:
                return oo(row)
            else:
                return

        return _

    helper_function = helper_func()
    csv(csv_file_name, helper_function)
    return True


def test_coerce():
    custom_assert_equals(utils.coerce("true"), True)
    custom_assert_equals(utils.coerce("false"), False)
