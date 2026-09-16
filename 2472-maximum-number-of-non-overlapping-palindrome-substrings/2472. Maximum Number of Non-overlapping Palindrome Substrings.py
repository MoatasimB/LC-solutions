class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n = len(s)

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


        
