class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        mpp = defaultdict(int)

        l = 0
        ans = float("inf")
        for r in range(len(cards)):

            mpp[cards[r]] += 1

            while mpp[cards[r]] > 1:
                ans = min(ans, r - l + 1)
                mpp[cards[l]] -= 1
                l += 1
        
        return ans if ans != float("inf") else -1

