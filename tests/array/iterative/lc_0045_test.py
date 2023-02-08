import pytest
from src.array.iterative.lc_0045 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2)
    ])
    def test_jump(self, solution, nums, expected):
        result = solution.jump(nums)
        assert_that(result, equal_to(expected))
