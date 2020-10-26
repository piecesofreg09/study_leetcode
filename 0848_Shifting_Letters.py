'''
calculate cumulated summation
but not pre cumulated summation, but post cumulated summation
'''
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        left = 97
        right = 122
        
        newshifts = []
        summ = 0
        for shift in shifts[::-1]:
            summ += shift
            newshifts.append(summ)
        
        result = []
        for idd, char in enumerate(S):
            shift = newshifts[len(S) - 1 - idd]
            
            newasc = (ord(char) - left + shift) % 26 + left
            result.append(chr(newasc))
        
        return ''.join(result)
