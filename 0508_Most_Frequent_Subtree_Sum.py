# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tra(self, root):
        #print(root)
        left = 0
        right = 0
        if root.left:
            left = self.tra(root.left)
        if root.right:
            right = self.tra(root.right)
        
        sm = root.val + left + right
        #print(sm)
        if sm in self.res:
            self.res[sm] += 1
        else:
            self.res[sm] = 1
        return sm
        
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res = {}
        self.tra(root)
        #print(list(self.res.items()))
        temp = sorted(list(self.res.items()), key=lambda x:x[1])
        
        res = []
        count = temp[-1][1]
        cur = -1
        while cur >= -len(temp) and temp[cur][1] == count:
            res.append(temp[cur][0])
            cur -= 1
        
        return res
