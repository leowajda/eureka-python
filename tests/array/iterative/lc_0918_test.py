import pytest
from hamcrest import assert_that, equal_to
from src.array.iterative.lc_0918 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        ([1,-2,3,-2], 3),
        ([5,-3,5],   10),
        ([-3,-2,-3], -2)
    ])
    def test_max_subarray_sum_circular(self, solution, nums, expected):
        result = solution.maxSubarraySumCircular(nums)
        assert_that(result, equal_to(expected))
