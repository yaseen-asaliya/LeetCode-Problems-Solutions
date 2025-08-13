# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        def travers(root):
            nonlocal total
            if not root:
                return
            if root.val >= low and root.val <= high:
                total += root.val

            travers(root.left)
            travers(root.right)

        travers(root)
        return total