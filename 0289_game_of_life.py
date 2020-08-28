'''
The importance is to distinguish
dead->live and already alive ones
live->dead and already dead ones
so that the original state is memorized
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dxy = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        
        n = len(board)
        m = len(board[0])
        
        for row in range(n):
            for col in range(m):
                
                alive_n = 0
                
                for dx, dy in dxy:
                    rt = row + dx
                    ct = col + dy
                    if (0 <= rt < n) and (0 <= ct < m) and abs(board[rt][ct]) == 1:
                        alive_n += 1
                    
                # -1 means the current cell is dead but originally alive
                if board[row][col] == 1 and (alive_n < 2 or alive_n > 3):
                    board[row][col] = -1
                    
                # 2 is for cell that now alive but originially dead
                if alive_n == 3 and board[row][col] == 0:
                    board[row][col] = 2
        
        for row in range(n):
            for col in range(m):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
