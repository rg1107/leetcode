# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        pred, succ = [], [] # O(h)

        curr = root
        while curr: # O(h)
            if curr.val <= target:
                pred.append(curr)
                curr = curr.right
            else:
                succ.append(curr)
                curr = curr.left

        res = []
        while len(res) < k and (pred or succ): # O(k + h)
            dist_pred = abs(pred[-1].val - target) if pred else float("inf")
            dist_succ = abs(succ[-1].val - target) if succ else float("inf")
            if dist_pred <= dist_succ:
                node = pred.pop()
                # the next inorder predecessor
                curr = node.left
                while curr:
                    pred.append(curr)
                    curr = curr.right
            else:
                node = succ.pop()
                # the next inorder successor
                curr = node.right
                while curr:
                    succ.append(curr)
                    curr = curr.left
            res.append(node.val)
        return res
        