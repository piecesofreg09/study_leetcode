class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_dict = {str(i): 1 for i in range(1 ,10)}
        
        letter = ''
        for i in range(9):
            hash_dict = {str(i): 1 for i in range(1 ,10)}
            for letter in board[i]:
                if letter in hash_dict:
                    if hash_dict[letter] == 0:
                        return False
                    else:
                        hash_dict[letter] -= 1
        letter = ''
        for i in range(9):
            hash_dict = {str(i): 1 for i in range(1 ,10)}
            #print()
            for j in range(9):
                letter = board[j][i]
                #print(letter)
                if letter in hash_dict:
                    #print(hash_dict[letter])
                    if hash_dict[letter] == 0:
                        return False
                    else:
                        hash_dict[letter] -= 1
        
        letter = ''
        for i in range(3):
            for j in range(3):
                hash_dict = {str(i): 1 for i in range(1 ,10)}
                for k in range(3):
                    for l in range(3):
                        letter = board[3 * i + k][3 * j + l]
                        if letter in hash_dict:
                            if hash_dict[letter] == 0:
                                return False
                            else:
                                hash_dict[letter] -= 1
        
        return True
