class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ini = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token in ops:
                b = ini.pop()
                a = ini.pop()
                if token == "+":
                    temp = a + b
                elif token == "-":
                    temp = a - b
                elif token == "*":
                    temp = a * b
                elif token == "/":
                    if a / b > 0:
                        temp = int(math.floor(a / b))
                    elif a / b < 0:
                        temp = int(math.ceil(a / b))
                    else:
                        temp = 0
                else:
                    continue
                ini.append(temp)
            else:
                ini.append(int(token))
            #print(ini)
        
        return ini[0]
            
