# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return
    
        root = TreeNode(preorder[0])
        
        def insert(val, node):            
            while True:
                if node.val > val:
                    if not node.left:
                        node.left = TreeNode(val)
                        break
                    else:
                        node = node.left
                else:
                    if not node.right:
                        node.right = TreeNode(val)
                        break
                    else:
                        node = node.right
        head = root       
        for i in range(1, len(preorder)):
            head = root
            insert(preorder[i], head)
        
        return head