# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        cur1 = l1
        while cur1:
            num1.append(cur1.val)
            cur1 = cur1.next
        
        num2 = []
        cur2 = l2
        while cur2:
            num2.append(cur2.val)
            cur2 = cur2.next
        
        res = []
        carry = 0
        while num1 and num2:
            t1 = num1.pop()
            t2 = num2.pop()
            temp = t1 + t2 + carry
            res.append(temp % 10)
            carry = temp // 10
        
        numrest = num1 if num1 else num2
        while numrest:
            t1 = numrest.pop()
            temp = t1 + carry
            res.append(temp % 10)
            carry = temp // 10
        if carry == 1:
            res.append(carry)
        
        dummy = ListNode(val=1)
        cur = dummy
        for i in range(len(res) - 1, -1, -1):
            tempnode = ListNode(res[i])
            cur.next = tempnode
            cur = cur.next
        
        return dummy.next
