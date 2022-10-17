import pytest
from hamcrest import assert_that, equal_to
from src.array.iterative.lc_0162 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        ([1, 2, 1, 3, 5, 6, 4], 5),
        ([1, 2, 3, 1],          2)
    ])
    def test_find_peak(self, solution, nums, expected):
        result = solution.findPeakElement(nums)
        assert_that(result, equal_to(expected))
