from binary_tree.TreeNode import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        nodes = []

        def helper(node):
            if node is None:
                nodes.append('#')
                return

            nodes.append(str(node.val))
            helper(node.left)
            helper(node.right)

        helper(root)
        return ' '.join(nodes)

    def deserialize(self, data: str) -> TreeNode:
        nodes = iter(data.split())

        def helper():
            val = next(nodes)

            if val == '#':
                return None

            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()

            return node

        return helper()
