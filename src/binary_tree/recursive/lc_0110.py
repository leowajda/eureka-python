from typing import Optional

from src.binary_tree.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node: Optional[TreeNode]) -> int:

            if node is None:
                return 0

            left, right = helper(node.left), helper(node.right)
            if left is -1 or right is -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return helper(root) is not -1
