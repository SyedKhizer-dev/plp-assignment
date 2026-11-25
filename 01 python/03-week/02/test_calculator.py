import pytest
from calculator import add, mul, div


@pytest.fixture
def sample_values():
    return {"a": 10, "b": 5, "expected_sum": 15}


def test_add_positive(sample_values):
    result = add(sample_values["a"], sample_values["b"])
    assert result == sample_values["expected_sum"]


@pytest.mark.parametrize(
    "a, b, expected", [(2, 3, 6), (4, 5, 20), (-2, 3, -6), (0, 10, 0), (-3, -4, 12)]
)
def test_multiply(a, b, expected):
    assert mul(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)


def test_divide_zero():
    assert div(0, 5) == 0.0
