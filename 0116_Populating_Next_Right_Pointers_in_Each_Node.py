"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def conmini(root):
            if not root.left and not root.right:
                return
            else:
                conmini(root.left)
                conmini(root.right)
                
                templeft = root.left
                tempright = root.right
                
                while templeft:
                    templeft.next = tempright
                    templeft = templeft.right
                    tempright = tempright.left
                return
        
        if not root:
            return root
        conmini(root)
        
        return root
