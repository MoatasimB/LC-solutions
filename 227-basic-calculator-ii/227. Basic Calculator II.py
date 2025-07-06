class Solution:
    def calculate(self, s: str) -> int:
        

        curr = 0
        op = "+"
        stack = []
        
        s = s.replace(" ", "")
        for i in range(len(s)):

            if s[i].isdigit():
                curr = (curr * 10) + int(s[i])
            
            if (not s[i].isdigit()) or (i == (len(s)-1)):
                if op == "+":
                    stack.append(curr)
                elif op == "-":
                    stack.append(-curr)
                elif op == "*":
                    prev = stack.pop()
                    stack.append(curr * prev)
                elif op == "/":
                    prev = stack.pop()
                    sign_p = 1
                    sign_c = 1
                    if prev < 0:
                        sign_p = -1
                    if curr < 0:
                        sign_c = -1
                    sign = sign_c * sign_p
                    stack.append(sign * (abs(prev) // abs(curr)))
                
                op = s[i]
                curr = 0

        return sum(stack)                    
            


