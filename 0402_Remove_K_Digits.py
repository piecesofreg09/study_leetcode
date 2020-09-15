'''
1axxxxx > 1bxxx if a > b

so compare the stack, 
if the next element is smaller than the stack top, 
  (1) pop the top until the top element is smaller than the next element 
  (2) or the required k digits are removed
 
deal with the fact where removed < k,
the resulting stack will be a mono stack, just remove the last few digits

deal with leading zeros

'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [int(num[0])]
        
        count = k
        for char in num[1:]:
            n = int(char)
            while stack and n < stack[-1] and count > 0:
                stack.pop()
                count -= 1
            stack.append(n)
            #print(stack)
        
        if count > 0:
            res = stack[:-count]
        else:
            res = stack
        
        cur = 0
        while cur < len(res) and res[cur] == 0:
            cur += 1
        
        res = res[cur:]
        if len(res) == 0:
            return "0"
        
        return "".join([str(n) for n in res])
            
