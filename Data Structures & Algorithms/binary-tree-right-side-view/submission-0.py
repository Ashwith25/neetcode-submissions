# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        while queue:
            length = len(queue)
            right = None
            for i in range(length):
                # print(queue)
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    right = node
                if i==length-1 and right:
                    res.append(right.val)

        return res
            