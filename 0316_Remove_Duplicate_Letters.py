from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        res = []
        seen = set()
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
            
        for idd, charr in enumerate(s):
            if charr in seen:
                continue
            else:
                while res and res[-1] > charr and last[res[-1]] > idd:
                    rm = res.pop()
                    seen.remove(rm)
                
                seen.add(charr)
                res.append(charr)
                #print(res)
        
        return "".join(res)
        '''
        if len(s) == 0:
            return ""
        
        hash_dict = {}
        for idd, ch in enumerate(s):
            if ch in hash_dict:
                hash_dict[ch].append(idd)
            else:
                hash_dict[ch] = [idd]
        
        
        order = sorted(hash_dict.items(), key=lambda x: x[0])
        
        print(order)
        
        result = [[order[0][0], order[0][1][0]]]
        print(result)
        for idd, group in enumerate(order[1:]):
            print(idd)
            print(group)
            letter, choices = group
            if choices[-1]
            for choice in choices:
                pass
        '''
