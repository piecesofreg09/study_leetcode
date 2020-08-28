'''
Backtrack attempt 1
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False for j in range(m)] for i in range(n)]
        
        def backtrack(locx, locy, lid):
            #print([board[locx][locy], word[lid]])
            if lid == len(word) -1:
                if board[locx][locy] == word[lid]:
                    return True
                else:
                    return False
            
            if board[locx][locy] != word[lid]:
                return False
            else:
                cor = [[1,0],[0,1],[-1,0],[0,-1]]
                visited[locx][locy] = True
                res = False
                for dx, dy in cor:
                    tx = (locx + dx)
                    ty = (locy + dy)
                    if 0 <= tx < n and 0 <= ty < m and (not visited[tx][ty]):
                        res = res | backtrack(locx+dx, locy+dy, lid + 1)
                        if res:
                            return True

                visited[locx][locy] = False
                return False
        
        for i in range(n):
            for j in range(m):
                res = backtrack(i, j, 0)
                if res:
                    return True
        
        return False
