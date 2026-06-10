class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        
        flavors = defaultdict(int)
        n = len(candies)
        for c in candies:
            flavors[c] += 1
        ans = 0
        for r in range(n):
            flavors[candies[r]] -= 1
            if flavors[candies[r]] == 0:
                del flavors[candies[r]]
            if r == k - 1:
                ans = max(ans, len(flavors))
            if r - k >= 0:
                flavors[candies[r - k]] += 1
                ans = max(ans, len(flavors))
        
        return ans