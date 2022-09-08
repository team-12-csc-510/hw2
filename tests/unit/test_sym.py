from src.sym import Sym
from src.utils import custom_assert_equals, custom_assert_greater_equals


def test_add() -> None:
    sym = Sym()
    data = ["a", "a", "a", "a", "b", "b", "c"]
    for i in data:
        sym.add(i)
    return_value = {"a": 4, "b": 2, "c": 1}
    msg = "Adder error"
    return custom_assert_equals(sym.n, 7, msg) and custom_assert_equals(
        sym._has, return_value, msg
    )


def test_mid() -> None:
    sym = Sym()
    data = ["a", "a", "a", "a", "b", "b", "c"]
    for i in data:
        sym.add(i)
    mode = sym.mid()
    return custom_assert_equals(mode, "a", "Mode error")


def test_div() -> None:
    sym = Sym()
    data = ["a", "a", "a", "a", "b", "b", "c"]
    for i in data:
        sym.add(i)
    entropy = sym.div()
    return custom_assert_greater_equals(
        entropy, 1.37, "Entropy error"
    ) and custom_assert_greater_equals(1.38, entropy, "Entropy error")
