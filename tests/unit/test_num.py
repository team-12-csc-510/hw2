from unittest import TestCase

from src.num import Num


class TestNum(TestCase):
    def setUp(self) -> None:
        self.num: Num = Num()
        for i in range(1, 101):
            self.num.add(i)

    def test_add(self) -> None:
        assert self.num.n == 100

    def test_div(self) -> None:
        self.div: float = self.num.div()
        assert self.div > 30.5
        assert self.div < 32

    def test_mid(self) -> None:
        self.mid: int = self.num.mid()
        assert self.mid <= 52
        assert self.mid >= 50
