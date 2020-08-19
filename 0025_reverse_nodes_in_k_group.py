'''

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        start = dummy
        
        while True:
            first = start
            count = 0
            
            while first.next and count < k:
                count += 1
                first = first.next
                
            if count == k:
                
                end = first.next
                x = start.next
                new_start = x
                
                for i in range(k - 1):
                    first.next, t = x, x.next
                    x.next, end, x = end, x, t
                    #print(dummy.next)
                
                start.next = first
                start = new_start
                
                
            else:
                return dummy.next
