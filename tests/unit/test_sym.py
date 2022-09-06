from unittest import TestCase

from src.sym import Sym


class TestSym(TestCase):
    def setUp(self):
        self.sym = Sym()
        data = ["a", "a", "a", "a", "b", "b", "c"]
        for i in data:
            self.sym.add(i)

    def test_add(self):
        return_value = {"a": 4, "b": 2, "c": 1}
        self.assertEqual(self.sym.n, 7, "Adder error")
        self.assertEqual(self.sym._has, return_value, "Adder error")

    def test_mid(self):
        mode = self.sym.mid()
        self.assertEqual(mode, "a", "Mode error")

    def test_div(self):
        entropy = self.sym.div()
        assert 1.37 <= entropy <= 1.38, "Entropy error"
