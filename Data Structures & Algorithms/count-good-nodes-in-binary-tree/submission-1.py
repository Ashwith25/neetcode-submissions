# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def checkNodes(root, currentMax):
            if root is None:
                return

            if root.val >= currentMax:
                # print(root.val, currentMax)
                self.count+=1
                currentMax = root.val

            checkNodes(root.left, currentMax)
            checkNodes(root.right, currentMax)
            
        checkNodes(root, root.val)
        return self.count