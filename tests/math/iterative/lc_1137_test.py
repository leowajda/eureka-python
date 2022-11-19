import pytest
from src.math.iterative.lc_1137 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (4, 4), (25, 1389537)
    ])
    def test_tribonacci(self, n, expected, solution):
        result = solution.tribonacci(n)
        assert_that(result, equal_to(expected))
