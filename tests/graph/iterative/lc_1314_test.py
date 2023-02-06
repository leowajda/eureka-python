import pytest
from hamcrest import assert_that, equal_to

from src.graph.iterative.lc_1314 import Solution

class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("matrix, k, expected", [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [[12, 21, 16], [27, 45, 33], [24, 39, 28]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, [[45, 45, 45], [45, 45, 45], [45 ,45, 45]])
    ])
    def test_matrixBlockSum(self, solution, matrix, k, expected):
        result = solution.matrixBlockSum(matrix, k)
        assert_that(result, equal_to(expected))