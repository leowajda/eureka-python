import pytest
from src.math.iterative.lc_0509 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (2, 1), (3, 2), (4, 3)
    ])
    def test_fib(self, n, expected, solution):
        result = solution.fib(n)
        assert_that(result, equal_to(expected))
