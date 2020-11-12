'''
basically mono stack
keep track of the location of the element that has been put into the stack
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        cur = head
        res = []
        stack = []
        ind = 0
        while cur:
            while stack and stack[-1][1] < cur.val:
                temp = stack.pop()
                res[temp[0]] = cur.val
            stack.append([ind, cur.val])
            res.append(0)
            cur = cur.next
            ind += 1
        
        return res
        
