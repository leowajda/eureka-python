import pytest
from hamcrest import assert_that, equal_to

from src.binary_tree.TreeNode import deserialize
from src.binary_tree.recursive.lc_0110 import Solution


class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("root, expected", [
        (deserialize([3, 9, 20, None, None, 15, 7]),     True),
        (deserialize([1, 2, 2, 3, 3, None, None, 4, 4]), False),
        (deserialize([]),                                True)
    ])
    def test_search(self, solution, root, expected):
        result = solution.isBalanced(root)
        assert_that(result, equal_to(expected))
