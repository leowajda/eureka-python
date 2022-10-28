import pytest
from hamcrest import assert_that, equal_to

from binary_tree.TreeNode import deserialize
from src.binary_tree.recursive.lc_0297 import Codec


class TestCodec:

    @pytest.fixture
    def solution(self):
        return Codec()

    @pytest.mark.parametrize("root", [
        deserialize([1, 2, 3, None, None, 4, 5]),
        deserialize([])
    ])
    def test_codec(self, solution, root):
        result = solution.deserialize(solution.serialize(root))
        assert_that(result, equal_to(root))
