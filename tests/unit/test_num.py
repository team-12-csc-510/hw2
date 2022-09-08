from src.num import Num
from src.utils import (
    custom_assert_equals,
    custom_assert_greater,
    custom_assert_greater_equals,
)


def test_add() -> None:
    num: Num = Num()
    for i in range(1, 101):
        num.add(i)
    return custom_assert_equals(num.n, 100, "Adder error")


def test_div() -> None:
    num: Num = Num()
    for i in range(1, 101):
        num.add(i)
    div: float = num.div()
    msg = "Div error"
    cond1 = custom_assert_greater(div, 30.5, msg)
    return cond1 and custom_assert_greater(32, div, msg)


def test_mid() -> None:
    num: Num = Num()
    for i in range(1, 101):
        num.add(i)
    mid: int = num.mid()
    return custom_assert_greater_equals(
        52, mid, "Mid error"
    ) and custom_assert_greater_equals(mid, 50, "Mid error")
