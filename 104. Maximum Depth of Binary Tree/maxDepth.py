# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #If there is no children, return 0
        if not root:
            return 0
        #Otherwise, return a recursive call to maxDepth taking the max of the left and right root
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))