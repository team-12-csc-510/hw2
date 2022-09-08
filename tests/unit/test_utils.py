from src import utils
from src.num import Num
from src.utils import custom_assert_equals


def test_the() -> None:
    return custom_assert_equals(utils.the.get("nums"), 512, "Utils the error")


def test_big_num() -> None:
    num: Num = Num()
    for i in range(1, 1001):
        num.add(i)
    return custom_assert_equals(len(num.has), 512, "Big num error")
