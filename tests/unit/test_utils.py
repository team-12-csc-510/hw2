# import os

# abs_file_path = os.path.abspath(__file__)
# path_ls = abs_file_path.split("/")[:-3]
# new_path = "/".join(path_ls)
# sys.path.append(new_path)
from src import data, utils
from src.num import Num
from src.utils import custom_assert_equals, o

# import sys


def test_the() -> None:
    return custom_assert_equals(utils.the.get("nums"), 512, "Utils the error")


def test_big_num() -> None:
    num: Num = Num()
    for i in range(1, 1001):
        num.add(i)
    return custom_assert_equals(len(num.has), 512, "Big num error")


# Print some stats on columns.
def test_stats() -> bool:
    def helper_stats_div(col):
        return col.div()

    def helper_stats_mid(col):
        return col.mid()

    csv_file_name = "auto93.csv"
    # csv_file_path = os.path.join(
    #     "/".join(os.path.abspath(__file__).split("/")[:-3]),
    #     "data", csv_file_name
    # )
    # print(csv_file_path)
    data = data.Data(csv_file_name)
    div = helper_stats_div
    mid = helper_stats_mid
    print("xmid", o(data.stat(2, data.cols.x, mid)))
    print("xdiv", o(data.stat(3, data.cols.x, div)))
    print("ymid", o(data.stat(2, data.cols.y, mid)))
    print("ydiv", o(data.stat(3, data.cols.y, div)))
    return True
