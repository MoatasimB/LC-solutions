class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        
        n = len(s)
        half_len = n // 2
        half = s[:(n //2)]

        freq = [0] * 26
        total = 0
        for ch in half:
            freq[ord(ch) - ord('a')] += 1
            total += 1
        middle = ""
        if n % 2 == 1:
            middle = s[n//2]
        ans = []

        
        def countWays(limit, len_, remaining):
            count = 1
            for i, val in enumerate(remaining):
                if val == 0:
                    continue
                
                # len choose val
                

                count *= calculate(len_, val)
                if count >= limit:
                    return limit
                len_ -= val
                
            return count

        
        
        
        # 4 choose 2  = 4 * 3 
        #                 2 * 1

        def calculate(n, m):
            ans = 1
            m = min(m, n - m)

            for i in range(1, m + 1):

                ans = ans * (n - i + 1) // (i)
            
            return ans

        if countWays(k, half_len, freq) < k:
                    return ""
        
        
        for i in range(half_len):
            for j in range(26):
                len_ = half_len - i - 1
                if freq[j] == 0:
                    continue
                freq[j] -= 1
                 
                total = countWays(k, len_, freq)
                if total < k:
                    k -= total
                    freq[j] += 1
                else:
                    ans.append(chr(j + ord("a")))
                    break






        left = "".join(ans)

        return left + middle + left[::-1]
