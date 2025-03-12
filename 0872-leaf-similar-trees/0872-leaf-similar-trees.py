# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        temp1 = []
        temp2 = []

        def traversal(root, tt):
            if root is None:
                return None

            if root.left == None and root.right == None:
                tt.append(root.val)

            traversal(root.left, tt)
            traversal(root.right, tt)
        
        traversal(root1, temp1)
        traversal(root2, temp2)
        return temp1 == temp2
            