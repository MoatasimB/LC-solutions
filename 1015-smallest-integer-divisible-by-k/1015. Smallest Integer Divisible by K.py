class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0:
            return -1
        
        curr = 1
        ans = 1
        seen = set()
        for _ in range(1, k + 1):
            if curr % k == 0:
                return ans
            curr = (10 * (curr % k)) + 1
            ans += 1
        
        return -1

        while (curr % k != 0):
            if curr % k in seen:
                return -1
            curr = (10 * (curr % k)) + 1
        
            ans += 1
        return ans