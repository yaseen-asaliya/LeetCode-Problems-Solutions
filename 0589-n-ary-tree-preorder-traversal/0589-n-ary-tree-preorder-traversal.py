"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        output = []
        self.traverse(root, output)
        return output

    def traverse(self, root, output):
        if root is None: return
        output.append(root.val)
        for child in root.children:
            self.traverse(child, output)
    