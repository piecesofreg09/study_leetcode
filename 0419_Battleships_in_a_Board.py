class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if (not board) or (not board[0]):
            return 0
        
        width, height = len(board[0]), len(board)
        result = 1 if board[0][0] == 'X' else 0
        
        for i in range(1, height):
            result += 1 if (board[i-1][0], board[i][0]) == ('.', 'X') else 0
        
        for i in range(1, width):
            result += 1 if (board[0][i-1], board[0][i]) == ('.', 'X') else 0
        
        for i in range(1, height):
            for j in range(1, width):
                if (board[i-1][j], board[i][j]) == ('.', 'X') and (board[i][j-1], board[i][j]) == ('.', 'X'):
                    result += 1
        
        return result
        
        
