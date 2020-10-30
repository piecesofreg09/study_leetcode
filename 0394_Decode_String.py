'''
Recursion
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = []
        
        string = ""
        
        for idd, char in enumerate(s):
            if char == '[':
                stack.append(idd)
                # remember the number it needs to repeat
                numstart = idd - 1
                while numstart >= 0 and 48 <= ord(s[numstart]) <= 57:
                    numstart -= 1
                nums.append(int(s[(numstart+1):idd]))
            elif 48 <= ord(char) <= 57:
                continue
            elif char == ']':
                startid = stack.pop()
                num = nums.pop()
                if len(stack) == 0:
                    x = self.decodeString(s[startid+1:idd])
                    string += x * num
            else:
                if len(stack) == 0:
                    string += char
        
        return string
