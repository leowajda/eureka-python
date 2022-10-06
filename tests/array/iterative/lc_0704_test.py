import pytest
from hamcrest import assert_that, equal_to
from src.array.iterative.lc_0704 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, target, expected", [
        ([-1, 0, 3, 5, 9, 12], 9,  4),
        ([-1, 0, 3, 5, 9, 12], 2, -1)
    ])
    def test_search(self, solution, nums, target, expected):
        result = solution.search(nums, target)
        assert_that(result, equal_to(expected))
