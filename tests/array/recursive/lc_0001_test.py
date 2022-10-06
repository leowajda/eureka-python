from src.array.recursive.lc_0001 import Solution
from hamcrest import contains_inanyorder, assert_that
import pytest


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, target, expected", [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4],      6, [0, 2]),
        ([3, 3],         6, [0, 1])
    ])
    def test_two_sum(self, nums, target, expected, solution):
        result = solution.twoSum(nums, target)
        assert_that(*result, contains_inanyorder(*expected))
