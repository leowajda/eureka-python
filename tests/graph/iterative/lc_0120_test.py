import pytest
from hamcrest import assert_that, equal_to

from src.graph.iterative.lc_0120 import Solution

class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("triangle, expected", [
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
        ([[-10]],                               -10)
    ])
    def test_minimumTotal(self, solution, triangle, expected):
        result = solution.minimumTotal(triangle)
        assert_that(result, equal_to(expected))