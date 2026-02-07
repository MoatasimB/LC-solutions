class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        a_count_after = 0
        for ch in s:
            if ch == "a":
                a_count_after += 1
        
        

        ans = float("inf")
        b_count = 0
        for ch in s:
            if ch == "a":
                a_count_after -= 1
                ans = min(ans, b_count + a_count_after)

            else:
                ans = min(ans, b_count + a_count_after)
                b_count += 1
        
        return ans
