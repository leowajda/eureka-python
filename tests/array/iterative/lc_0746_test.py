import pytest
from hamcrest import assert_that, equal_to
from src.array.iterative.lc_0746 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("cost, expected", [
        ([10,15,20], 15),
        ([1,100,1,1,1,100,1,1,100,1], 6)
    ])
    def test_search_range(self, solution, cost, expected):
        result = solution.minCostClimbingStairs(cost)
        assert_that(result, equal_to(expected))
