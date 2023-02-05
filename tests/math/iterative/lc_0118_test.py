import pytest
from src.math.iterative.lc_0118 import Solution
from hamcrest import assert_that, equal_to


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (5, [[1],[1, 1],[1, 2, 1],[1, 3, 3, 1],[1, 4, 6, 4, 1]]), (1, [[1]])
    ])
    def test_generate(self, n, expected, solution):
        result = solution.generate(n)
        assert_that(result, equal_to(expected))
