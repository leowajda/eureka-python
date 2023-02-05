import pytest
from src.strings.iterative.lc_0438 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("s, p, expected", [
        ("cbaebabacd", "abc", [0,6]), ("abab", "ab", [0,1,2])
    ])
    def test_num_decodings(self, solution, s, p, expected):
        result = solution.findAnagrams(s, p)
        assert_that(result, equal_to(expected))
