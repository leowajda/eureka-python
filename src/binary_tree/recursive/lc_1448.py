from src.binary_tree.TreeNode import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node: TreeNode, prev: int) -> int:
            if node is None:
                return 0
            return (node.val >= prev) + helper(node.left, max(node.val, prev)) + helper(node.right, max(node.val, prev))

        return helper(root, root.val)
