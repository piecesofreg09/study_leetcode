'''
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            res = []
            prd = 2 * numRows - 2
            n = len(s)
            
            
            for i in range(numRows):
                for j in range(n // prd):
                    mul = j * prd
                    charr = s[mul + i]
                    res.append(charr)
                    if (i > 0 and i < numRows - 1):
                        charr = s[mul + prd - i]
                        res.append(charr)
                j = n // prd
                mul = j * prd
                if (j * prd + i) < n:
                    charr = s[mul + i]
                    res.append(charr)
                    if (i > 0 and i < numRows - 1):
                        if (j + 1) * prd - i < n:
                            charr = s[mul + prd - i]
                            res.append(charr)
            
            return "".join(res)
