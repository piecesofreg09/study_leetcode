class Solution:
    def customSortString(self, S: str, T: str) -> str:
        weight = {letter: idd for idd, letter in enumerate(S)}
        
        result = list(T)
        #print(result)
        
        result.sort(key=lambda x: weight[x] if x in weight else 27)
        
        return ''.join(result)
