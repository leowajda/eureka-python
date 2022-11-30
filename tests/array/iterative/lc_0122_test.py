import pytest
from src.array.iterative.lc_0122 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("prices, expected", [
        ([7, 1, 5, 3, 6, 4], 7),
        ([7, 6, 4, 3, 1],    0),
        ([1, 2, 3, 4, 5],    4)
    ])
    def test_max_profit(self, solution, prices, expected):
        result = solution.maxProfit(prices)
        assert_that(result, equal_to(expected))
