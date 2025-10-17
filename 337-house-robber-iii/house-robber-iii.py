# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def rec(root, toRob: bool) -> int:
            if not root:
                return 0
            
            if toRob:
                return max(root.val + rec(root.left, False) + rec(root.right, False), rec(root.left, True) + rec(root.right, True))
            else:
                return rec(root.left, True) + rec(root.right, True)
        
        return rec(root, True)
        