# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        nodes = set(G)
        
        count = 0
        cur = head
        
        while cur:
            if cur.val in nodes:
                if not cur.next:
                    count += 1
                elif cur.next.val not in nodes:
                    count += 1
            cur = cur.next
        
        return count
