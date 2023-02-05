import pytest
from hamcrest import assert_that, equal_to

from src.graph.iterative.lc_0931 import Solution

class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("matrix, expected", [
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
        ([[-19, 57], [-40, -5]],           -59)
    ])
    def test_minFallingPathSum(self, solution, matrix, expected):
        result = solution.minFallingPathSum(matrix)
        assert_that(result, equal_to(expected))