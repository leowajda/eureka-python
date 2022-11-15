import pytest
from hamcrest import assert_that, equal_to

from src.binary_tree.TreeNode import deserialize
from src.binary_tree.recursive.lc_1448 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("root, expected", [
        (deserialize([3, 1, 4, 3, None, 1, 5]), 4),
        (deserialize([3, 3, None, 4, 2]), 3),
        (deserialize([1]), 1),
    ])
    def test_goodNodes(self, solution, root, expected):
        result = solution.goodNodes(root)
        assert_that(result, equal_to(expected))
