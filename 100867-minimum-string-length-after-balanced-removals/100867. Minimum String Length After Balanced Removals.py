class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        #longest subarray with equal chs

        stack = []

        a_count = 0
        b_count = 0
        
        for i in range(len(s)):
            ch = s[i]

            if ch == "a":
                if stack and stack[-1] == "b":
                    stack.pop()
                    continue
            else:
                if stack and stack[-1] == "a":
                    stack.pop()
                    continue

            stack.append(ch)


        return len(stack)
            
            
        