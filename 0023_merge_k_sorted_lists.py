'''
using merging of two linked list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        ret = res
        
        while l1 and l2:
            if l1.val < l2.val:
                ret.next = l1
                l1 = l1.next
            else:
                ret.next = l2
                l2 = l2.next
            
            ret = ret.next
        
        if not l1:
            ret.next = l2
        else:
            ret.next = l1
        
        return res.next
    
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if not lists:
            return None
        
        elif len(lists) == 1:
            return lists[0]
       
        else:
            half = len(lists) // 2
            return self.mergeTwoLists(self.mergeKLists(lists[:half]), self.mergeKLists(lists[half:]))
        
        return res.next
        
        
