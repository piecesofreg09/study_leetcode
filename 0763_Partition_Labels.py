'''
Intervals and counting of the covering intervals
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        hashmap = {}
        for idd, char in enumerate(S):
            if char in hashmap:
                hashmap[char].append(idd)
            else:
                hashmap[char] = [idd]
        
        results = []
        included = {char:False for char in hashmap}
        for char, li in hashmap.items():
            if included[char] == False:
                lettersrange = [hashmap[char][0], hashmap[char][-1]]
                for charr, lii in hashmap.items():
                    if included[charr] == False and charr != char:
                        start = hashmap[charr][0]
                        end = hashmap[charr][-1]
                        
                        if lettersrange[0] <= start <= lettersrange[-1] or lettersrange[0] <= end <= lettersrange[-1]:
                            lettersrange = [min(lettersrange[0], start), max(lettersrange[-1], end)]
                            included[charr] = True
                
                results.append(lettersrange)
                print(results)
        
        results.sort(key=lambda a: a[0])
        
        return [rangee[-1] - rangee[0] + 1 for rangee in results]
