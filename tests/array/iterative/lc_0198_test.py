import pytest
from hamcrest import assert_that, equal_to
from src.array.iterative.lc_0198 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        ([1, 2, 3, 1],     4),
        ([2, 7, 9, 3, 1], 12)
    ])
    def test_search_range(self, solution, nums, expected):
        result = solution.rob(nums)
        assert_that(result, equal_to(expected))
