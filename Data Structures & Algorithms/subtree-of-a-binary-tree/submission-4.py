# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):
            if not root1 and not root2:
                return True

            if root1 and root2 and root1.val == root2.val:
                return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

            return False

       

        if not root or not subRoot:
            return False

        queue = deque([root])
        mainNodes = []
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.val == subRoot.val:
                    # mainNodes.append(node)
                    if dfs(node, subRoot):
                        return True

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        
        return False
        # return any([dfs(mainNode, subRoot) for mainNode in mainNodes])

        