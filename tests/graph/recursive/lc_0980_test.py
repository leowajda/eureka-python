import pytest
from hamcrest import assert_that, equal_to

from src.graph.recursive.lc_0980 import Solution

class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("grid, expected", [
        ([
             [1, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 2, -1]
         ], 2),
        ([
             [1, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 2]
        ], 4),
        ([
             [0, 1],
             [2, 0]
        ], 0)
    ])
    def test_uniquePathsIII(self, solution, grid, expected):
        result = solution.uniquePathsIII(grid)
        assert_that(result, equal_to(expected))