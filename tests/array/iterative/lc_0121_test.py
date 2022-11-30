import pytest
from src.array.iterative.lc_0121 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("prices, expected", [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1],    0)
    ])
    def test_max_profit(self, solution, prices, expected):
        result = solution.maxProfit(prices)
        assert_that(result, equal_to(expected))
