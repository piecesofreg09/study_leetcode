'''
Recursive
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            
            return (t1.val == t2.val) \
                and (isMirror(t1.left, t2.right)) \
                and (isMirror(t1.right, t2.left))
        
        if not root:
            return True
        return isMirror(root.left, root.right)


'''
Iterative
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        stack = [root]
        while stack:
            length = len(stack)
            temp = []
            for node in stack:
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
            stack = temp
            
            for i in range(len(stack) // 2):
                if not stack[i] and not stack[len(stack) - i - 1]:
                    continue
                if not stack[i] or not stack[len(stack) - i - 1]:
                    return False
                if stack[i].val != stack[len(stack) - i - 1].val:
                    return False
                else:
                    continue
        
        return True
