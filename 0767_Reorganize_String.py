class Solution:
    def reorganizeString(self, S: str) -> str:
        countdict = {}
        for char in S:
            if char in countdict:
                countdict[char] += 1
            else:
                countdict[char] = 1
        
        temp = sorted(list(countdict.items()), key=lambda x:x[1], reverse=True)
        
        if temp[0][1] > (len(S) + 1) // 2:
            return ""
        
        con = []
        for i in range(len(temp)):
            con += [temp[i][0]] * temp[i][1]
        #print(con)
        
        right = (len(S) + 1) // 2
        left = len(S) - right
        
        #print([right, left])
        
        result = [None] * len(S)
        
        result[::2] = con[:right]
        result[1::2] = con[-left:]
        
        return "".join(result)
