import pytest
from hamcrest import assert_that, equal_to

from src.graph.recursive.lc_0079 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("word, expected", [
        ("ABCCED", True),
        ("SEE", True),
        ("ABCB", False)
    ])
    def test_exist(self, solution, word, expected):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        
        result = solution.exist(board, word)
        assert_that(result, equal_to(expected))
