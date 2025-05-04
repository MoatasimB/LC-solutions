class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # letter : count of adj before
        curr_ch = None
        curr_ch_count = 0
        for i in range(len(s)):
            curr_ch_count = 1
            if stack and s[i] == stack[-1][0]:
                curr_ch_count = stack[-1][1] + 1
            
            if curr_ch_count == k:
                for _ in range(k - 1):
                    stack.pop()
            else:
                stack.append([s[i], curr_ch_count])
        final = [ch for ch, count in stack]
        return "".join(final)


