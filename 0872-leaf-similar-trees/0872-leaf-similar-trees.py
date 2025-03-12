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
        
        self.traversal(root1, temp1)
        self.traversal(root2, temp2)
        return temp1 == temp2

    def traversal(self, root, tt):
        if root is None:
            return

        if root.left is None and root.right is None:
            tt.append(root.val)
            return  

        self.traversal(root.left, tt)
        self.traversal(root.right, tt)