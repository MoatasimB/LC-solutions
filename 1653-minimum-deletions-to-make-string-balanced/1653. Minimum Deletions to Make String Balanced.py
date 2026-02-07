class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        b_count_after = 0
        a_count_after = 0
        for ch in s:
            if ch == "b":
                b_count_after += 1
            else:
                a_count_after += 1
        

        ans = float("inf")
        a_count = 0
        b_count = 0
        for ch in s:
            if ch == "a":
                a_count_after -= 1
                ans = min(ans, b_count + a_count_after)
                a_count += 1

            else:
                b_count_after -= 1
                ans = min(ans, b_count + a_count_after)
                b_count += 1
        
        return ans
