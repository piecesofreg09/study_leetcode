'''

check if letters are the same at different locations
only two or zero locations are allowed to be different 

edge cases:
(1) strings that have different lengths
(2) exactly the same string, there will be two situation
  (1) abcd and abcd: they are all unique letters
  (2) aabcd and aabcd: there are duplicate letters, can be used to swap
'''
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        pair = []
        
        for i in range(len(A)):
            if A[i] != B[i]:
                pair.append([A[i], B[i]])
        
        if len(pair) > 2 or len(pair) == 1:
            return False
        
        if len(pair) == 0:
            
            x = set(A)
            if len(x) == len(A):
                return False
            else:
                return True
            
        else:
            if pair[0][-1] == pair[1][0] and pair[1][-1] == pair[0][0]:
                return True
            else:
                return False
