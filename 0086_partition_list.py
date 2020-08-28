'''
Use two layer dummy system
remember to cut the remaining links, or else there might be loops
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        cur = head
        dummy1 = ListNode(200)
        dummy2 = ListNode(200)
        dummy1_head = ListNode(100)
        dummy2_head = ListNode(100)
        dummy1_head.next = dummy1
        dummy2_head.next = dummy2
        
        while cur:
            
            if cur.val < x:
                temp = cur.next
                dummy1.next = cur
                dummy1 = dummy1.next
                dummy1.next = None
                cur = temp
            else:
                temp = cur.next
                dummy2.next = cur
                dummy2 = dummy2.next
                dummy2.next = None
                cur = temp
            
        dummy1.next = dummy2_head.next.next
        
        return dummy1_head.next.next
                
        
        
