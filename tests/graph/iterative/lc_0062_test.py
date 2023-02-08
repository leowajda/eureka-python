import pytest
from hamcrest import assert_that, equal_to

from src.graph.iterative.lc_0062 import Solution

class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("m, n, expected", [
        (3, 7, 28), (3, 2, 3)
    ])
    def test_uniquePaths(self, solution, m, n, expected):
        result = solution.uniquePaths(m, n)
        assert_that(result, equal_to(expected))