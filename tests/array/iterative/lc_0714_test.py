import pytest
from src.array.iterative.lc_0714 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("prices, fee, expected", [
        ([1, 3, 2, 8, 4,  9], 2, 8),
        ([1, 3, 7, 5, 10, 3], 3, 6),
    ])
    def test_max_profit(self, solution, prices, fee, expected):
        result = solution.maxProfit(prices, fee)
        assert_that(result, equal_to(expected))
