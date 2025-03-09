class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"

        
        stack = []
        pops = 0

        for i in range(len(num)):

            while stack and int(stack[-1]) > int(num[i]) and pops < k:
                stack.pop()
                pops += 1
        

            stack.append(num[i])

        end = len(stack)
        while pops < k:
            end -= 1
            pops += 1
        new = "".join(stack[:end])
        start = 0
        while start < len(new) and new[start] == "0":
            start += 1
        return new[start:] if new[start:] != "" else "0"

        