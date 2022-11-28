import pytest
from src.strings.iterative.lc_0091 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("s, expected", [
        ("12", 2), ("226", 3), ("06", 0)
    ])
    def test_num_decodings(self, solution, s, expected):
        result = solution.numDecodings(s)
        assert_that(result, equal_to(expected))
