class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        
        def calculate(val, l, r):
            cnt = min(val, r - l + 1)
            return ((2 * val - (cnt - 1)) * cnt) // 2
        
        dp = [0] * n #max we can make from index i using books[i]
        stack = [] #indices

       # books[i] - (i - j) <= books[j] we can use shelf j in our progression

        for i in range(n):
            #while we can use the previous as part of our current prog, we pop
            #if the prev is too small to use for current prog we keep
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()
            
            if stack:
                dp[i] = dp[stack[-1]] + calculate(books[i], stack[-1] + 1, i)
            else:
                dp[i] = calculate(books[i], 0, i)
            stack.append(i)
        return max(dp)