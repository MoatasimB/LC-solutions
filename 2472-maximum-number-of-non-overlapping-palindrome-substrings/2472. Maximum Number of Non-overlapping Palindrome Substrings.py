class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n = len(s)

        isPali = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2 or isPali[i + 1][j - 1]:
                        isPali[i][j] = True
                    
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            for j in range(i - k + 1):
                if isPali[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]


        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        ans = 0
        start = 0
        for right in range(k - 1, n):
            left = right - k + 1

            if left >= start and isPalindrome(left, right):
                start = right + 1
                ans += 1
                continue
            
            left = right - k
            if left >= start and isPalindrome(left, right):
                start = right + 1
                ans += 1
        
        return ans


        
