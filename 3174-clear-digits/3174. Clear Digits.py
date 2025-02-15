class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch in "0123456789" and stack and stack[-1].isalpha():
                stack.pop()
                continue
            stack.append(ch)

        return "".join(stack)