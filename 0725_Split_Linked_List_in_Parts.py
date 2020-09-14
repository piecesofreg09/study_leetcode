# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        count = 0
        cur = root
        while cur:
            count += 1
            cur = cur.next
        
        period = count // k
        remainder = count % k
        main = k - remainder
        
        res = []
        count = 0
        newhead = root
        
        for i in range(remainder):
            cur = newhead
            temp = cur
            for j in range(period):
                cur = cur.next
            
            newhead = cur.next
            cur.next = None
            #print(temp)
            res.append(temp)
        for i in range(main):
            if period > 0:
                cur = newhead
                temp = cur
                for j in range(period - 1):
                    cur = cur.next

                newhead = cur.next
                cur.next = None
                #print(temp)
            else:
                temp = None
            res.append(temp)

        return res
        
        
        
