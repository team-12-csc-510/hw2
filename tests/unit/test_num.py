import unittest

from src.Num import Num


class TestNum(unittest.TestCase):
    def setUp(self) -> None:
        self.num: Num = Num()
        for i in range(1, 101):
            self.num.add(i)
        self.div: float = self.num.div()
        self.mid: int = self.num.mid()

    def test_div(self) -> None:
        assert self.div > 30.5
        assert self.div < 32

    def test_mid(self) -> None:
        assert self.mid <= 52
        assert self.mid >= 50
