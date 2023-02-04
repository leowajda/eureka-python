import pytest
from src.math.iterative.lc_0264 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (10, 12), (1, 1)
    ])
    def test_nthUglyNumber(self, n, expected, solution):
        result = solution.nthUglyNumber(n)
        assert_that(result, equal_to(expected))
