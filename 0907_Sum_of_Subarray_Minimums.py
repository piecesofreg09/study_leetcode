'''
two monotone stacks
'''
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = [None] * len(arr)
        right = [None] * len(arr)
        
        stackleft = []
        for i in range(len(arr)):
            while stackleft and arr[stackleft[-1]] >= arr[i]:
                stackleft.pop()
            
            left[i] = stackleft[-1] if stackleft else -1
            stackleft.append(i)
        print(left)
        
        stackright = []
        for i in range(len(arr)-1, -1, -1):
            while stackright and arr[stackright[-1]] > arr[i]:
                stackright.pop()
            
            right[i] = stackright[-1] if stackright else len(arr)
            stackright.append(i)
        print(right)
        
        
        res = 0
        modd = (10**9) + 7
        for i in range(len(arr)):
            res += ((i - left[i]) * (right[i] - i) * arr[i]) % modd
        res = res % modd
        
        return res
