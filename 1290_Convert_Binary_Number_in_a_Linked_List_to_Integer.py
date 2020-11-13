'''
copy the result into list, and then add
faster than going through linkedlist twice
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        
        res = 0
        for i, v in enumerate(li):
            if v == 1:
                res += 1 << (len(li) - i - 1)
        
        return res

'''
traverse linked list twice, slow
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        
        res = 0
        cur = head
        i = 0
        while cur:
            i += 1
            if cur.val == 1:
                res += 1 << (count - i)
            cur = cur.next
        
        return res
