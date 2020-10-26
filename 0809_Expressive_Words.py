'''
find groups first, then compare groups
'''
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def group(s):
            if len(s) == 0:
                return []
            res = [[s[0],1]]
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    res[-1][1] += 1
                else:
                    res.append([s[i], 1])
            return res
        
        maingroup = group(S)
        #print(maingroup)
        res = 0
        for word in words:
            abbreved = group(word)
            #print(abbreved)
            if len(abbreved) == len(maingroup):
                breakFlag = False
                for i in range(len(maingroup)):
                    if abbreved[i][0] != maingroup[i][0]:
                        breakFlag = True
                        break
                    else:
                        if maingroup[i][1] < abbreved[i][1]:
                            breakFlag = True
                            break
                        elif maingroup[i][1] > abbreved[i][1]:
                            if maingroup[i][1] < 3:
                                breakFlag = True
                                break
                        else:
                            continue
                
                if not breakFlag:
                    res += 1
        
        return res
            
