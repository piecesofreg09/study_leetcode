class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
               'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
               'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm',
                'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
        
        keys = {**{i:1 for i in row1}, **{j:2 for j in row2}, **{k:3 for k in row3}}
        
        res = []
        for word in words:
            group = keys[word[0]]
            flag = False
            for char in word[1:]:
                if keys[char] != group:
                    flag = True
                    break
            if flag:
                continue
            else:
                res.append(word)
        
        return res
