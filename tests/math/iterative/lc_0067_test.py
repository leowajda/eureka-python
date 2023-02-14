import pytest
from src.math.iterative.lc_0067 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("a, b, expected", [
        ('11', '1', '100'), ('1010', '1011', '10101'), ('111', '111', '1110')
    ])
    def test_addBinary(self, a, b, expected, solution):
        result = solution.addBinary(a, b)
        assert_that(result, equal_to(expected))
