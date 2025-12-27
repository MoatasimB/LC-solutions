class Solution:
    def isValid(self, s: str) -> bool:
        
        mpp = {")" : "(", "]" : "[", "}" : "{"}

        stack = []

        for ch in s:
            if ch in mpp:
                if stack and stack[-1] == mpp[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0