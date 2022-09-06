from unittest.mock import Mock, patch

from src import app


@patch("src.app.add")
def test_add(adder: Mock):
    adder.return_value = 5
    assert adder.return_value == app.add(2, 3)
