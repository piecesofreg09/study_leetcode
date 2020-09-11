'''
Using dummy heads
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummyone = ListNode(-1)
        dummytwo = ListNode(-1)
        
        curone = dummyone
        curtwo = dummytwo
        cur = head
        count = 0
        while cur:
            count += 1
            if count % 2 == 1:
                curone.next = cur
                curone = curone.next
                temp = cur.next
                curone.next = None
                cur = temp
            else:
                curtwo.next = cur
                curtwo = curtwo.next
                temp = cur.next
                curtwo.next = None
                cur = temp
            
            #print(dummyone)
            #print(dummytwo)
            
        curone.next = dummytwo.next
        
        return dummyone.next
        
