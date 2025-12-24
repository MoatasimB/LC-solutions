class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        #everything including position i and before is == s[i]
        #everything after s[i] is 1
        n = len(s)
        suffix = [0] * n
        suffix[n -1] = int(s[n - 1])
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + int(s[i])
        
        # [22210]
        ans = float("inf")
        zero_count_front = 0
        one_count_front = 0
        for i in range(len(s)):
            zero_count_back = (n - i - 1 - suffix[i + 1]) if i + 1 < n else 0
            one_count_back = suffix[i + 1] if i + 1 < n else 0
            
            if s[i] == "0":
                before = one_count_front
                after = zero_count_back

                ans = min(ans, before + after)
                zero_count_front += 1
            else:
                before = one_count_front
                after = zero_count_back
                ans = min(ans, before + after)
                one_count_front += 1
        

        return ans
        # 22210 
        # 00110

        # zeros = 0
        # ones = 0
        

