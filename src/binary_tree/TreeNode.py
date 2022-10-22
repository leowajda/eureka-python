from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def serialize(root: Optional[TreeNode]):
    if root is None:
        return []

    queue, res = deque([root]), []

    while queue:
        temp = queue.popleft()
        res.append(temp.val if temp else None)

        if temp:
            queue.append(temp.left)
            queue.append(temp.right)

    return res


def deserialize(data: List[Optional[int]]):
    if len(data) == 0:
        return None

    root, queue = TreeNode(data.pop(0)), deque()
    queue.append(root)

    while queue:
        temp = queue.popleft()

        left, right = data.pop(0) if len(data) > 0 else None, data.pop(0) if len(data) > 0 else None
        temp.left, temp.right = TreeNode(left) if left else None, TreeNode(right) if right else None

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    return root
