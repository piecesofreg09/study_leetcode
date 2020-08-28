'''
backtrack
no need to reset data, because the condition checking only involves the line above
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = [None for i in range(n)]
        
        finalRes = 0
        
        def backtrack(row, res, pot):
            nonlocal finalRes
            if row == n - 1:
                loc = pot[0]
                res[row] = loc
                flag = True
                for prev_row in range(row):
                    if abs(prev_row-row) == abs(res[prev_row]-loc):
                        flag = False
                        break
                    else:
                        continue
                if flag:
                    #print('in possible result')
                    #print(res)
                    finalRes += 1
                res[row] = None
                
            
            else:
                #print(pot)
                for idd, potloc in enumerate(pot):
                    res[row] = potloc
                    next_pot = [l for l in pot if l !=potloc]
                    #print(next_pot)
                    if row == 0:
                        backtrack(row + 1, res, next_pot)
                    else:
                        flag = True
                        for prev_row in range(row):
                            if abs(prev_row-row) == abs(res[prev_row]-potloc):
                                flag = False
                                break
                        if flag:
                            backtrack(row + 1, res, next_pot)
                    res[row] = None
                
                return
                
                
        
        pot = [i for i in range(n)]
        backtrack(0, res, pot)
        
        return finalRes
