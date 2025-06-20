# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepestLevel = 0
        s = 0

        def deepestLeafLevel(root):
            if not root:
                return 0

            left_height = deepestLeafLevel(root.left)
            right_height = deepestLeafLevel(root.right)

            return max(left_height, right_height) + 1
        
        deepestLevel = deepestLeafLevel(root)
        
        def sumAtDepth(node, level):
            if not node:
                return 0
            if level == deepestLevel:
                return node.val
            return sumAtDepth(node.left, level + 1) + sumAtDepth(node.right, level + 1)
        
        return sumAtDepth(root, 1)
            
            
