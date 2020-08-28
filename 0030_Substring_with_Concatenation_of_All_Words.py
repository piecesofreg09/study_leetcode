'''
compare words consecutively
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        wn = len(words[0])
        ini_hash = set()
        dict_hash = {}
        for word in words:
            ini_hash.add(word[0])
            if word in dict_hash:
                dict_hash[word] += 1
            else:
                dict_hash[word] = 1
        
        #print(ini_hash)
        #print(dict_hash)
        
        res = []
        for idd, c in enumerate(s[:(len(s) - wn * len(words) + 1)]):
            if c in ini_hash:
                count = {**dict_hash}
                start = idd
                #print('at ' + str(start) + ' is ' + c)
                while start + wn <= len(s):
                    tempw = s[start:(start+wn)]
                    #print(tempw)
                    if tempw not in count:
                        break
                    else:
                        count[tempw] -=1
                        if count[tempw] == 0:
                            del count[tempw]
                        if len(count) == 0:
                            res.append(idd)
                            break
                    start += wn
        
        return res


'''
sort and compare tuple
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        wn = len(words[0])
        ini_hash = set()
        
        for word in words:
            ini_hash.add(word[0])
        
        x = tuple(sorted(words))
        
        res = []
        for idd, c in enumerate(s[:(len(s) - wn * len(words) + 1)]):
            if c in ini_hash:
                temp = []
                for i in range(idd, idd+ wn * len(words), wn):
                    temp.append(s[i:(i+wn)])
                y = tuple(sorted(temp))
                if x == y:
                    res.append(idd)
                
        
        return res
