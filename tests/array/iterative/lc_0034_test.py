import pytest
from hamcrest import assert_that, equal_to
from src.array.iterative.lc_0034 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, target, expected", [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([],                  0, [-1, -1])

    ])
    def test_search_range(self, solution, nums, target, expected):
        result = solution.searchRange(nums, target)
        assert_that(result, equal_to(expected))
