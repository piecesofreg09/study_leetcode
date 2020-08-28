'''
(1) take care of the last character
(2) "12" will be split into "1" and "2"
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        start = len(chars) - 1
        end = len(chars)
        count = 0
        while start > 0:
            while start > 0 and chars[start] == chars[start - 1]:
                start -= 1
                count += 1
            
            '''
            start = 0 can only be reached when the last letter has duplicates
            if the last letter is unique, then start is never equal to 0, so the condition goes to the next one
            '''
            if start == 0:
                count += 1
                chars[start:end] = [chars[start]] + list(str(count))
            else:
                count += 1
                if count > 1:
                    chars[start:end] = [chars[start]] + list(str(count))
                    end = start
                    start -= 1
                    count = 0
                else:
                    # if the count is just equal to 1, then make no modify
                    end = start
                    start -= 1
                    count = 0
            #print(chars)
        
        return len(chars)
