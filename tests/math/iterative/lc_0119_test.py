import pytest
from src.math.iterative.lc_0119 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (3, [1, 3, 3, 1]), (0, [1]), (1, [1, 1])
    ])
    def test_getRow(self, n, expected, solution):
        result = solution.getRow(n)
        assert_that(result, equal_to(expected))
