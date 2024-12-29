class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        for ch in s:
            if ch in dic:
                if stack and stack[-1] != dic[ch]:
                    return False
                else:
                    if stack:
                        stack.pop()
                        continue
                    else:
                        return False
            stack.append(ch)
        
        return len(stack) == 0
