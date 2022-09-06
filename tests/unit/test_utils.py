from unittest import TestCase

from src import utils
from src.num import Num


class TestUtils(TestCase):
    def setUp(self) -> None:
        self.num: Num = Num()

    def test_the(self):
        assert utils.the.get("nums") == 512

    def test_big_num(self) -> None:
        for i in range(1, 1001):
            self.num.add(i)
        assert len(self.num.has) == 512
